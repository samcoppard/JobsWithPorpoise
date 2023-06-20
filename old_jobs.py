""" Pull all live jobs from the PSQL database, and check if they're in the most recent scrape.
    Any jobs that haven't been scraped again are no longer live, so we update the jobs in
    PSQL and delete them from Webflow """

import pandas as pd
from datetime import date
import psql_functions
import webflow_functions

# Pull in the scraped and categorised jobs as a dataframe
categorised_jobs_csv = pd.read_csv("categorised_jobs.csv")
scraped_jobs = pd.DataFrame(categorised_jobs_csv)

# Connect to the PSQL database and create a cursor object
conn, cursor = psql_functions.connect_to_psql_database()

# Pull all jobs from PSQL database that were scraped, have a Webflow item ID, and are live
cursor.execute(
    "SELECT * FROM jobs_for_webflow \
               WHERE date_removed IS null \
               AND job_scraped IS TRUE \
               AND job_webflow_id IS NOT null;"
)

live_webflow_jobs_from_psql = cursor.fetchall()

# Create a list to store the Webflow item IDs of the jobs we're going to delete
records_to_delete = []

# Check each live job to see if it's been scraped again
for job in live_webflow_jobs_from_psql:
    if job["concat_name"] not in scraped_jobs["concat"].tolist():
        # If a job is no longer live, add its item ID to the list of item IDs to delete
        records_to_delete.append(job["job_webflow_id"])

        # And update the PSQL database to say the job was removed today
        cursor.execute(
            "UPDATE jobs \
                      SET date_removed = TO_DATE(%s, 'YYYY-MM-DD') \
                      WHERE concat_name = %s \
                      AND date_removed IS NULL;",
            (str(date.today()), job["concat_name"]),
        )

# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)

# Now delete these expired jobs from Webflow
webflow_functions.delete_webflow_items("Jobs", records_to_delete)
