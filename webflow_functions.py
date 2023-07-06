import requests
import json
import keyring
import time


def get_site_id():
    """Fetch Webflow site ID, stored locally in MacOS Keychain"""

    webflow_site_id = keyring.get_password("login", "Webflow Site ID")

    return webflow_site_id


def get_api_key():
    """Fetch Webflow API key, stored locally in MacOS Keychain"""

    webflow_api_key = keyring.get_password("login", "Webflow Token")

    return webflow_api_key


site_id = get_site_id()
api_key = get_api_key()


def get_collections():
    """Return a dictionary of all Webflow collection names and IDs"""

    url = f"https://api.webflow.com/sites/{site_id}/collections"

    headers = {"accept": "application/json", "authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)

    json_string = response.text
    data = json.loads(json_string)

    collection_dict = {collection["name"]: collection["_id"] for collection in data}

    return collection_dict


def get_collection_items(collection, offset, dict={}):
    """Return a dictionary of all item names and IDs for a particular collection"""

    if collection not in [
        "Organisations",
        "Jobs",
        "Sectors",
        "Accreditations",
        "Business or charities",
        "Available roles",
        "Locations",
        "Seniorities",
    ]:
        print("Please use a valid collection name")

    else:
        # Cache the results of get_collections() to prevent unnecessary extra calls
        if not hasattr(get_collection_items, "get_collections"):
            get_collection_items.get_collections = get_collections()

        url = f"https://api.webflow.com/collections/{get_collection_items.get_collections[collection]}/items?limit=100&offset={offset}"

        headers = {"accept": "application/json", "authorization": f"Bearer {api_key}"}

        response = requests.get(url, headers=headers)

        # Parse the text part of the response into JSON
        json_string = response.text
        data = json.loads(json_string)

        # Add returned collection items and their item IDs to the dictionary
        for item in data["items"]:
            dict[f"{collection} - {item['name']}"] = item["_id"]

        if data["count"] + data["offset"] < data["total"]:
            offset += 100
            get_collection_items(collection, offset, dict)

        return dict


def get_static_collection_items():
    """Return a dictionary of all item names and IDs for all static collections i.e. not Jobs or Organisations, plus IDs for dropdown options"""
    static_collection_items_dict = {}

    for collection in [
        "Sectors",
        "Accreditations",
        "Business or charities",
        "Available roles",
        "Locations",
        "Seniorities",
    ]:
        get_collection_items(collection, offset=0, dict=static_collection_items_dict)

    # Add the extra IDs you need that aren't stored in collections (these are dropdown options in Webflow)
    static_collection_items_dict[
        "Multiple locations - true"
    ] = "455ae768ed4cb346f4a0e6a28621f8bf"
    static_collection_items_dict[
        "Multiple locations - false"
    ] = "27ac7f940152cdfc8a8368aa282da9e3"
    static_collection_items_dict[
        "Rewilding - true"
    ] = "dacaf901d0aeed0c3359f1447380ada3"
    static_collection_items_dict[
        "Rewilding - false"
    ] = "4c1341378df85b075fe19ae70c0c9b96"
    static_collection_items_dict[
        "BizOrChar - Business"
    ] = "7f61f4cb6e6c23177283916a85bf40db"
    static_collection_items_dict[
        "BizOrChar - Charity"
    ] = "6396a5d85efc020870e39f39ac2758d8"

    return static_collection_items_dict


def split_list_decorator(func):
    def wrapper(collection, list_of_item_ids):
        if len(list_of_item_ids) <= 100:
            return func(collection, list_of_item_ids)
        else:
            num_sublists = (len(list_of_item_ids) + 99) // 100
            for i in range(num_sublists):
                sublist = list_of_item_ids[i * 100 : (i + 1) * 100]
                func(collection, sublist)

    return wrapper


@split_list_decorator
def delete_items(collection, list_of_item_ids):
    """Delete multiple items in a single Webflow collection"""

    # No need to cache get_collections() because delete_items() is never called twice
    url = f"https://api.webflow.com/collections/{get_collections()[collection]}/items"

    payload = {"itemIds": list_of_item_ids}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}",
    }

    response = requests.delete(url, json=payload, headers=headers)

    print(response.text)


