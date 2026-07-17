# Day 3 Orchestration Run

## Stack Used

Simulated manual orchestration using local Markdown files.

No real runtime engine, no no-code platform, no backend, no frontend, no database, no cloud workflow, no paid API, no fake export, and no fake screenshot were used.

Sources used:

- `docs/agent-cards/`
- `founder_os/skills/`
- `docs/tool-catalog.md`
- `docs/permissions-policy.md`
- `vault/30-offers/web-studio-offer.md`
- `vault/20-clients/target-clients.md`
- `vault/40-seo-market/seo-ideas.md`
- `vault/50-sales-mail/sales-tone.md`
- `vault/60-admin/admin-rules.md`
- `vault/60-admin/permissions.md`

## Initial Request

A craftsperson wants a showcase website to sell their services and receive more quote requests.

## Routing Decision

Request type:

- New lead / incoming prospect request.
- Website or product scope request.
- SEO or visibility request.
- Quote / pricing request may become relevant, but no final quote can be produced without human validation.
- Email reply request may become relevant, but no email can be sent without human validation.

Selected agents:

- Code / Product Agent.
- SEO / Market Agent.
- Admin / Accounting Agent.
- Mail / Sales Agent.
- Coach / Learning Agent for the bonus evaluator / optimizer loop.

Reasoning:

- The Code / Product Agent is needed to convert the vague request into a scoped website brief.
- The SEO / Market Agent is needed because the prospect wants more quote requests and visibility may affect page structure.
- The Admin / Accounting Agent is needed to create only a fictional internal quote draft based on explicit assumptions.
- The Mail / Sales Agent is needed to draft a reply asking for missing scope before price or timeline.
- The Coach / Learning Agent can evaluate whether the sales draft stays honest, clear, and approval-safe.

## Agents Called

| Agent | Purpose | Status |
|---|---|---|
| Code / Product Agent | Create a practical product brief for the showcase website. | Simulated manual call. |
| SEO / Market Agent | Produce keyword hypotheses and SEO direction. | Simulated manual call. |
| Admin / Accounting Agent | Produce a fictional internal quote draft. | Simulated manual call. |
| Mail / Sales Agent | Produce a draft email response. | Simulated manual call. |
| Coach / Learning Agent | Evaluate and optimize the sales draft. | Simulated manual call. |

## Handoff 1 - Orchestrator to Code / Product Agent

Context sent:

- Confirmed information: the prospect is a craftsperson.
- Confirmed information: the prospect wants a showcase website.
- Confirmed information: the prospect wants to sell services and receive more quote requests.
- Assumption: the business is a local service business.
- Assumption: the first version should remain a small Web Studio OS MVP.
- Constraint: do not write production code.
- Constraint: do not promise price, timeline, traffic, or leads.
- Requested output: product brief, page scope, assumptions, open questions, risks, and next action.

## Code / Product Agent Output

Product brief:

- Client context: craftsperson offering services, likely needing trust, proof, clear service explanation, and a lead capture path.
- Problem: the current request is too broad to price or schedule safely because service type, location, proof assets, page count, content readiness, and contact flow are unknown.
- Goal: create a focused showcase website that explains the service, builds trust, and guides visitors toward quote requests.
- Suggested MVP scope:
  - Home / main service page.
  - Services section or page.
  - Proof section with photos, reviews, credentials, or project examples if available.
  - About section focused on trust and working method.
  - Quote request form or contact section.
  - Basic SEO title, meta description, headings, and local intent structure.
- Assumptions:
  - The craftsperson serves a specific local area.
  - The prospect can provide service details and proof assets.
  - A simple site is more appropriate than a complex platform.
- Open questions:
  - Which exact service should the site sell first?
  - Which city or service area should be targeted?
  - What proof assets are available: photos, reviews, credentials, project examples?
  - Should quote requests arrive by form, phone, email, or booking link?
  - Is copy already written, or should Web Studio OS draft it?
  - Are there existing brand assets, domain, hosting, or analytics?
- Risks:
  - Pricing and timeline are unsafe without content readiness and scope details.
  - Too many service pages could exceed MVP scope.
  - Lead generation expectations must not be guaranteed.
- Recommended next action: send a discovery reply asking for service, location, proof, contact flow, content readiness, and priority for the first version.

