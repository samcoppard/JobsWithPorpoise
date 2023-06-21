""" Update organisations in the Webflow CMS so that they match the details in
    the PSQL database """

import psql_functions
import webflow_functions as webflow

""" Pull all the key attributes for every org in Webflow, and every org in PSQL """

# Pull attributes for Webflow orgs first
webflow_orgs = webflow.get_orgs_with_all_attributes()

# Then pull the PSQL orgs, and map the fields to Webflow fields so we can easily compare

# Connect to the PSQL database and create a cursor object
conn, cursor = psql_functions.connect_to_psql_database()

# Pull attributes for all organisations in PSQL database
cursor.execute(
    "SELECT name, mission, website, careers_page, sectors, available_roles, biz_or_char, \
        accreditations, currently_hiring, webflow_item_id, webflow_slug \
               FROM organisations;"
)
pulled_psql_orgs = cursor.fetchall()

# Convert these DictRow objects into regular python dictionaries, then
# map the PSQL fields of each org to the correctly formatted Webflow fields
# e.g. '🤖 Software' gets mapped to '6425b9336545cb72069357c7'
psql_orgs = [webflow.prep_org_for_webflow(dict(org)) for org in pulled_psql_orgs]


""" Delete from Webflow any orgs that are no longer in the PSQL database.
    Then add to Webflow any orgs that are in the PSQL database but not in Webflow.
    And patch in Webflow any orgs whose attributes are different in the PSQL database. """


# Create a list containing the names of all organisations in Webflow, and the same for PSQL
webflow_orgs_names = [org["name"] for org in webflow_orgs]
psql_orgs_names = [org["name"] for org in psql_orgs]

# Check for any orgs that are in Webflow but not in PSQL, and delete any you find
org_ids_to_delete = []

for org in webflow_orgs:
    if org["name"] not in psql_orgs_names:
        org_ids_to_delete.append(org["webflow_item_id"])

if org_ids_to_delete != []:
    webflow.delete_items("Organisations", org_ids_to_delete)


# Now check orgs in PSQL against those in Webflow
org_ids_to_publish = []

# If any are in PSQL but not Webflow, add them to Webflow
for org in psql_orgs:
    if org["name"] not in webflow_orgs_names:
        (
            webflow_org_id,
            webflow_org_slug,
        ) = webflow.create_or_patch_org("create", org)

        org_ids_to_publish.append(webflow_org_id)

        # Add the job's Webflow item ID into the postgres database
        cursor.execute(
            "UPDATE organisations \
                    SET webflow_item_id = %s,  webflow_slug = %s\
                    WHERE name = %s;",
            (webflow_org_id, webflow_org_slug, org["name"]),
        )

    # Check if the org's attributes are different in PSQL vs Webflow; patch any that are
    elif org not in webflow_orgs:
        # N.B. If nothing has changed in PSQL, then each org dict in psql_orgs should have
        # an org dict in webflow_orgs that matches it exactly
        webflow.create_or_patch_org("patch", org)

        org_ids_to_publish.append(org["webflow_item_id"])


# Publish the new / patched orgs in Webflow
if org_ids_to_publish != []:
    webflow.publish_items("Organisations", org_ids_to_publish)

# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)