def create_job(prepped_dict_of_job_attributes):
    """Create a new item in the Jobs collection, and return its Webflow item ID"""

    # Check for valid HTML first
    if prepped_dict_of_job_attributes["job_link"][:4] != "http":
        raise ValueError("Link to apply contains invalid HTML")

    # If HTML is valid, go ahead and add the job to Webflow
    url = "https://api.webflow.com/collections/6347d24d945dd61cc70ba3de/items"

    payload = {
        "fields": {
            "slug": "",  # Webflow will auto-generate the slug if this is left blank
            "_archived": False,
            "_draft": False,  # Setting this to False leaves the item in draft
            "name": prepped_dict_of_job_attributes["job_name"],
            # This doesn't need to be unique
            "title": prepped_dict_of_job_attributes["job_title"],
            "link-to-apply": prepped_dict_of_job_attributes["job_link"],
            # YYYY-MM-DD format
            "date-added": prepped_dict_of_job_attributes["job_date"],
            "date-added-text": prepped_dict_of_job_attributes["job_date_str"],
            # List of Webflow item IDs
            "location-3": prepped_dict_of_job_attributes["job_location"],
            "multiple-locations": prepped_dict_of_job_attributes[
                "job_multiple_locations"
            ],
            # List of Webflow item IDs
            "seniority": prepped_dict_of_job_attributes["job_seniority"],
            # List of Webflow item IDs
            "type-of-job": prepped_dict_of_job_attributes["job_type"],
            # Single Webflow ID (this is a dropdown in Webflow)
            "rewilding": prepped_dict_of_job_attributes["job_rewilding"],
            # Single Webflow ID for the organisation
            "organisation": prepped_dict_of_job_attributes["org"],
            "organisation-name": prepped_dict_of_job_attributes["org_name"],
            "website": prepped_dict_of_job_attributes["org_website"],
            "careers-page": prepped_dict_of_job_attributes["org_careers_page"],
            "mission": prepped_dict_of_job_attributes["org_mission"],
            # List of Webflow item IDs (or an empty string)
            "accreditations": prepped_dict_of_job_attributes["org_accreditations"],
            # Single Webflow ID (this is a dropdown in Webflow)
            "bizorchar": prepped_dict_of_job_attributes["org_bizorchar"],
            # List of Webflow item IDs
            "sectors": prepped_dict_of_job_attributes["org_sectors"],
        }
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}",
    }

    response = requests.post(url, json=payload, headers=headers)

    # Parse the text part of the response into JSON, then extract the collection item ID
    json_string = response.text
    data = json.loads(json_string)
    return data["_id"]


def get_orgs_with_all_attributes(offset=0, orgs_list=[]):
    """Return a dictionary of all orgs in Webflow with all their key attributes"""

    url = f"https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items?limit=100&offset={offset}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_key}",
    }

    response = requests.get(url, headers=headers)

    # Parse the text part of the response into JSON
    json_string = response.text
    data = json.loads(json_string)

    # Add returned collection items and their item IDs to the dictionary
    for item in data["items"]:
        orgs_list.append(
            {
                "name": item["name"],
                "mission": item["mission"],
                "website": item["org-website"],
                "careers_page": item["careers-page"],
                "sectors": item["sectors"],
                "available_roles": item["available-roles"]
                if "available-roles" in item and item["available-roles"] is not None
                else "",
                "biz_or_char": item["biz"],
                "accreditations": item["accreditations-2"]
                if "accreditations-2" in item and item["accreditations-2"] is not None
                else "",
                "currently_hiring": item["currently-hiring-2"],
                "webflow_item_id": item["_id"],
                "webflow_slug": item["slug"],
            }
        )

    if data["count"] + data["offset"] < data["total"]:
        offset += 100
        get_orgs_with_all_attributes(offset, orgs_list)

    return orgs_list


def create_or_patch_org(create_or_patch, prepped_dict_of_org_attributes):
    """Create a new item in the Organisations collection, and return its Webflow item ID"""

    payload = {
        "fields": {
            "slug": ""
            if create_or_patch == "create"
            else prepped_dict_of_org_attributes["webflow_slug"],
            "_archived": False,
            "_draft": False,  # Setting this to False leaves the item in draft
            "name": prepped_dict_of_org_attributes["name"],
            "org-website": prepped_dict_of_org_attributes["website"],
            "careers-page": prepped_dict_of_org_attributes["careers_page"],
            "mission": prepped_dict_of_org_attributes["mission"],
            "accreditations-2": prepped_dict_of_org_attributes["accreditations"],
            "available-roles": prepped_dict_of_org_attributes["available_roles"],
            "currently-hiring-2": prepped_dict_of_org_attributes["currently_hiring"],
            "biz": prepped_dict_of_org_attributes["biz_or_char"],
            "sectors": prepped_dict_of_org_attributes["sectors"],
        }
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}",
    }

    if create_or_patch == "create":
        url = "https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items"
        response = requests.post(url, json=payload, headers=headers)
    else:
        url = f"https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items/{prepped_dict_of_org_attributes['webflow_item_id']}"
        response = requests.patch(url, json=payload, headers=headers)

    # Parse the text part of the response into JSON, then extract the collection item ID
    json_string = response.text
    data = json.loads(json_string)

    if create_or_patch == "create":
        return data["_id"], data["slug"]
    else:
        pass

    # Deal with rate limiting issues (will do something more sophisticated in future)
    time.sleep(1)


@split_list_decorator
def publish_items(collection, list_of_item_ids):
    """Publish multiple items in a single Webflow collection"""

    # No need to cache get_collections() because publish_items() is never called twice
    url = f"https://api.webflow.com/collections/{get_collections()[collection]}/items/publish"

    payload = {"itemIds": list_of_item_ids}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}",
    }

    response = requests.put(url, json=payload, headers=headers)

    print(response.text)


