# Memory Journal

## Purpose

Record how memory is used in this exercise and what should be improved later.

## Current Run Context

- The current memory system is a local Markdown vault compatible with Obsidian.
- Retrieval is manual: the agent reads selected notes and cites exact paths.
- No vector database, semantic search, automated RAG, cloud knowledge base, Open WebUI, Flowise, or Langflow integration is configured for this exercise.
- This makes the setup limited but easy to audit.

## Coach Agent Use Case

Required question:

> Based on my notes, what should I learn this week to better launch my offer?

The Coach Agent should answer from vault notes only, cite sources, avoid invented facts, and mark recommendations clearly.

## Improvement Ideas

- Add a real search index later if note volume grows.
- Add retrieval tests that show which notes were selected for a question.
- Add a human validation step before any agent writes permanent vault notes.

## Related Notes

- [[learning-plan]]
- [[permissions]]
- [[decisions]]
