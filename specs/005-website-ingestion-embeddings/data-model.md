# Data Model for Website Ingestion

This document defines the data structures used in the ingestion pipeline.

## 1. Content Chunk

- **Description**: Represents a semantically meaningful piece of text extracted from a single page of the Docusaurus book.
- **Fields**:
    - `doc_id` (string, required): A unique identifier for the chunk.
    - `source_url` (string, required): The URL of the page from which the chunk was extracted.
    - `text` (string, required): The text content of the chunk.
    - `metadata` (object, optional): A flexible field for additional metadata, such as:
        - `module` (string): The book module the page belongs to.
        - `chapter` (string): The chapter the page belongs to.
        - `title` (string): The title of the page.
- **Relationships**: A single book page can be broken down into multiple `ContentChunk` entities.

## 2. Vector Embedding

- **Description**: Represents the vector embedding of a `ContentChunk` stored in the vector database. In Qdrant, this corresponds to a `Point`.
- **Fields**:
    - `id` (string, required): The unique identifier of the point, corresponding to `ContentChunk.doc_id`.
    - `vector` (array of floats, required): The dense vector representation of the chunk's text.
    - `payload` (object, required): The metadata associated with the vector, which contains the `ContentChunk` fields (`source_url`, `text`, `metadata`).

- **Validation Rules**:
    - The `id` of the vector embedding must match the `doc_id` of a `ContentChunk`.
    - The `vector` must be of the dimension expected by the embedding model (e.g., 1024 for Cohere's `embed-english-v3.0`).
