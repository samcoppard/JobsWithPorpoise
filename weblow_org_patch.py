#Patching allows us to only change specific fields, whereas updating is a complete replacement/modification of the collection item, so you'd need to enter all the fields, even the ones that aren't changing

import requests
import json
import keyring

# Get your Webflow authorisation token
webflow_token = keyring.get_password("login", "Webflow Token")

url = "https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items/6465fcbf5999b804c7a020a9" # /collections/collection_id/items/item_id

payload = {"fields": {
    "slug": "another-new-org-7", #required
    "name": "Another New Org", #required
    "_archived": False,
    "_draft": False,
    "currently-hiring-2": "Yes", #"Yes" or "No"
    "available-roles": [ #Set to "" if the org has no mapped jobs
        "6425b9321e7eec65aa48868e",
        "6425b92e1e7eeca6634880fe"
    ]
}}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {webflow_token}"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.text)
