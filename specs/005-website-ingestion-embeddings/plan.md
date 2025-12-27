# Implementation Plan: Website Ingestion, Embeddings, and Vector Storage

**Branch**: `005-website-ingestion-embeddings` | **Date**: 2025-12-24 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/005-website-ingestion-embeddings/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan refines the backend structure and ingestion flow for the Python-based ingestion pipeline. It outlines crawling Docusaurus URLs, chunking content, generating embeddings using Cohere, and storing vectors with metadata in Qdrant, all orchestrated through a `uv`-initialized backend with a single `main.py`.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: uv, Cohere, Qdrant-client, BeautifulSoup4, LangChain, Typer
**Storage**: Qdrant Cloud
**Testing**: pytest
**Target Platform**: Linux server (for the script execution environment)
**Project Type**: Single project (backend ingestion script)
**Performance Goals**: Under 30 minutes for a full ingestion run (initial implementation).
**Constraints**: The ingestion script will accept a single root URL of the Docusaurus website as a command-line argument, attempting to find and parse `sitemap.xml` for page discovery, with recursive crawling as a fallback.
**Scale/Scope**: Ingest a single Docusaurus book of moderate size.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Spec-First, Reproducible AI Authorship**: The plan follows the spec-first process.
- [X] **Source-Grounded, Non-Hallucinatory Responses**: This plan is the foundation for source-grounding the chatbot.
- [X] **Clear Separation of Concerns**: The ingestion pipeline is a separate concern from retrieval and inference.
- [X] **Production-Grade Engineering Standards**: The plan will use a standard Python project structure with testing.

## Project Structure

### Documentation (this feature)

```text
specs/005-website-ingestion-embeddings/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
backend/
├── .venv/         # uv managed virtual environment
├── main.py        # Contains all ingestion logic (URL fetching, chunking, embedding, Qdrant storage)
└── pyproject.toml # Project configuration
```

**Structure Decision**: A new `backend/` directory will house the ingestion logic. It utilizes `uv` for environment management and consolidates all ingestion functionality into a single `main.py` file for simplicity and easier execution. This structure is chosen as the feature is a self-contained, backend ingestion script and does not require a more complex service-oriented architecture.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| | | |
| | | |