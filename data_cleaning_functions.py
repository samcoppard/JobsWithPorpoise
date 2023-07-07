import yaml

""" Functions for job_data_cleaning.py """


def load_exclusions():
    """Load a list of words that shouldn't be capitalized from a YAML file"""
    with open("./other_yamls/capital_exclusions.yaml", "r") as file:
        return yaml.safe_load(file)


def remove_incomplete_rows(df):
    """Remove all rows with a missing value anywhere, then reset the index"""
    df.dropna(how="any", axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)


def clean_locations(df, column):
    """Create a new column to store locations in title case, and deal with a couple
    of edge cases that mess up location mapping"""
    df[column] = (
        df[column]
        # Convert to title case and remove whitespace
        .str.title()
        .str.strip()
        # Remove mentions of New York and New South Wales
        .str.replace("New York", "USA")
        .str.replace("New South Wales", "Australia")
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
        # Add space around slashes (so splitting and capitalizing strings is easier)
        .str.replace("/", " / ")
        # Remove extra spaces again (including mid-string this time)
        .str.strip()
        .str.replace("  ", " ")
    )


def convert_to_title_case(string):
    """Change the string to title case, except where you wouldn't actually want to"""

    # Cache the results of load_exclusions() so we don't run that function every single
    # time we run this function
    if not hasattr(convert_to_title_case, "exclusions"):
        convert_to_title_case.exclusions = load_exclusions()

    # Split the string into a list of strings, convert those strings to title case,
    # then join them back together into a single string again
    words = string.split()
    capitalized_words = [
        word.title() if word not in convert_to_title_case.exclusions else word
        for word in words
    ]
    capitalized_string = " ".join(capitalized_words)

    # Fix a few edge cases
    capitalized_string = (
        capitalized_string.replace("Nextjs", "Next.js")
        .replace("Nodejs", "Node.js")
        .replace("UI / UX", "UI/UX")
        .replace("UX / UI", "UI/UX")
    )
    return capitalized_string


def convert_df_column_to_title_case(df, column):
    """Change a df column of string values to title case"""
    df[column] = df[column].apply(convert_to_title_case)


def create_concat_column(df):
    """Create a column that concatenates org - role - location, limited to 255 chars"""
    df["concat"] = (
        df["Company"]
        + " - "  # Looks clunky but can't use f-strings here
        + df["Job Title"]
        + " - "
        + df["Location"]
    ).str[:255]


""" Functions for org_data_cleaning.py """


def clean_job_types(list_of_job_types):
    """Separate out the job types for each job (so e.g. ["IT, HR"] becomes ["IT", "HR"])
    Then remove duplicate job types, sort the job types (unordered sets make for lots
    of unnecessary PSQL & Webflow updating) and remove the string 'not mapped'"""
    split_job_types = [item for ele in list_of_job_types for item in ele.split(", ")]
    unique_job_types = sorted(set(split_job_types))
    unique_job_types = [string for string in unique_job_types if string != "not mapped"]
    return unique_job_types
