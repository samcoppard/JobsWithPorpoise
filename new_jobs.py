import keyring
import pandas as pd
from datetime import date
import requests
import json
import time
import psql_functions

# Pull in the csv of categorised jobs
scraped_csv = pd.read_csv('categorised_jobs.csv')

# Turn this into a dataframe
scraped_jobs = pd.DataFrame(scraped_csv)

conn, cursor = psql_functions.connect_to_psql_database()

# Create an empty list to contain details of all the new jobs we're going to add to the database
new_jobs = []

# Get today's date (so we can add it to the date_added field in SQL for new jobs
tdy = date.today()

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
            "date_added_string": f"🗓  Posted {tdy.strftime('%d/%m/%y')}",
            "location": scraped_jobs['mapped_location'][ind].split(', '),
            "seniority": scraped_jobs['seniority'][ind].split(', '),
            "job_type": scraped_jobs['job_types'][ind].split(', '),
            "organisation": scraped_jobs['Company'][ind],
        })

# Now we need to actually add each of these jobs to the postgres database
for job in new_jobs:
    cursor.execute("INSERT INTO jobs(concat_name, title, link_to_apply, organisation, job_type, seniority, location, date_added, date_added_string, date_removed) \
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL);",
                (job['concat_name'][:255], job['title'][:255], job['link_to_apply'][:255], job['organisation'], job['job_type'], job['seniority'], job['location'], tdy, job['date_added_string']))


""" WEBFLOW TIME """

#We need to get the item IDs for job types, sectors, locations, etc before we can add the jobs to Webflow

# Get your Webflow authorisation token and site ID
site_id = keyring.get_password("login", "Webflow Site ID")
webflow_token = keyring.get_password("login", "Webflow Token")

def get_webflow_collections():
    """Return a dictionary of all Webflow collection names and IDs"""
    url = f"https://api.webflow.com/sites/{site_id}/collections"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.get(url, headers=headers)

    json_string = response.text
    data = json.loads(json_string)

    collection_dict = {collection["name"]: collection["_id"] for collection in data}

    return collection_dict


def get_collection_items(collection, offset):
    """Return a dictionary of all item names and IDs for a particular collection"""

    if collection not in ["Organisations", "Jobs", "Sectors", "Accreditations", "Business or charities", "Available roles", "Locations", "Seniorities"]:
        print("Please use a valid collection name")

    else:
        url = f"https://api.webflow.com/collections/{get_webflow_collections()[collection]}/items?limit=100&offset={offset}"

        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {webflow_token}"
        }

        response = requests.get(url, headers=headers)

        # Parse the text part of the response into JSON
        json_string = response.text
        data = json.loads(json_string)

        # Add returned collection items and their item IDs to the dictionary
        for item in data['items']:
            collection_items_dict[f"{collection} - {item['name']}"] = item['_id']

        if data['count'] + data['offset'] < data['total']:
            offset += 100
            get_collection_items(collection, offset)

        return collection_items_dict

#This dictionary will store the names and Webflow Item IDs of every item in every collection (except Jobs & Organisations)
collection_items_dict = {}

get_webflow_collections()
for collection in ['Sectors', 'Accreditations', 'Business or charities', 'Available roles', 'Locations', 'Seniorities']:
    get_collection_items(collection, offset=0)

#Add the extra IDs you need that aren't stored in collections (these are dropdown options in Webflow)
collection_items_dict["Multiple locations - true"] = "455ae768ed4cb346f4a0e6a28621f8bf"
collection_items_dict["Multiple locations - false"] = "27ac7f940152cdfc8a8368aa282da9e3"
collection_items_dict["Rewilding - true"] = "dacaf901d0aeed0c3359f1447380ada3"
collection_items_dict["Rewilding - false"] = "4c1341378df85b075fe19ae70c0c9b96"
collection_items_dict["BizOrChar - Business"] = "7f61f4cb6e6c23177283916a85bf40db"
collection_items_dict["BizOrChar - Charity"] = "6396a5d85efc020870e39f39ac2758d8"


# Pull a list of all the jobs we've just created in the database
cursor.execute("SELECT * FROM jobs_for_webflow \
               WHERE date_added = %s;",
               (tdy,))

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


psql_functions.close_psql_connection(conn, cursor)


""" Publishing time """

def publish_items(collection, item_ids):
    url = f"https://api.webflow.com/collections/{get_webflow_collections()[collection]}/items/publish"

    payload = {"itemIds": item_ids}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.put(url, json=payload, headers=headers)

    print(response.text)


publish_items("Jobs", item_ids_to_publish)
