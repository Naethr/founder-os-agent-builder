# Tool Catalog

This catalog defines practical actions for Web Studio OS. Actions are documentation-first and human-supervised. Unless a real implementation is explicitly documented in evidence, the stack is simulated.

## `qualify_lead`

Mission:
Assess whether an inbound request fits the Web Studio OS offer and identify the next human-reviewed step.

Authorized agents:
Orchestrator, Prospecting Agent, Coach Agent.

Inputs:
Lead message, business type, requested service, location if provided, budget or timeline if provided, known constraints, and source context.

Expected output:
A `LeadQualificationResult` with fit assessment, client need, agents to mobilize, main risk, validation requirement, and next action.

Permissions:
Allowed for internal analysis. Importing or storing prospect data requires human validation. Personal data must be minimized.

Risks:
Misclassifying a lead, storing unnecessary personal data, overpromising scope, or treating assumptions as facts.

Approval required:
Required before contacting the lead, importing prospect data, storing personal data, or making a commercial commitment.

Stack used:
Simulated for the current exercise. Future implementation may use no-code or local tools after validation.

## `draft_email_reply`

Mission:
Prepare a clear email draft responding to a lead, prospect, or client without sending it automatically.

Authorized agents:
Orchestrator, Mail / Sales Agent, Coach Agent.

Inputs:
Recipient context, original message, desired objective, approved offer details, known constraints, tone guidance, and required disclaimers.

Expected output:
An `EmailDraftResult` with recipient context, subject, body, tone, approval requirement, and approval reason.

Permissions:
Drafting is allowed. Sending real emails is not automated. Human approval is required before any message is sent or scheduled.

Risks:
Creating false expectations, disclosing sensitive information, using an unsuitable tone, or making unapproved pricing or timeline promises.

Approval required:
Always required before sending, scheduling, or copying the draft into a real email thread.

Stack used:
Simulated. Future implementation may use no-code or cloud/API tools only for draft creation, not automatic sending.

## `create_mock_quote`

Mission:
Create a fictional quote draft for planning, discussion, or human review.

Authorized agents:
Orchestrator, Admin / Accounting Agent, Code / Product Agent.

Inputs:
Requested website type, scope assumptions, page count, content readiness, maintenance needs, optional add-ons, currency, and fictional pricing model.

Expected output:
A `MockQuoteResult` with quote type, line items, estimated total, currency, assumptions, fictional status, and approval requirement.

Permissions:
Allowed as an internal fictional draft. It must not be sent, used commercially, entered into accounting, or presented as final without human validation.

Risks:
Incorrect pricing, hidden scope, legal or commercial misunderstanding, and client expectation risk.

Approval required:
Always required before sending, using commercially, or converting into a real quote or invoice.

Stack used:
Simulated. Future implementation may use local documents or no-code tools. Paid accounting APIs require explicit approval.

## `extract_seo_keywords`

Mission:
Generate practical local SEO keyword ideas for a small service website or landing page.

Authorized agents:
SEO Agent, Orchestrator, Code / Product Agent.

Inputs:
Business type, services, target location, audience, known competitors if validated, target page, and current offer.

Expected output:
Keyword ideas grouped by intent, page usage suggestions, title/meta draft ideas, and uncertainty notes.

Permissions:
Allowed for drafting from provided context. Paid SEO APIs, scraping restricted sources, and storing competitor or personal data require human validation.

Risks:
Unverifiable ranking claims, weak search intent, stale keyword assumptions, or misuse of paid tools.

Approval required:
Required before publishing SEO content, editing a live site, using paid APIs, or storing external research data.

Stack used:
Simulated. Future implementation may use no-code, local research notes, or cloud/API tools. Paid APIs must be flagged before use.

## `search_knowledge_base`

Mission:
Search validated project documentation or vault memory for relevant context before an agent acts.

Authorized agents:
Orchestrator, all specialized agents.

Inputs:
Search query, allowed knowledge sources, requested result type, confidence threshold, and privacy constraints.

Expected output:
A `MemorySearchResult` with query, relevant results, confidence, missing information, and suggested next step.

Permissions:
Reading approved project documentation is allowed. Reading sensitive client memory depends on context. Permanent writes require human validation.

Risks:
Retrieving outdated notes, exposing sensitive context, confusing drafts with validated memory, or citing unsupported information.

Approval required:
Required before writing to permanent vault memory, storing personal data, or using sensitive client context externally.

Stack used:
Simulated with local Markdown context for this exercise. Future implementation may use local search, vault plugins, or approved cloud/API retrieval.

## `write_note_draft`

Mission:
Prepare a draft note for the vault without treating it as permanent memory.

Authorized agents:
Orchestrator, Coach Agent, all specialized agents when summarizing their own work.

Inputs:
Source material, note purpose, proposed title, relevant tags, evidence links if available, and validation status.

Expected output:
A draft note with source context, summary, decisions, unresolved questions, and explicit validation status.

Permissions:
Draft note creation is allowed. Writing into permanent Obsidian or vault memory requires human validation.

Risks:
Persisting wrong assumptions, storing sensitive data, duplicating noisy notes, or making temporary drafts look authoritative.

Approval required:
Required before moving a draft into permanent memory, storing personal data, or using the note as validated client context.

Stack used:
Simulated. Future implementation may use local vault files or no-code tools after validation.
