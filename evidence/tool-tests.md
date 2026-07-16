# Tool Tests

All tests in this document are simulated manual tests. No real API, n8n workflow, Flowise flow, Langflow flow, Open WebUI action, database, email system, or no-code platform was used.

## Test 1: `qualify_lead`

Input:

```text
A craftsperson asks for a showcase website to sell renovation services. They want to know the price, timeline, and what they need to provide.
```

Expected output:
A lead qualification result that identifies the request as a good fit for Web Studio OS, flags pricing and timeline as requiring validation, lists missing inputs, and recommends drafting a human-reviewed reply.

Obtained output:

```json
{
  "request_summary": "A renovation craftsperson wants a showcase website and asks about price, timeline, and required materials.",
  "client_type": "craftsperson",
  "need": "Showcase website for renovation services with commercial framing and lead capture.",
  "agents_to_mobilize": ["Mail / Sales Agent", "Code / Product Agent", "Admin / Accounting Agent"],
  "main_risk": "The requested price and timeline cannot be reliable without scope, content readiness, and validation.",
  "human_validation_required": true,
  "next_action": "Prepare a draft email asking for service details, target location, photos, testimonials, deadline, and budget range before creating a fictional quote.",
  "fit_level": "high",
  "missing_information": ["target location", "number of services", "photos", "testimonials", "desired launch date", "budget range"]
}
```

Verdict:
Pass.

Correction to make if needed:
No correction needed. The result avoids inventing price or timeline and requires human validation.

## Test 2: `draft_email_reply`

Input:

```text
Recipient context: inbound renovation craftsperson lead.
Goal: answer their question about price, timeline, and what they need to provide without making a final quote.
Tone: professional, clear, and concise.
```

Expected output:
An email draft with a subject, useful answer, required information list, and explicit human approval requirement before sending.

Obtained output:

```json
{
  "recipient_context": "Inbound lead asking about a showcase website for renovation services.",
  "subject": "Showcase website for your renovation services",
  "body": "Hi, thanks for your message. A showcase website could be a good fit for presenting your renovation services and helping potential clients request a quote. To estimate price and timeline properly, I would first need your service list, target area, any photos or testimonials, examples of websites you like, and your preferred launch date. Once I have that, I can prepare a draft scope and fictional quote for review. As a rough process, the next step would be to clarify the pages, content, and lead capture needs before confirming anything commercially.",
  "tone": "professional and concise",
  "requires_human_approval": true,
  "approval_reason": "This message would be sent to a real prospect and discusses commercial expectations.",
  "open_questions": ["Which renovation services should be highlighted?", "Do they already have photos and testimonials?", "Is there a specific launch deadline?"]
}
```

Verdict:
Pass.

Correction to make if needed:
No correction needed. The output remains a draft and avoids final pricing.

## Test 3: `create_mock_quote`

Input:

```text
Create a fictional quote for a small renovation showcase website with one homepage, three service sections, a contact form, basic local SEO structure, and no booking or payment integration.
```

Expected output:
A fictional quote with line items, total, currency, assumptions, exclusions, and mandatory human approval before commercial use.

Obtained output:

```json
{
  "quote_type": "showcase website draft",
  "items": [
    {
      "label": "Website structure and homepage",
      "description": "One responsive homepage with hero section, service overview, trust section, and contact call to action.",
      "quantity": 1,
      "unit_price": 1200,
      "subtotal": 1200
    },
    {
      "label": "Service sections",
      "description": "Three renovation service sections based on client-provided details.",
      "quantity": 3,
      "unit_price": 150,
      "subtotal": 450
    },
    {
      "label": "Basic local SEO structure",
      "description": "Draft title, meta description, heading structure, and local keyword suggestions.",
      "quantity": 1,
      "unit_price": 300,
      "subtotal": 300
    }
  ],
  "estimated_total": 1950,
  "currency": "USD",
  "assumptions": ["Client provides service details, photos, logo if available, and testimonials.", "No booking system, payment integration, custom CRM, or advanced analytics are included."],
  "is_fictional": true,
  "requires_human_approval": true,
  "timeline_estimate": "2 to 4 weeks after content is validated",
  "excluded_items": ["Booking system", "Payment integration", "Paid advertising", "Advanced SEO campaign"],
  "approval_reason": "The quote is fictional and must be validated before being sent or used commercially."
}
```

Verdict:
Pass.

Correction to make if needed:
No correction needed. The output clearly marks the quote as fictional.

## Test 4: `search_knowledge_base`

Input:

```text
Query: What does Web Studio OS offer to small service businesses?
Allowed sources: docs/business-brief.md and docs/architecture.md.
```

Expected output:
A memory search result citing only checked local documents, summarizing the offer, and flagging missing validated pricing information.

Obtained output:

```json
{
  "query": "What does Web Studio OS offer to small service businesses?",
  "results": [
    {
      "source": "docs/business-brief.md",
      "summary": "Web Studio OS supports landing pages, small business websites, basic local SEO, lead capture, maintenance checklists, and AI-assisted research, copy drafting, implementation planning, and quality review.",
      "relevance": "high"
    },
    {
      "source": "docs/architecture.md",
      "summary": "The system should remain human-supervised with an orchestrator, specialized agents, local vault memory, Git documentation, evidence storage, and validation gates.",
      "relevance": "medium"
    }
  ],
  "confidence": "high",
  "missing_information": ["No validated final pricing model is documented; only fictional planning ranges exist."],
  "suggested_next_step": "Use the offer summary for internal drafting, but request human validation before quoting price, timeline, or scope.",
  "sources_checked": ["docs/business-brief.md", "docs/architecture.md"]
}
```

Verdict:
Pass.

Correction to make if needed:
No correction needed. The result is honest about local sources and missing validated pricing.

## Test 5: `extract_seo_keywords`

Input:

```text
Business: renovation craftsperson.
Services: bathroom renovation, kitchen renovation, interior remodeling.
Location: not provided.
Goal: generate draft keyword ideas for a showcase website.
```

Expected output:
Keyword ideas grouped by intent with a warning that local SEO terms need a validated location.

Obtained output:

```text
Commercial intent:
- bathroom renovation contractor
- kitchen renovation services
- interior remodeling contractor

Local intent requiring validation:
- bathroom renovation contractor in [validated city]
- kitchen remodeling services in [validated city]

Content support:
- how to prepare for a bathroom renovation
- renovation project timeline

Validation note:
Location is missing, so local keyword variants must not be finalized.
```

Verdict:
Pass.

Correction to make if needed:
No correction needed. The output avoids inventing a city.

## Bonus Status

Bonus not completed: no configured no-code or agent platform was available in this environment.

The actions remain simulated for now. No n8n, Flowise, Langflow, Open WebUI, database, or external automation evidence was produced.
