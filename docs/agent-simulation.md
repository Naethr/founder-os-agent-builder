# Agent Simulation

## Why Simulation Is Used

Day 3 uses a local documentation-based simulation because the project goal is to prove the Founder OS operating model, not to fake a no-code platform setup.

No real visual agent platform is configured for this exercise. No cloud data was sent. No paid API was used. No external automation happened.

## How Agents Are Represented

Agents are represented by Markdown cards in `docs/agent-cards/`.

Each card defines:

- mission;
- when to use the agent;
- skills used;
- tools or actions used;
- memory sources;
- inputs and outputs;
- approval rules;
- risks;
- example task;
- simulation status.

This makes the agent team auditable without claiming that a runtime agent platform exists.

## How Skills Are Selected

Skills are reusable Markdown operating instructions stored in `founder_os/skills/`.

The simulated orchestrator selects a skill by matching the user request to the skill purpose:

- product scoping uses `product-brief.md`;
- SEO preparation uses `seo-research.md`;
- sales messages use `sales-copy.md`;
- admin planning uses `admin-sandbox.md`;
- founder learning uses `learning-coach.md`;
- prospecting preparation uses `prospecting.md`.

If a request crosses domains, the primary skill handles the output and secondary skills are used only when needed.

## How Tools / Actions Are Selected

Tool names come from `docs/tool-catalog.md`. The simulation does not execute real tools. It records which documented action would be used.

Examples:

- `qualify_lead` for lead fit and next-step analysis;
- `draft_email_reply` for email drafts;
- `create_mock_quote` for fictional quote drafts;
- `extract_seo_keywords` for keyword hypotheses;
- `search_knowledge_base` for local Markdown memory lookup;
- `write_note_draft` for proposed notes that still need approval.

## How Vault Memory May Be Used

The vault is a local Markdown memory folder. Agents may read relevant notes manually and cite exact paths.

Memory use must follow these rules:

- cite note paths when notes are used;
- separate source-supported facts from recommendations;
- do not treat drafts as validated facts;
- do not write permanent notes without human approval;
- do not store personal, client, prospect, or billing data without approval.

## How Test Traces Are Produced

Test traces are Markdown files in `evidence/runs/`.

Each trace records:

- input;
- skill used;
- simulated tool or action;
- memory used when relevant;
- output;
- format compliance;
- observed limits.

These traces are not screenshots, platform exports, or real automation logs. They are local, auditable evidence of how the simulated agents should behave.

## Limits Of The Simulation

- No live agent runtime exists.
- No visual platform was configured.
- No APIs were called.
- No emails were sent.
- No SEO tools were queried.
- No scraping happened.
- No accounting or quoting platform was connected.
- Manual memory selection can miss relevant notes.
- The traces prove workflow design, not production reliability.

## Future Real Platform Requirements

To implement this in a real visual platform later, the project would need:

- a selected platform such as n8n, Flowise, Langflow, Open WebUI, or another approved tool;
- explicit data exposure and cost review;
- configured agent nodes or workflows;
- permission gates for sending, publishing, quoting, storing data, and paid API use;
- real tool execution logs;
- test runs with inputs, outputs, timestamps, and failure cases;
- exported configuration files only if the platform actually supports export and was really configured.

## Bonus Status

The bonus was not completed because no configured visual platform was available in this repository. No fake exports or fake platform configuration were created.
