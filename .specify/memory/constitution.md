<!--
---
Sync Impact Report
---
Version change: none → 1.0.0
Modified principles: n/a (initial creation)
Added sections: All
Removed sections: n/a
Templates requiring updates:
- ✅ .specify/templates/plan-template.md
- ❔ .specify/templates/spec-template.md (no changes needed)
- ❔ .specify/templates/tasks-template.md (no changes needed)
Follow-up TODOs: none
-->
# AI-Spec-Driven Technical Book with Embedded RAG Chatbot Constitution

## Core Principles

### I. Spec-First, Reproducible AI Authorship
All content is generated via Spec-Kit Plus using the Gemini CLI, ensuring a reproducible and version-controlled authoring process. Each chapter follows a standard structure: objectives, instructional examples, and concise summaries, written in a developer-focused tone using Markdown/MDX.

### II. Source-Grounded, Non-Hallucinatory Responses
The embedded RAG chatbot MUST derive answers strictly from the book's content or user-selected text. It is forbidden to invent, infer, or provide information from outside the retrieved context. All responses must cite the relevant source sections.

### III. Clear Separation of Concerns
The system maintains a strict architectural separation between three domains: (1) content authoring and generation, (2) context retrieval and chunking, and (3) language model inference and response generation. This ensures modularity, testability, and independent evolution of components.

### IV. Production-Grade Engineering Standards
The entire system—from the book's static site to the backend API—is built, tested, and deployed with production-level rigor. This includes secure secret management via environment variables, version control on GitHub, and automated build/deployment pipelines.

## Platform & Technology Stack

- **Book Platform**: Docusaurus static site, deployed to GitHub Pages, version-controlled on GitHub.
- **RAG Chatbot**: Embedded in the book UI.
  - **Stack**: FastAPI backend, Neon Serverless Postgres, Qdrant Cloud.
  - **Modes**: Global book Q&A, User-selected text Q&A.
- **Constraints**:
  - **Backend**: FastAPI (Python)
  - **Vector DB**: Qdrant Cloud
  - **Database**: Neon Serverless Postgres
  - **Secrets**: Secure environment-based secrets only.

## Quality & Success Criteria

- **Quality Gates**:
  - Successful Docusaurus build and deployment.
  - Accurate, grounded chatbot responses.
  - No hallucinations or uncited content.
- **Success Criteria**:
  - Live book on GitHub Pages.
  - Fully functional embedded RAG chatbot.
  - All responses traceable to book content.

## Governance

- **Retrieval Rules**:
  - Answers MUST be derived only from retrieved chunks.
  - User-selected text takes priority.
  - The system MUST provide an explicit fallback when context is missing.

**Version**: 1.0.0 | **Ratified**: 2025-12-18 | **Last Amended**: 2025-12-18