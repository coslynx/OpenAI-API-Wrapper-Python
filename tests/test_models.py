import pytest
from core.models.models import RequestBody, ResponseModel

# Import the data models to be tested
from core.models.models import RequestBody, ResponseModel

# Test cases for RequestBody model
def test_request_body_valid_data():
    # Valid input data
    text = "This is a test text."
    model = "gpt-3.5-turbo"

    # Create RequestBody instance
    request_body = RequestBody(text=text, model=model)

    # Assert that the data is correctly assigned
    assert request_body.text == text
    assert request_body.model == model

def test_request_body_empty_text():
    # Invalid input data with empty text
    text = ""
    model = "gpt-3.5-turbo"

    # Attempt to create RequestBody instance
    with pytest.raises(ValueError) as excinfo:
        RequestBody(text=text, model=model)

    # Assert the error message
    assert str(excinfo.value) == "Text cannot be empty."

def test_request_body_invalid_model():
    # Invalid input data with an invalid model name
    text = "This is a test text."
    model = "invalid_model"

    # Attempt to create RequestBody instance
    with pytest.raises(ValueError) as excinfo:
        RequestBody(text=text, model=model)

    # Assert the error message
    assert str(excinfo.value) == "Invalid model name."

# Test cases for ResponseModel model
def test_response_model_valid_data():
    # Valid response data
    text = "This is a test response."

    # Create ResponseModel instance
    response_model = ResponseModel(text=text)

    # Assert that the data is correctly assigned
    assert response_model.text == text

def test_response_model_empty_text():
    # Valid response data with empty text
    text = ""

    # Create ResponseModel instance
    response_model = ResponseModel(text=text)

    # Assert that the data is correctly assigned
    assert response_model.text == text