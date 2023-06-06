import os
import requests
import json
from pyairtable import Table, utils
from datetime import date
import pandas as pd

# Pull in the csv of categorised jobs
scraped_csv = pd.read_csv('categorised_jobs.csv')

# Turn this into a dataframe
scraped_jobs = pd.DataFrame(scraped_csv)

# Fetch your personal access token, stored in MacOS Keychain
import keyring
api_key = keyring.get_password("login", "Airtable PAT")

# We're going to be using the Table class here as we're only changing things in the Jobs table
jobs_table = Table(api_key, 'appMMCMN6W3Ica4z3', 'tblLs2iM1yQciaCmw')

# Fetch all the records in the Jobs table, excluding those that are not scraped or are 'semi-scraped' according to Airtable
records = jobs_table.all(fields=['Name'], sort=[
                         'Name'], formula="NOT(OR({Scraped?}=0, {Semi-scraped}=1))")

# Create an empty list to populate with record IDs of jobs that we're going to remove
records_to_delete = []

# Iterate over every job in Airtable
for job in records:
  # If the job also appears in the list of jobs we've scraped, then we don't need to do anything
  if job['fields']['Name'] in scraped_jobs['concat'].tolist():
    continue
  # If the job hasn't been scraped, then we need to delete it from Airtable. This will be nicer to do in one big batch, so we'll just add these to a list for now
  else:
    records_to_delete.append(job['id'])

# Now delete the records of jobs that are no longer active
jobs_table.batch_delete(records_to_delete)


# Going the other way (iterating over every job we've scraped to add the new ones) is a lot more complicated

# We need a list of jobs in Airtable to compare with, so let's create a list containing the name of every job in Airtable
airtable_concats = [job['fields']['Name'] for job in records]

# And an empty list to contain details of all the new jobs we're going to add to Airtable
new_records = []


# For every field that links to another record, we're going to have to find the record ID for the linked record in order to upload all the details to Airtable. Let's start with getting the record IDs for all the organisations in Airtable:

# Access the 'All Organisations' table
orgs_table = Table(api_key, 'appMMCMN6W3Ica4z3', 'tblcqjayNWs42jBBg')
# Fetch the names of every organisation in Airtable (which actually produces a list of dictionaries, which gives us the name and record ID of each organisation)
all_orgs = orgs_table.all(fields=['Name'], sort=['Name'])
# Now we can use a dictionary comprehension to make a big dictionary with org names as the keys and record IDs as the values
all_orgs_dict = {org['fields']['Name']: org['id'] for org in all_orgs}
# Then we can easily look up the record ID for any given organisation if we know its name


# And now we've got to do the same for the 'Job roles', 'Locations', and 'Seniority' tables...
job_roles_table = Table(api_key, 'appMMCMN6W3Ica4z3', 'tblcjD3EIT9D1LHve')
all_job_roles = job_roles_table.all(fields=['Name'], sort=['Name'])
all_job_roles_dict = {job_role['fields']['Name']: job_role['id'] for job_role in all_job_roles}

locations_table = Table(api_key, 'appMMCMN6W3Ica4z3', 'tblsSU0r3H0J3bW3A')
all_locations = locations_table.all(fields=['Name'], sort=['Name'])
all_locations_dict = {location['fields']['Name']: location['id'] for location in all_locations}

seniorities_table = Table(api_key, 'appMMCMN6W3Ica4z3', 'tblJJXvIsFhFzuh05')
all_seniorities = seniorities_table.all(fields=['Name'], sort=['Name'])
all_seniorities_dict = {seniority['fields']['Name']: seniority['id'] for seniority in all_seniorities}


# Finally, we need to get today's date in an Airtable compatible ISO 8601 string so that we can put it in the 'Date added' field
tdy = utils.date_to_iso_str(date.today())

for ind in scraped_jobs.index:
  if scraped_jobs['concat'][ind] in airtable_concats:
    continue
  else:
    new_records.append({
        'Name': scraped_jobs['concat'][ind],
        'Title': scraped_jobs['Job Title'][ind],
        'Organisation': [all_orgs_dict[scraped_jobs['Company'][ind]]],
        'Link to apply': scraped_jobs['Job URL'][ind],
        # Got to use list comprehensions for the next few because each job could be mapped to more than one type of job, location, or seniority. So we split up the e.g. job types we've mapped the role to, which creates a list, and then we can easily find the record ID for each of those job types using the dictionary we created above
        'Type of job': [all_job_roles_dict[k] for k in scraped_jobs['job_types'][ind].split(", ")],
        'Location': [all_locations_dict[k] for k in scraped_jobs['mapped_location'][ind].split(", ")],
        'Seniority': [all_seniorities_dict[k] for k in scraped_jobs['seniority'][ind].split(", ")],
        'Date added': tdy,
        'Date added string': "🗓 Posted " + date.today().strftime('%d/%m/%y')
    })
 
