""" Functions for categorisation.py """

import os
import yaml


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
