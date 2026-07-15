# Provider Choice

The provisional recommendation is a **hybrid setup**.

This choice does not block the next steps. It is a practical MVP decision that can change after real usage, cost, privacy needs, and performance requirements are better understood.

## Recommended MVP Setup

- Obsidian / vault stored locally.
- Documentation and project files stored in Git.
- Cloud AI model provider used for stronger reasoning, drafting, planning, and review.
- Local model option through Ollama for private drafts, experiments, and low-risk tasks.

## Local Models

Local models provide better privacy, offline control, and potentially lower recurring cost. They are useful for private drafts, experiments, summarizing non-sensitive local notes, and workflows where external data transfer is not acceptable.

The tradeoff is performance. Local models may have weaker reasoning, smaller context windows, slower inference, and hardware constraints. For a small founder project, this can slow execution if the model struggles with multi-step planning or precise writing.

## Cloud Models

Cloud models usually provide stronger reasoning, easier setup, better reliability, and faster iteration. They are a good fit for business planning, agent coordination, technical writing, and reviewing complex outputs.

The tradeoff is dependency. Cloud providers introduce recurring cost, availability risk, data handling concerns, and vendor lock-in. Sensitive client data should not be sent to a cloud provider without a clear policy and human validation.

## Hybrid Setup

Hybrid is the most pragmatic MVP choice:

- Keep durable memory and project files local.
- Use Git for traceability and review.
- Use cloud AI where model quality materially improves output.
- Use local models where privacy or experimentation matters more than maximum reasoning quality.

This avoids premature infrastructure decisions. The first goal is to validate the Founder OS workflow, not to optimize hosting or model deployment too early.

## Decision Rule

Use cloud AI for high-value reasoning and complex planning when the input is allowed to leave the local machine. Use local models for private, low-risk, or experimental work. Require human validation before sending sensitive client, prospect, financial, or personal data to any external provider.

## First Functional Agent MVP

For the first functional agent, the chosen platform is a **local rule-based CLI prototype** implemented with Python standard library code.

This choice is intentionally narrower than the provisional hybrid setup above. The goal of this exercise is to create a working Founder OS qualification agent, not to configure a full cloud or local LLM stack.

### Data Sent or Not Sent

No request data is sent outside the local machine during the current MVP run. The script reads a local command-line input and prints a local Markdown result.

There is no cloud model call, no API request, no external database, no analytics tool, and no third-party automation platform involved.

### Potential Cost

The current local CLI run has zero provider cost.

Future cloud model versions could create API costs depending on the model, token usage, logging policy, retry behavior, and volume of requests. Those costs should be reviewed before using the agent with real client or prospect data.

### Machine Constraints

Machine constraints are very low. The prototype only needs Python 3 and the standard library.

It does not require GPU acceleration, local model weights, Docker, a database, a browser, or long-running services.

### Limitations

The current agent is rule-based. Its main limits are:

- no deep reasoning;
- no semantic understanding beyond keyword rules;
- no real tool use;
- no external memory;
- no automatic access to project files, emails, calendars, CRMs, or websites;
- no reliable handling of ambiguous or unusual wording;
- no ability to produce final prices, timelines, quotes, or client-ready commitments.

### Why This Is Acceptable for the First Agent MVP

This is acceptable for the first agent MVP because it demonstrates the core qualification workflow with minimal risk:

- it reformulates the need;
- it selects relevant Web Studio OS agents;
- it identifies the main risk;
- it flags human validation;
- it proposes a next action;
- it keeps sensitive data local;
- it avoids premature infrastructure work.

The first milestone is to prove the workflow shape. Model quality can be improved later once the expected input, output, evidence format, and validation rules are clearer.

### Future LLM Improvements

A future cloud or local LLM version could improve:

- understanding of varied wording;
- dynamic follow-up questions;
- better risk detection;
- better routing between agents;
- more nuanced sales, SEO, product, and admin reasoning;
- integration with a validated vault memory;
- generation of draft emails, questionnaires, and scope checklists.

Before using a cloud provider, the project should define which client or prospect data may leave the local machine, what should be redacted, how outputs are reviewed, and what evidence must be stored.
