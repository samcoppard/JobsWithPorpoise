import sys
import os
import pandas as pd
import pytest

# Modify the sys.path list to include the path to the folder containing the functions
# we want to test
# Get the path of this file, then of its parent folder, then of that folder's parent folder
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from data_cleaning_functions import remove_incomplete_rows


@pytest.fixture
def sample_dataframe():
    """Create a sample dataframe for testing that includes null values"""
    data = {
        "column_1": ["Data Analyst", "Marine Biologist", None, "Account Executive"],
        "column_2": ["Bristol", "Cardiff", "Edinburgh", None],
        "column_3": [None, "Project Seagrass", "Seabird Sanctuary", "Battery Co"],
    }
    return pd.DataFrame(data)


def test_remove_incomplete_rows(sample_dataframe):
    # Call the remove_incomplete_rows function on the sample dataframe
    remove_incomplete_rows(sample_dataframe)

    # Create a df that only contains the rows of the sample dataframe with no null values
    no_empty_rows_data = {
        "column_1": ["Marine Biologist"],
        "column_2": ["Cardiff"],
        "column_3": ["Project Seagrass"],
    }
    no_empty_rows_df = pd.DataFrame(no_empty_rows_data)

    # Verify that the values in the first row of both dataframes are identical
    for i in range(3):
        assert no_empty_rows_df.iloc[0, i] == sample_dataframe.iloc[0, i]

    # Verify that the sample dataframe doesn't have any other rows left
    assert sample_dataframe.shape == (1, 3)


from data_cleaning_functions import clean_locations


@pytest.fixture
def sample_dataframe_2():
    """Create a sample dataframe for testing the clean_locations function"""
    data = {
        "column_1": ["Job1", "Job2", "Job3", "Job4"],
        "locations": [
            "new york or san francisco  ",
            " sydney, New South Wales",
            "Bury or Derby",
            " sale ",
        ],
        "column_3": ["Org1", "Org2", "Org3", "Org4"],
    }
    return pd.DataFrame(data)


def test_clean_locations(sample_dataframe_2):
    # Call the clean_locations function on the sample dataframe
    clean_locations(sample_dataframe_2, "locations")

    # Verify that the locations have been cleaned as expected
    assert sample_dataframe_2["locations"][0] == "USA Or San Francisco"
    assert sample_dataframe_2["locations"][1] == "Sydney, Australia"
    assert sample_dataframe_2["locations"][2] == "Bury Or Derby"
    assert sample_dataframe_2["locations"][3] == "Manchester"

    # Verify that the other columns are unchanged
    assert sample_dataframe_2["column_1"].tolist() == ["Job1", "Job2", "Job3", "Job4"]
    assert sample_dataframe_2["column_3"].tolist() == ["Org1", "Org2", "Org3", "Org4"]
