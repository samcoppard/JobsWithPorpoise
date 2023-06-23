import os


# Create a method to run individual files
def runpy(filename):
    string = "python3 " + "./JobsWithPorpoise/" + filename
    os.system(string)


# Create a method to run everything
def scrape_to_postgres_to_webflow():
    # Run the file that scrapes jobs
    runpy("scraping.py")

    # Run the file that cleans job titles and locations
    print("Cleaning job titles and locations...")
    runpy("job_data_cleaning.py")

    # Run the file that categorises scraped jobs
    print("Categorising jobs...")
    runpy("categorisation.py")

    # Run the file that updates Postgres and Webflow with removed jobs
    print("Updating old jobs...")
    runpy("old_jobs.py")

    # Run the file that updates Postgres and Webflow with new jobs
    print("Adding new jobs...")
    runpy("new_jobs.py")

    # Run the file that cleans the job types each organisation is hiring for
    print("Cleaning org data...")
    runpy("org_data_cleaning.py")

    # Run the file that updates organisations in Postgres
    print("Updating orgs in PSQL...")
    runpy("psql_org_update.py")

    # Run the file that syncs orgs in Webflow CMS with orgs in psql
    print("Syncing orgs from PSQL to Webflow")
    runpy("org_sync.py")


scrape_to_postgres_to_webflow()
print("Done!")
