# Quickstart: Backend-Frontend Integration

This guide explains how to run the FastAPI backend and the Docusaurus frontend to use the integrated chatbot.

## Prerequisites

- Python 3.14+
- Node.js and npm
- `uv` installed (`pip install uv`)

## 1. Install Backend Dependencies

Navigate to the `backend` directory and install the Python dependencies:

```bash
cd backend
uv pip sync pyproject.toml
```

## 2. Install Frontend Dependencies

Navigate to the root of the project and install the Node.js dependencies:

```bash
npm install
```

## 3. Run the Backend Server

From the `backend` directory, run the FastAPI server using `uvicorn`:

```bash
cd backend
uvicorn api:app --reload
```

The backend server will be running at `http://localhost:8000`.

## 4. Run the Frontend Server

From the root of the project, run the Docusaurus development server:

```bash
npm start
```

The Docusaurus site will be running at `http://localhost:3000`.

## 5. Use the Chatbot

Open your browser and navigate to `http://localhost:3000`. You should see the chatbot UI component in the bottom-right corner of the screen. You can now ask questions to the RAG agent.
