# Founder OS Blueprint

Founder OS Blueprint is a Day 1 planning repository for a future AI-assisted operating system for founders. It defines the initial business case, agent responsibilities, architecture, memory model, permissions policy, provider choice, and run journal before any system is built.

In this project, Founder OS means a lightweight coordination layer for repeatable founder work: planning offers, preparing client deliverables, organizing knowledge, drafting sales material, tracking evidence, and keeping sensitive actions under human control.

## Chosen Case

The selected project case is **Web Studio OS**, a small AI-assisted web development micro-agency operating system.

Web Studio OS is intended to help deliver landing pages, small websites, SEO basics, lead capture, maintenance, and AI-assisted client work for freelancers, artisans, local businesses, coaches, consultants, and small service businesses.

## Repository Structure

```text
founder-os-agent-builder/
  README.md
  docs/
    business-brief.md
    architecture.md
    agent-roles.md
    permissions-policy.md
    provider-choice.md
    run-journal.md
  evidence/
    screenshots/
    runs/
  exports/
  vault/
```

## How to Read This Repository

Start with `docs/business-brief.md` to understand the business case. Then read `docs/architecture.md` for the system shape, `docs/agent-roles.md` for responsibilities, and `docs/permissions-policy.md` for safety boundaries. `docs/provider-choice.md` explains the provisional local/cloud setup. `docs/run-journal.md` records the Day 1 reasoning and next questions.

## Current Status

This repository is a **Day 1 blueprint only**. It is not an implemented system. There is no backend, frontend, automation, real integration, or production workflow yet.

## Evidence Policy

Future screenshots, execution logs, manual test notes, and run artifacts should be stored under `evidence/`. Screenshots belong in `evidence/screenshots/`. Run logs and structured execution notes belong in `evidence/runs/`.

No fake evidence should be added. If an artifact was not produced by a real run or real review, it does not belong in `evidence/`.

## Safety Note

Sensitive actions require human validation. This includes sending real emails, contacting leads, storing personal data, publishing public content, modifying client deliverables, using paid APIs, pushing to remotes, and recording accounting data.
