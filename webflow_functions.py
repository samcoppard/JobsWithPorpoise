import requests
import json
import keyring

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

    collection_dict = {collection["name"]: collection["_id"] for collection in data}

    return collection_dict


def get_collection_items(collection, offset, collection_items_dict={}):
    """Return a dictionary of all item names and IDs for a particular collection"""

    # Get your Webflow authorisation token
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
            collection_items_dict[item['name']] = item['_id']

        if data['count'] + data['offset'] < data['total']:
            offset += 100
            get_collection_items(collection, offset, collection_items_dict)

        return collection_items_dict



def delete_webflow_jobs(list_of_item_ids):
    """ Delete all Webflow item IDs provided in a list, provided they're all in the Jobs collection """

    # Get your Webflow authorisation token
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = "https://api.webflow.com/collections/6347d24d945dd61cc70ba3de/items"

    payload = {"itemIds": list_of_item_ids}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.delete(url, json=payload, headers=headers)

    print(response.text)



def create_webflow_job(job_name, job_title, job_link, job_date, job_date_str, job_location, job_multiple_locations, job_seniority, job_type, job_rewilding, org, org_name, org_website, org_careers_page, org_mission, org_accreditations, org_bizorchar, org_sectors):
    """ Create a new item in the Jobs collection, and return its Webflow item ID """

    # Get your Webflow authorisation token
    webflow_token = keyring.get_password("login", "Webflow Token")

    url = "https://api.webflow.com/collections/6347d24d945dd61cc70ba3de/items"

    payload = {"fields": {
        "slug": "",  # Webflow will auto-generate the slug if this is left blank, avoiding duplication issues
        "_archived": False,
        "_draft": False,  # It might look like this publishes the item, but it doesn't
        "name": job_name,
        "title": job_title,  # This doesn't need to be unique
        "link-to-apply": job_link,
        "date-added": job_date,  # YYYY-MM-DD format
        "date-added-text": job_date_str,
        "location-3": job_location, # List of Webflow item IDs
        "multiple-locations": job_multiple_locations,
        "seniority": job_seniority,  # List of Webflow item IDs
        "type-of-job": job_type,  # List of Webflow item IDs
        "rewilding": job_rewilding,  # Single Webflow ID (this is a dropdown in Webflow)
        "organisation": org,  # Single Webflow ID for the organisation
        "organisation-name": org_name,
        "website": org_website,
        "careers-page": org_careers_page,
        "mission": org_mission,
        "accreditations": org_accreditations,  # List of Webflow item IDs (or an empty string)
        "bizorchar": org_bizorchar,  # Single Webflow ID (this is a dropdown in Webflow)
        "sectors": org_sectors  # List of Webflow item IDs
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
    return data["_id"]



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
