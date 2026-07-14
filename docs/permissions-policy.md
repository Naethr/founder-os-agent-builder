# Permissions Policy

The default rule is conservative: internal drafts are usually allowed, while external, financial, public, permanent, or privacy-sensitive actions require human validation. Some actions are forbidden because they create legal, ethical, operational, or trust risks that are not appropriate for a Day 1 MVP.

| Action | Classification | Reason | Required evidence |
|---|---|---|---|
| Sending a real email | Allowed only with human validation | External communication can create commitments, reputational risk, or compliance issues. | Draft email, recipient, purpose, approval note, and sent confirmation if applicable. |
| Writing into a permanent note | Allowed only with human validation | Durable memory can spread incorrect or sensitive information if not reviewed. | Proposed note content, source, reason for storing, and approval status. |
| Modifying a project file | Allowed only with human validation | File changes can affect project direction or deliverables. | File list, change summary, reviewer approval, and Git commit if committed. |
| Generating a quote | Allowed only with human validation | Pricing and scope can create client expectations even when drafted. | Scope, assumptions, pricing basis, draft quote, and approval status. |
| Using a paid API | Allowed only with human validation | Paid APIs create cost, data exposure, and vendor dependency. | API name, purpose, estimated cost, data sent, and approval note. |
| Importing prospect data | Allowed only with human validation | Prospect data may include personal data and consent obligations. | Data source, fields imported, purpose, retention plan, and approval note. |
| Deleting files | Allowed only with human validation | Deletion can destroy evidence, project history, or useful drafts. | File list, reason, backup status, and approval note. |
| Changing pricing | Allowed only with human validation | Pricing affects positioning, profitability, and client expectations. | Proposed pricing, rationale, impact analysis, and approval note. |
| Publishing public content | Allowed only with human validation | Public content affects reputation and can contain mistakes or unsupported claims. | Content draft, publication target, review notes, and approval status. |
| Contacting a lead | Allowed only with human validation | Outreach can create compliance and reputation risk. | Prospect context, message draft, channel, approval note, and outcome if contacted. |
| Storing personal data | Allowed only with human validation | Personal data creates privacy, security, and retention obligations. | Data fields, source, purpose, retention rule, and approval note. |
| Updating a client deliverable | Allowed only with human validation | Client-facing work must be reviewed before changes are made. | Deliverable link or file, change summary, review notes, and approval status. |
| Running automated outreach | Forbidden | Automated outreach is high-risk for spam, compliance, deliverability, and brand trust at MVP stage. | Decision note explaining why it was not run. |
| Committing code or documentation | Allowed only with human validation | Commits create project history and should reflect intentional changes. | Git diff summary, commit message, and commit hash. |
| Pushing to a remote repository | Allowed only with human validation | Pushes publish project history and can affect collaboration or PR workflows. | Branch name, remote target, reason, and approval or PR link. |
| Deploying to production | Forbidden | Production deployment is outside the Day 1 blueprint scope. | Decision note confirming no deployment occurred. |
| Accessing client credentials | Forbidden | Credential access is unnecessary for the blueprint and creates severe security risk. | Decision note confirming credentials were not requested or used. |
| Drafting internal notes | Allowed | Low-risk internal drafts are useful as long as they are not treated as validated memory. | Draft location, authoring context, and review status if promoted to permanent memory. |
| Reading project documentation | Allowed | Reading local project documents is necessary for coordination and planning. | File references when used for decisions. |
