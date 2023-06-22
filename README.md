# Jobs With Porpoise

This is the code that powers the back end of [Jobs With Porpoise](https://www.jobswithporpoise.com), which now has 3x more jobs than any other known green job board in the UK.

A daily cron job runs the file __synchronise.py__, which runs the following files in turn:
- __scraping.py__
    * 9000+ lines of code to scrape 1500+ jobs from the careers pages of 250+ green organisations

- __categorisation.py__
    * Formats the job titles so everything's nice and uniform
    * Filters out non-UK jobs
    * Maps the remaining jobs to the correct area of the UK
    * Maps each role to the job categories it fits under e.g. Marketing or Software
    * Maps each role to its seniority level
    * Creates a separate dataframe to store all the job categories each organisation is currently hiring for

- __old_jobs.py__
    * Checks all the current live jobs to see if they've been scraped this time around
    * If they haven't, those jobs have an end date added in a locally hosted PostgreSQL database
    * They're then also deleted from the Webflow CMS

- __new_jobs.py__
    * Checks all the scraped jobs to see which ones are new today i.e. not already in the PostgreSQL database
    * Any new jobs are added to the database
    * They're also added to the Webflow CMS (with many interlinked records to make things fun) and published to the live site

- __org_data_cleaning.py__
    * Computes the unique job categories each organisation is currently hiring for

- __psql_org_update.py__
    * Updates the PostgreSQL database with the job categories each organisation is currently hiring for

- __org_sync.py__
    * Syncs any changes made to organisations in the PostgreSQL database across to the Webflow CMS
   
_N.B. This is a new repo that replaces an earlier private repo, which would have exposed sensitive information if I made it public._
