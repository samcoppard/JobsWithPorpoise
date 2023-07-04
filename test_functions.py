import os
import yaml
import tempfile
import pytest
from categorisation import get_mapping_keywords

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
        expected_output = {'key1': ['value1', 'value2'], 'key2': ['value3', 'value4']}

        # Assert that the result matches the expected output
        assert result == expected_output