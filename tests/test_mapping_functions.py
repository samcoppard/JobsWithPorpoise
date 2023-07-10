import os
import sys
import tempfile
import pandas as pd
import pytest

# Modify the sys.path list to include the path to the folder containing the functions
# we want to test
# Get the path of this file, then of its parent folder, then of that folder's parent folder
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from mapping_functions import get_mapping_keywords


def test_get_mapping_keywords():
    # Create a temporary test directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary YAML files with test data
        file1 = os.path.join(temp_dir, "file1.yaml")
        with open(file1, "w") as f:
            f.write("- key1\n- value1\n- value2\n")
        file2 = os.path.join(temp_dir, "file2.yaml")
        with open(file2, "w") as f:
            f.write("- key2\n- value3\n- value4\n")

        # Call the function with the test directory
        result = get_mapping_keywords(temp_dir)

        # Define the expected output based on the test data
        expected_output = {"key1": ["value1", "value2"], "key2": ["value3", "value4"]}

        # Assert that the result matches the expected output
        assert result == expected_output


from mapping_functions import map_jobs


@pytest.fixture
def sample_dataframe():
    """Create a sample dataframe for testing"""
    data = {
        "job_role": [
            "Junior Backend Software Engineer",
            "Data Scientist",
            "Woodland Creation Project Manager",
            "Unexpected Job Role",
        ],
        "location": ["London", "Belgium", "Birmingham or Liverpool", "Fakeland"],
        "mapped_job_types": ["not mapped"] * 4,
        "mapped_locations": ["not mapped"] * 4,
        "mapped_seniorities": ["mid level"] * 4,
    }
    return pd.DataFrame(data)


def test_map_jobs_job_types(sample_dataframe):
    # Define the mapping dictionary for testing,
    job_types_dict = get_mapping_keywords(
        os.path.join(current_dir, "..", "job_type_yamls"), {}
    )

    # Call the map_jobs function, which returns an altered sample_dataframe
    map_jobs(sample_dataframe, "job_role", "mapped_job_types", job_types_dict)

    # Verify the expected mappings
    assert sorted(sample_dataframe.loc[0, "mapped_job_types"].split(", ")) == [
        "🤖 Software"
    ]
    assert sorted(sample_dataframe.loc[1, "mapped_job_types"].split(", ")) == [
        "📊 Data & Analysis",
        "🤖 Software",
        "🧪 Science",
    ]
    assert sorted(sample_dataframe.loc[2, "mapped_job_types"].split(", ")) == [
        "🌳 Rewilding",
        "🎯 Project Management",
        "🐝 Conservation",
    ]

    # Verify the unmapped row
    assert sample_dataframe.loc[3, "mapped_job_types"] == "not mapped"


def test_map_jobs_locations(sample_dataframe):
    # Define the mapping dictionary for testing
    locations_dict = get_mapping_keywords(
        os.path.join(current_dir, "..", "location_yamls/initial_yamls"), {}
    )

    # Call the map_jobs function, which returns an altered sample_dataframe
    map_jobs(sample_dataframe, "location", "mapped_locations", locations_dict)

    # Verify the expected mappings
    assert sorted(sample_dataframe.loc[0, "mapped_locations"].split(", ")) == ["London"]
    assert sorted(sample_dataframe.loc[1, "mapped_locations"].split(", ")) == ["Abroad"]
    assert sorted(sample_dataframe.loc[2, "mapped_locations"].split(", ")) == [
        "North West",
        "West Midlands",
    ]

    # Verify the unmapped row
    assert sample_dataframe.loc[3, "mapped_locations"] == "not mapped"


def test_map_jobs_seniorities(sample_dataframe):
    # Define the mapping dictionary for testing
    seniority_dict = get_mapping_keywords(
        os.path.join(current_dir, "..", "./seniority_yamls/initial_yamls"), {}
    )

    # Call the map_jobs function, which returns an altered sample_dataframe
    map_jobs(sample_dataframe, "job_role", "mapped_seniorities", seniority_dict)

    # Verify the expected mappings
    assert sample_dataframe.loc[0, "mapped_seniorities"] == "👶 Entry Level"
    assert sample_dataframe.loc[1, "mapped_seniorities"] == "mid level"
    assert sample_dataframe.loc[2, "mapped_seniorities"] == "👵🏻 Senior"

    # Verify the unmapped row
    assert sample_dataframe.loc[3, "mapped_seniorities"] == "mid level"
