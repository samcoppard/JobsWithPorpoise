# -*- coding: utf-8 -*-

""" Update orgs in Webflow CMS to match orgs in PSQL database """

import keyring
import psycopg2
from psycopg2 import extras
import requests
import json


#def delete_org_from_webflow():
    # Delete


#def add_new_org_to_webflow():
    # Add new


#def update_org_in_webflow():
    # Update


""" Pull all attributes for all orgs in PSQL database """

# Fetch your personal access token, stored in MacOS Keychain
postgres_password = keyring.get_password(
    "login", "postgres_password")

# Connect to PostgreSQL database
conn = psycopg2.connect(
    database="jobs_with_porpoise",
    user="postgres",
    password=postgres_password,
    host="localhost"
)
conn.set_client_encoding('UTF8')

# Create a cursor object (necessary to execute SQL queries and fetch results from the database)
# Using the DictCursor cursor allows us to pull data from the database as a list of dictionaries, rather than as a list of tuples, so we can extract individual attributes more easily / readably
cursor = conn.cursor(cursor_factory=extras.DictCursor)

# Pull all attributes for all organisations in PSQL database
cursor.execute("SELECT name, mission, website, careers_page, sectors, available_roles, biz_or_char, accreditations, currently_hiring, webflow_item_id, webflow_slug \
               FROM organisations \
               WHERE name = 'Citizens of Soil';")
rows = cursor.fetchall()

#DictCursor returns rows as psycopg2.extras.DictRow objects, which behave like dictionaries but aren't quite dictionaries
#So we need to conver the DictRow objects to regular python dictionaries
psql_orgs = [dict(row) for row in rows]

# Close the database connection
cursor.close()
conn.close()


""" Pull all fields for all orgs in Webflow CMS """


def get_webflow_collections():
    """Return a dictionary of all Webflow collection names and IDs"""

    # Get your Webflow authorisation token and site ID
    site_id = keyring.get_password("login", "Webflow Site ID")
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = f"https://api.webflow.com/sites/{site_id}/collections"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.get(url, headers=headers)

    json_string = response.text
    data = json.loads(json_string)

    collection_dict = {collection["name"]
        : collection["_id"] for collection in data}

    return collection_dict


def get_webflow_orgs(offset, orgs_list=[]):
    """Return a dictionary of all item names and IDs for a particular collection"""

    # Get your Webflow authorisation token
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = f"https://api.webflow.com/collections/{get_webflow_collections()['Organisations']}/items?limit=100&offset={offset}"

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
        orgs_list.append({
            "name": item['name'],
            "mission": item['mission'],
            "website": item['org-website'],
            "careers_page": item['careers-page'],
            "sectors": item['sectors'],
            "available_roles": item['available-roles'] if 'available-roles' in item else "",
            "biz_or_char": item['biz'],
            "accreditations": item['accreditations-2'] if 'accreditations-2' in item else "",
            "currently_hiring": item['currently-hiring-2'],
            "webflow_item_id": item['_id'],
            "webflow_slug": item['slug']
        })

    if data['count'] + data['offset'] < data['total']:
        offset += 100
        get_webflow_orgs(offset, orgs_list)

    return orgs_list
    

webflow_orgs = get_webflow_orgs(0)


""" Compare webflow orgs with psql orgs """
# To make it a fair comparison, we need to convert psql strings e.g. 'Software' into Webflow item IDs e.g. '6425b9336545cb72069357c7'


def get_collection_items(collection, offset):
    """Return a dictionary of all item names and IDs for a particular collection"""

    # Get your Webflow authorisation token and site ID
    webflow_token = keyring.get_password("login", "Webflow Token")

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


# This dictionary will store the names and Webflow Item IDs of every item in every collection (except Jobs & Organisations)
collection_items_dict = {}

get_webflow_collections()
for collection in ['Sectors', 'Accreditations', 'Business or charities', 'Available roles']:
    get_collection_items(collection, offset=0)


for org in psql_orgs:
    org['sectors'] = [collection_items_dict[f"Sectors - {sector}"] for sector in org['sectors']] if org['sectors'] is not None else ""
    org['available_roles'] = [collection_items_dict[f"Available roles - {role}"]
                              for role in org['available_roles']] if org['available_roles'] is not None else ""
    org['biz_or_char'] = [collection_items_dict[f"Business or charities - {biz_type}"]
                          for biz_type in org['biz_or_char']] if org['biz_or_char'] is not None else ""
    org['accreditations'] = [collection_items_dict[f"Accreditations - {accreditation}"]
                             for accreditation in org['accreditations']] if org['accreditations'] is not None else ""
    org['currently_hiring'] = "Yes" if org['currently_hiring'] == True else "No"


print(webflow_orgs[0])
print(psql_orgs[0])


