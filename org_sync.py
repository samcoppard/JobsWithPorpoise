""" Update orgs in Webflow CMS to match orgs in PSQL database """

import keyring
import psycopg2
from psycopg2 import extras
import requests
import json
import time

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

# Create a cursor object (necessary to execute SQL queries and fetch results from the database)
# Using the DictCursor cursor allows us to pull data from the database as a list of dictionaries, rather than as a list of tuples, so we can extract individual attributes more easily / readably
cursor = conn.cursor(cursor_factory=extras.DictCursor)

# Pull all attributes for all organisations in PSQL database
cursor.execute("SELECT name, mission, website, careers_page, sectors, available_roles, biz_or_char, accreditations, currently_hiring, webflow_item_id, webflow_slug \
               FROM organisations;")
rows = cursor.fetchall()

#DictCursor returns rows as psycopg2.extras.DictRow objects, which behave like dictionaries but aren't quite dictionaries
#So we need to conver the DictRow objects to regular python dictionaries
psql_orgs = [dict(row) for row in rows]


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
            "available_roles": item['available-roles'] if 'available-roles' in item and item['available-roles'] is not None else "",
            "biz_or_char": item['biz'],
            "accreditations": item['accreditations-2'] if 'accreditations-2' in item and item['accreditations-2'] is not None else "",
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

# Transform psql attributes into webflow attributes for each organisation
for org in psql_orgs:
    org['sectors'] = [collection_items_dict[f"Sectors - {sector}"] for sector in org['sectors']] if org['sectors'] is not None else ""
    org['available_roles'] = [collection_items_dict[f"Available roles - {role}"]
                              for role in org['available_roles']] if org['available_roles'] is not None else ""
    org['biz_or_char'] = [collection_items_dict[f"Business or charities - {biz_type}"]
                          for biz_type in org['biz_or_char']] if org['biz_or_char'] is not None else ""
    org['accreditations'] = [collection_items_dict[f"Accreditations - {accreditation}"]
                             for accreditation in org['accreditations']] if org['accreditations'] is not None else ""
    org['currently_hiring'] = "Yes" if org['currently_hiring'] == True else "No"




""" First check if any webflow orgs are no longer in the psql database - these should be deleted from webflow
    Then check if any psql orgs are not in webflow - these should be added to webflow
    Then check that the other psql orgs have the same attributes as those in webflow - any that don't should be patched in webflow """

def delete_orgs_from_webflow(list_of_item_ids):
    """ Delete all Webflow item IDs provided in a list, provided they're all in the Organisations collection """

    # Get your Webflow authorisation token
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = "https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items"

    payload = {"itemIds": list_of_item_ids}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.delete(url, json=payload, headers=headers)

    print(response.text)


def add_new_org_to_webflow(name, website, careers_page, mission, accreditations, available_roles, hiring, bizorchar, sectors):
    """ Create a new item in the Organisations collection, and return its Webflow item ID """

    # Get your Webflow authorisation token
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = "https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items"

    payload = {"fields": {
        "slug": "",  # Webflow will auto-generate the slug if this is left blank, avoiding duplication issues
        "_archived": False,
        "_draft": False,  # It might look like this publishes the item, but it doesn't
        "name": name,  # This doesn't need to be unique
        "org-website": website,
        "careers-page": careers_page,
        "mission": mission,
        # List of Webflow item IDs (or an empty string)
        "accreditations-2": accreditations,
        # List of Webflow item IDs (or an empty string)
        "available-roles": available_roles,
        "currently-hiring-2": hiring,  # "Yes" or "No"
        "biz": bizorchar,  # List containing a single Webflow item ID
        "sectors": sectors  # List of Webflow item IDs (or an empty string)
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

    # Add the org's new Webflow item ID into the list of item IDs to publish
    if "_id" in data:
        org_ids_to_publish.append(data["_id"])

        # Add the job's Webflow item ID into the postgres database
        cursor.execute("UPDATE organisations \
                    SET webflow_item_id = %s,  webflow_slug = %s\
                    WHERE name = %s;", (data["_id"], data["slug"], name))

    # Simplest way to get around rate limiting issues
    time.sleep(1)


def patch_org_in_webflow(webflow_item_id, webflow_slug, org_name, website, careers_page, mission, accreditations, available_roles, hiring, bizorchar, sectors):
    """ Patch an item in the Organisations collection """

    # Get your Webflow authorisation token
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = f"https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items/{webflow_item_id}"

    payload = {"fields": {
        "slug": webflow_slug,  # required
        "name": org_name,  # required
        "_archived": False,
        "_draft": False,  # It might look like this publishes the item, but it doesn't
        "org-website": website,
        "careers-page": careers_page,
        "mission": mission,
        "accreditations-2": accreditations,
        "available-roles": available_roles,
        "currently-hiring-2": hiring,
        "biz": bizorchar,
        "sectors": sectors
    }}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.patch(url, json=payload, headers=headers)

    # Parse the text part of the response into JSON, then extract the collection item ID
    json_string = response.text
    data = json.loads(json_string)

    # Add the org's new Webflow item ID into the list of item IDs to publish
    if "_id" in data:
        org_ids_to_publish.append(data["_id"])

    # Simplest way to get around rate limiting issues
    time.sleep(1)


webflow_orgs_names = [org['name'] for org in webflow_orgs]
psql_orgs_names = [org['name'] for org in psql_orgs]

org_ids_to_delete = []

for org in webflow_orgs:
    if org['name'] not in psql_orgs_names:
        org_ids_to_delete.append(org['webflow_item_id'])

if org_ids_to_delete != []:
    delete_orgs_from_webflow(org_ids_to_delete)

org_ids_to_publish = []

for org in psql_orgs:
    if org['name'] not in webflow_orgs_names:
        add_new_org_to_webflow(name=org['name'], website=org['website'], careers_page=org['careers_page'],
                               mission=org['mission'], accreditations=org['accreditations'],
                               available_roles=org['available_roles'], hiring=org['currently_hiring'],
                               bizorchar=org['biz_or_char'], sectors=org['sectors'])
    else:
        if org not in webflow_orgs: # i.e. if the org's attributes are different in psql vs webflow
            patch_org_in_webflow(webflow_item_id=org['webflow_item_id'], webflow_slug=org['webflow_slug'],
                                 org_name=org['name'], website=org['website'], careers_page=org['careers_page'],
                                 mission=org['mission'], accreditations=org['accreditations'],
                                 available_roles=org['available_roles'], hiring=org['currently_hiring'],
                                 bizorchar=org['biz_or_char'], sectors=org['sectors'])


# Publish the new / patched orgs in Webflow
def publish_items(collection, list_of_item_ids):
    """ Publish multiple items in a single Webflow collection """

    # Get your Webflow authorisation token
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = f"https://api.webflow.com/collections/{get_webflow_collections()[collection]}/items/publish"

    payload = {"itemIds": list_of_item_ids}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.put(url, json=payload, headers=headers)

    print(response.text)


if org_ids_to_publish != []:
    publish_items('Organisations', org_ids_to_publish)

# Commit the changes
conn.commit()

# Close the database connection
cursor.close()
conn.close()