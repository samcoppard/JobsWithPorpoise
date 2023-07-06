""" Create a dataframe with two columns - one for the name of each organisation,
    and one for a list of the unique job categories that organisation is hiring for """

import pandas as pd
from data_cleaning_functions import clean_job_types

# Pull in the scraped and categorised jobs as a dataframe
categorised_jobs_import = pd.read_json("categorised_jobs.json")
scraped_jobs = pd.DataFrame(categorised_jobs_import)

# Create a new dataframe with a row for each org with scraped jobs,
# and a column containing all the job types available at each company
orgs = (
    scraped_jobs.groupby("Company")["job_types"]
    .apply(list)
    .reset_index(name="job_types")
)

# Create a new column to hold the unique job types each org is hiring for
orgs["unique_job_types"] = orgs["job_types"].apply(lambda lst: clean_job_types(lst))

# Remove any rows where the 'unique_job_types' column is []
# (i.e. none of that organisation's open roles were mapped to a job type)
orgs = orgs[orgs["unique_job_types"].apply(lambda x: x != [])]

# Remove the non-unique job_types column as it just needlessly takes up memory later
orgs = orgs.drop("job_types", axis=1)

# Export dataframe to JSON
orgs.to_json("orgs_job_types.json", orient="records")
