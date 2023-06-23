""" Clean up the scraped jobs so that you can effectively categorise them later """

import pandas as pd
import yaml

# Pull in the scraped jobs as a dataframe
scraped_csv = pd.read_csv("scraped_jobs.csv")
scraped_jobs = pd.DataFrame(scraped_csv)


def remove_incomplete_rows(df):
    """Remove all rows with a missing value anywhere, then reset the index"""
    df.dropna(how="any", axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)


def clean_locations(df, column):
    """Create a new column to store locations in title case, and deal with a couple
    of edge cases that mess up location mapping"""
    df[column] = (
        df[column]
        # Convert to title case
        .str.title()
        # Remove mentions of New York and New South Wales
        .str.replace("New York", "USA").str.replace("New South Wales", "Australia")
    )
    # Change "Sale" & "Bury" to "Manchester" (by using a boolean mask)
    mask = df[column].isin(["Sale", "Bury"])
    df.loc[mask, column] = "Manchester"


def clean_job_titles(df, column):
    """Remove useless phrases & characters; limit to 255 chars; tidy up punctuation"""

    # Get rid of extra phrases that aren't needed
    phrases_to_remove = [
        "(All Genders)",
        "(all genders)",
        "all genders",
        " - Permanent (no closing date – apply now)",
        "/ ANNUM ",
        "docx",
        "Job Description",
    ]
    for phrase in phrases_to_remove:
        df[column] = df[column].str.replace(phrase, "")

    # Get rid of punctuation that's never needed
    chars_to_remove = [".", "!", "?", "→", "🌿"]
    for char in chars_to_remove:
        df[column] = df[column].str.replace(char, "")

    # Limit the 'Job Title' column to 255 characters (to match length in PSQL)
    df[column] = df[column].str[:255]

    df[column] = (
        df[column]
        # Tidy up hyphens
        .str.replace("- ", " - ")
        .str.replace(" -", " - ")
        .str.replace("  ", " ")
        # Tidy up colons
        .str.replace(" :", ": ")
        .str.replace("  ", " ")
        # Replace a weird apostrophe with a normal one
        .str.replace("’", "'")
        # Remove whitespace at the end
        .str.strip()
        # Get rid of trailing punctuation
        .str.replace(r"[:,(/-]+$", "", regex=True)
        # Remove extra spaces again (including mid-string this time)
        .str.strip()
        .str.replace("  ", " ")
    )


def load_exclusions():
    """Load a list of words from a YAML file to exclude from being capitalized"""
    with open("./JobsWithPorpoise/capital_exclusions.yaml", "r") as file:
        return yaml.safe_load(file)


exclusions = load_exclusions()


def convert_to_title_case(string):
    """Change the string to title case, except where you wouldn't actually want to"""
    words = string.split()
    capitalized_words = [
        word.capitalize() if word not in exclusions else word for word in words
    ]
    capitalized_string = " ".join(capitalized_words)
    # Fix an edge case with Next.js
    capitalized_string = capitalized_string.replace("Nextjs", "Next.js")
    return capitalized_string


def convert_df_column_to_title_case(df, column):
    """Change a df column of string values to title case"""
    df[column] = df[column].apply(convert_to_title_case)


remove_incomplete_rows(scraped_jobs)
clean_locations(scraped_jobs, "Location")
clean_job_titles(scraped_jobs, "Job Title")
convert_df_column_to_title_case(scraped_jobs, "Job Title")


def create_new_columns(df):
    # Create a new column for concatenating org - role - location, limited to 255 chars
    scraped_jobs["concat"] = (
        scraped_jobs["Company"]
        + " - "  # Looks clunky but can't use f-strings here
        + scraped_jobs["Job Title"]
        + " - "
        + scraped_jobs["Location"]
    ).str[:255]

    # Create new columns for the jobs' mapped locations, job types, and seniorities
    scraped_jobs["mapped_location"] = "not mapped"
    scraped_jobs["job_types"] = "not mapped"
    scraped_jobs["seniority"] = "mid level"


create_new_columns(scraped_jobs)

# Export the cleaned jobs to csv
scraped_jobs.to_csv("cleaned_jobs.csv", index=False)
