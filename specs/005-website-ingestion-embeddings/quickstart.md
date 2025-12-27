# Quickstart: Website Ingestion

This guide provides instructions on how to set up and run the website ingestion pipeline.

## Prerequisites

- Python 3.11 or higher
- An active Qdrant Cloud instance or a local Qdrant container
- A Cohere API key

## Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/HuzaifaLk/physical_ai_and_humanoid_robotics_book
    cd physical_ai_and_humanoid_robotics_book
    ```

2.  **Initialize `uv` project and add dependencies**:
    ```bash
    cd backend
    uv init # if not already done
    uv add cohere qdrant-client beautifulsoup4 langchain-text-splitters typer requests python-dotenv # Add all necessary dependencies
    cd ..
    ```

3.  **Configure environment variables**:
    Create a `.env` file in the root of the project and add the following:
    ```
    QDRANT_URL="..."
    QDRANT_API_KEY="..."
    COHERE_API_KEY="..."
    ```

## Running the Ingestion Script

The ingestion script is run from the command line from the project root. You need to provide the root URL of the Docusaurus book to be ingested.

```bash
uv run python backend/main.py --url https://path-to-docusaurus-book.com
```

The script will then:
1.  Crawl the website starting from the provided URL.
2.  Extract content from each page.
3.  Chunk the content.
4.  Generate embeddings using Cohere.
5.  Store the embeddings in your Qdrant instance.