# We need to check for any duplicate records before sending to Airtable, or else this will cause errors

unique_dicts = []  # initialize an empty list to store the unique dictionaries
seen_names = set()  # initialize an empty set to keep track of seen 'Name' values

for d in new_records:
  if d['Name'] not in seen_names:  # if 'Name' is not a duplicate
    # add the dictionary to the list of unique dictionaries
    unique_dicts.append(d)
    seen_names.add(d['Name'])  # add the 'Name' value to the set of seen names

# And finally we can batch create all the new unique records
jobs_table.batch_create(unique_dicts)


# ORGANISATIONS

# Need to automatically update the job types available for each organisation as well. We'll go through all the scraped orgs with job types available first, and add / update those job types in Airtable. Then we'll delete all the job types for orgs in Airtable that no longer have jobs available

# We're going to be using the Table class again
orgs_table = Table(api_key, 'appMMCMN6W3Ica4z3', 'tblcqjayNWs42jBBg')

# ADDING / UPDATING

# Pull in the csv of orgs with job types
scraped_orgs_import = pd.read_csv('orgs_job_types.csv')

# Turn this into a dataframe
scraped_orgs = pd.DataFrame(scraped_orgs_import)

# Remove any rows where the 'no dupes' column is empty (i.e. none of that organisation's open roles were successfully mapped to a job type)
scraped_orgs = scraped_orgs.dropna(subset=['no dupes']).reset_index(drop=True)

# Now we need to clean up the 'no dupes' field before the rest is going to work. Issues are caused by jobs that aren't matched to a job type, which either end up as ", " at the start of the 'no dupes' field, or as "," at the end, or as ", , " in the middle

# Fix the middle first
scraped_orgs['no dupes'] = scraped_orgs['no dupes'].apply(
    lambda x: x.replace(", , ", ", "))
# Now the start
scraped_orgs['no dupes'] = scraped_orgs['no dupes'].apply(
    lambda x: x[2:] if x[0] == "," else x)
# Now the end
scraped_orgs['no dupes'] = scraped_orgs['no dupes'].apply(
    lambda x: x[:-1] if x[-1] == "," else x)

# Create an empty list to store all the orgs and their available job types that we need to add to / update in Airtable
orgs_with_job_types_to_add = []

# Find the record ID for each organisation with job types to add, and the record IDs for those job types
for ind in scraped_orgs.index:
  a = all_orgs_dict[scraped_orgs['Company'][ind]]
  b = [all_job_roles_dict[k]
       for k in scraped_orgs['no dupes'][ind].split(", ")]
  # Then append a dictionary for each of these organisations to the list above, containing both the org ID and the job type IDs
  orgs_with_job_types_to_add.append(
      {'id': a, "fields": {'Available roles': b}})

# Now we can batch update all of those organisations in Airtable, giving them the correct available roles
orgs_table.batch_update(orgs_with_job_types_to_add)


# DELETING

# Pull in a list of all orgs in Airtable that have job types associated with them, giving the name of each org and their current jobs and job types
airtable_orgs = orgs_table.all(fields=['Name', 'Available roles', 'Jobs'], sort=[
                               'Name'], formula="{Available roles}!=''")

# Create an empty list to hold the record IDs of all the organisations with job types listed but which should no longer have any job types associated with them
orgs_with_job_types_to_delete = []

# Iterate over all the organisations, check if they have any jobs associated with them (rather than checking against what we've just scraped, as we have some jobs listed on Airtable that have been input manually). Then add their record IDs to the list above if they don't have any jobs anymore
for org in airtable_orgs:
  a = org['fields']
  if 'Jobs' not in a:
    orgs_with_job_types_to_delete.append(
        {'id': org['id'], "fields": {'Available roles': ''}})

# Now we can batch update all of those organisations in Airtable, removing the job types associated with them
orgs_table.batch_update(orgs_with_job_types_to_delete)