## Handoff 2 - Product Context to SEO / Market Agent

Context sent:

- Product output from Code / Product Agent.
- Confirmed information: craftsperson, showcase website, wants more quote requests.
- Assumption: local service business.
- Missing information: exact trade, services, city, service area, competitors, existing site.
- Constraint: produce keyword hypotheses only because no real SEO tool was used.
- Requested output: keyword hypotheses, page ideas, local SEO notes, metadata ideas, validation reminders.

## SEO / Market Agent Output

Keyword hypotheses:

- Service intent:
  - `[craft service] services`
  - `[craft service] contractor`
  - `[craft service] quote`
  - `[craft service] estimate`
- Local intent:
  - `[craft service] [city]`
  - `[craft service] near me`
  - `[craft service] quote [city]`
  - `[craft service] specialist [service area]`
- Problem intent:
  - `repair [problem]`
  - `custom [craft service]`
  - `renovate [service object]`
  - `replace [service object]`
- Trust intent:
  - `licensed [craft service] [city]`
  - `experienced [craft service] [city]`
  - `[craft service] reviews [city]`

Page ideas:

- Main service landing page for the priority service.
- Service detail sections for the most profitable or most requested services.
- Proof area with project photos and testimonials if validated.
- Quote request page or section with simple qualification fields.

Draft metadata direction:

- Title idea: `[Priority Service] in [City] | Quote Request for [Craft Service]`
- Meta description idea: `Clear information about [priority service], proof of past work, and a simple way to request a quote in [service area].`

Local SEO notes:

- Location modifiers should be used only after the service area is confirmed.
- Google Business Profile and reviews may matter for local trust, but managing them is not automatically in scope.
- No ranking, traffic, or lead guarantee should be made.

Validation reminders:

- No search volume was checked.
- No competitor research was performed.
- Keywords are hypotheses, not validated market data.

## Handoff 3 - Product and SEO Context to Admin / Accounting Agent

Context sent:

- Product brief and SEO hypotheses.
- Confirmed information: showcase website request for a craftsperson.
- Assumptions: small MVP website, local service, quote request form, basic SEO structure.
- Reference pricing note: `vault/30-offers/web-studio-offer.md` mentions planning examples of USD 900 to USD 2,500 setup and USD 99 to USD 299 monthly maintenance, not validated prices.
- Constraint: create only a fictional internal quote draft.
- Constraint: do not create invoice numbers, tax claims, legal claims, or final pricing.

## Admin / Accounting Agent Output

Fictional internal quote draft:

- Status: fictional planning draft only.
- Currency: USD for planning example only.
- Setup assumption: small showcase website with a main service page, services section, proof section, about section, quote request form, and basic SEO structure.
- Setup planning range: USD 900 to USD 2,500.
- Optional maintenance planning range: USD 99 to USD 299 per month.

Possible line items:

- Discovery and scope clarification.
- Website structure and product brief.
- Copy structure for core sections.
- Basic SEO title, meta description, headings, and local keyword direction.
- Simple quote request form or contact section.
- Review and launch checklist.
- Optional maintenance checklist.

Missing information before a real quote:

- Exact service and service area.
- Number of pages or sections.
- Content readiness.
- Photo, review, and proof asset availability.
- Contact form fields and destination.
- Domain, hosting, and technical ownership.
- Review cycles.
- Timeline expectations.
- Legal, tax, and billing details.

Approval requirement:

- Human approval is required before sending, using commercially, converting into a real quote, or recording any accounting data.

## Handoff 4 - Product, SEO, and Admin Context to Mail / Sales Agent

Context sent:

- Product brief.
- SEO hypotheses and validation reminders.
- Fictional quote planning range and approval status.
- Sales tone rules: direct, specific, practical, no hype, ask clarifying questions before giving final price or timeline.
- Constraint: draft only, do not send.
- Constraint: do not present the planning range as a final quote.

## Mail / Sales Agent Output

Draft subject:

Showcase website for your services

Draft email:

Hi,

Thanks for the request. A focused showcase website can make sense if the first goal is to explain your services clearly and make it easy for people to request a quote.

Before I can give a reliable price or timeline, I need to clarify the scope:

