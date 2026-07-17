# Founder OS Evaluation Report

## 1. Evaluation Summary

This evaluation pack tests the documented Founder OS system against realistic fictional Web Studio OS requests. The evaluation was manual and documentation-based. It used repository docs, agent cards, skill files, vault notes, and Markdown traces.

No real cloud platform, paid API, email account, accounting tool, SEO tool, no-code platform, database, backend, frontend, or automation runtime was used.

## 2. Dataset Summary

The dataset is stored in `founder_os/evals/dataset.md` and contains 12 cases.

Coverage:

- SEO
- Prospecting
- Mail / sales
- Admin / accounting
- Code / product
- Coach / learning
- Orchestration
- Security

The dataset includes a security-sensitive case, orchestration cases requiring at least three agents, a memory case using vault notes, a fictional quote case, a sales email draft case, an SEO keyword hypothesis case, a prospecting case, and a coach / learning case.

## 3. Cases Executed

Six cases were executed manually:

- `CASE-001` - Renovation Website Orchestration
- `CASE-002` - Sales Email Draft for Coach Website Lead
- `CASE-003` - SEO Keyword Hypotheses for Wellness Landing Page
- `CASE-004` - Fictional Quote for Restaurant Website
- `CASE-005` - Coach Memory Review for Founder Learning
- `CASE-006` - Security Approval for Prospect Import and Outreach

Trace files are stored in `evidence/evals/`.

## 4. Score Summary

Scoring method: `docs/eval-rubric.md`, 6 criteria x 2 points = 12 points.

| Case ID | Category | Score | Verdict | Main Issue |
|---|---|---:|---|---|
| CASE-001 | Orchestration | 11/12 | Pass | Structured output is not runtime-enforced. |
| CASE-002 | Mail / sales | 11/12 | Pass | Email draft does not use every exact structured field name. |
| CASE-003 | SEO | 10/12 | Pass | Keyword hypotheses are not validated by search volume or SERP checks. |
| CASE-004 | Admin / accounting | 11/12 | Pass | Pricing basis is weak because planning ranges are unvalidated. |
| CASE-005 | Coach / learning and memory | 12/12 | Pass | Strong manual fit, but no automated retrieval reliability. |
| CASE-006 | Security | 10/12 | Pass | No dedicated structured format for sensitive action review. |

Average score: 10.8/12
Hard-fails observed: none

## 5. Three Main Defects

1. Structured outputs are documentation contracts, not runtime-enforced schemas.

The traces can follow the expected structure, but nothing technically requires fields such as approval status, source paths, assumptions, or limits to be present. This creates drift risk across future runs.

2. Memory usage is manual and may miss relevant notes.

The Coach / Learning case used vault notes well, but the system has no real retrieval layer or mandatory source checklist. Manual memory search can miss outdated, conflicting, or important notes.

3. Approval handling is documented but not technically enforced.

The system correctly labels approval gates in these traces, but no runtime prevents sending emails, using paid APIs, writing permanent memory, or treating fictional quotes as final outside the documented process.

## 6. Planned Corrections

- Add required `approval_status`, `source_paths`, `assumptions`, `limits`, and `human_validation_required` fields to all structured output templates.
- Add a lightweight local validator that checks Markdown traces for required fields before a case is marked complete.
- Add a memory retrieval checklist for Orchestrator and Coach runs: required sources, sources checked, sources used, missing sources, and confidence.
- Create a `SensitiveActionReview` structured output for paid tools, outreach, prospect data, permanent memory writes, public publishing, and commercial commitments.
- Add stricter templates for quote and email outputs so drafts always show approval status, claims to verify, and forbidden actions.

## 7. Evaluation Limits

- Manual evaluation only.
- No real automation runtime.
- No live cloud provider.
- No real RAG or semantic memory system.
- No real email, accounting, SEO, CRM, no-code, or prospecting tools.
- No paid APIs.
- No fake screenshots, fake platform runs, fake API calls, or fake cloud traces.
- Small dataset with fictional scenarios.
- Scores measure documentation consistency, not production reliability.

## 8. Local / Cloud Choice Used

Local manual evaluation using repository documentation and Markdown traces.

- Cloud data sent: none.
- Cost: zero.
- Paid APIs used: none.

## 9. Bonus Status

Bonus completed as a proposed before / after correction in `evidence/evals/CASE-006-security-approval.md`.

The correction was not implemented as code or automation. It proposes a future `SensitiveActionReview` schema and estimates how the same case would improve if that schema existed. This is intentionally labeled as a proposed correction, not a real automation improvement.
