from pydantic import BaseModel, validator

class RequestBody(BaseModel):
    text: str
    model: str

    @validator("text")
    def text_cannot_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty.")
        return value

    @validator("model")
    def model_must_be_valid(cls, value):
        allowed_models = ["gpt-3.5-turbo", "text-davinci-003", "code-davinci-002", "gpt-4"]
        if value not in allowed_models:
            raise ValueError("Invalid model name.")
        return value

class ResponseModel(BaseModel):
    text: str