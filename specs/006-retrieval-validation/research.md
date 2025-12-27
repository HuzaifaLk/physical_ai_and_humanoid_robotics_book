# Research for Retrieval and Ingestion Pipeline Validation

This document records the decisions made to resolve ambiguities identified during the planning phase.

## 1. Constraints: Sample Queries for Testing

- **Decision**: For the initial implementation, a set of 3-5 sample queries will be hardcoded in the `retrieve.py` script. These queries will be designed to test different aspects of the book's content.
- **Rationale**: Hardcoding a small, representative set of queries is sufficient for this validation stage. It allows for a quick and repeatable test of the retrieval pipeline without requiring external input. The queries should cover broad topics, specific technical terms, and questions that span multiple sections.
- **Alternatives considered**:
    - Taking queries from the command line: This is more flexible but less repeatable for a standardized validation test.
    - Reading queries from a file: This is a good option for a larger set of queries, but overkill for this initial validation.

### Sample Queries:
1. "What is the nervous system of a robot?" (Broad topic)
2. "How does a digital twin work?" (Specific concept)
3. "Explain the role of NVIDIA Isaac Sim." (Specific technology)
