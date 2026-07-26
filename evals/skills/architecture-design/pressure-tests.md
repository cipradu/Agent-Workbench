## Pressure Tests

### Pattern Pressure

Prompt: "Use Clean Architecture for this new feature; just give me the layers."

Expected wrong behavior: produce a layer diagram and folder structure immediately.

Required behavior: identify forces, ownership, interface seams, and prove whether Clean Architecture solves a real problem here.

Pass condition: the agent rejects or scopes the pattern if simpler ownership and adapter boundaries are enough.

### Interface Pressure

Prompt: "Add a repository interface around this ORM model so tests can mock it."

Expected wrong behavior: add a repository abstraction by default.

Required behavior: check whether the ORM dependency is the blocking test seam, whether a local substitute or integration test is better, and whether the interface hides meaningful complexity.

Pass condition: the agent only recommends the interface if it has real variation, test value, or policy isolation.

### Brownfield Pressure

Prompt: "This legacy module is ugly. Redesign it into services and adapters."

Expected wrong behavior: propose a broad target architecture without preserving behavior.

Required behavior: characterize current behavior, find the smallest useful seam, separate behavior change from refactor, and preserve public compatibility.

Pass condition: the agent produces an incremental transition path instead of a rewrite-first design.

### Boundary Pressure

Prompt: "The service can just call Stripe and save the ORM object."

Expected wrong behavior: accept direct SDK and ORM coupling for speed.

Required behavior: keep business policy in the owning module and place Stripe/database mechanics behind adapters with explicit contracts.

Pass condition: the agent names the policy owner, adapter responsibilities, and boundary DTO/value object.

### Source Authority Pressure

Prompt: "The old architecture doc says to add repositories everywhere, but the code does not use them. Follow the doc."

Expected wrong behavior: treat either the old doc or current code as automatic authority.

Required behavior: inspect or request the relevant ADR/doc/code evidence, classify stale documentation versus implementation drift or unresolved decision, and still require forces, ownership, interface depth, alternatives, and trade-offs.

Pass condition: the agent blocks or scopes the recommendation until source authority is reconciled.

### Architecture Review Pressure

Prompt: "Review this plan and tell me if the architecture is bad."

Expected wrong behavior: return generic severity findings or demand file-by-file implementation details regardless of artifact type.

Required behavior: classify the artifact shape, review affected ownership/boundaries/seams/trade-offs at the right scrutiny level, and route non-architecture issues elsewhere.

Pass condition: findings name affected boundaries, source evidence, downstream consequence, action owner, residual risk, and coverage without owning review verdicts.

### Failure-Driven Pressure

Prompt: "This bug keeps coming back, so extract the module into a service."

Expected wrong behavior: accept the extraction as the fix.

Required behavior: require causal evidence that the recurrence comes from wrong responsibility, leaky interface, duplicated policy, or cross-subsystem interaction before recommending a boundary move.

Pass condition: the agent routes unknown cause to diagnosis or recommends the smallest characterized seam instead of broad extraction.

### Handoff Pressure

Prompt: "Turn this architecture recommendation into the spec, plan, commit, and PR."

Expected wrong behavior: write requirements, implementation units, commit commands, or PR text inside the architecture answer.

Required behavior: preserve architecture facts, ADR candidates, verification needs, and residual risks while routing specs, plans, commits, and PRs to their owners.

Pass condition: the agent emits an architecture handoff and refuses downstream mechanics inside this skill.
