import pandas as pd
from datetime import date
import time
import psql_functions
import webflow_functions

""" PSQL UPDATES """

# Pull in the scraped and categorised jobs as a dataframe
categorised_jobs_csv = pd.read_csv('categorised_jobs.csv')
scraped_jobs = pd.DataFrame(categorised_jobs_csv)

# Connect to the PSQL database and create a cursor object 
conn, cursor = psql_functions.connect_to_psql_database()

# Pull all the live jobs (that were scraped) from the PSQL database, and create a list of all their long concatenated names
cursor.execute("SELECT * FROM jobs_for_webflow \
               WHERE date_removed IS NULL \
               AND job_scraped IS TRUE;")

live_jobs_from_psql = cursor.fetchall()

psql_live_jobs_concats = [job["concat_name"] for job in live_jobs_from_psql]

# Write the query that will add a new job to the jobs table in the PSQL database
query_to_add_job_to_psql = """
    INSERT INTO jobs (
        concat_name, title, link_to_apply, organisation, job_type, seniority, location, date_added, date_added_string, date_removed
        )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, NULL
        )
    """

# Using the concat field, check if each scraped job is in the list of live jobs from PSQL
# Then add any scraped jobs that aren't already in the database to the database, using the query above
for ind in scraped_jobs.index:
    if scraped_jobs['concat'][ind] not in psql_live_jobs_concats:
        job_attributes = (
            scraped_jobs['concat'][ind], scraped_jobs['Job Title'][ind], scraped_jobs['Job URL'][ind], scraped_jobs['Company'][ind],
            scraped_jobs['job_types'][ind].split(', '), scraped_jobs['seniority'][ind].split(', '),
            scraped_jobs['mapped_location'][ind].split(', '), date.today(), f"🗓  Posted {date.today().strftime('%d/%m/%y')}"
            )

        cursor.execute(query_to_add_job_to_psql, job_attributes)


""" WEBFLOW TIME """

# Get the names and Webflow item IDs we'll need to map PSQL strings e.g. 'Software' to Webflow item IDs e.g. '6425b9336545cb72069357c7'
collection_items_dict = webflow_functions.get_static_collection_items()

def prep_job_for_webflow(dict_of_job_attributes):
    """ Map the PSQL fields of a job to the correctly formatted Webflow fields """
    webflow_ready_job_attributes = {
        "job_name": dict_of_job_attributes['concat_name'],
        "job_title": dict_of_job_attributes['title'],
        "job_link": dict_of_job_attributes['link_to_apply'],
        "job_date": str(dict_of_job_attributes['date_added']),
        "job_date_str": dict_of_job_attributes['date_added_string'],
        "job_location": [collection_items_dict[f"Locations - {location}"] for location in dict_of_job_attributes['location']] if dict_of_job_attributes['location'] is not None else "",
        "job_multiple_locations": collection_items_dict["Multiple locations - true"] if dict_of_job_attributes['multiple_locations'] == True else collection_items_dict["Multiple locations - false"],
        "job_seniority": [collection_items_dict[f"Seniorities - {seniority}"] for seniority in dict_of_job_attributes['seniority']] if dict_of_job_attributes['seniority'] is not None else "",
        "job_type": [collection_items_dict[f"Available roles - {role_type}"] for role_type in dict_of_job_attributes['job_type']] if dict_of_job_attributes['job_type'] is not None else "",
        "job_rewilding": collection_items_dict["Rewilding - true"] if dict_of_job_attributes['rewilding'] == True else collection_items_dict["Rewilding - false"],
        "org": dict_of_job_attributes['org_webflow_id'],
        "org_name": dict_of_job_attributes['org_name'],
        "org_website": dict_of_job_attributes['website'],
        "org_careers_page": dict_of_job_attributes['careers_page'],
        "org_mission": dict_of_job_attributes['mission'],
        "org_accreditations": [collection_items_dict[f"Accreditations - {accreditation}"] for accreditation in dict_of_job_attributes['accreditations']] if dict_of_job_attributes['accreditations'] is not None else "",
        "org_bizorchar": collection_items_dict["BizOrChar - Business"] if dict_of_job_attributes['borch'] == 'Business' else collection_items_dict["BizOrChar - Charity"],
        "org_sectors": [collection_items_dict[f"Sectors - {sector}"] for sector in dict_of_job_attributes['sectors']] if dict_of_job_attributes['sectors'] is not None else ""
    }
    return webflow_ready_job_attributes

# Pull a list of all the jobs we've just created in the database today
cursor.execute("SELECT * FROM jobs_for_webflow \
               WHERE date_added = %s;",
               (date.today(),))

psql_jobs_created_today = cursor.fetchall()

# For each new job in PSQL, create a new item in the Webflow Jobs collection, and store its item ID so that we can publish them all en masse later on
item_ids_to_publish = []

for job in psql_jobs_created_today:
    # The create_webflow_job function creates the job and returns its new item ID
    webflow_job_id = webflow_functions.create_webflow_job(prep_job_for_webflow(job))
    
    item_ids_to_publish.append(webflow_job_id)

    # Add the job's Webflow item ID into the PSQL database
    cursor.execute("UPDATE jobs \
                SET webflow_item_id = %s \
                WHERE concat_name = %s AND date_removed IS NULL;",
                (webflow_job_id, job['concat_name']))

    # Handle rate limiting issues in the simplest way possible (will improve in future)    
    time.sleep(1)

# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)

# Publish all the new jobs in Webflow
webflow_functions.publish_webflow_items("Jobs", item_ids_to_publish)