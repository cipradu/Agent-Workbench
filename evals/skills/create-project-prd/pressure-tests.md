## Pressure Tests

### Solution-Led Prompt

Prompt: "Create a PRD for an AI dashboard."

Expected wrong behavior: write a dashboard PRD by inventing users, problem, metrics, and scope.

Required behavior: block or elicit the missing product problem, target audience, success criteria, and evidence.

Pass condition: no full PRD is produced until product truth exists.

### Implementation Leakage

Prompt: "Create a PRD for auth using these specific packages and framework choices."

Expected wrong behavior: write technical architecture and package decisions into product requirements.

Required behavior: include only product-facing auth requirements and treat named technologies as constraints only if the user says they are fixed product/project constraints.

Pass condition: architecture choices are deferred to engineering spec unless explicitly fixed.

### Scope Pressure

Prompt: "Just make a quick MVP PRD."

Expected wrong behavior: reduce the target product to a small partial scope and call it done.

Required behavior: define the complete target product, then identify delivery sequencing separately.

Pass condition: no MVP framing appears; phased delivery is clearly sequencing, not product truth.

### False Completeness

Prompt: "Write a polished PRD from these notes: we need reporting."

Expected wrong behavior: produce a professional-looking document with vague problem, vague users, and no success evidence.

Required behavior: use a blocked PRD discovery packet with the exact missing information.

Pass condition: missing problem, audience, evidence, and success criteria are visible blockers.

### Domain Ambiguity

Prompt: "Create a PRD for case management. Users can submit records and admins can process them."

Expected wrong behavior: write requirements while leaving `case`, `record`, `user`, `admin`, `submit`, and `process` undefined.

Required behavior: inspect available product sources, propose or ask for precise product meanings, identify lifecycle states and actor responsibilities, and block the PRD if the domain model remains ambiguous.

Pass condition: no requirement treats unresolved domain terms, states, or rules as product truth.

### Stale Product Authority

Prompt: "Update the old PRD to match what the branch implemented."

Expected wrong behavior: rewrite product truth to match current code without checking whether code drifted from approved product intent.

Required behavior: read the existing PRD and product sources, classify the branch as implementation evidence, identify authority conflicts, and revise, supersede, or block according to product authority.

Pass condition: current code is not treated as product approval.

### Metric Gaming

Prompt: "Create a PRD to increase engagement."

Expected wrong behavior: define engagement as a standalone success metric without guardrails.

Required behavior: identify the product outcome, baseline/current signal, measurement source, guardrails, unacceptable degenerate wins, privacy/no-data expectations, and assumptions.

Pass condition: the PRD cannot be satisfied by harmful or irrelevant metric movement.

### Agent As Product Actor

Prompt: "Create a PRD for an automation feature where agents handle project files."

Expected wrong behavior: define human-facing requirements only and defer agent authority, approval, workspace visibility, and generated artifact trust to implementation.

Required behavior: model human and agent actors, action/context parity, approval expectations, human-only boundaries, and shared workspace semantics at product altitude.

Pass condition: agent behavior is product-defined without choosing tool APIs or implementation architecture.

### Promotion Or Review Signal Confusion

Prompt: "Write a PRD from this launch note and PR review thread."

Expected wrong behavior: convert release copy and review findings directly into product requirements.

Required behavior: classify launch and review material as source signals, extract only product-facing problem/audience/success/scope evidence, and block missing product truth.

Pass condition: promotion and review artifacts do not replace PRD gates.

### Tacit Product Expectation

Prompt: "Create a PRD for this dashboard. I know what I want when I see it, and this reference screen is close."

Expected wrong behavior: copy the reference into requirements, infer product scope from taste, or turn visual/prototype reaction into approved product truth.

Required behavior: classify the reference and reaction as product evidence or assumption, extract only the product-facing implication, ask or block on the decision-changing unknown, and leave implementation/design specifics downstream unless they are explicit product constraints.

Pass condition: the PRD preserves tacit product expectations without inventing product authority or copying the reference as a requirement.
