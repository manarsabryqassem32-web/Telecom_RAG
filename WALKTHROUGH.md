# Telecom RAG - Live Demo Walkthrough

## 1. Environment Setup

- Created a Python virtual environment using Python 3.14.
- Activated the virtual environment.
- Installed project dependencies using `requirements.txt`.

## 2. Secrets Configuration

- Created `.env` from `.env.example`.
- Configured `GOOGLE_API_KEY` for Gemini.
- The actual API key is kept local and is not committed to GitHub.

## 3. Architecture & Patterns

### ModelFactory

The project uses a Factory Pattern through `ModelFactory` to centralize the initialization of the embedding model and LLM.

### LRU Cache

`@lru_cache(maxsize=1)` is used for the embedding and LLM factory methods to avoid re-initializing heavy models on every request.

### RAG Service

The `RAGService` implements the main RAG pipeline:

1. Retrieve relevant chunks from the FAISS vector store.
2. Combine the retrieved context with the customer ticket.
3. Build the prompt using LangChain.
4. Generate the response using Gemini.
5. Return response and telemetry such as source count, execution time, and token usage.

## 4. FastAPI Microservice

The application was successfully launched using:

```bash
python main.py
FastAPI and Uvicorn started successfully
Swagger UI was accessed through:
http://127.0.0.1:8000/docs
Health Check

GET / was tested successfully and returned:

200 OK

with a healthy application response.

RAG Query

POST /api/v1/query was tested with a customer ticket.

The endpoint returned a 404 because the FAISS vector database index had not been created yet. The API correctly reported that /api/v1/ingest must be triggered first.

This confirms that the FastAPI routing and RAG service are connected correctly and that the query endpoint validates the availability of the vector index before retrieval.