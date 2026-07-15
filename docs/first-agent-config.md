# First Agent Configuration

## Agent Name

Founder OS Qualifier

## Platform Used

Local rule-based CLI prototype.

## Why This Platform Was Chosen

This platform was chosen because the Day 1 goal is to validate agent understanding and qualification logic, not to build infrastructure.

- It is free.
- It runs locally.
- It does not send data to external providers.
- It requires no paid API, cloud account, database, backend, frontend, Docker setup, or automation platform.
- It is simple enough to inspect and extend.

This is limited compared with a real LLM-powered agent. It does not deeply understand language, reason over long context, use tools, access memory, or adapt dynamically beyond the rules implemented in the script. For this MVP, that tradeoff is acceptable because the exercise is about proving the first qualification workflow.

## Agent Mission

The Founder OS Qualifier receives an incoming Web Studio OS request and turns it into a structured qualification summary.

It must identify:

- the reformulated need;
- the Founder OS agents to mobilize;
- the main risk;
- whether human validation is required;
- the next action.

The default case is Web Studio OS, an AI-assisted web development micro-agency operating system.

## Full Agent Instructions

1. Read the incoming request.
2. Reformulate the prospect or founder need in clear business terms.
3. Detect whether the request concerns a website, sales reply, SEO, pricing, timeline, quote, lead qualification, or administrative scope.
4. Select the relevant Web Studio OS agents:
   - Orchestrator;
   - Code / Product Agent;
   - SEO Agent;
   - Prospecting Agent;
   - Mail / Sales Agent;
   - Admin / Accounting Agent;
   - Coach Agent.
5. Always include the Orchestrator for routing and the Coach Agent for scope control.
6. Add the Code / Product Agent for website, landing page, product scope, or implementation requests.
7. Add the SEO Agent for service business, local business, SEO, selling services, or showcase website needs.
8. Add the Mail / Sales Agent when a prospect or client expects a reply, proposal, or commercial answer.
9. Add the Admin / Accounting Agent when pricing, quote, payment, invoice, budget, or timeline commitments are involved.
10. Add the Prospecting Agent only when the request concerns leads, outreach, prospect research, or lead qualification.
11. Identify the main risk, especially missing scope before price or timeline commitments.
12. Require human validation before any external, financial, public, permanent, privacy-sensitive, or client-facing action.
13. Propose a practical next action that keeps the workflow in MVP scope.

## Expected Input Format

The CLI accepts a plain English request as a single argument:

```bash
python3 scripts/run_founder_os_qualifier.py "A prospect asks for a showcase website and wants a price."
```

If no argument is provided, the script runs the mandatory Day 1 test request:

```bash
python3 scripts/run_founder_os_qualifier.py
```

## Expected Output Format

The agent outputs Markdown with these sections:

- Input Request
- Reformulated Need
- Agents to Mobilize
- Main Risk
- Human Validation Required
- Next Action

## Agent Limits

- It is rule-based, not LLM-powered.
- It uses keyword detection, so it can miss intent when wording changes.
- It cannot ask dynamic follow-up questions.
- It cannot inspect documents, websites, emails, calendars, CRMs, or external tools.
- It has no external memory.
- It does not produce final prices, timelines, quotes, or client-ready commitments.
- It cannot validate market, SEO, legal, accounting, or technical facts.

## When Human Validation Is Required

Human validation is required before:

- sending any email, proposal, quote, or client-facing message;
- giving a price, delivery timeline, or commercial commitment;
- publishing public content;
- storing personal, client, billing, or prospect data;
- using paid tools or APIs;
- changing official pricing, scope, project files, or production systems;
- making a decision that affects a real client or prospect.

## Evidence Required After a Run

After a real run, evidence should be stored in `evidence/runs/` and include:

- the tested request;
- the exact output obtained;
- a quality analysis;
- a cost analysis;
- an exposed data analysis;
- the next improvement.

Evidence must describe what actually happened. It must not claim screenshots, cloud model usage, API calls, or external tool runs unless they really occurred.
