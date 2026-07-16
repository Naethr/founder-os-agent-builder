# Memory Setup

## Memory System Name

Founder OS Local Obsidian Memory.

## Stack Used

Local Markdown vault with manual note reading.

## Why This Stack Was Chosen

This stack was chosen because the exercise goal is to prove understanding of memory, sources, and agent grounding, not to fake an advanced retrieval system.

- It is simple and auditable.
- It is compatible with Obsidian because notes are plain Markdown files.
- It costs nothing.
- It keeps all exercise data inside the local repository.
- It makes citations traceable because the agent can name exact note paths.

Obsidian was not launched as part of this setup. No cloud knowledge base, vector database, Open WebUI, Flowise, Langflow, semantic search, or automated RAG system was configured.

## Vault Folder Structure

```text
vault/
  10-business/
  20-clients/
  30-offers/
  40-seo-market/
  50-sales-mail/
  60-admin/
  70-learning/
  90-agent-runs/
```

## How Notes Are Organized

- `10-business/` stores durable business context and decisions.
- `20-clients/` stores target client profiles and qualification signals.
- `30-offers/` stores the Web Studio OS offer and scope boundaries.
- `40-seo-market/` stores SEO ideas and market-facing assumptions.
- `50-sales-mail/` stores sales tone and discovery questions.
- `60-admin/` stores permissions, validation, quote, and evidence rules.
- `70-learning/` stores founder learning priorities.
- `90-agent-runs/` stores memory-use journal notes.

Notes are concise, practical, and linked with Obsidian-style links where useful.

## How The Coach Agent Uses Notes

The Coach Agent uses only vault notes as its knowledge source for memory-grounded answers.

Manual workflow:

1. Read the user question.
2. Select relevant vault notes by note title and folder purpose.
3. Read the selected notes directly.
4. Answer only from those notes.
5. Separate explicit source-supported facts from recommendations.
6. Cite every note used with its repository path.
7. State limitations when the notes do not support a stronger claim.

## Coach Agent Configuration

Mission: help the founder decide what to learn next to launch Web Studio OS, using only the local vault as memory.

Required question:

```text
Based on my notes, what should I learn this week to better launch my offer?
```

The Coach Agent must:

- use only the vault notes as its knowledge source;
- cite the exact note paths used;
- avoid inventing facts;
- distinguish what is explicitly supported by notes from recommendations;
- propose a realistic one-week learning plan;
- prioritize simple, practical learning steps for launching Web Studio OS.

The Coach Agent must not:

- claim external market research unless it exists in the vault;
- invent client data;
- invent prices beyond documented planning examples;
- write permanent notes without validation;
- send emails or perform external actions.

## How Citations Are Produced

Citations are produced manually by listing the exact Markdown note paths used for the answer, for example:

```text
Source: vault/30-offers/web-studio-offer.md
```

Inline citations may also use bracketed paths such as `[vault/70-learning/learning-plan.md]`.

## Limits Of Manual Note Reading

- No semantic search.
- No automatic retrieval.
- No vector database.
- No real RAG.
- Note selection can miss relevant files.
- Answer quality depends on note quality.
- This approach does not scale well to a large vault.

## Data Exposure

No data is exposed outside the local repository for this exercise.

## Cost Analysis

Cost is zero for the memory stack used in this exercise.

## Future Improvement Path

A future version could add real semantic search or RAG with a configured tool. That should include clear evidence of the tool used, indexed documents, retrieval results, cost, data exposure, and limitations.
