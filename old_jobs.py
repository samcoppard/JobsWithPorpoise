import pandas as pd
from datetime import date
import requests
import keyring
import psql_functions

# Pull in the csv of categorised jobs
scraped_csv = pd.read_csv('categorised_jobs.csv')

# Turn this into a dataframe
scraped_jobs = pd.DataFrame(scraped_csv)

# Restrict the 'concat' column to 255 characters, so the format matches that in Postgres (otherwise you delete and recreate jobs with long concat names every day)
scraped_jobs['concat'] = [i[:255] for i in scraped_jobs['concat']]

conn, cursor = psql_functions.connect_to_psql_database()

# Create an empty list to populate with Webflow item IDs of the jobs that we're going to remove
records_to_delete = []

# Get today's date (so we can add it to the date_removed field in SQL for jobs that are no longer live)
tdy = date.today()

# Execute query to only get jobs that were scraped, that are still live, and that have an item ID in Webflow (a few never get added to Webflow if there's an error e.g. a URL field doesn't start with http)
cursor.execute("SELECT * FROM jobs_for_webflow \
               WHERE date_removed IS null \
               AND job_scraped IS TRUE \
               AND job_webflow_id IS NOT null;")

# Fetch the results, then check if each job has been scraped
# If a job hasn't been scraped, that means it's no longer live, so we add its Webflow item ID to the list of item IDs to delete
# And then we update the SQL database with the date the job was removed
rows = cursor.fetchall()
for row in rows:
    if row[0] not in scraped_jobs['concat'].tolist():
       records_to_delete.append(row[12])
       # To use variables in the SQL query that are defined elsewhere in the script, we have to use parameterized queries (with '%s' as a placeholder, and then the outside variables added in a tuple as a second argument) 
       cursor.execute("UPDATE jobs \
                      SET date_removed = TO_DATE(%s, 'YYYY-MM-DD') \
                      WHERE concat_name = %s \
                      AND date_removed IS NULL;", (str(tdy), row[0]))

psql_functions.close_psql_connection(conn, cursor)

# Now delete these expired jobs from Webflow

# Get your Webflow authorisation token
webflow_token = keyring.get_password("login", "Webflow Token")

def delete_webflow_jobs(list):
    url = "https://api.webflow.com/collections/6347d24d945dd61cc70ba3de/items"

    payload = {"itemIds": list}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {webflow_token}"
    }

    response = requests.delete(url, json=payload, headers=headers)

    print(response.text)

delete_webflow_jobs(records_to_delete)