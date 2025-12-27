# Tasks: OpenAI Agent for RAG

**Input**: Design documents from `/specs/007-openai-agent-rag/`

## Path Conventions

-   All new source code will be in `backend/agent.py`.
-   All new tests will be in `backend/tests/`.

---

## Phase 1: Setup

**Purpose**: Prepare the project for the new agent code.

- [X] T001: Create the `backend/agent.py` file with initial placeholder content.
- [X] T002: Add the `openai` dependency to the `backend/pyproject.toml` file.

---

## Phase 2: Foundational

**Purpose**: Implement core infrastructure for the agent script.

- [X] T003: Implement environment variable loading in `agent.py` to securely load `QDRANT_URL`, `QDRANT_API_KEY`, `COHERE_API_KEY`, and `OPENAI_API_KEY`.
- [X] T004: Implement a basic `typer` application structure in `agent.py` that accepts a user's question as a command-line argument.

---

## Phase 3: User Story 1 - Contextual Retrieval

**Goal**: Connect to the vector database and retrieve relevant context for a given question.

### Tests for User Story 1
- [X] T005: Create `backend/tests/unit/test_agent.py` with a placeholder test.
- [X] T006: Create `backend/tests/integration/test_agent_flow.py` with a placeholder test for the end-to-end agent flow.
- [X] T007: In `test_agent.py`, add a unit test to mock and verify the context retrieval function.

### Implementation for User Story 1
- [X] T008: In `agent.py`, implement a function `retrieve_context` that takes a user query, embeds it using Cohere, and searches the Qdrant database to return relevant text chunks. This can reuse logic from `retrieve.py`.

---

## Phase 4: User Story 2 & 3 - Grounded Generation & Refusal

**Goal**: Generate an answer based only on the retrieved context, or refuse to answer if no context is found.

### Tests for User Story 2 & 3
- [X] T009: In `test_agent.py`, add a unit test to verify that the prompt sent to the LLM is correctly constructed from the user query and retrieved context.
- [X] T010: In `test_agent.py`, add a unit test to ensure the agent returns a "cannot answer" message when the `retrieve_context` function returns no chunks.

### Implementation for User Story 2 & 3
- [X] T011: In `agent.py`, implement a function `generate_grounded_answer` that takes the original query and context chunks, constructs a system prompt instructing the model to answer only from the provided text, and calls the OpenAI API.
- [X] T012: In `agent.py`, implement the main orchestration logic that:
    - Calls `retrieve_context`.
    - Checks if context was found.
    - If context exists, calls `generate_grounded_answer`.
    - If no context exists, prints a "cannot answer" message.
    - Prints the final answer and the sources of the context.

---

## Phase N: Polish & Cross-Cutting Concerns

- [X] T013: Run `quickstart.md` validation, ensuring the documented steps correctly run the agent.
- [X] T014: Add comprehensive error handling throughout the `agent.py` script.
- [X] T015: Refactor and clean up the code in `agent.py` for clarity and readability.