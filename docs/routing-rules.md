# Routing Rules

These routing rules define how the Founder OS v1 Orchestrator selects agents for Web Studio OS requests. The rules are practical for a documentation-first MVP and assume local Markdown orchestration only.

| Request Type | Trigger Examples | Agents to Call | Skills Used | Tools / Actions | Approval Notes |
|---|---|---|---|---|---|
| New lead / incoming prospect request | "I need a website", "Can you help me get more quote requests?", "How much for a service page?" | Prospecting Agent, Code / Product Agent, Mail / Sales Agent, Admin / Accounting Agent when price is requested | Prospecting, Product Brief, Sales Copy, Admin Sandbox | `qualify_lead`, `search_knowledge_base`, `draft_email_reply`, `create_mock_quote` if needed | Approval required before replying, contacting the lead, storing personal data, or sending a quote. |
| Website or product scope request | "I want a showcase website", "Define the pages", "What should be included in the first version?" | Code / Product Agent, SEO / Market Agent when page structure affects visibility, Admin / Accounting Agent if scope affects quote | Product Brief, SEO Research, Admin Sandbox | `search_knowledge_base`, `extract_seo_keywords`, `create_mock_quote` | Approval required before committing to price, timeline, deliverables, or changing a real client project. |
| SEO or visibility request | "I want more local traffic", "What keywords should I target?", "Improve my search visibility" | SEO / Market Agent, Code / Product Agent, Mail / Sales Agent if client explanation is needed | SEO Research, Product Brief, Sales Copy | `extract_seo_keywords`, `search_knowledge_base`, `draft_email_reply` | Approval required before publishing SEO content, editing a live site, using paid SEO tools, or making performance claims. |
| Email reply or sales copy request | "Reply to this prospect", "Draft a follow-up", "Explain the offer" | Mail / Sales Agent, Code / Product Agent when scope is unclear, Admin / Accounting Agent when pricing is mentioned | Sales Copy, Product Brief, Admin Sandbox | `draft_email_reply`, `qualify_lead`, `search_knowledge_base` | Approval always required before sending or copying the draft into a real thread. No unapproved price or deadline. |
| Quote / pricing request | "How much would this cost?", "Prepare a quote", "Add maintenance pricing" | Admin / Accounting Agent, Code / Product Agent, Mail / Sales Agent for reply draft | Admin Sandbox, Product Brief, Sales Copy | `create_mock_quote`, `search_knowledge_base`, `draft_email_reply` | Quote must be marked fictional until human validation. Approval required before client use, accounting use, or any commercial commitment. |
| Prospecting request | "Find prospects", "Who should I target?", "Prepare outreach angles" | Prospecting Agent, SEO / Market Agent if segment visibility matters, Mail / Sales Agent for draft outreach | Prospecting, SEO Research, Sales Copy | `qualify_lead`, `search_knowledge_base`, `write_note_draft`, `draft_email_reply` | Approval required before importing data, storing personal data, contacting anyone, enriching leads, or running outreach. Automated outreach is forbidden. |
| Admin or accounting request | "Prepare an invoice", "Draft payment terms", "Summarize admin steps", "Create a quote draft" | Admin / Accounting Agent, Code / Product Agent if scope is unclear | Admin Sandbox, Product Brief | `create_mock_quote`, `search_knowledge_base`, `write_note_draft` | No real invoices, tax claims, accounting records, or final quotes. Human validation required for financial use. |
| Learning or coaching request | "What should I learn next?", "Evaluate this workflow", "What is the bottleneck?" | Coach / Learning Agent, Orchestrator, relevant specialist agent if the question is domain-specific | Learning Coach, Product Brief when tied to scoping | `search_knowledge_base`, `write_note_draft` | Approval required before changing official decisions, writing permanent vault notes, or changing the roadmap. |
| Memory search request | "Check the vault", "Use previous notes", "What did we decide?" | Orchestrator, then any relevant agent | Learning Coach, Product Brief, Prospecting, Sales Copy, SEO Research as needed | `search_knowledge_base` | Reading local docs is allowed. Permanent writes or use of sensitive client data externally require approval. |
| Sensitive action request | "Send the email", "Publish the page", "Use a paid API", "Push this", "Store this client data" | Orchestrator first, then specialist only after approval rules are clear | Relevant skill depends on action | Relevant action only after approval; otherwise draft or stop | Human approval required. Some actions are forbidden at this stage, including automated outreach, fake evidence, production deployment, and credential access. |

## Example Routing

A prospect asking for a showcase website should route to:

- Code / Product Agent to create the product brief and smallest useful scope.
- SEO / Market Agent to produce keyword hypotheses and page visibility direction.
- Admin / Accounting Agent to create a fictional internal quote draft if pricing is requested.
- Mail / Sales Agent to draft a reply asking for missing information and proposing the next step.

Human approval is required before sending any reply or quote.

## Routing Principles

- Start with the business problem, not the requested artifact.
- Use the smallest set of agents needed to make a safe decision.
- Add Admin / Accounting Agent whenever price, billing, quote, or payment is involved.
- Add Mail / Sales Agent whenever a client-facing message is needed.
- Add Coach / Learning Agent when the workflow needs evaluation or learning improvement.
- Mark all assumptions and missing facts before final synthesis.
