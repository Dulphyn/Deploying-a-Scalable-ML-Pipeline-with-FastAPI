import pytest
# TODO: add necessary import
import os
import numpy as np
from ml.model import load_model
from ml.data import apply_label

# TODO: implement the first test. Change the function name and input as needed
@pytest.fixture
def input_labels():
    """
    Get model labels from saved model.
    """
    # Get saved model path
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "model", "model.pkl")

    # Read model pickle file
    model = load_model(data_path)

    # Get labels
    labels = model.classes_
    return labels

def test_apply_labels(input_labels):
    """
    Asserts model labels are converted to the correct string.

    Inputs
    ------
    labels : np.array
        Model label classes
    """
    # Expected model labels
    expected_0, expected_1 = "<=50K", ">50K"

    # Actual converted model labels
    
    actual_0, actual_1 = apply_label([input_labels[0]]), apply_label([input_labels[1]])

    # Assert equivalent labels
    assert expected_0==actual_0
    assert expected_1==actual_1


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass