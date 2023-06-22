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


def clean_job_types(list_of_job_types):
    """Separate out the job types for each job (so e.g. ["IT, HR"] becomes ["IT", "HR"])
    Then remove duplicate job types, and remove the string 'not mapped'"""
    split_job_types = [item for ele in list_of_job_types for item in ele.split(", ")]
    unique_job_types = list(set(split_job_types))
    unique_job_types = [string for string in unique_job_types if string != "not mapped"]
    return unique_job_types


# Create a new column to hold the unique job types each org is hiring for
orgs["unique_job_types"] = orgs["job_types"].apply(lambda lst: clean_job_types(lst))

# Remove any rows where the 'unique_job_types' column is []
# (i.e. none of that organisation's open roles were mapped to a job type)
orgs = orgs[orgs["unique_job_types"].apply(lambda x: x != [])]

# Remove the non-unique job_types column as it just needlessly takes up memory later
orgs = orgs.drop("job_types", axis=1)

# Export dataframe to JSON
orgs.to_json("orgs_job_types.json", orient="records")
