import keyring
import pandas as pd
from datetime import date
import requests
import json
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

# Create a new item in the Webflow Jobs collection for each new job, and print its Webflow item ID at the end
for job in jobs_created_today:
    job_sectors = [collection_items_dict[f"Sectors - {sector}"]
                for sector in job['sectors']] if job['sectors'] is not None else ""
    job_accreditations = [collection_items_dict[f"Accreditations - {accreditation}"]
                        for accreditation in job['accreditations']] if job['accreditations'] is not None else ""
    job_types = [collection_items_dict[f"Available roles - {role_type}"]
                for role_type in job['job_type']] if job['job_type'] is not None else ""
    job_locations = [collection_items_dict[f"Locations - {location}"]
                    for location in job['location']] if job['location'] is not None else ""
    job_seniorities = [collection_items_dict[f"Seniorities - {seniority}"]
                    for seniority in job['seniority']] if job['seniority'] is not None else ""
    job_multiple_locations = collection_items_dict["Multiple locations - true"] if job['multiple_locations'] == True else collection_items_dict["Multiple locations - false"]
    job_rewilding = collection_items_dict["Rewilding - true"] if job['rewilding'] == True else collection_items_dict["Rewilding - false"]
    job_bizorchar = collection_items_dict["BizOrChar - Business"] if job['borch'] == 'Business' else collection_items_dict["BizOrChar - Charity"]


    url = "https://api.webflow.com/collections/6347d24d945dd61cc70ba3de/items"

    payload = {"fields": {
        "slug": "",  # If you leave this blank, Webflow generates a slug for you, so you don't have to worry about accidentally providing a duplicate
        "name": job['concat_name'],
        "title": job['title'],  # This doesn't need to be unique
        "link-to-apply": job['link_to_apply'],
        "date-added": str(job['date_added']),  # Needs to be a string in YYYY-MM-DD format
        "date-added-text": job['date_added_string'],
        "location-3": job_locations,
        "multiple-locations": job_multiple_locations,
        "seniority": job_seniorities,
        "type-of-job": job_types,
        "rewilding": job_rewilding,
        "_archived": False,
        "_draft": False,  # It might look like this publishes the item, but it doesn't
        "organisation": job['org_webflow_id'],
        "organisation-name": job['org_name'],
        "website": job['website'],
        "careers-page": job['careers_page'],
        "mission": job['mission'],
        "accreditations": job_accreditations,
        "bizorchar": job_bizorchar,
        "sectors": job_sectors
    }}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Parse the text part of the response into JSON, then extract the collection item ID
    json_string = response.text
    data = json.loads(json_string)
    
    # Add the job's Webflow item ID into the list of item IDs to publish
    if "_id" in data:
        item_ids_to_publish.append(data["_id"])

        # Add the job's Webflow item ID into the postgres database (so we can use it to delete the job from Webflow when it's no longer live)
        cursor.execute("UPDATE jobs \
                    SET webflow_item_id = %s \
                    WHERE concat_name = %s AND date_removed IS NULL;", (data["_id"], job['concat_name']))

    #Simplest way to get around rate limiting issues (should do this in a better way in future)    
    time.sleep(1)


# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)


# Publish all the new jobs in Webflow
webflow_functions.publish_webflow_items("Jobs", item_ids_to_publish)
