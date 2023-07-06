""" Clean up the scraped jobs so that you can effectively categorise them later """

import pandas as pd
import data_cleaning_functions as dcf

# Pull in the scraped jobs as a dataframe
scraped_csv = pd.read_csv("scraped_jobs.csv")
scraped_jobs = pd.DataFrame(scraped_csv)

# Remove rows with empty values, and tidy up the scraped job titles and locations
dcf.remove_incomplete_rows(scraped_jobs)
dcf.clean_locations(scraped_jobs, "Location")
dcf.clean_job_titles(scraped_jobs, "Job Title")
dcf.convert_df_column_to_title_case(scraped_jobs, "Job Title")

# Create a column that concatenates org - role - location
dcf.create_concat_column(scraped_jobs)

# Export the dataframe of cleaned jobs to JSON
scraped_jobs.to_json("cleaned_jobs.json", orient="records")
