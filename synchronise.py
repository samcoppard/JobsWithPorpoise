import os
import time

# Create a method to run individual files

def runpy(filename):
    string = 'python3 ' + './Jobs_With_Porpoise/' + filename
    os.system(string)

# Create a method to run everything

def scrape_to_postgres_to_webflow():
    # Run the file that scrapes jobs
    runpy("scraping.py")

    # Run the file that categorises scraped jobs
    runpy("categorisation.py")

    # Run the file that updates Postgres and Webflow with removed jobs
    runpy("old_jobs.py")

    # Run the file that updates Postgres and Webflow with new jobs
    runpy("new_jobs.py")


scrape_to_postgres_to_webflow()
print("Done!")