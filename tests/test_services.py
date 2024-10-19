import pytest
from fastapi import HTTPException
from unittest.mock import patch, MagicMock
from core.services.openai_service import OpenAIService
from core.models.models import RequestBody, ResponseModel

@pytest.fixture
def openai_service():
    return OpenAIService("your_openai_api_key")

def test_openai_service_init(openai_service):
    assert openai_service.openai is not None

@patch("openai.OpenAI.completions.create")
async def test_generate_text_success(mock_create, openai_service):
    mock_create.return_value = MagicMock(choices=[MagicMock(text="Generated text")])
    text = "This is a test text."
    model = "gpt-3.5-turbo"
    response = await openai_service.generate_text(text, model)
    assert response.text == "Generated text"
    mock_create.assert_called_once_with(model=model, prompt=text, temperature=0.7, max_tokens=2048)

@patch("openai.OpenAI.completions.create")
async def test_generate_text_error(mock_create, openai_service):
    mock_create.side_effect = Exception("Error generating text")
    text = "This is a test text."
    model = "gpt-3.5-turbo"
    with pytest.raises(HTTPException) as excinfo:
        await openai_service.generate_text(text, model)
    assert excinfo.value.detail == "Error generating text: Error generating text"

@patch("openai.OpenAI.translations.create")
async def test_translate_text_success(mock_create, openai_service):
    mock_create.return_value = MagicMock(choices=[MagicMock(text="Translated text")])
    text = "This is a test text."
    model = "gpt-3.5-turbo"
    target_language = "fr"
    response = await openai_service.translate_text(text, model, target_language)
    assert response.text == "Translated text"
    mock_create.assert_called_once_with(model=model, prompt=text, target_language=target_language)

@patch("openai.OpenAI.translations.create")
async def test_translate_text_error(mock_create, openai_service):
    mock_create.side_effect = Exception("Error translating text")
    text = "This is a test text."
    model = "gpt-3.5-turbo"
    target_language = "fr"
    with pytest.raises(HTTPException) as excinfo:
        await openai_service.translate_text(text, model, target_language)
    assert excinfo.value.detail == "Error translating text: Error translating text"

def test_request_body_valid_data():
    text = "This is a test text."
    model = "gpt-3.5-turbo"
    request_body = RequestBody(text=text, model=model)
    assert request_body.text == text
    assert request_body.model == model

def test_request_body_empty_text():
    with pytest.raises(ValueError) as excinfo:
        RequestBody(text="", model="gpt-3.5-turbo")
    assert str(excinfo.value) == "Text cannot be empty."

def test_request_body_invalid_model():
    with pytest.raises(ValueError) as excinfo:
        RequestBody(text="This is a test text.", model="invalid_model")
    assert str(excinfo.value) == "Invalid model name."

def test_response_model_valid_data():
    text = "This is a test response."
    response_model = ResponseModel(text=text)
    assert response_model.text == text

def test_response_model_empty_text():
    text = ""
    response_model = ResponseModel(text=text)
    assert response_model.text == text