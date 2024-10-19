#!/bin/bash

# Startup script for the AI Wrapper for OpenAI Requests MVP

set -e

echo "Starting AI Wrapper for OpenAI Requests MVP..."

# Source environment variables from .env
if [ -f .env ]; then
  source .env
fi

# Start the backend service (FastAPI/Uvicorn)
echo "Starting backend service..."
uvicorn main:app --reload &

# Start the database service (PostgreSQL)
echo "Starting database service..."
docker-compose up -d db &

# Wait for services to start
sleep 5

# Check if services are running
echo "Checking if services are running..."
if [[ $(docker ps -aqf "name=db") ]]; then
  echo "Database service started."
else
  echo "Error: Database service failed to start."
  exit 1
fi

if [[ $(pg_isready -h localhost -p 5432 -U user) ]]; then
  echo "Database connection established."
else
  echo "Error: Database connection failed."
  exit 1
fi

# Check if the backend service is listening on port 8000
if [[ $(nc -z localhost 8000) ]]; then
  echo "Backend service started."
else
  echo "Error: Backend service failed to start."
  exit 1
fi

echo "AI Wrapper for OpenAI Requests MVP started successfully."
echo "Access the API at http://localhost:8000/"