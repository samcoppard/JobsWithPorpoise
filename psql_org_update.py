import pandas as pd
import psql_functions

""" Update all organisations, in the PostgreSQL database and the Webflow CMS, to show which job roles (if any) they're currently hiring for.
    Note that the currently_hiring field in the organisations table in the database is automatically generated, so we don't need to touch it here. """

# We'll go through all the scraped orgs with job types available first, then deal with any orgs that no longer have jobs available

# Pull in the csv of orgs with job types
scraped_orgs_import = pd.read_csv('orgs_job_types.csv')

# Turn this into a dataframe
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

# Create an empty list to store all the orgs and their available job types that we need to update in PostgreSQL / Webflow
orgs_with_job_types_to_add = []

conn, cursor = psql_functions.connect_to_psql_database()

for ind in scraped_orgs.index:
  cursor.execute("UPDATE organisations \
                 SET available_roles = %s \
                 WHERE name = %s;",
                 (scraped_orgs['no dupes'][ind].split(', '), scraped_orgs['Company'][ind]))


# Now we need to set available_roles = null for all other scraped organisations
# (This should be null for non-scraped orgs anyway, unless I've added a job manually, in which case organisations.available_roles needs to be updated manually as well)

# Start off with a CTE to get all scraped organisations that do not have any live jobs associated with them in the jobs table of the PostgreSQL database
# Note that we have to filter 'jobs.date_removed IS NULL' as part of the JOIN statement, as jobs is the right hand table and this is a left join, so we can't do this filtering as part of the WHERE clause
cursor.execute("WITH scraped_orgs_not_hiring AS( \
    SELECT org.name \
    FROM organisations AS org \
    LEFT JOIN jobs ON org.name=jobs.organisation AND jobs.date_removed IS NULL \
    WHERE org.scraped=TRUE \
    GROUP BY org.name \
    HAVING COUNT(jobs.title)=0 \
) \
    UPDATE organisations \
    SET available_roles=NULL \
    WHERE name IN(SELECT * FROM scraped_orgs_not_hiring)")
# The second part of the SQL above is simply setting available_roles = NULL for all the organisations pulled in the CTE

psql_functions.close_psql_connection(conn, cursor)