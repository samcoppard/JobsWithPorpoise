# Jobs With Porpoise

This is the code that powers the back end of [Jobs With Porpoise](https://www.jobswithporpoise.com), which now has 3x more jobs than any other known green job board in the UK.

A daily cron job runs the file __synchronise.py__, which runs the following files in turn:
- __scraping.py__
    * Scrapes 1500+ jobs from 250+ green organisations
    * Some are pulled from APIs, some are scraped from Applicant Tracking Systems, but most are scraped from individual careers pages

- __job_data_cleaning.py__
    * Removes any jobs with missing data
    * Formats the remaining job titles and locations to match a consistent style
    * Preps jobs for categorisation

- __categorisation.py__
    * Filters out non-UK jobs
    * Maps the remaining jobs to the correct area of the UK
    * Maps each role to the job categories it fits under e.g. Marketing or Software
    * Maps each role to its seniority level

- __old_jobs.py__
    * Checks all the current live jobs to see if they've been scraped this time around
    * If they haven't, those jobs have an end date added in a locally hosted PostgreSQL database
    * They're then also deleted from the Webflow CMS

- __new_jobs.py__
    * Checks all the scraped jobs to see which ones are new today i.e. not already in the PostgreSQL database
    * Any new jobs are added to the database
    * They're also added to the Webflow CMS (with many interlinked records to make things fun) and published to the live site

- __org_data_cleaning.py__
    * Maps the unique job categories each organisation is currently hiring for

- __psql_org_update.py__
    * Updates the PostgreSQL database with the job categories each organisation is currently hiring for

- __org_sync.py__
    * Syncs any changes made to organisations in the PostgreSQL database across to the Webflow CMS
