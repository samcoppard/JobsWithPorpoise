import os


def runpy(filename):
    """Run individual files in the current working directory"""
    command = "python3 " + filename
    os.system(command)


def scrape_to_postgres_to_webflow():
    """Run all of the files that are required each day, in the correct order"""

    # Run the file that scrapes jobs
    runpy("scraping.py")

    # Run the file that cleans job titles and locations
    runpy("job_data_cleaning.py")

    # Run the file that categorises scraped jobs
    runpy("categorisation.py")

    # Run the file that updates Postgres and Webflow with removed jobs
    runpy("old_jobs.py")

    # Run the file that updates Postgres and Webflow with new jobs
    runpy("new_jobs.py")

    # Run the file that cleans the job types each organisation is hiring for
    runpy("org_data_cleaning.py")

    # Run the file that updates organisations in Postgres
    runpy("psql_org_update.py")

    # Run the file that syncs orgs in Webflow CMS with orgs in psql
    runpy("org_sync.py")


scrape_to_postgres_to_webflow()
print("Done!")
