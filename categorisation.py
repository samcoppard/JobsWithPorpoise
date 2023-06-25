import pandas as pd
import os
import yaml

# Pull in the scraped jobs as a dataframe
scraped_csv = pd.read_csv('cleaned_jobs.csv')
scraped_jobs = pd.DataFrame(scraped_csv)

""" Map each job to its location(s) first """

# Create a dict to hold the regions of the UK and all the locations in that region
locations_dict = {}

location_yamls_directory = './JobsWithPorpoise/location_yamls'

# Loop over all the location YAML files and read the values in each file into a list
for filename in os.listdir(location_yamls_directory):
    filepath = os.path.join(location_yamls_directory, filename)
    with open(filepath, 'r') as file:
        list_of_loc_terms = yaml.safe_load(file)
        # Add the region and its locations to the dictionary
        locations_dict[list_of_loc_terms[0]] = list_of_loc_terms[1:]


# Check each job / row in scraped_jobs
for ind in scraped_jobs.index:
  # Start off with an empty list that we'll populate with the locations
  a = []
  # For each possible location, check if one of the defining terms for that location appears in the scraped location, then add it to the list if it does
  for area in locations_dict:
    if any(ele in scraped_jobs['Location'][ind]
           for ele in locations_dict[area]):
      a.append(area)
    # Combine all the mapped locations in the dictionary into a single string
    if a != []:
      b = ", ".join(a)
      # Add the string to the 'mapped_location' column of the scraped_jobs dataframe
      # NB if the scraped location didn't match any of the possible mapped locations, this will still read 'unmapped'
      scraped_jobs['mapped_location'][ind] = b

# Deal with awkward scraped locations, starting with Remote jobs
remote_matches = [
    'Remote', 'Fully Remote', 'Remote Job', 'Uk', 'Remote, United Kingdom',
    'Uk, United Kingdom', 'Remote (Ireland Or Uk Only)', 'United Kingdom',
    'Home Based', 'Home-Based', 'Working From Home', 'Europe', 'Nationwide',
    'Flexible/Home Working', 'Uk Wide', 'Flexible'
]
midlands_matches = ['Midlands', 'Midlands, United Kingdom', 'Midlands, Gb']
north_matches = ['Northern England', 'England, North']
england_matches = ['England, United Kingdom']
abroad_matches = ['Ireland', 'Northern Ireland']
all_matches = ['Nearby Any Sustrans Office Hub Across The Uk']

for ind in scraped_jobs.index:
  if any(x == scraped_jobs['Location'][ind] for x in remote_matches):
    scraped_jobs['mapped_location'][ind] = "Fully Remote"
  elif any(x == scraped_jobs['Location'][ind] for x in midlands_matches):
    scraped_jobs['mapped_location'][ind] = "East Midlands, West Midlands"
  elif any(x == scraped_jobs['Location'][ind] for x in north_matches):
    scraped_jobs['mapped_location'][ind] = "North East, North West"
  elif any(x == scraped_jobs['Location'][ind] for x in england_matches):
    scraped_jobs['mapped_location'][
        ind] = "London, South East, South West, North East, North West, East Midlands, West Midlands, East of England, Yorkshire / Humber"
  elif any(x == scraped_jobs['Location'][ind] for x in abroad_matches):
    scraped_jobs['mapped_location'][ind] = "Abroad"
  elif any(x in scraped_jobs['Location'][ind] for x in all_matches):
    scraped_jobs['mapped_location'][
        ind] = "Scotland, Wales, London, South East, South West, North East, North West, East Midlands, West Midlands, East of England, Yorkshire / Humber"

# Sometimes the location only appears in the job title, not where it 'should' be, so let's deal with that by checking job titles for locations IF the normal way hasn't worked

for ind in scraped_jobs.index:
  if scraped_jobs['mapped_location'][ind] == "not mapped":
    a = []
    for area in locations_dict:
      if any(ele in scraped_jobs['Job Title'][ind]
             for ele in locations_dict[area]):
        a.append(area)
      if a != []:
        b = ", ".join(a)
        scraped_jobs['mapped_location'][ind] = b

# Ensure that Remote jobs are only tagged as Remote, not other locations as well
for ind in scraped_jobs.index:
  if "Fully Remote" in scraped_jobs['mapped_location'][ind]:
    scraped_jobs['mapped_location'][ind] = "Fully Remote"

# NB - What to do with jobs like ones from EVenergy that are e.g. 'New York - Fully Remote'? Need to exclude, not class as remote

# Print out any jobs that haven't been mapped to any area (for easy review)
print("These jobs haven't been mapped to any location:")
print(scraped_jobs[scraped_jobs['mapped_location'] == 'not mapped'])

# Remove jobs in non-UK locations
for ind in scraped_jobs.index:
  # NB Check that the job has only been mapped to 'Abroad' so that we don't accidentally exclude jobs with a scraped location like 'Brussels, London, Amsterdam'
  if scraped_jobs['mapped_location'][ind] == 'Abroad':
    scraped_jobs.drop(index=ind, inplace=True)


""" Now map each job to its job type(s) """

# Create a dict to hold the regions of the UK and all the locations in that region
job_types_dict = {}

job_type_yamls_directory = './JobsWithPorpoise/job_type_yamls'

