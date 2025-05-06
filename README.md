# JobChaser-AI

**JobChaser-AI** is an intelligent AI-driven platform built to help users create customized resumes and cover letters tailored to specific job descriptions using the power of AI. The platform integrates with a PostgreSQL database and utilizes various AI APIs like OpenRouter for resume generation.

This repository contains both the **backend** and **frontend** components of the project, as well as the necessary tools for running and managing the application using Docker.

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Running the Application](#running-the-application)
5. [Contributing](#contributing)

---

## Features

- **AI-Powered Resume Generator**: Tailor resumes and cover letters to specific job descriptions using OpenRouter AI.
- **PostgreSQL Database**: Store and manage job descriptions, resumes, and user data.
- **Docker Integration**: Easily deploy the application with Docker for managing both the backend (PostgreSQL) and the application environment.
- **Frontend Integration**: A user-friendly interface for interacting with the AI and viewing generated resumes.

---

## Tech Stack

- **Frontend**: 
  - React.js
  - Tailwind CSS
  - Vite
  
- **Backend**: 
  - Python
  - Flask (or FastAPI)
  - PostgreSQL (via Docker)
  
- **AI Integration**:
  - OpenRouter API (for resume generation)
  
- **DevOps**:
  - Docker & Docker Compose
  - GitHub Actions
  - Render/Fly.io/Vercel

---

## Installation

### Prerequisites

1. **Docker**: Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. **Git**: Install [Git](https://git-scm.com/).
3. **Python 3.x**: Install Python from [python.org](https://www.python.org/downloads/).
4. **Node.js and npm**: Install Node.js from [nodejs.org](https://nodejs.org/).

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/JobChaser-AI.git
cd JobChaser-AI
```
## Project Structure
```
JobChaser-AI/
├── ai/
│   ├── resume_ai.py
│   ├── requirements.txt
│   └── .env
├── backend/
│   └── (your backend logic)
├── frontend/
│   ├── src/
│   ├── package.json
│   └── tailwind.config.cjs
├── docker/
│   └── docker-compose.yml
├── .gitignore
└── README.md
```

## Running the Application

1. Clone the Repository
```bash
git clone https://github.com/yourusername/jobchaser-ai.git
cd jobchaser-ai
```

2. Frontend (React + Tailwind)
```bash
cd frontend
npm install
npm run dev
```

3. Backend (Spring Boot)
```bash
cd backend
./mvnw spring-boot:run
```
Ensure your application.properties is configured with PostgreSQL URL, username, and password.

4. Scraper (Python + Playwright)
```bash
cd scraper
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install
python scraper.py
```

5. AI Resume Generator (Python + LLM)
```bash
cd ai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python resume_ai.py
```
Configure your OpenAI API key in an .env file or directly in the script.

6. PostgreSQL Database via Docker
```bash
docker compose -f docker/docker-compose.yml up -d
```
This sets up PostgreSQL on port 5432 with default user/password. Adjust as needed.


## Contributing

1. Fork the project
2. Create your feature branch: git checkout -b feature/awesome-feature
3. Commit your changes: git commit -am 'Add awesome feature'
4. Push to the branch: git push origin feature/awesome-feature
5. Open a pull request


