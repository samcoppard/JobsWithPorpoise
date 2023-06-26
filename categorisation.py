import pandas as pd
import os
import yaml

# Pull in the scraped jobs as a dataframe
scraped_jobs_import = pd.read_json("cleaned_jobs.json")
scraped_jobs = pd.DataFrame(scraped_jobs_import)

""" Map each job to its location(s) first """


def get_mapping_keywords(yamls_directory, dict={}):
    """Create a dict of all the keywords required for mapping jobs"""
    # Load keywords from every YAML file in a folder in turn
    for filename in os.listdir(yamls_directory):
        filepath = os.path.join(yamls_directory, filename)
        with open(filepath, "r") as file:
            keywords_list = yaml.safe_load(file)
            # Add the key:value pairs to the dictionary
            dict[keywords_list[0]] = keywords_list[1:]
    return dict


# Add a new column to the dataframe to store each job's mapped locations
scraped_jobs["mapped_location"] = "not mapped"

# Create a dict to hold every region, and the location keywords that map to them
locations_dict = get_mapping_keywords(
    "./JobsWithPorpoise/location_yamls/initial_yamls", {}
)


def map_jobs(df, scraped_column, mapped_column, mapping_dict):
    """Map jobs into the correct categories"""
    # Iterate over every job / row in the dataframe
    for ind, scraped_value in df[scraped_column].items():
        # Map the attributes to the right categories
        categories = set()
        # For each category, iterate over the keywords that map to it, checking if they're
        # contained within the string. If they are, add the category to the set and move
        # on to the next category
        for category, keywords in mapping_dict.items():
            for keyword in keywords:
                if keyword in scraped_value:
                    categories.add(category)
                    break
        # Update the row with the mapped categories (if mapping was successful)
        if categories:
            df.at[ind, mapped_column] = ", ".join(categories)


# Map each job to its correct region(s)
map_jobs(scraped_jobs, "Location", "mapped_location", locations_dict)

# Overwrite the mappings above for cases where the scraped location is awkward - either
# it's too short to map like that ("Remote"), or it maps to multiple regions ("Midlands")

# Create a dict to handle regions and keywords for these awkward cases
awkward_locations_dict = get_mapping_keywords(
    "./JobsWithPorpoise/location_yamls/refining_yamls", {}
)

for ind in scraped_jobs.index:
    location = scraped_jobs["Location"][ind]

    if location in awkward_locations_dict["remote_matches"]:
        scraped_jobs["mapped_location"][ind] = "Fully Remote"
    elif location in awkward_locations_dict["midlands_matches"]:
        scraped_jobs["mapped_location"][ind] = "East Midlands, West Midlands"
    elif location in awkward_locations_dict["north_matches"]:
        scraped_jobs["mapped_location"][ind] = "North East, North West"
    elif location in awkward_locations_dict["england_matches"]:
        scraped_jobs["mapped_location"][
            ind
        ] = "London, South East, South West, North East, North West, East Midlands, West Midlands, East of England, Yorkshire / Humber"
    elif location in awkward_locations_dict["abroad_matches"]:
        scraped_jobs["mapped_location"][ind] = "Abroad"
    elif location in awkward_locations_dict["all_matches"]:
        scraped_jobs["mapped_location"][
            ind
        ] = "Scotland, Wales, London, South East, South West, North East, North West, East Midlands, West Midlands, East of England, Yorkshire / Humber"


# Sometimes the location only appears in the job title, not where it 'should' be, so
# let's deal with that by mapping job titles to regions IF the normal way hasn't worked
not_mapped_rows = scraped_jobs[scraped_jobs["mapped_location"] == "not mapped"]
map_jobs(not_mapped_rows, "Job Title", "mapped_location", locations_dict)
scraped_jobs.update(not_mapped_rows)


# Ensure that Remote jobs are only tagged as Remote. This works by creating a Boolean
# mask and only replacing those values where the condition is met
scraped_jobs.loc[
    scraped_jobs["mapped_location"].str.contains("Fully Remote"), "mapped_location"
] = "Fully Remote"

# TK - How to handle jobs that are e.g. 'New York - Fully Remote'? Need to exclude them!

# Remove non-UK jobs (by checking the job has only been mapped to 'Abroad' so we don't
# accidentally exclude jobs with a scraped location like 'Brussels, London, Amsterdam'
scraped_jobs = scraped_jobs[scraped_jobs["mapped_location"] != "Abroad"]

# Print out any jobs that haven't been mapped to any area (for easy review)
print("These jobs haven't been mapped to any location:")
print(scraped_jobs[scraped_jobs["mapped_location"] == "not mapped"])


""" Now map each job to its job type(s) """
# Add a new column to the dataframe to store each job's mapped job types
scraped_jobs["job_types"] = "not mapped"

# Create a dict to hold all the different job types, and the keywords that map to them
job_types_dict = get_mapping_keywords("./JobsWithPorpoise/job_type_yamls", {})

# Map jobs to the category of job they're in
map_jobs(scraped_jobs, "Job Title", "job_types", job_types_dict)

# Print out any jobs that haven't been mapped to any job types (for easy review)
print("These jobs haven't been mapped to any job type:")
print(scraped_jobs[scraped_jobs["job_types"] == "not mapped"])

# Remove jobs that have been categorised as Weird other, or Volunteering
scraped_jobs = scraped_jobs[
    ~scraped_jobs["job_types"].str.contains("Weird other|Volunteering")
]


""" Now map each job to its seniority level """
# Add a new column to the dataframe to store each job's mapped seniority level
scraped_jobs["seniority"] = "mid level"

# Create a dict to hold the different seniorities, and the keywords that map to them
seniority_dict = get_mapping_keywords(
    "./JobsWithPorpoise/seniority_yamls/initial_yamls", {}
)

# Map jobs to their seniority level
map_jobs(scraped_jobs, "Job Title", "seniority", seniority_dict)


# The initial mapping isn't perfect, so now we need to remove incorrect seniority tags

# Create a dict to hold the keywords for refining the mapping of seniorities
refining_seniority_dict = get_mapping_keywords(
    "./JobsWithPorpoise/seniority_yamls/refining_yamls", {}
)

# Iterate over every job / row in the dataframe
for ind, scraped_value in scraped_jobs["Job Title"].items():
    # Check if the job title gets mapped to any of the anti-categories
    categories = set()
    for category, keywords in refining_seniority_dict.items():
        for keyword in keywords:
            if keyword in scraped_value:
                categories.add(category)
                break
    # If the job has been mapped to "Not Entry Level", then make that change
    if "Not Entry Level" in categories:
        scraped_jobs["seniority"][ind] = scraped_jobs["seniority"][ind].replace(
            "👶 Entry Level", "mid level"
        )
    # Same for "Not Management", unless it's ALSO been mapped to "Definitely Management"
    elif "Not Management" in categories and "Definitely Management" not in categories:
        scraped_jobs["seniority"][ind] = scraped_jobs["seniority"][ind].replace(
            "👵🏻 Senior", "mid level"
        )


# We can end up with some jobs where the seniority is now duplicated, so let's fix that
scraped_jobs["seniority"] = scraped_jobs["seniority"].str.replace(
    "mid level, mid level", "mid level"
)

# Export the dataframe of categorised jobs to JSON
scraped_jobs.to_json("categorised_jobs.json", orient="records")
