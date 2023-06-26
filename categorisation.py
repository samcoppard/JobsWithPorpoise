import pandas as pd
import os
import yaml

# Pull in the scraped jobs as a dataframe
scraped_jobs_import = pd.read_json('cleaned_jobs.json')
scraped_jobs = pd.DataFrame(scraped_jobs_import)

""" Map each job to its location(s) first """

def get_mapping_keywords(yamls_directory, dict={}):
    """ Create a dict of all the keywords required for mapping jobs """
    # Load keywords from every YAML file in a folder in turn
    for filename in os.listdir(yamls_directory):
        filepath = os.path.join(yamls_directory, filename)
        with open(filepath, 'r') as file:
            keywords_list = yaml.safe_load(file)
            # Add the key:value pairs to the dictionary
            dict[keywords_list[0]] = keywords_list[1:]
    return dict

# Add a new column to the dataframe to store each job's mapped locations
scraped_jobs["mapped_location"] = "not mapped"

# Create a dict to hold every region, and the location keywords that map to them
locations_dict = get_mapping_keywords('./JobsWithPorpoise/location_yamls/initial_yamls')

# Iterate over every job / row in the dataframe
for ind, location in scraped_jobs['Location'].items():
    # Map locations to regions
    regions = set()
    # For each region, iterate over the keywords that map to it, checking if they're contained within the job's location string. If they are, add the region to the set and move on to the next region
    for region, locs in locations_dict.items():
        for loc in locs:
            if loc in location:
                regions.add(region)
                break
    # Update the row with the mapped regions (if mapping was successful)
    if regions:
        scraped_jobs.at[ind, 'mapped_location'] = ", ".join(regions)

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

# Create a dict to hold larger regions, and the keywords that map to them
wider_locations_dict = get_mapping_keywords('./JobsWithPorpoise/location_yamls/refining_yamls')

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
# Add a new column to the dataframe to store each job's mapped job types
scraped_jobs["job_types"] = "not mapped"

# Create a dict to hold all the different job types, and the keywords that map to them
job_types_dict = get_mapping_keywords('./JobsWithPorpoise/job_type_yamls')

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
# Add a new column to the dataframe to store each job's mapped seniority level
scraped_jobs["seniority"] = "mid level"

# Create a dict to hold the different seniorities, and the keywords that map to them
seniority_dict = get_mapping_keywords('./JobsWithPorpoise/seniority_yamls/initial_yamls')


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

""" Remove seniority tags that aren't actually correct """

# Create a dict to hold the keywords for refining the mapping of seniorities
refining_seniority_dict = get_mapping_keywords('./JobsWithPorpoise/seniority_yamls/refining_yamls')


# Now for each job, check if the job title contains any of the terms that would mean it's not actually entry level, then remove the entry level tag if it was given one erroneously
for ind in scraped_jobs.index:
  if any(ele in scraped_jobs['Job Title'][ind]
         for ele in refining_seniority_dict['Not Entry Level']):
    scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
        "👶 Entry Level", "mid level")
  # And then same deal for the management tag
  if any(ele in scraped_jobs['Job Title'][ind]
         for ele in refining_seniority_dict['Not Management']):
    # But make sure we're not removing the management tag from any that definitely are management
    if not any(ele in scraped_jobs['Job Title'][ind]
               for ele in refining_seniority_dict['Definitely Management']):
      scraped_jobs['seniority'][ind] = scraped_jobs['seniority'][ind].replace(
          "👵🏻 Senior", "mid level")

# Occasionally we can end up with a job where the seniority has now been classed as "mid level, mid level" which causes an error due to duplication when we try to send it to Airtable later on
scraped_jobs['seniority'] = scraped_jobs['seniority'].str.replace(
      "mid level, mid level", "mid level")

# Export the dataframe of categorised jobs to JSON
scraped_jobs.to_json('categorised_jobs.json', orient="records")
