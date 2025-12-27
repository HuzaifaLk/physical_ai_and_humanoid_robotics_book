---
id: 0001
title: Create Project Constitution for AI Book with RAG
stage: constitution
date: 2025-12-18
surface: agent
model: Gemini
feature: none
branch: unknown
user: unknown
command: /sp.constitution
labels: [constitution, RAG, AI-book]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
 - none
---

## Prompt

/sp.constitution

Project: AI-Spec-Driven Technical Book with Embedded RAG Chatbot

Purpose:
Create a technical book authored via Spec-Kit Plus and Gemini CLI, published with Docusaurus on GitHub Pages, and enhanced with an embedded RAG chatbot that answers questions strictly from the book or user-selected text.

Core Principles:
- Spec-first, reproducible AI authorship
- Source-grounded, non-hallucinatory responses
- Clear separation of authoring, retrieval, and inference
- Production-grade engineering standards

Authoring Standards:
- All content generated via Spec-Kit Plus using Gemini CLI
- Markdown/MDX as canonical format
- Developer-focused, instructional tone
- Each chapter includes objectives, examples, and summaries

Book Platform:
- Docusaurus static site
- Deployed to GitHub Pages
- Version-controlled on GitHub

RAG Chatbot:
- Embedded in book UI
- Stack:
  - OpenAI Agents or ChatKit SDK
  - FastAPI backend
  - Neon Serverless Postgres
  - Qdrant Cloud (Free Tier)
- Modes:
  1. Global book Q&A
  2. User-selected text Q&A
- Must refuse answers outside retrieved context
- Responses cite relevant book sections

Retrieval Rules:
- Answers derived only from retrieved chunks
- User-selected text takes priority
- Explicit fallback when context is missing

Constraints:
- Backend: FastAPI (Python)
- Vector DB: Qdrant Cloud
- Database: Neon Serverless Postgres
- Secure env-based secrets only

Quality Gates:
- Successful Docusaurus build and deployment
- Accurate, grounded chatbot responses
- No hallucinations or uncited content

Success Criteria:
- Live book on GitHub Pages
- Fully functional embedded RAG chatbot
- All responses traceable to book content

## Response snapshot

Created the project constitution and updated the plan template.

## Outcome

- ✅ Impact: Project constitution created and dependent templates updated.
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md, .specify/templates/plan-template.md
- 🔁 Next prompts: none
- 🧠 Reflection: The agent correctly identified the need to create the constitution, update dependent templates, and create a PHR. It also correctly handled the case where the PHR script was for a different OS.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
