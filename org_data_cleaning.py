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


def test_func(lst):
    new_list = [item for element in lst for item in element.split(", ")]
    return new_list


orgs["job_types"] = orgs["job_types"].apply(lambda lst: test_func(lst))


def clean_job_types(lst):
    """Remove duplicate strings from a list, and remove the string 'not mapped' too"""
    unique_list = list(set(lst))
    mapped_list = [string for string in unique_list if string != "not mapped"]
    return mapped_list


# Create a new column to hold the unique job types each org is hiring for
orgs["unique_job_types"] = orgs["job_types"].apply(lambda lst: clean_job_types(lst))


# Export dataframe to csv
orgs.to_csv("orgs_job_types.csv", index=False)
