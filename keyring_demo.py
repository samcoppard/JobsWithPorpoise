import keyring

keyring.set_password("login", "Account Name e.g. Airtable API",
                     "API_key")

airtable_api_key = keyring.get_password(
    "login", "Account Name e.g. Airtable API")

print(airtable_api_key)


