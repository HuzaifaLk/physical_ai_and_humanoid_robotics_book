# Tasks: Website Ingestion, Embeddings, and Vector Storage

**Input**: Design documents from `/specs/005-website-ingestion-embeddings/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- All source code and tests will reside within the `backend/` directory as specified in `plan.md`.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for the `backend/` directory.

- [X] T001 Create `backend/` directory and initialize a `uv` project.
- [X] T002 Create `backend/pyproject.toml` and add necessary dependencies (uv, Cohere, Qdrant-client, BeautifulSoup4, LangChain, Typer, pytest).
- [X] T003 Configure basic `uv` environment and create `backend/.venv/`.
- [X] T004 [P] Setup `pytest` for testing, create `backend/tests/` directory.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T005 Implement command-line argument parsing for the root URL in `backend/main.py`.
- [X] T006 Implement environment variable loading for API keys (Qdrant, Cohere) in `backend/main.py`.
- [X] T007 Implement a basic logging setup in `backend/main.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - Content Extraction (Priority: P1) 🎯 MVP

**Goal**: Automatically crawl and extract all text content from a deployed Docusaurus website.

**Independent Test**: The system can be given a root URL of the Docusaurus site, and it should produce a collection of documents, each containing the text content of a single page.

### Tests for User Story 1

- [X] T008 [P] [US1] Unit test for URL crawling logic, including sitemap discovery and recursive fallback in `backend/tests/unit/test_crawler.py`.
- [X] T009 [P] [US1] Unit test for content extraction logic (parsing HTML, removing boilerplate) in `backend/tests/unit/test_extractor.py`.
- [X] T010 [US1] Integration test for successful URL crawling and content extraction from a mock Docusaurus site in `backend/tests/integration/test_ingestion_flow.py`.

### Implementation for User Story 1

- [X] T011 [US1] Implement `main()` orchestration function in `backend/main.py`.
- [X] T012 [US1] Implement URL crawling logic (sitemap discovery + recursive fallback) within `backend/main.py` or a helper function.
- [X] T013 [US1] Implement content extraction (parsing HTML, removing boilerplate) within `backend/main.py` or a helper function.
- [X] T014 [US1] Handle error logging for unreachable URLs during crawling in `backend/main.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Content Chunking and Embedding (Priority: P2)

**Goal**: Chunk the extracted content into semantically meaningful pieces and generate vector embeddings for each chunk.

**Independent Test**: Provide a sample of extracted text. The system should output a set of smaller text chunks and a corresponding set of vector embeddings.

### Tests for User Story 2

- [X] T015 [P] [US2] Unit test for content chunking logic, ensuring semantic boundaries are preserved in `backend/tests/unit/test_chunker.py`.
- [X] T016 [P] [US2] Unit test for embedding generation using mock Cohere API responses in `backend/tests/unit/test_embedder.py`.
- [X] T017 [US2] Integration test for chunking and embedding a sample text in `backend/tests/integration/test_ingestion_flow.py`.

### Implementation for User Story 2

- [X] T018 [US2] Implement content chunking logic within `backend/main.py` or a helper function.
- [X] T019 [US2] Integrate with Cohere API for embedding generation within `backend/main.py` or a helper function.
- [X] T020 [US2] Handle errors for unavailable Cohere API or failed embedding generation.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Vector Storage (Priority: P3)

**Goal**: Store the generated embeddings and their associated metadata in a specified vector database (Qdrant).

**Independent Test**: Provide a set of embeddings and metadata. The system should successfully insert them into a Qdrant collection. A subsequent similarity search should be able to retrieve the correct vectors.

### Tests for User Story 3

- [X] T021 [P] [US3] Unit test for Qdrant client initialization and collection management in `backend/tests/unit/test_qdrant_manager.py`.
- [X] T022 [US3] Integration test for storing embeddings in Qdrant and basic retrieval in `backend/tests/integration/test_ingestion_flow.py`.

### Implementation for User Story 3

- [X] T023 [US3] Implement Qdrant client initialization and collection management within `backend/main.py` or a helper function.
- [X] T024 [US3] Implement storing embeddings and metadata in Qdrant within `backend/main.py` or a helper function.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T025 Run `quickstart.md` validation, ensuring the documented steps correctly set up and run the ingestion pipeline.
- [X] T026 Add comprehensive error handling throughout the `backend/main.py` script.
- [X] T027 Refactor `backend/main.py` into smaller, more modular functions/files within `backend/` for better organization and readability.
- [X] T028 Implement performance optimization across the entire ingestion flow.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
