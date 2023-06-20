""" Update all organisations in the PSQL database to show which job types they're currently hiring for (if any).
    N.B. The organisations.currently_hiring field is automatically generated, so we don't need to touch it here. """

import pandas as pd
import psql_functions

""" Deal with the scraped orgs that are currently hiring first """

# Pull in the scraped orgs that are currently hiring (and the job types they're hiring for) as a dataframe
scraped_orgs_import = pd.read_csv('orgs_job_types.csv')
scraped_orgs = pd.DataFrame(scraped_orgs_import)

# Remove any rows where the 'no dupes' column is empty (i.e. none of that organisation's open roles were successfully mapped to a job type)
scraped_orgs = scraped_orgs.dropna(subset=['no dupes']).reset_index(drop=True)

# Now we need to clean up the 'no dupes' field before the rest is going to work. Issues are caused by jobs that aren't matched to a job type, which either end up as ", " at the start of the 'no dupes' field, or as "," at the end, or as ", , " in the middle

# Fix the middle first
scraped_orgs['no dupes'] = scraped_orgs['no dupes'].apply(
    lambda x: x.replace(", , ", ", "))
# Now the start
scraped_orgs['no dupes'] = scraped_orgs['no dupes'].apply(
    lambda x: x[2:] if x[0] == "," else x)
# Now the end
scraped_orgs['no dupes'] = scraped_orgs['no dupes'].apply(
    lambda x: x[:-1] if x[-1] == "," else x)

# Connect to the PSQL database and create a cursor object
conn, cursor = psql_functions.connect_to_psql_database()

# Update the available roles for each organisation in PSQL
for ind in scraped_orgs.index:
  cursor.execute("UPDATE organisations \
                 SET available_roles = %s \
                 WHERE name = %s;",
                 (scraped_orgs['no dupes'][ind].split(', '), scraped_orgs['Company'][ind]))


""" Now we deal with all the other scraped orgs i.e. the ones that are not currently hiring """

# Use a CTE to get all scraped organisations that do not have any live jobs associated with them in the jobs table of the PSQL database
# Then set available_roles = null for all the organisations pulled in the CTE
cursor.execute("WITH scraped_orgs_not_hiring AS ( \
    SELECT org.name \
    FROM organisations AS org \
    LEFT JOIN jobs ON org.name=jobs.organisation AND jobs.date_removed IS NULL \
    WHERE org.scraped = TRUE \
    GROUP BY org.name \
    HAVING COUNT(jobs.title) = 0 \
) \
    UPDATE organisations \
    SET available_roles = NULL \
    WHERE name IN (SELECT * FROM scraped_orgs_not_hiring)")

# Commit changes and close the PSQL connection
psql_functions.close_psql_connection(conn, cursor)

""" N.B. Any organisations that haven't been scraped, but have had jobs manually added, also need to be updated manually for now """