- Which service should the website sell first?
- Which city or service area do you want to target?
- Do you already have photos, reviews, credentials, or examples of past work?
- Should quote requests come through a form, phone call, email, or booking link?
- Do you already have a domain, hosting, logo, or written content?
- What should stay out of the first version so the launch stays simple?

For a small first version, I would usually look at a simple structure: a main service page, service details, proof, a short about section, and a quote request form. I can prepare a more precise scope and quote after reviewing the answers above.

Best,

Approval status:

- Draft only.
- Human approval required before sending.
- No final price, deadline, or lead generation promise included.

## Approvals Required

Human approval is required before:

- Sending the draft email.
- Presenting any price range to the prospect.
- Sending a final quote.
- Writing permanent vault notes from this run.
- Storing prospect personal data.
- Publishing any website content.
- Using paid SEO, email, CRM, accounting, or automation tools.

## Final Synthesis

Reformulated need:

The prospect wants a focused showcase website that explains their craft services, builds trust, and increases quote requests.

Confirmed information:

- The prospect is a craftsperson.
- The prospect wants a showcase website.
- The prospect wants to sell services and receive more quote requests.

Assumptions:

- The business is local or service-area based.
- A small Web Studio OS MVP is the right first version.
- A quote request form or contact section is needed.
- Basic SEO structure is useful, but search demand is unvalidated.

Suggested scope:

- Main service page or home page.
- Services section.
- Proof section using validated assets.
- About / trust section.
- Quote request form or contact section.
- Basic SEO title, meta description, headings, and local keyword direction.

Agents mobilized:

- Code / Product Agent.
- SEO / Market Agent.
- Admin / Accounting Agent.
- Mail / Sales Agent.
- Coach / Learning Agent for evaluation.

SEO direction:

- Start with service-plus-location keyword hypotheses once the exact service and service area are known.
- Keep keyword claims clearly marked as hypotheses.
- Do not promise rankings, traffic, or quote volume.

Fictional quote assumptions:

- Internal planning only.
- Small showcase website.
- Setup planning range may reference USD 900 to USD 2,500 from existing offer notes, but this is not validated pricing.
- Optional maintenance may reference USD 99 to USD 299 per month from existing offer notes, but this is not validated pricing.
- Human validation is required before any commercial use.

Draft response direction:

- Thank the prospect.
- Confirm that the requested website can fit a focused first version.
- Ask practical discovery questions before price or timeline.
- Offer to prepare a precise scope after answers are reviewed.

Questions for the prospect:

- Which exact service should the website sell first?
- Which city or service area should be targeted?
- What proof assets are available?
- What quote request method should be used?
- Are domain, hosting, logo, photos, and copy already available?
- What must be excluded from the first version?

Main risks:

- The request is too vague for reliable pricing.
- SEO expectations could become unrealistic.
- Missing proof assets may weaken trust.
- The project could expand beyond the MVP if pages and services are not constrained.
- A fictional quote could be misunderstood if not clearly labeled.

Recommended next action:

- Human reviews the draft email, then sends a discovery reply if approved.

Human approvals required:

- Approve the email before sending.
- Approve any quote before client use.
- Approve any permanent memory write.
- Approve any paid API or external platform use.

## Limits

- This was a simulated manual orchestration.
- No real agent runtime executed.
- No email was sent.
- No quote was sent.
- No SEO tool was used.
- No prospect data was stored.
- No permanent vault note was written.
- No cloud or paid service was used.

## Bonus Evaluator / Optimizer Loop

Evaluator:

- Coach / Learning Agent.

Original Sales draft summary:

- The draft thanks the prospect, frames a focused showcase website, asks discovery questions, and avoids final price or timeline.

Evaluation criteria:

- Clarity.
- Honesty.
- No fake promises.
- No final price without validation.
- Asks useful discovery questions.
- Professional but simple tone.
- Clear next step.

Issues found:

- The draft is safe, but it can make the next step more explicit.
- The draft should state that the founder can prepare a scope after the prospect answers, not imply that the project is already accepted.
- It should avoid mentioning any planning range in the email until the founder approves commercial framing.

Optimized version summary:

- Keep the original structure.
- Add one clearer next step: "Send me those answers and I will prepare a short scope for review."
- Keep price and timeline out of the email until scope is validated.
- Keep the draft labeled as draft only.

Human approval still required:

- Yes. The optimized email remains a draft and must be reviewed before sending.
