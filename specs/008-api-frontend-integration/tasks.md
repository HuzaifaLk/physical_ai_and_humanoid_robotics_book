# Tasks: Backend-Frontend Integration

**Input**: Design documents from `/specs/008-api-frontend-integration/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Add new dependencies for the FastAPI backend.

- [ ] T001 [P] Add `fastapi` and `uvicorn` to `backend/pyproject.toml`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create the basic file structure for the new API and UI components.

- [ ] T002 Create `backend/api.py` with a placeholder FastAPI application.
- [ ] T003 [P] Create a new React component file at `src/components/Chatbot/index.js`.
- [ ] T004 [P] Create a CSS file for the new component at `src/components/Chatbot/index.css`.

---

## Phase 3: User Story 1 - Expose RAG agent via FastAPI (Priority: P1) 🎯 MVP

**Goal**: Expose the existing RAG agent via a FastAPI backend so that it can be accessed programmatically.

**Independent Test**: The FastAPI server can be run locally, and a `curl` request to the `/qa/` endpoint returns a valid JSON response from the agent.

### Implementation for User Story 1

- [ ] T005 [US1] In `backend/api.py`, import the agent logic from `backend/agent.py`.
- [ ] T006 [US1] In `backend/api.py`, define a Pydantic model for the question input.
- [ ] T007 [US1] In `backend/api.py`, implement the `/qa/` endpoint that accepts a POST request, calls the agent, and returns the answer.
- [ ] T008 [US1] Add CORS middleware to `backend/api.py` to allow requests from the Docusaurus frontend.

**Checkpoint**: At this point, the FastAPI server should be fully functional and testable with `curl`.

---

## Phase 4: User Story 2 - Integrate FastAPI with Docusaurus UI (Priority: P1)

**Goal**: Allow a reader to ask questions to the RAG agent directly from the book's UI.

**Independent Test**: A user can type a question into the chatbot UI, and the agent's answer is displayed.

### Implementation for User Story 2

- [ ] T009 [US2] In `src/components/Chatbot/index.js`, implement the basic UI with an input field, a submit button, and a display area for the conversation.
- [ ] T010 [US2] In `src/components/Chatbot/index.js`, add state management for the user's input, the conversation history, and loading status.
- [ ] T011 [US2] In `src/components/Chatbot/index.js`, implement the `fetch` logic to send the user's question to the `http://localhost:8000/qa/` backend endpoint.
- [ ] T012 [US2] To make the chatbot persistent, swizzle the Docusaurus `Layout` component and import and render the `Chatbot` component within it. The file to modify will likely be `src/theme/Layout/index.js`.

**Checkpoint**: At this point, the chatbot UI should be visible and functional within the Docusaurus site.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [ ] T013 Add comprehensive error handling to the `backend/api.py` endpoint.
- [ ] T014 [P] Add loading and error states to the UI in `src/components/Chatbot/index.js`.
- [ ] T015 [P] Style the chatbot component using `src/components/Chatbot/index.css` to match the Docusaurus theme.
- [ ] T016 Create a `quickstart.md` in `specs/008-api-frontend-integration/` explaining how to run the backend and frontend together.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup.
- **User Story 1 (Phase 3)**: Depends on Foundational.
- **User Story 2 (Phase 4)**: Depends on User Story 1. The frontend needs the backend to be available.
- **Polish (Phase 5)**: Depends on all other phases.