def prep_job_for_webflow(dict_of_job_attributes):
    """Map the PSQL fields of a job to the correctly formatted Webflow fields"""

    # Cache the results of get_static_collection_items() so we don't end up calling that
    # function hundreds of times when this function is called in a loop
    if not hasattr(prep_job_for_webflow, "collection_items_dict"):
        prep_job_for_webflow.collection_items_dict = get_static_collection_items()

    webflow_ready_job_attributes = {
        "job_name": dict_of_job_attributes["concat_name"],
        "job_title": dict_of_job_attributes["title"],
        "job_link": dict_of_job_attributes["link_to_apply"],
        "job_date": str(dict_of_job_attributes["date_added"]),
        "job_date_str": dict_of_job_attributes["date_added_string"],
        "job_location": [
            prep_job_for_webflow.collection_items_dict[f"Locations - {location}"]
            for location in dict_of_job_attributes["location"]
        ]
        if dict_of_job_attributes["location"] is not None
        else "",
        "job_multiple_locations": prep_job_for_webflow.collection_items_dict[
            "Multiple locations - true"
        ]
        if dict_of_job_attributes["multiple_locations"] == True
        else prep_job_for_webflow.collection_items_dict["Multiple locations - false"],
        "job_seniority": [
            prep_job_for_webflow.collection_items_dict[f"Seniorities - {seniority}"]
            for seniority in dict_of_job_attributes["seniority"]
        ]
        if dict_of_job_attributes["seniority"] is not None
        else "",
        "job_type": [
            prep_job_for_webflow.collection_items_dict[f"Available roles - {role_type}"]
            for role_type in dict_of_job_attributes["job_type"]
        ]
        if dict_of_job_attributes["job_type"] is not None
        else "",
        "job_rewilding": prep_job_for_webflow.collection_items_dict["Rewilding - true"]
        if dict_of_job_attributes["rewilding"] == True
        else prep_job_for_webflow.collection_items_dict["Rewilding - false"],
        "org": dict_of_job_attributes["org_webflow_id"],
        "org_name": dict_of_job_attributes["org_name"],
        "org_website": dict_of_job_attributes["website"],
        "org_careers_page": dict_of_job_attributes["careers_page"],
        "org_mission": dict_of_job_attributes["mission"],
        "org_accreditations": [
            prep_job_for_webflow.collection_items_dict[
                f"Accreditations - {accreditation}"
            ]
            for accreditation in dict_of_job_attributes["accreditations"]
        ]
        if dict_of_job_attributes["accreditations"] is not None
        else "",
        "org_bizorchar": prep_job_for_webflow.collection_items_dict[
            "BizOrChar - Business"
        ]
        if dict_of_job_attributes["borch"] == "Business"
        else prep_job_for_webflow.collection_items_dict["BizOrChar - Charity"],
        "org_sectors": [
            prep_job_for_webflow.collection_items_dict[f"Sectors - {sector}"]
            for sector in dict_of_job_attributes["sectors"]
        ]
        if dict_of_job_attributes["sectors"] is not None
        else "",
    }
    return webflow_ready_job_attributes


def prep_org_for_webflow(dict_of_org_attributes):
    """Map the PSQL fields of an org to the correctly formatted Webflow fields"""

    # Cache the results of get_static_collection_items() so we don't end up calling that
    # function hundreds of times when this function is called in a loop
    if not hasattr(prep_org_for_webflow, "collection_items_dict"):
        prep_org_for_webflow.collection_items_dict = get_static_collection_items()

    dict_of_org_attributes["sectors"] = (
        [
            prep_org_for_webflow.collection_items_dict[f"Sectors - {sector}"]
            for sector in dict_of_org_attributes["sectors"]
        ]
        if dict_of_org_attributes["sectors"] is not None
        else ""
    )
    dict_of_org_attributes["available_roles"] = (
        [
            prep_org_for_webflow.collection_items_dict[f"Available roles - {role}"]
            for role in dict_of_org_attributes["available_roles"]
        ]
        if dict_of_org_attributes["available_roles"] is not None
        else ""
    )
    dict_of_org_attributes["biz_or_char"] = (
        [
            prep_org_for_webflow.collection_items_dict[
                f"Business or charities - {biz_type}"
            ]
            for biz_type in dict_of_org_attributes["biz_or_char"]
        ]
        if dict_of_org_attributes["biz_or_char"] is not None
        else ""
    )
    dict_of_org_attributes["accreditations"] = (
        [
            prep_org_for_webflow.collection_items_dict[
                f"Accreditations - {accreditation}"
            ]
            for accreditation in dict_of_org_attributes["accreditations"]
        ]
        if dict_of_org_attributes["accreditations"] is not None
        else ""
    )
    dict_of_org_attributes["currently_hiring"] = (
        "Yes" if dict_of_org_attributes["currently_hiring"] == True else "No"
    )

    webflow_ready_org_attributes = dict_of_org_attributes
    return webflow_ready_org_attributes
