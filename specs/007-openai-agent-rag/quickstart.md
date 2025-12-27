# Quickstart: OpenAI Agent for RAG

This guide provides instructions on how to run the RAG agent script.

## Prerequisites

- All setup from the previous specs (`005-website-ingestion-embeddings` and `006-retrieval-validation`) must be complete.
- The `backend/.venv` virtual environment must be created and synced.
- The Qdrant collection `docusaurus_book` must be populated with data from the ingestion script.

## Setup

1.  **Add OpenAI API Key**: You must add your OpenAI API key to the `backend/.env` file. Open the file and add the following line:

    ```
    OPENAI_API_KEY="..."
    ```

    Ensure your `.env` file now contains keys for QDRANT, COHERE, and OPENAI.

## Running the RAG Agent

The agent script is run from the command line from the project root. You provide the question you want to ask as an argument.

1. **Activate the virtual environment** (if not already active):
    ```bash
    # From the project root
    cd backend
    .\.venv\Scripts\activate
    ```
2. **Run the script**:
    ```bash
    # From the backend directory
    python agent.py "Your question about the book here"
    ```

### Example

```bash
python agent.py "What is a digital twin?"
```

The script will then:
1.  Connect to the Qdrant collection.
2.  Embed your question using Cohere.
3.  Retrieve relevant context from Qdrant.
4.  Pass the context and question to an OpenAI model to generate a grounded answer.
5.  Print the final answer and the sources used.