# Loop over all the location YAML files and read the values in each file into a list
for filename in os.listdir(job_type_yamls_directory):
    filepath = os.path.join(job_type_yamls_directory, filename)
    with open(filepath, 'r') as file:
        list_of_job_type_terms = yaml.safe_load(file)
        # Add the region and its locations to the dictionary
        job_types_dict[list_of_job_type_terms[0]] = list_of_job_type_terms[1:]

# Check each job / row in scraped_jobs
for ind in scraped_jobs.index:
  # Start off with an empty list that we'll populate with the job types
  a = []
  # For each job type, check if one of the defining terms for that job type appears in the job title, then add it to the list if it does
  for type in job_types_dict:
    if any(ele in scraped_jobs['Job Title'][ind]
           for ele in job_types_dict[type]):
      a.append(type)
    # Combine all the job types in the dictionary into a single string
    if a != []:
      b = ", ".join(a)
      # Add the string to the 'job_types' column of the scraped_jobs dataframe
      # NB if the job title didn't match any job types, this will still read 'unmapped'
      scraped_jobs['job_types'][ind] = b

# Print out any jobs that haven't been mapped to any job types (for easy review)
print("These jobs haven't been mapped to any job type:")
print(scraped_jobs[scraped_jobs['job_types'] == 'not mapped'])

# Remove jobs that have been categorised as Weird other, or Volunteering
for ind in scraped_jobs.index:
  if any(x in scraped_jobs['job_types'][ind]
         for x in ['Weird other', 'Volunteering']):
    scraped_jobs.drop(index=ind, inplace=True)

""" Now map each job to its seniority level """

# Create a dict to hold the regions of the UK and all the locations in that region
seniority_dict_2 = {}

seniority_yamls_directory = './JobsWithPorpoise/seniority_yamls'

# Loop over all the location YAML files and read the values in each file into a list
for filename in os.listdir(seniority_yamls_directory):
    filepath = os.path.join(seniority_yamls_directory, filename)
    with open(filepath, 'r') as file:
        list_of_seniority_terms = yaml.safe_load(file)
        # Add the region and its locations to the dictionary
        seniority_dict_2[list_of_seniority_terms[0]] = list_of_seniority_terms[1:]


# Check each job / row in scraped_jobs
for ind in scraped_jobs.index:
  # Start off with an empty list that we'll populate with the seniority level (this should eventually be unnecessary when you've improved the mappings enough that nothing gets tagged as both entry level and senior)
  y = []
  # For each seniority level, check if one of the defining terms for that seniority level appears in the job title, then add it to the list if it does
  for seniority in seniority_dict:
    if any(ele in scraped_jobs['Job Title'][ind]
           for ele in seniority_dict[seniority]):
      y.append(seniority)
    # Combine all the job types in the dictionary into a single string
    if y != []:
      z = ", ".join(y)
      # Add the string to the 'seniority' column of the scraped_jobs dataframe
      scraped_jobs['seniority'][ind] = z

# Remove seniority tags that aren't actually correct
# Same procedure as above - start by making the lists of terms that should be used for exclusion
not_entry_level = [
    'International', 'Business Partner', 'Marketing Manager', 'Senior',
    'Contract Manager', 'Development Manager', 'Assistant Manager', 'Internal',
    'Account Manager', 'Accounts Manager', 'Retail Manager',
    'Communications Manager', 'Sales Manager'
]
not_management = [
    'Assistant', 'Junior', 'Graduate', 'Trainee', 'Project Manage',
    'Account Manager', 'Management Accountant', 'Social Media Manage',
    'Office Manager', 'Change Management Engineer', 'Relationship Manager',
    'Relationships Manager', 'Database Manager', 'Product Manager',
    'Contracts Manage', 'Nursery Manager', 'Nature Connection Manager'
]
definitely_management = [
    'Senior', 'Director', 'Head of', 'Lead', 'Chair', 'Team Leader', 'Foreman',
    'Key Account Manager'
]

# Then make a dictionary from those lists
not_seniority_dict = {
    'Not Entry Level': not_entry_level,
    'Not Management': not_management,
    'Definitely Management': definitely_management
}

# Now for each job, check if the job title contains any of the terms that would mean it's not actually entry level, then remove the entry level tag if it was given one erroneously
for ind in scraped_jobs.index:
  if any(ele in scraped_jobs['Job Title'][ind]
         for ele in not_seniority_dict['Not Entry Level']):
    scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
        "👶 Entry Level", "mid level")
  # And then same deal for the management tag
  if any(ele in scraped_jobs['Job Title'][ind]
         for ele in not_seniority_dict['Not Management']):
    # But make sure we're not removing the management tag from any that definitely are management
    if not any(ele in scraped_jobs['Job Title'][ind]
               for ele in not_seniority_dict['Definitely Management']):
      scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
          "👵🏻 Senior", "mid level")

# Occasionally we can end up with a job where the seniority has now been classed as "mid level, mid level" which causes an error due to duplication when we try to send it to Airtable later on
for ind in scraped_jobs.index:
  scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
      "mid level, mid level", "mid level")

# Export all the jobs (with their new locations and job type categorisations and seniority levels) as csv
scraped_jobs.to_csv('categorised_jobs.csv', index=False)
