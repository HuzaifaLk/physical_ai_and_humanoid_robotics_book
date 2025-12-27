# Research for OpenAI Agent for RAG

This document records the decisions made to resolve ambiguities identified during the planning phase.

## 1. Technical Approach

- **Decision**: The implementation will follow a standard and straightforward Retrieval-Augmented Generation (RAG) pattern.
- **Rationale**: The feature description is clear and aligns with well-established patterns for building RAG agents. The process will be:
    1.  Receive user query.
    2.  Embed the query using the existing Cohere embedding function.
    3.  Use the query embedding to search the Qdrant database and retrieve context.
    4.  Construct a prompt for an OpenAI model, including the user query and the retrieved context.
    5.  Send the prompt to the OpenAI API and return the generated response.
    6.  If no context is retrieved, return a predefined message stating the question cannot be answered.
- **Alternatives considered**: No alternatives were necessary as the approach is well-defined by the specification and standard industry practice.
