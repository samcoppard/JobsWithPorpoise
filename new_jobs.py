import pandas as pd
from datetime import date
import time
import psql_functions
import webflow_functions

# Pull in the csv of categorised jobs
scraped_csv = pd.read_csv('categorised_jobs.csv')

# Turn this into a dataframe
scraped_jobs = pd.DataFrame(scraped_csv)

# Connect to the PSQL database and create a cursor object 
conn, cursor = psql_functions.connect_to_psql_database()

# Create an empty list to contain details of all the new jobs we're going to add to the database
new_jobs = []

# We need a list of jobs in the database to compare with, so let's pull all the live jobs
cursor.execute("SELECT * FROM jobs_for_webflow \
               WHERE date_removed IS NULL \
               AND job_scraped IS TRUE;")

# Fetch the results, create a list of all the live jobs (using the concatenated field), then check if each scraped job is in this list
# If it is, we don't need to do anything. If it's not, then we need to add that job to the database
rows = cursor.fetchall()
live_jobs_concat = [row["concat_name"] for row in rows]

for ind in scraped_jobs.index:
    if scraped_jobs['concat'][ind][:255] not in live_jobs_concat:
        #Add all the role's details to the new_jobs list, formatted ready to go straight into the Postgres database
        new_jobs.append({
            "concat_name": scraped_jobs['concat'][ind],
            "title": scraped_jobs['Job Title'][ind],  # This doesn't need to be unique
            "link_to_apply": scraped_jobs['Job URL'][ind],
            "date_added_string": f"🗓  Posted {date.today().strftime('%d/%m/%y')}",
            "location": scraped_jobs['mapped_location'][ind].split(', '),
            "seniority": scraped_jobs['seniority'][ind].split(', '),
            "job_type": scraped_jobs['job_types'][ind].split(', '),
            "organisation": scraped_jobs['Company'][ind],
        })

# Now we need to actually add each of these jobs to the postgres database
for job in new_jobs:
    cursor.execute("INSERT INTO jobs(concat_name, title, link_to_apply, organisation, job_type, seniority, location, date_added, date_added_string, date_removed) \
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL);",
                (job['concat_name'][:255], job['title'][:255], job['link_to_apply'][:255], job['organisation'], job['job_type'], job['seniority'], job['location'], date.today(), job['date_added_string']))


""" WEBFLOW TIME """

#We need to get the item IDs for job types, sectors, locations, etc before we can add the jobs to Webflow

# Get your Webflow authorisation token
webflow_token = webflow_functions.get_webflow_api_key()

# Store the names and Webflow item IDs of every item in every collection (except Jobs & Organisations), plus the IDs for important dropdown options in Webflow
collection_items_dict = webflow_functions.get_static_collection_items()

# Pull a list of all the jobs we've just created in the database
cursor.execute("SELECT * FROM jobs_for_webflow \
               WHERE date_added = %s;",
               (date.today(),))

# Get the results
jobs_created_today = cursor.fetchall()

# And make another list to hold the Webflow item IDs of all these new jobs so that we can publish them after this next bit
item_ids_to_publish = []

def prep_job_for_webflow(dict_of_job_attributes):
    prepped_dict_of_job_attributes = {
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
    return prepped_dict_of_job_attributes


# Create a new item in the Webflow Jobs collection for each new job, and print its Webflow item ID at the end
for job in jobs_created_today:
    webflow_job_id = webflow_functions.create_webflow_job(prep_job_for_webflow(job))
    
    # Add the job's new Webflow item ID into the list of item IDs to publish
    item_ids_to_publish.append(webflow_job_id)

    # Add the job's Webflow item ID into the postgres database (so we can use it to delete the job from Webflow when it's no longer live)
    cursor.execute("UPDATE jobs \
                SET webflow_item_id = %s \
                WHERE concat_name = %s AND date_removed IS NULL;", (webflow_job_id, job['concat_name']))

    #Simplest way to get around rate limiting issues (should do this in a better way in future)    
    time.sleep(1)


# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)


# Publish all the new jobs in Webflow
webflow_functions.publish_webflow_items("Jobs", item_ids_to_publish)
