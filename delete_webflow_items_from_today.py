"""
Delete all the jobs added to Webflow today - basically a way to easily undo any unexpected screw ups
"""

import requests
import json
from datetime import date
import keyring

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
            collection_items_list.append(
                {'Date added': item['date-added'], 'Webflow Item ID': item['_id']})

        if data['count'] + data['offset'] < data['total']:
            offset += 100
            get_collection_items(collection, offset)

        return collection_items_list


collection_items_list = []
collection = 'Jobs'
offset = 0

get_webflow_collections()
get_collection_items(collection, offset)
print(collection_items_list)
tdy = date.today()

records_to_delete = [role['Webflow Item ID']
                   for role in collection_items_list if role['Date added'][:10] == tdy]

records_to_delete_100 = records_to_delete[:100]


url = "https://api.webflow.com/collections/6347d24d945dd61cc70ba3de/items"

payload = {"itemIds": records_to_delete_100}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {webflow_token}"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.text)
