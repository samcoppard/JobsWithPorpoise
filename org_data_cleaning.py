import pandas as pd

# Pull in the scraped and categorised jobs as a dataframe
categorised_jobs_csv = pd.read_csv("categorised_jobs.csv")
scraped_jobs = pd.DataFrame(categorised_jobs_csv)

# Create a new dataframe with a row for each org with scraped jobs,
# and a column containing all the job types available at each company
orgs = (
    scraped_jobs.groupby("Company")["job_types"]
    .apply(list)
    .reset_index(name="job_types")
)


def clean_job_types(lst):
    """Remove duplicate strings from a list, and remove the string 'not mapped' too"""
    unique_list = list(set(lst))
    mapped_list = [string for string in unique_list if string != "not mapped"]
    return mapped_list


# Create a new column to store unique job types
orgs["unique_job_types"] = orgs["job_types"].apply(lambda lst: clean_job_types(lst))

# Remove any rows where the 'unique_job_types' column is "" (i.e. none of that organisation's open roles were mapped to a job type)
# This works by creating a boolean mask, which is then negated using ~ (so that rows with unique_job_types == "" are False, and then used to subset the original dataframe)
orgs = orgs[~orgs["unique_job_types"].apply(lambda x: x == "")]

# Clean up the 'unique_job_types' field by removing excess commas in the middle, beginning or end of a value.
# These issues are caused by jobs that aren't matched to a job type
orgs["unique_job_types"] = (
    orgs["unique_job_types"].str.replace(", , ", ", ").str.strip(", ")
)

# There's no need to keep the non-unique job_types column, and it just takes up memory later, so let's remove that now
orgs = orgs.drop("job_types", axis=1)

# Export dataframe to csv
orgs.to_csv("orgs_job_types.csv", index=False)
