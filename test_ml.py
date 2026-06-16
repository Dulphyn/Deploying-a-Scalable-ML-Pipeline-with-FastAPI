import pytest
import os
import numpy as np
from ml.model import load_model
from ml.data import apply_label

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
    input_labels : np.array
        Model label classes
    """
    # Expected model labels
    expected_0, expected_1 = "<=50K", ">50K"

    # Actual converted model labels
    
    actual_0, actual_1 = apply_label([input_labels[0]]), apply_label([input_labels[1]])

    # Assert equivalent labels
    assert expected_0 == actual_0
    assert expected_1 == actual_1

@pytest.fixture
def input_slice():
    """
    Get sample count, precision, recall, and F1 score for Federal-gov workclass. 
    """
    # Read slice_output.txt
    with open("slice_output.txt", "r") as f:
        lines = f.readlines()

    # Federal-gov line number index
    n = 2

    # Sample count
    count = lines[n].rstrip("\n")[-3:]

    # Stats
    stats = lines[n+1].rstrip("\n").split(" | ")

    # Precision
    precision = stats[0][-6:]
    
    # Recall
    recall = stats[1][-6:]

    # F1
    f1 = stats[2][-6:]
    return count, precision, recall, f1

def test_slice_output(input_slice):
    """
    Assert Federal-gov workclass performance is the expected value.

    Inputs
    ------
    input_slice[count] : str
        Federal-gov workclass sample count
    input_slice[precision] : str
        Federal-gov workclass precision
    input_slice[recall] : str
        Federal-gov workclass recall
    input_slice[f1] : str
        Federal-gov workclass F1 score
    """
    # Expected performance values
    expected_count, expected_precision, expected_recall, expected_f1 = "191", "0.7971", "0.7857", "0.7914"

    # Actual performance values
    actual_count, actual_precision, actual_recall, actual_f1 = input_slice[0], input_slice[1], input_slice[2], input_slice[3]
    
    #Assert equivalent performance values
    assert expected_count == actual_count
    assert expected_precision == actual_precision
    assert expected_recall == actual_recall
    assert expected_f1 == actual_f1

@pytest.fixture
def input_encoder():
    """
    Get data type of saved encoder.
    """
    # Get saved encoder path
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "model", "encoder.pkl")

    # Read encoder pickle file
    encoder = load_model(data_path)

    # Get data type
    data_type = encoder.__class__.__name__
    return data_type

def test_encoder_data_type(input_encoder):
    """
    Assert saved encoder is the expected data type.

    Inputs
    ------
    input_encoder : str
        Encoder data type
    """
    # Expected encoder data type
    expected_data_type = "OneHotEncoder"

    # Assert equivalent data type
    assert input_encoder == expected_data_type