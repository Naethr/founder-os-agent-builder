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
