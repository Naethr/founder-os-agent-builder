# Orchestration Setup

## Stack Used

Manual documented orchestration using local Markdown files.

## Tool Used

The tool used for this exercise is local Markdown documentation in the repository:

- Agent definitions in `docs/agent-cards/`.
- Skills in `founder_os/skills/`.
- Tool and permission rules in `docs/tool-catalog.md` and `docs/permissions-policy.md`.
- Business memory in `vault/`.
- Run evidence in `evidence/runs/`.

No no-code platform, backend, frontend, database, Docker setup, or cloud workflow engine was configured for this exercise.

## Local / Cloud / Hybrid Choice

Local only.

All orchestration artifacts are Markdown files stored in the repository. No data was sent to a cloud service by this exercise.

## What Is Automated

Nothing is fully automated yet, except local repository operations and existing local file editing. There is no automatic agent execution, no real runtime router, no live memory retrieval, and no tool execution engine.

## What Is Simulated

The following parts are simulated manually and documented in Markdown:

- Agent calls.
- Agent handoffs.
- Context passing.
- Intermediate outputs.
- Final synthesis.
- Approval gates.

The simulation is intentional because the current goal is to prove orchestration understanding before adding runtime complexity.

## How the Orchestrator Selects Agents

The orchestrator selects agents by matching the request type against `docs/routing-rules.md`.

Example:

- A prospect request for a showcase website triggers Code / Product Agent for scope, SEO / Market Agent for visibility direction, Admin / Accounting Agent for fictional quote planning, and Mail / Sales Agent for a reply draft.
- A request involving price triggers Admin / Accounting Agent and requires human approval before any commercial use.
- A request involving external communication triggers Mail / Sales Agent and requires human approval before sending.

## How Context Is Passed

Context is passed through explicit handoff sections:

1. The orchestrator records confirmed facts, assumptions, missing information, and constraints.
2. Each agent receives only the context needed for its mission.
3. Each agent output preserves uncertainty labels.
4. Downstream agents receive prior outputs with their validation status.
5. The final synthesis separates confirmed information, assumptions, questions, recommended next action, and required approvals.

## How Intermediate Outputs Are Collected

Intermediate outputs are collected in the run trace under `evidence/runs/`.

For the Day 3 workflow, the complete trace is stored in `evidence/runs/day-3-orchestration.md`.

## How Approvals Are Handled

Approvals are documented, not executed.

Human approval is required before:

- Sending emails.
- Sending or using quotes commercially.
- Writing permanent vault notes.
- Storing personal, client, prospect, or billing data.
- Publishing content.
- Using paid APIs.
- Contacting leads.
- Pushing to a remote repository.

If approval is missing, the orchestrator may create a draft or recommendation, but it must not perform the sensitive action.

## Data Exposure

Data exposure for this exercise:

- Data sent to cloud: none.
- Paid APIs used: none.
- External platforms configured: none.
- Real client or prospect personal data stored: none.
- Fake screenshots, exports, or API calls created: none.

All work is local Markdown documentation.

## Cost Analysis

Cost for this exercise: zero.

No paid API, SaaS workflow tool, hosting platform, database, or external automation was used.

## Limitations

- No real runtime engine.
- No automatic agent execution.
- No real RAG system.
- No live tools.
- No connected email, CRM, accounting, SEO, or no-code platform.
- No automatic approval workflow.
- Manual traces can prove reasoning, but not operational reliability.
- SEO outputs are unvalidated hypotheses unless future tooling is added.
- Quote outputs are fictional planning drafts unless validated by a human.

## Next Improvement

The next improvement should be one narrow real orchestration, implemented only after the manual workflow is validated.

Reasonable options:

- A small local script that reads a request file, applies routing rules, and generates a structured Markdown trace.
- A minimal n8n workflow for internal draft creation only.
- A Flowise, Langflow, or Open WebUI workflow if a real platform is configured and evidenced.

The first automated version should still avoid sending emails, using paid APIs, publishing content, or writing permanent memory without explicit approval.
