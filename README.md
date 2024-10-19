<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
OpenAI-API-Wrapper-Python
</h1>
<h4 align="center">A Python backend service that simplifies interaction with OpenAI's API</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework: FastAPI" />
  <img src="https://img.shields.io/badge/Backend-Python-red" alt="Backend: Python" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database: PostgreSQL" />
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="LLMs: OpenAI" />
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/OpenAI-API-Wrapper-Python?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/OpenAI-API-Wrapper-Python?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/OpenAI-API-Wrapper-Python?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

This repository contains a Minimum Viable Product (MVP) for a Python backend service called "AI Wrapper for OpenAI Requests". This service simplifies interacting with OpenAI's API by providing a user-friendly wrapper that handles request formatting, authentication, and response parsing.  

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   |  A robust and efficient architecture built using FastAPI, PostgreSQL, and the OpenAI Python library. |
| 📄 | **Documentation**  |  Clear and detailed documentation explaining the MVP's functionalities, setup, and usage. |
| 🔗 | **Dependencies**   |  Leverages carefully selected Python libraries for efficient development and robust functionality. |
| 🧩 | **Modularity**     |  Well-structured codebase with separate modules for different functionalities, promoting code reusability and maintainability.  |
| 🧪 | **Testing**        |  Includes unit tests to ensure the correctness and reliability of the core components. |
| ⚡️  | **Performance**    |  Optimized for efficient request handling and response processing, ensuring fast and responsive results.  |
| 🔐 | **Security**       | Implements secure API key management and access control using JWT authentication. |
| 🔀 | **Version Control**|  Utilizes Git for version control, ensuring collaboration and trackability of changes. |
| 🔌 | **Integrations**   |  Seamless integration with OpenAI's API using the official Python library. |
| 📶 | **Scalability**    | Designed with scalability in mind to handle growing request volumes. |

## 📂 Structure

```text
├── core
│   ├── services
│   │   └── openai_service.py
│   └── models
│       └── models.py
├── utils
│   └── logger.py
├── tests
│   └── test_services.py
├── db
│   ├── models
│   │   └── __init__.py
│   └── schemas
│       └── __init__.py
├── config
│   └── settings.py
├── .gitignore
├── .env
├── startup.sh
├── commands.json
├── requirements.txt
└── main.py

```

## 💻 Installation

### 🔧 Prerequisites

- Python 3.9+
- PostgreSQL 14+
- `pip` (Python package manager)
- Docker (Optional for local development)

### 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/coslynx/OpenAI-API-Wrapper-Python.git
   cd OpenAI-API-Wrapper-Python
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables, replacing the placeholders with your actual values:
     ```
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     DATABASE_URL=postgres://user:password@host:port/database
     JWT_SECRET_KEY=YOUR_JWT_SECRET_KEY
     ```

4. **Start the database (optional):**
   - If you're using Docker for local development, start the PostgreSQL database container:
     ```bash
     docker-compose up -d db
     ```

5. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

## 🏗️ Usage

### 🏃‍♂️ Running the MVP

1. **Start the development server:**
   ```bash
   uvicorn main:app --reload
   ```
2. **Access the API:**
   - The API is now running at `http://localhost:8000/`. 
   - You can send requests using tools like `curl` or `Postman`.

### ⚙️ Configuration

- **Environment Variables:** The application reads settings from the `.env` file, so you can customize it to suit your environment. 

## 🌐 Hosting

### 🚀 Deployment Instructions

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```
2. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your database:**
   - Ensure you have a PostgreSQL database set up and configured.
   - Update the `DATABASE_URL` environment variable in your `.env` file with the correct connection string.
5. **Create a deployment script:**
   - You can use a script like `startup.sh` to automate the deployment process. 
6. **Deploy the code:**
   - Choose a deployment platform (e.g., Heroku, AWS Lambda, Google Cloud Functions) and follow their specific deployment instructions.

### 🔑 Environment Variables

- **`OPENAI_API_KEY`:** Your OpenAI API key.
- **`DATABASE_URL`:** The connection string for your PostgreSQL database.
- **`JWT_SECRET_KEY`:** A secret key for signing JWT tokens (used for authentication).

## 📜 API Documentation

### 🔍 Endpoints

- **POST /generate:**
   - Description: Generate text using an OpenAI model.
   - Body: `{ "text": "Your input text", "model": "The OpenAI model name (e.g., gpt-3.5-turbo)" }`
   - Response: `{ "text": "Generated text" }`
- **POST /translate:**
   - Description: Translate text between languages using an OpenAI model.
   - Body: `{ "text": "Your input text", "model": "The OpenAI translation model (e.g., gpt-3.5-turbo)", "target_language": "The target language code (e.g., 'fr', 'es', 'de')" }`
   - Response: `{ "text": "Translated text" }`
- **POST /register:**
   - Description: Register a new user.
   - Body: `{ "username": "Your username", "password": "Your password" }`
   - Response: `{ "message": "Registration successful!" }`
- **POST /login:**
   - Description: Log in an existing user.
   - Body: `{ "username": "Your username", "password": "Your password" }`
   - Response: `{ "token": "JWT access token" }`

### 🔒 Authentication

1. **Register or Log In:** New users can register using the `/register` endpoint. Existing users can log in using the `/login` endpoint.
2. **Obtain JWT Token:**  Upon successful registration or login, the server returns a JWT access token.
3. **Authorization:**  Include the JWT access token in the `Authorization` header of all subsequent requests to the API.

## 📜 License & Attribution

### 📄 License

This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP

This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: OpenAI-API-Wrapper-Python

### 📞 Contact

For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
<img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
<img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
<img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
<img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>