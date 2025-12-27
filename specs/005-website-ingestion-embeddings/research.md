# Research for Website Ingestion

This document records the decisions made to resolve ambiguities identified during the planning phase.

## 1. Performance Goals: Ingestion Time

- **Decision**: For the initial implementation, a full ingestion run should complete in **under 30 minutes**.
- **Rationale**: This is a reasonable upper bound for a moderately sized Docusaurus site. It allows for network latency, API calls to the embedding model, and database writes without being excessively long for a manual or semi-automated process. This can be optimized later if needed.
- **Alternatives considered**:
    - A shorter time (e.g., <5 minutes) might be too restrictive and require significant optimization upfront.
    - A longer time (e.g., >1 hour) would be inconvenient for developers running the script.

## 2. Constraints: Docusaurus Book URLs

- **Decision**: The ingestion script will accept a single root URL of the Docusaurus website as a command-line argument. The script will then attempt to find and parse a `sitemap.xml` file from the root of the site to discover all available pages. If a sitemap is not found, it will perform a recursive crawl starting from the root URL.
- **Rationale**: This approach is robust. A sitemap is the most reliable way to discover all pages. The recursive crawl provides a good fallback. A command-line argument makes the script flexible and easy to use in different environments.
- **Alternatives considered**:
    - Requiring a manifest file with all URLs: This would be more work to prepare and maintain.
    - Hardcoding the URLs: This is not flexible and would require code changes for different books.
