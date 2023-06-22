""" Update all organisations in the PSQL database to show which job types
    they're currently hiring for (if any).
    N.B. The organisations.currently_hiring field is automatically generated,
    so we don't need to touch it here. """

import pandas as pd
import psql_functions

""" Deal with the scraped orgs that are currently hiring first """

# Pull in the scraped orgs that are currently hiring (and the job types they're
# hiring for) as a dataframe
scraped_orgs_import = pd.read_json("orgs_job_types.json")
scraped_orgs = pd.DataFrame(scraped_orgs_import)

# Connect to the PSQL database and create a cursor object
conn, cursor = psql_functions.connect_to_psql_database()

# Update the available roles for each organisation in PSQL
for ind in scraped_orgs.index:
    cursor.execute(
        "UPDATE organisations \
                 SET available_roles = %s \
                 WHERE name = %s;",
        (
            scraped_orgs["unique_job_types"][ind],
            scraped_orgs["Company"][ind],
        ),
    )


""" Now deal with all the scraped orgs that are not currently hiring """

# Use a CTE to get all scraped organisations that do not have any live jobs
# associated with them in the jobs table of the PSQL database
# Then set available_roles = null for all the organisations that appear in the CTE
cursor.execute(
    "WITH scraped_orgs_not_hiring AS ( \
    SELECT org.name \
    FROM organisations AS org \
    LEFT JOIN jobs ON org.name=jobs.organisation AND jobs.date_removed IS NULL \
    WHERE org.scraped = TRUE \
    GROUP BY org.name \
    HAVING COUNT(jobs.title) = 0 \
) \
    UPDATE organisations \
    SET available_roles = NULL \
    WHERE name IN (SELECT * FROM scraped_orgs_not_hiring)"
)

# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)

""" N.B. Any organisations that haven't been scraped, but have had jobs
    manually added, will also need to be updated manually for now """
