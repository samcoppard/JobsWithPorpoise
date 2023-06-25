""" Check all scraped and categorised jobs to see if any are not in the PSQL database yet.
    Add all these new jobs to PSQL, then add them to Webflow, then add their Webflow item
    IDs to PSQL, and finally publish them all to the live site. """

import pandas as pd
from datetime import date
import time
import psql_functions
import webflow_functions as webflow

""" PSQL UPDATES """

# Pull in the scraped and categorised jobs as a dataframe
categorised_jobs_import = pd.read_json("categorised_jobs.json")
scraped_jobs = pd.DataFrame(categorised_jobs_import)

# Connect to the PSQL database and create a cursor object
conn, cursor = psql_functions.connect_to_psql_database()

# Pull all the live jobs (that were scraped) from the PSQL database,
# and create a list of all their long concatenated names
cursor.execute(
    "SELECT * FROM jobs_for_webflow \
               WHERE date_removed IS NULL \
               AND job_scraped IS TRUE;"
)

live_jobs_from_psql = cursor.fetchall()

psql_live_jobs_concats = [job["concat_name"] for job in live_jobs_from_psql]

# Write the query that will add a new job to the jobs table in the PSQL database
query_to_add_job_to_psql = """
    INSERT INTO jobs (
        concat_name, title, link_to_apply, organisation, job_type, seniority, location, date_added, date_added_string, date_removed
        )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, NULL
        )
    """

# Using the concat field, check if each scraped job is in the list of live jobs from PSQL
# Then add any scraped jobs that aren't already in the database to the database
for ind in scraped_jobs.index:
    if scraped_jobs["concat"][ind] not in psql_live_jobs_concats:
        job_attributes = (
            scraped_jobs["concat"][ind],
            scraped_jobs["Job Title"][ind],
            scraped_jobs["Job URL"][ind],
            scraped_jobs["Company"][ind],
            scraped_jobs["job_types"][ind].split(", "),
            scraped_jobs["seniority"][ind].split(", "),
            scraped_jobs["mapped_location"][ind].split(", "),
            date.today(),
            f"🗓  Posted {date.today().strftime('%d/%m/%y')}",
        )

        cursor.execute(query_to_add_job_to_psql, job_attributes)


""" WEBFLOW TIME """

# Pull a list of all the jobs we've just created in the database today
cursor.execute(
    "SELECT * FROM jobs_for_webflow \
               WHERE date_added = %s;",
    (date.today(),),
)

psql_jobs_created_today = cursor.fetchall()

# Store the Webflow item IDs of all the new jobs so we can publish them en masse later
item_ids_to_publish = []

for job in psql_jobs_created_today:
    # Map the PSQL fields of each new job to the correctly formatted Webflow fields
    # And then create a new item in the Webflow Jobs collection
    try:
        webflow_job_id = webflow.create_job(webflow.prep_job_for_webflow(job))
    except ValueError:
        continue

    item_ids_to_publish.append(webflow_job_id)

    # Add the job's Webflow item ID into the PSQL database
    cursor.execute(
        "UPDATE jobs \
                SET webflow_item_id = %s \
                WHERE concat_name = %s AND date_removed IS NULL;",
        (webflow_job_id, job["concat_name"]),
    )

    # Handle rate limiting issues in the simplest way possible (will improve in future)
    time.sleep(1)

# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)

# Publish all the new jobs in Webflow
if item_ids_to_publish != []:
    webflow.publish_items("Jobs", item_ids_to_publish)
