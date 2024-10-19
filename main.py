from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pydantic import BaseModel, validator
import os
import json
from openai import OpenAI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .utils.logger import get_logger
from .core.models.models import RequestBody, ResponseModel
from .core.services.openai_service import OpenAIService
from .db.models import User
from .db.schemas import UserSchema
from .auth.jwt_handler import create_access_token

app = FastAPI()
logger = get_logger(__name__)

# Load environment variables
if os.environ.get("ENV") == "production":
    logger.info("Production environment detected, loading environment variables.")
    from dotenv import load_dotenv
    load_dotenv()

# Define the database engine
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# Define a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base model for database models
Base = declarative_base()

# Create a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CORS middleware for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

# Initialize the OpenAI service
openai_service = OpenAIService(os.environ.get("OPENAI_API_KEY"))

# --- Authentication ---

@app.post("/register", response_model=UserSchema)
async def register(request_body: UserSchema, db: Session = fastapi.Depends(get_db)):
    new_user = User(**request_body.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login", response_model=ResponseModel)
async def login(request_body: UserSchema, db: Session = fastapi.Depends(get_db)):
    user = db.query(User).filter(User.username == request_body.username, User.password == request_body.password).first()
    if user:
        access_token = create_access_token(data={"sub": user.username})
        return ResponseModel(text=f"Login successful! Access token: {access_token}")
    else:
        return ResponseModel(text="Invalid username or password")

# --- API Endpoints ---

@app.post("/generate", response_model=ResponseModel, dependencies=[fastapi.Depends(get_db)])
async def generate_text(request_body: RequestBody, db: Session = fastapi.Depends(get_db), request: Request = fastapi.Depends()):
    try:
        # Extract authentication token
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        token = auth_header.split(" ")[1]
        if not token:
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        # TODO: Implement token validation (using JWT) to check for valid authentication
        # ... 

        # Perform text generation
        response = await openai_service.generate_text(request_body.text, request_body.model)
        return response
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        return ResponseModel(text=f"Error generating text: {e}")

@app.post("/translate", response_model=ResponseModel, dependencies=[fastapi.Depends(get_db)])
async def translate_text(request_body: RequestBody, db: Session = fastapi.Depends(get_db), request: Request = fastapi.Depends()):
    try:
        # Extract authentication token
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        token = auth_header.split(" ")[1]
        if not token:
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        # TODO: Implement token validation (using JWT) to check for valid authentication
        # ... 

        # Perform text translation
        response = await openai_service.translate_text(request_body.text, request_body.model)
        return response
    except Exception as e:
        logger.error(f"Error translating text: {e}")
        return ResponseModel(text=f"Error translating text: {e}")

# --- Health Check ---

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")