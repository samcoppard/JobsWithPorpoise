import pandas as pd
import pytest


from job_data_cleaning import remove_incomplete_rows


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
