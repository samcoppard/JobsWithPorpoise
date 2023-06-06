import requests
import json
import keyring

#Create a new item in the Organisations collection, and print its Webflow item ID at the end

# Get your Webflow authorisation token
webflow_token = keyring.get_password("login", "Webflow Token")

url = "https://api.webflow.com/collections/62e3ab17f169f84e746dc54e/items"

payload = {"fields": {
    "slug": "", #If you leave this blank, Webflow generates a slug for you, so you don't have to worry about accidentally providing a duplicate
    "name": "Another New Org", #This doesn't need to be unique
    "_archived": False,
    "_draft": False, #It might look like this publishes the item, but it doesn't
    "org-website": "https://neworg.com",
    "careers-page": "https://neworg.com/careers/",
    "mission": "Making the world a better place",
    "accreditations-2": ["6425b9332e038f164bb54855"], #If text array has no entries, this should just be "" without any []
    "available-roles": [
        "6425b92d6545cb2be7934fb6",
        "6425b9336545cb72069357c7"
    ],
    "currently-hiring-2": "No", #"Yes" or "No"
    "biz": ["6425b922570ac73def0deded"],
    "sectors": [
        "6425b9241912de59ad8a0ceb"
    ]
}}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {webflow_token}"
}

response = requests.post(url, json=payload, headers=headers)

#Parse the text part of the response into JSON, then extract the collection item ID
json_string = response.text
data = json.loads(json_string)
print(data["_id"])

