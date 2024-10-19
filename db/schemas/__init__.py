from pydantic import BaseModel, validator
from typing import Optional

class UserSchema(BaseModel):
    username: str
    password: str
    api_key: Optional[str] = None

    @validator("username")
    def username_must_be_unique(cls, value, values):
        # Access the database session from the FastAPI dependency
        db = values.get("db")
        if db:
            existing_user = db.query(User).filter(User.username == value).first()
            if existing_user:
                raise ValueError("Username already exists.")
        return value

    @validator("password")
    def password_must_be_at_least_8_characters(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return value

    @validator("api_key")
    def api_key_must_be_valid(cls, value):
        if value is not None:
            # Implement validation logic for API key format 
            # (e.g., length, character restrictions)
            pass
        return value