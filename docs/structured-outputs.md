# Structured Outputs

These schemas define the expected shape of agent outputs for Web Studio OS actions. They are documentation contracts, not code implementations.

## `LeadQualificationResult`

Purpose:
Summarize whether a lead fits the Web Studio OS offer and what should happen next.

Used by action(s):
`qualify_lead`

Required fields:

| Field | Type | Description |
|---|---|---|
| `request_summary` | string | Short neutral summary of the lead request. |
| `client_type` | string | Business category, such as craftsperson, consultant, local service, or unknown. |
| `need` | string | Primary need expressed by the lead. |
| `agents_to_mobilize` | array of strings | Agents that should help with the next step. |
| `main_risk` | string | Most important risk or missing information. |
| `human_validation_required` | boolean | Whether a human must validate before action. |
| `next_action` | string | Recommended next step. |

Optional fields:
`budget_signal`, `timeline_signal`, `missing_information`, `fit_level`, `source_context`.

Example output:

```json
{
  "request_summary": "A renovation craftsperson wants a showcase website to present services and generate inquiries.",
  "client_type": "craftsperson",
  "need": "Showcase website with service positioning, lead capture, pricing guidance, and timeline explanation.",
  "agents_to_mobilize": ["Mail / Sales Agent", "Code / Product Agent", "Admin / Accounting Agent"],
  "main_risk": "Price and timeline expectations may be inaccurate without validated scope and content readiness.",
  "human_validation_required": true,
  "next_action": "Draft a reply asking for service list, target location, examples, content assets, desired launch date, and budget range.",
  "fit_level": "high",
  "missing_information": ["page count", "existing brand assets", "photos", "target location", "deadline"]
}
```

Validation notes:
Do not invent budget, location, contact details, or external IDs. Mark validation required before outreach, prospect data import, or commercial promises.

## `EmailDraftResult`

Purpose:
Provide a human-reviewable email draft without sending it.

Used by action(s):
`draft_email_reply`

Required fields:

| Field | Type | Description |
|---|---|---|
| `recipient_context` | string | Who the email is for and why they are being contacted. |
| `subject` | string | Proposed email subject line. |
| `body` | string | Full draft body. |
| `tone` | string | Tone used in the draft. |
| `requires_human_approval` | boolean | Always true for real outbound email. |
| `approval_reason` | string | Why approval is needed. |

Optional fields:
`open_questions`, `claims_to_verify`, `suggested_attachments`, `follow_up_timing`.

Example output:

```json
{
  "recipient_context": "Inbound lead asking about a showcase website for renovation services.",
  "subject": "Showcase website for your renovation services",
  "body": "Hi, thanks for your message. A showcase website could be a good fit if the goal is to present your services clearly and help potential clients request a quote. To estimate price and timeline properly, I would need your service list, target area, any photos or testimonials, examples of websites you like, and your preferred launch date. After that, I can prepare a draft scope and fictional quote for review.",
  "tone": "professional and direct",
  "requires_human_approval": true,
  "approval_reason": "The draft would be sent to a real prospect and may influence commercial expectations.",
  "open_questions": ["What services should be prioritized?", "Are photos and testimonials available?", "Is there a launch deadline?"]
}
```

Validation notes:
Email actions produce drafts only. Do not include unapproved guarantees, final prices, fake case studies, or unsupported delivery timelines.

## `MockQuoteResult`

Purpose:
Represent a fictional quote draft for planning and human review.

Used by action(s):
`create_mock_quote`

Required fields:

| Field | Type | Description |
|---|---|---|
| `quote_type` | string | Type of quote, such as showcase website draft. |
| `items` | array of objects | Draft line items with label, description, quantity, unit price, and subtotal. |
| `estimated_total` | number | Sum of draft line items. |
| `currency` | string | Currency code, such as USD or EUR. |
| `assumptions` | array of strings | Assumptions behind the estimate. |
| `is_fictional` | boolean | Must be true until validated by a human. |
| `requires_human_approval` | boolean | Must be true before external or commercial use. |

Optional fields:
`timeline_estimate`, `excluded_items`, `payment_terms_draft`, `approval_reason`.

Example output:

```json
{
  "quote_type": "showcase website draft",
  "items": [
    {
      "label": "Website setup",
      "description": "One homepage, two service sections, contact form structure, and basic responsive layout planning.",
      "quantity": 1,
      "unit_price": 1500,
      "subtotal": 1500
    },
    {
      "label": "Basic local SEO structure",
      "description": "Draft page title, meta description, heading structure, and local service keyword suggestions.",
      "quantity": 1,
      "unit_price": 300,
      "subtotal": 300
    }
  ],
  "estimated_total": 1800,
  "currency": "USD",
  "assumptions": ["Client provides photos and service details.", "No booking system or payment integration is included."],
  "is_fictional": true,
  "requires_human_approval": true,
  "timeline_estimate": "2 to 4 weeks after content is validated",
  "approval_reason": "Pricing and scope must be reviewed before commercial use."
}
```

Validation notes:
Do not present fictional quotes as final. Do not create fake invoice IDs, tax IDs, client IDs, or accounting records.

## `MemorySearchResult`

Purpose:
Return relevant knowledge base context while making uncertainty visible.

Used by action(s):
`search_knowledge_base`

Required fields:

| Field | Type | Description |
|---|---|---|
| `query` | string | Search query or question. |
| `results` | array of objects | Matching notes or documents with source, summary, and relevance. |
| `confidence` | string | Low, medium, or high confidence in the result set. |
| `missing_information` | array of strings | Information not found or not validated. |
| `suggested_next_step` | string | Recommended action after the search. |

Optional fields:
`sources_checked`, `privacy_flags`, `requires_human_validation`.

Example output:

```json
{
  "query": "What is the approved Web Studio OS offer for small service businesses?",
  "results": [
    {
      "source": "docs/business-brief.md",
      "summary": "The offer focuses on landing pages, small business websites, basic local SEO, lead capture, maintenance checklists, and AI-assisted drafting.",
      "relevance": "high"
    },
    {
      "source": "docs/architecture.md",
      "summary": "The MVP should remain human-supervised with local vault memory, Git documentation, evidence storage, and validation gates.",
      "relevance": "medium"
    }
  ],
  "confidence": "high",
  "missing_information": ["No validated niche-specific pricing beyond fictional planning ranges."],
  "suggested_next_step": "Use the approved offer as context, but ask for human validation before quoting price or timeline.",
  "sources_checked": ["docs/business-brief.md", "docs/architecture.md"]
}
```

Validation notes:
Results must cite real local sources that were checked. Do not claim access to a database, API, or vault plugin unless it was actually used.
