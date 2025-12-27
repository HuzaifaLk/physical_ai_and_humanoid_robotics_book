# Data Model for Retrieval and Ingestion Pipeline Validation

This document defines the data structures used in the retrieval validation pipeline.

## 1. Sample Query

- **Description**: A text string representing a question to be used for validating the retrieval pipeline.
- **Fields**:
    - `query_id` (string, required): A unique identifier for the query.
    - `text` (string, required): The text of the query.
    - `expected_keywords` (list of strings, optional): A list of keywords expected to be in the retrieved chunks.

## 2. Retrieved Chunk

- **Description**: A content chunk returned from the vector database in response to a sample query.
- **Fields**:
    - `chunk_id` (string, required): The unique identifier of the chunk.
    - `source_url` (string, required): The URL of the page from which the chunk was extracted.
    - `text` (string, required): The text content of the chunk.
    - `score` (float, required): The similarity score of the chunk with respect to the query.
    - `metadata` (object, optional): Additional metadata from the vector database.
