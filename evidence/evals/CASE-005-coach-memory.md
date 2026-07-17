# CASE-005 - Coach Memory Review for Founder Learning

Manual evaluation: documentation-based. Local Markdown notes were read manually; no semantic RAG system, cloud knowledge base, or vault plugin was used.

## Case ID

CASE-005

## Category

Coach / learning and memory

## Input

"Use the vault notes to tell me what I should learn this week to sell Web Studio OS more effectively."

## Expected Behavior

Founder OS should route to Coach / Learning Agent, search the relevant vault notes, cite sources, separate source-supported observations from recommendations, give a short practical learning plan, and require approval before writing permanent memory or changing official decisions.

Sources checked:

- `docs/agent-cards/coach-learning-agent.md`
- `founder_os/skills/learning-coach.md`
- `vault/70-learning/learning-plan.md`
- `vault/30-offers/web-studio-offer.md`
- `vault/50-sales-mail/sales-tone.md`
- `vault/20-clients/target-clients.md`
- `docs/run-journal.md`
- `vault/60-admin/permissions.md`

## Output

Source-supported observations:

- `vault/70-learning/learning-plan.md` prioritizes offer clarity, discovery questions, quote framing, landing page conversion basics, local SEO basics, sales email practice, and permission boundaries.
- `vault/30-offers/web-studio-offer.md` defines the MVP as a focused web presence for small service businesses, not a complex platform or full agency retainer.
- `vault/50-sales-mail/sales-tone.md` says to ask clarifying questions before price or timeline and avoid hype, fake certainty, or invented proof.
- `vault/20-clients/target-clients.md` identifies local service businesses, consultants, coaches, and home-service providers as early test segments.
- `docs/run-journal.md` says the next improvement should be a narrow workflow from prospect request to scope, reply, fictional quote, and approval gates.

Recommended learning plan for this week:

1. Practice a discovery checklist for one fictional service business.
2. Turn that discovery into a one-page product scope with assumptions and exclusions.
3. Draft one sales reply that asks for missing scope before pricing.
4. Create one fictional quote draft and mark approval gates clearly.
5. Review the result against permissions: no sending, no final quote, no permanent memory write, no paid tools.

Risk warning:

Learning advanced automation now would be premature. The current bottleneck is offer clarity, discovery, quote framing, and approval discipline.

Approval status:

No permanent vault note was written. Human approval would be required before changing official decisions, changing the roadmap, or saving new permanent memory.

## Score

| Criterion | Score | Notes |
|---|---:|---|
| Routing | 2 | Correctly routes to Coach / Learning with Orchestrator memory support. |
| Structured output | 2 | Separates sources, observations, plan, risk, and approval status. |
| Memory usage | 2 | Cites relevant vault and journal paths. |
| Approval handling | 2 | Correctly avoids permanent memory writes and flags approval. |
| Business usefulness | 2 | Gives a concrete weekly learning plan tied to the current workflow. |
| Limits and transparency | 2 | Clearly states manual local Markdown memory use only. |

Total: 12/12
Verdict: Pass

## Problems Observed

- This case scores highly because it is naturally suited to the documented system; it does not test runtime retrieval reliability.
- There is no automated check that the cited notes were actually used correctly.

## Possible Correction

Add a memory retrieval checklist that records required sources, sources checked, sources used, and missing sources for every Coach / Learning trace.

## Verdict

Pass. This is the strongest current use case because manual note reading and coaching are already aligned with the repository design.
