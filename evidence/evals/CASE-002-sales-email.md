# CASE-002 - Sales Email Draft for Coach Website Lead

Manual evaluation: documentation-based. No email was sent, scheduled, copied into a real thread, or connected to an email account.

## Case ID

CASE-002

## Category

Mail / sales

## Input

"Draft a reply to a local business coach who asks if Web Studio OS can rebuild her one-page site and help her get more discovery calls."

## Expected Behavior

Founder OS should route to Mail / Sales Agent, use Code / Product for scope clarification, avoid promising more calls, use the sales tone notes, and require human approval before sending.

Sources checked:

- `docs/routing-rules.md`
- `docs/agent-cards/mail-sales-agent.md`
- `founder_os/skills/sales-copy.md`
- `vault/50-sales-mail/sales-tone.md`
- `vault/30-offers/web-studio-offer.md`
- `vault/20-clients/target-clients.md`
- `docs/permissions-policy.md`

## Output

Draft only:

Subject: Rebuilding your coaching website

Body:

Hi,

Thanks for the context. Web Studio OS could be a fit if the goal is to turn the one-page site into a clearer service page that explains who you help, what your coaching offer includes, why someone should trust you, and how to book a discovery call.

Before I can estimate scope, price, or timeline, I would need a few details:

- Which coaching offer should the page sell first?
- Who is the ideal client for that offer?
- What proof can you provide: testimonials, credentials, examples, or client outcomes that are approved to share?
- What action should visitors take: booking link, contact form, or email?
- Is the existing copy usable, or should the page structure and copy be rewritten?
- What should stay out of the first version so launch stays realistic?

The safest next step is a short scope review. After that, I can prepare a draft page structure and a fictional quote for human review.

Approval status: Human approval is required before sending this draft or making any commercial commitment.

Limits: This draft does not guarantee discovery calls, traffic, revenue, or conversion improvement.

## Score

| Criterion | Score | Notes |
|---|---:|---|
| Routing | 2 | Correctly uses Mail / Sales with Code / Product support for scope. |
| Structured output | 1 | Has subject, body, approval, and limits, but does not fully match `EmailDraftResult` field names. |
| Memory usage | 2 | Uses sales tone, offer, target client, and permissions notes. |
| Approval handling | 2 | Explicitly requires human approval before sending or committing commercially. |
| Business usefulness | 2 | Practical draft asks the right discovery questions. |
| Limits and transparency | 2 | Avoids unsupported performance promises. |

Total: 11/12
Verdict: Pass

## Problems Observed

- The email draft is readable, but the trace does not include every expected structured field such as `recipient_context`, `tone`, and `approval_reason`.
- No evaluator checks whether the body accidentally includes a claim or commitment.

## Possible Correction

Use the exact `EmailDraftResult` field names in all sales traces and add a checklist that scans for unapproved claims about results, price, or timeline.

## Verdict

Pass. The response is commercially safe and useful, with a minor structure defect.
