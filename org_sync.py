""" Update organisations in the Webflow CMS so that they match the details in
    the PSQL database """

import requests
import json
import time
import psql_functions
import webflow_functions

""" Pull all the attributes we're going to need for every org in the PSQL database """

# Connect to the PSQL database and create a cursor object
conn, cursor = psql_functions.connect_to_psql_database()

# Pull attributes for all organisations in PSQL database
cursor.execute(
    "SELECT name, mission, website, careers_page, sectors, available_roles, biz_or_char, \
        accreditations, currently_hiring, webflow_item_id, webflow_slug \
               FROM organisations;"
)
pulled_psql_orgs = cursor.fetchall()

# Convert these DictRow objects into regular python dictionaries
psql_orgs = [dict(org) for org in pulled_psql_orgs]


""" Pull all the same attributes for all orgs in the Webflow CMS """

webflow_orgs = webflow_functions.get_webflow_orgs_all_attributes()


""" Compare webflow orgs with PSQL orgs """

# Get the names and Webflow item IDs we'll need to map PSQL strings e.g. 'Software' to
# Webflow item IDs e.g. '6425b9336545cb72069357c7'
collection_items_dict = webflow_functions.get_static_collection_items()

# Transform PSQL attributes into Webflow attributes for each organisation
for org in psql_orgs:
    org["sectors"] = (
        [collection_items_dict[f"Sectors - {sector}"] for sector in org["sectors"]]
        if org["sectors"] is not None
        else ""
    )
    org["available_roles"] = (
        [
            collection_items_dict[f"Available roles - {role}"]
            for role in org["available_roles"]
        ]
        if org["available_roles"] is not None
        else ""
    )
    org["biz_or_char"] = (
        [
            collection_items_dict[f"Business or charities - {biz_type}"]
            for biz_type in org["biz_or_char"]
        ]
        if org["biz_or_char"] is not None
        else ""
    )
    org["accreditations"] = (
        [
            collection_items_dict[f"Accreditations - {accreditation}"]
            for accreditation in org["accreditations"]
        ]
        if org["accreditations"] is not None
        else ""
    )
    org["currently_hiring"] = "Yes" if org["currently_hiring"] == True else "No"


""" Delete from Webflow any orgs that are no longer in the PSQL database
    Add to Webflow any orgs that are in the PSQL database but not in Webflow
    Patch in Webflow any orgs whose attributes are different in the PSQL database """


# Get your Webflow site ID and API key
site_id = webflow_functions.get_webflow_site_id()
api_key = webflow_functions.get_webflow_api_key()


def add_new_org_to_webflow(
    webflow_api_key,
    name,
    website,
    careers_page,
    mission,
    accreditations,
    available_roles,
    hiring,
    bizorchar,
    sectors,
):
    """Create a new item in the Organisations collection, and return its Webflow item ID"""

    url = "https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items"

    payload = {
        "fields": {
            "slug": "",  # Webflow will auto-generate the slug if this is left blank
            "_archived": False,
            "_draft": False,  # Leaving this False doesn't publish the item
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
            "sectors": sectors,  # List of Webflow item IDs (or an empty string)
        }
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_api_key}",
    }

    response = requests.post(url, json=payload, headers=headers)

    # Parse the text part of the response into JSON, then extract the collection item ID
    json_string = response.text
    data = json.loads(json_string)

    # Add the org's new Webflow item ID into the list of item IDs to publish
    if "_id" in data:
        org_ids_to_publish.append(data["_id"])

        # Add the job's Webflow item ID into the postgres database
        cursor.execute(
            "UPDATE organisations \
                    SET webflow_item_id = %s,  webflow_slug = %s\
                    WHERE name = %s;",
            (data["_id"], data["slug"], name),
        )

    # Deal with rate limiting issues (will do something more sophisticated in future)
    time.sleep(1)


def patch_org_in_webflow(
    webflow_api_key,
    webflow_item_id,
    webflow_slug,
    org_name,
    website,
    careers_page,
    mission,
    accreditations,
    available_roles,
    hiring,
    bizorchar,
    sectors,
):
    """Patch an item in the Organisations collection"""

    url = f"https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items/{webflow_item_id}"

    payload = {
        "fields": {
            "slug": webflow_slug,  # required
            "name": org_name,  # required
            "_archived": False,
            "_draft": False,  # Leaving this False doesn't publish the item
            "org-website": website,
            "careers-page": careers_page,
            "mission": mission,
            "accreditations-2": accreditations,
            "available-roles": available_roles,
            "currently-hiring-2": hiring,
            "biz": bizorchar,
            "sectors": sectors,
        }
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_api_key}",
    }

    response = requests.patch(url, json=payload, headers=headers)

    # Parse the text part of the response into JSON, then extract the collection item ID
    json_string = response.text
    data = json.loads(json_string)

    # Add the org's new Webflow item ID into the list of item IDs to publish
    if "_id" in data:
        org_ids_to_publish.append(data["_id"])

    # Deal with rate limiting issues (will do something more sophisticated in future)
    time.sleep(1)


# Create a list containing the names of all organisations in Webflow, and the same for PSQL
webflow_orgs_names = [org["name"] for org in webflow_orgs]
psql_orgs_names = [org["name"] for org in psql_orgs]

# Check for any orgs that are in Webflow but not in PSQL, and delete any you find
org_ids_to_delete = []

for org in webflow_orgs:
    if org["name"] not in psql_orgs_names:
        org_ids_to_delete.append(org["webflow_item_id"])

if org_ids_to_delete != []:
    webflow_functions.delete_webflow_items("Organisations", org_ids_to_delete)


# Now check orgs in PSQL against those in Webflow
org_ids_to_publish = []

# If any are in PSQL but not Webflow, add them to Webflow
for org in psql_orgs:
    if org["name"] not in webflow_orgs_names:
        add_new_org_to_webflow(
            webflow_api_key=api_key,
            name=org["name"],
            website=org["website"],
            careers_page=org["careers_page"],
            mission=org["mission"],
            accreditations=org["accreditations"],
            available_roles=org["available_roles"],
            hiring=org["currently_hiring"],
            bizorchar=org["biz_or_char"],
            sectors=org["sectors"],
        )
    # Patch any orgs in Webflow that have different attributes in PSQL
    else:
        if (
            org not in webflow_orgs
        ):  # i.e. if the org's attributes are different in PSQL vs Webflow
            patch_org_in_webflow(
                webflow_api_key=api_key,
                webflow_item_id=org["webflow_item_id"],
                webflow_slug=org["webflow_slug"],
                org_name=org["name"],
                website=org["website"],
                careers_page=org["careers_page"],
                mission=org["mission"],
                accreditations=org["accreditations"],
                available_roles=org["available_roles"],
                hiring=org["currently_hiring"],
                bizorchar=org["biz_or_char"],
                sectors=org["sectors"],
            )


# Publish the new / patched orgs in Webflow
if org_ids_to_publish != []:
    webflow_functions.publish_webflow_items("Organisations", org_ids_to_publish)

# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)
