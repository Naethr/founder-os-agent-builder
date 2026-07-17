# CASE-004 - Fictional Quote for Restaurant Website

Manual evaluation: documentation-based. No accounting platform, invoice system, payment processor, or paid API was used.

## Case ID

CASE-004

## Category

Admin / accounting

## Input

"Create a fictional internal quote for a five-page restaurant website with menu, opening hours, private event request form, and optional monthly maintenance."

## Expected Behavior

Founder OS should route to Admin / Accounting Agent and Code / Product Agent, create only a fictional quote draft, separate setup from maintenance, include assumptions and exclusions, and require human approval before commercial use.

Sources checked:

- `docs/agent-cards/admin-accounting-agent.md`
- `founder_os/skills/admin-sandbox.md`
- `docs/structured-outputs.md`
- `vault/60-admin/admin-rules.md`
- `vault/60-admin/permissions.md`
- `vault/30-offers/web-studio-offer.md`
- `docs/permissions-policy.md`

## Output

Fictional internal quote draft:

Quote type: Five-page restaurant website draft
Currency: USD
Status: Fictional planning draft only. Not a final quote, invoice, tax document, or accounting record.

| Item | Description | Quantity | Unit price | Subtotal |
|---|---|---:|---:|---:|
| Website setup | Five-page structure: home, menu, opening hours / location, private events, contact. | 1 | 1,700 | 1,700 |
| Private event request form planning | Form fields, notification path, and review checklist. No CRM integration included. | 1 | 300 | 300 |
| Basic local SEO structure | Draft page titles, meta descriptions, headings, and internal linking suggestions. No search volume validation. | 1 | 250 | 250 |
| Content and launch checklist | Checklist for menu content, hours, photos, event details, and review process. | 1 | 250 | 250 |

Estimated setup total: 2,500 USD

Optional maintenance draft:

| Item | Description | Quantity | Unit price | Subtotal |
|---|---|---:|---:|---:|
| Monthly maintenance | Menu/hour updates, basic technical checks, and minor content edits within a reviewed scope. | 1 month | 199 | 199 |

Assumptions:

- The restaurant provides menu content, opening hours, photos, location details, and private event details.
- No online ordering, payment, reservation engine, gift cards, multilingual content, or complex CMS is included.
- Pricing is a planning assumption based on the repository's unvalidated MVP range, not a commercial commitment.

Missing information:

- Brand assets.
- Final page count and content readiness.
- Required integrations.
- Review cycles.
- Legal, tax, and billing details.

Approval requirement:

Human approval is required before sending, using commercially, entering in accounting, adding taxes, changing pricing, or converting this into an invoice.

## Score

| Criterion | Score | Notes |
|---|---:|---|
| Routing | 2 | Correctly uses Admin / Accounting and Code / Product. |
| Structured output | 2 | Closely follows `MockQuoteResult` fields with line items, total, assumptions, fictional status, and approval. |
| Memory usage | 2 | Uses admin rules, permissions, structured output, and offer notes. |
| Approval handling | 2 | Strongly distinguishes fictional draft from commercial quote. |
| Business usefulness | 2 | Gives useful setup and maintenance separation with exclusions. |
| Limits and transparency | 1 | Manual status is clear, but pricing basis remains weak because the range is unvalidated. |

Total: 11/12
Verdict: Pass

## Problems Observed

- The draft total sits at the top of the documented planning range, but no pricing model explains why each number is appropriate.
- No tax, jurisdiction, or legal review is possible from current docs, which is correct but limits usefulness.

## Possible Correction

Add a quote-template field for `pricing_basis` and require each line item to state whether its price comes from a validated rate, a planning range, or a founder-supplied assumption.

## Verdict

Pass. The quote is useful as an internal draft and correctly avoids pretending to be a real commercial document.
