# Founder OS Blueprint

Founder OS Blueprint is the planning foundation for a future AI-assisted operating system for founder work.

In this repository, **Founder OS** means a lightweight coordination layer that helps a founder handle repeatable work: clarifying offers, preparing client deliverables, organizing knowledge, drafting sales material, tracking evidence, and keeping sensitive actions under human control.

This is the **Day 1 blueprint only**. The system is not implemented yet. There is no application code, production workflow, live integration, backend, frontend, or automation in this repository.

## Project Context

The chosen case is **Web Studio OS**: an AI-assisted operating system for a small web development micro-agency.

Web Studio OS is designed for work such as landing pages, small websites, local SEO basics, lead capture, maintenance, sales follow-up, quote preparation, and delivery planning.

The target customers are freelancers, artisans, local businesses, coaches, consultants, and small service businesses that need a professional web presence but lack time, technical confidence, or clear positioning.

## Repository Map

| Path | Purpose |
|---|---|
| `docs/business-brief.md` | Defines the Web Studio OS business case, target customers, offer, pricing model, and repetitive work the system should support. |
| `docs/architecture.md` | Describes the high-level system architecture, orchestrator, agents, vault memory, evidence storage, human validation, and local/cloud/hybrid options. |
| `docs/agent-roles.md` | Defines the orchestrator and six core agents with their missions, inputs, outputs, allowed actions, forbidden actions, validation triggers, and evidence expectations. |
| `docs/permissions-policy.md` | Classifies sensitive actions as allowed, forbidden, or allowed only with human validation. |
| `docs/provider-choice.md` | Explains the provisional hybrid provider choice: local vault and Git, cloud AI for stronger reasoning, and optional local models for private drafts or experiments. |
| `docs/run-journal.md` | Records the Day 1 reasoning, important agents, sensitive actions, open questions, and example requests for future workflows. |
| `evidence/` | Stores future proof of real work, including screenshots and run records. No fake evidence belongs here. |
| `exports/` | Reserved for future exported documents or deliverables generated from validated workflows. |
| `vault/` | Reserved for future Obsidian-style memory, durable notes, templates, decisions, and validated operating knowledge. |

## Recommended Reading Order

1. Read `docs/business-brief.md` to understand the business problem and chosen case.
2. Read `docs/architecture.md` to understand the system shape and human validation model.
3. Read `docs/agent-roles.md` to review each agent's scope and boundaries.
4. Read `docs/permissions-policy.md` to understand which actions require approval.
5. Read `docs/provider-choice.md` to understand the provisional local, cloud, and hybrid tradeoffs.
6. Read `docs/run-journal.md` to see the Day 1 reasoning and near-term questions.

## Agent Overview

The blueprint defines one orchestrator and six core agents:

- **Orchestrator:** coordinates requests, routes tasks, checks permissions, asks for human validation, and records outcomes.
- **Code / Product Agent:** turns business needs into product scopes, implementation checklists, acceptance criteria, and technical risk notes.
- **SEO Agent:** prepares practical SEO recommendations, metadata, heading structures, local keyword ideas, and content improvement notes.
- **Prospecting Agent:** prepares prospect research, qualification notes, pain hypotheses, and outreach context without contacting leads.
- **Mail / Sales Agent:** drafts emails, follow-ups, call notes, and objection handling material without sending messages.
- **Admin / Accounting Agent:** prepares fictional quote drafts, invoice drafts, scope summaries, and admin checklists for review.
- **Coach Agent:** challenges assumptions, reduces scope, identifies risks, and helps prioritize the next practical step.

The agents are deliberately scoped. They are planning and drafting helpers, not autonomous operators.

## Safety and Permissions

The core safety principle is **human validation before sensitive action**.

Sensitive actions include sending real emails, contacting leads, using paid APIs, importing prospect data, storing personal data, modifying permanent records, publishing public content, changing pricing, updating client deliverables, committing project history, and pushing to a remote repository.

Internal drafting is acceptable when it stays clearly labeled as draft work. Anything external, financial, public, permanent, privacy-sensitive, or production-affecting requires explicit human approval.

## Evidence Policy

Evidence should prove what actually happened during future runs.

- `evidence/screenshots/` is for real screenshots from future reviews, workflows, UI checks, or external artifacts.
- `evidence/runs/` is for real run logs, execution notes, validation records, and structured summaries of completed workflows.

No fake evidence should be added. If an artifact was not produced by a real run or real review, it does not belong in `evidence/`.

## Current Status

- Day 1 blueprint complete.
- No production system yet.
- No live integrations yet.
- Next step: review the blueprint through a Pull Request.

## Future Work

- Validate the agent scopes against realistic Web Studio OS workflows.
- Test one manual workflow from prospect request to draft quote and product checklist.
- Define the first vault note format for decisions, client context, and reusable templates.
- Choose the first low-risk automation only after the manual workflow is understood.
- Collect real evidence from future runs without fabricating screenshots, logs, or claims.
