from pydantic import BaseSettings, validator
from typing import Optional
import os
import json
import structlog

logger = structlog.get_logger(__name__)

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    LOG_LEVEL: str = "INFO"
    SENTRY_DSN: Optional[str] = None

    @validator("OPENAI_API_KEY")
    def openai_api_key_cannot_be_empty(cls, value):
        if not value.strip():
            raise ValueError("OPENAI_API_KEY cannot be empty.")
        return value

    @validator("DATABASE_URL")
    def database_url_cannot_be_empty(cls, value):
        if not value.strip():
            raise ValueError("DATABASE_URL cannot be empty.")
        return value

    @validator("JWT_SECRET_KEY")
    def jwt_secret_key_cannot_be_empty(cls, value):
        if not value.strip():
            raise ValueError("JWT_SECRET_KEY cannot be empty.")
        return value

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()