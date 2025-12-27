# Quickstart: Retrieval and Ingestion Pipeline Validation

This guide provides instructions on how to run the retrieval validation script.

## Prerequisites

- Python 3.11 or higher
- An active Qdrant Cloud instance with the data from Spec 1 ingested
- A Cohere API key

## Setup

1.  **Ensure the `backend` directory is set up**:
    Follow the setup instructions from the `quickstart.md` of `005-website-ingestion-embeddings`.

2.  **Configure environment variables**:
    Ensure your `.env` file in the project root contains:
    ```
    QDRANT_URL="..."
    QDRANT_API_KEY="..."
    COHERE_API_KEY="..."
    ```

## Running the Retrieval Validation Script

The validation script is run from the command line from the project root.

```bash
uv run python backend/retrieve.py
```

The script will then:
1.  Connect to the Qdrant collection.
2.  Use a set of hardcoded sample queries to perform similarity searches.
3.  Print the retrieved chunks and their metadata.
4.  Perform basic validation checks on the results and log the output.
