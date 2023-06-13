import requests
import json
import keyring

def get_webflow_site_id():
    """ Fetch Webflow site ID, stored locally in MacOS Keychain """

    webflow_site_id = keyring.get_password(
        "login", "Webflow Site ID")

    return webflow_site_id


def get_webflow_api_key():
    """ Fetch Webflow API key, stored locally in MacOS Keychain """

    webflow_api_key = keyring.get_password(
        "login", "Webflow Token")

    return webflow_api_key


def get_webflow_collections():
    """ Return a dictionary of all Webflow collection names and IDs """
    
    # Get your Webflow API key and site ID
    site_id = get_webflow_site_id()
    webflow_token = get_webflow_api_key()

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


def get_collection_items(collection, offset, dict={}):
    """ Return a dictionary of all item names and IDs for a particular collection """

    # Get your Webflow API key
    webflow_token = get_webflow_api_key()

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
            dict[f"{collection} - {item['name']}"] = item['_id']

        if data['count'] + data['offset'] < data['total']:
            offset += 100
            get_collection_items(collection, offset, dict)

        return dict



def get_static_collection_items():
    """ Return a dictionary of all item names and IDs for all static collections i.e. not Jobs or Organisations, plus IDs for dropdown options """
    static_collection_items_dict = {}

    for collection in ['Sectors', 'Accreditations', 'Business or charities', 'Available roles', 'Locations', 'Seniorities']:
        get_collection_items(collection, offset=0, dict=static_collection_items_dict)

    # Add the extra IDs you need that aren't stored in collections (these are dropdown options in Webflow)
    static_collection_items_dict["Multiple locations - true"] = "455ae768ed4cb346f4a0e6a28621f8bf"
    static_collection_items_dict["Multiple locations - false"] = "27ac7f940152cdfc8a8368aa282da9e3"
    static_collection_items_dict["Rewilding - true"] = "dacaf901d0aeed0c3359f1447380ada3"
    static_collection_items_dict["Rewilding - false"] = "4c1341378df85b075fe19ae70c0c9b96"
    static_collection_items_dict["BizOrChar - Business"] = "7f61f4cb6e6c23177283916a85bf40db"
    static_collection_items_dict["BizOrChar - Charity"] = "6396a5d85efc020870e39f39ac2758d8"

    return static_collection_items_dict



def delete_webflow_items(collection, list_of_item_ids):
    """ Delete multiple items in a single Webflow collection """

    # Get your Webflow API key
    webflow_token = get_webflow_api_key()

    url = f"https://api.webflow.com/collections/{get_webflow_collections()[collection]}/items"

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

    # Get your Webflow API key
    webflow_token = get_webflow_api_key()

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


def create_webflow_org(name, website, careers_page, mission, accreditations, available_roles, hiring, bizorchar, sectors):
    """ Create a new item in the Organisations collection, and return its Webflow item ID """

    # Get your Webflow API key
    webflow_token = get_webflow_api_key()

    url = "https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items"

    payload = {"fields": {
        "slug": "",  # Webflow will auto-generate the slug if this is left blank, avoiding duplication issues
        "_archived": False,
        "_draft": False,  # It might look like this publishes the item, but it doesn't
        "name": name,  # This doesn't need to be unique
        "org-website": website,
        "careers-page": careers_page,
        "mission": mission,
        "accreditations-2": accreditations, # List of Webflow item IDs (or an empty string)
        "available-roles": available_roles, # List of Webflow item IDs (or an empty string)
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
    return data["_id"]



def patch_webflow_org(org_webflow_id, org_slug, org_name, hiring, available_roles):
    """ Patch an item in the Organisations collection. We only ever need to change the 'currently hiring' and 'available roles' fields, so that's all this function does """

    # Get your Webflow API key
    webflow_token = get_webflow_api_key()
    
    url = f"https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items/{org_webflow_id}"

    payload = {"fields": {
        "slug": org_slug,  # required
        "name": org_name,  # required
        "_archived": False,
        "_draft": False,
        "currently-hiring-2": hiring,  # "Yes" or "No"
        "available-roles": available_roles  # List of Webflow item IDs (or an empty string)
    }}
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.patch(url, json=payload, headers=headers)

    print(response.text)



def publish_webflow_items(collection, list_of_item_ids):
    """ Publish multiple items in a single Webflow collection """

    # Get your Webflow API key
    webflow_token = get_webflow_api_key()

    url = f"https://api.webflow.com/collections/{get_webflow_collections()[collection]}/items/publish"

    payload = {"itemIds": list_of_item_ids}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.put(url, json=payload, headers=headers)

    print(response.text)
