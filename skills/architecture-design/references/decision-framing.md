# Decision Framing

Use this reference when comparing architecture options, selecting patterns, rejecting alternatives, or deciding whether a choice should become an ADR.

## Forces First

List only forces that affect the decision.

| Force                    | Questions                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------- |
| Functional behavior      | What must the system do? What must it never do?                                                   |
| Scale and performance    | What volume, latency, throughput, concurrency, or resource limits matter now?                     |
| Reliability and recovery | What failures are expected? What must degrade, retry, roll back, or be observable?                |
| Security and privacy     | What trust boundaries, secrets, permissions, audit needs, or data exposure risks exist?           |
| Data integrity           | What must be transactional, unique, ordered, immutable, recoverable, or historically traceable?   |
| Operability              | What must be configured, deployed, monitored, supported, rolled back, or migrated?                |
| Team and codebase        | What does the team know? What patterns already exist? What constraints do ADRs or rules impose?   |
| Compatibility            | Which APIs, consumers, persisted data, CLIs, files, workflows, or integrations must keep working? |

## Pattern Proof

Before accepting a pattern, answer all five questions.

1. What specific problem does this pattern solve in this system?
2. What simpler alternative would also work?
3. What new complexity, coupling, runtime cost, or maintenance cost does the pattern add?
4. What evidence says the complexity is needed now rather than later?
5. What would trigger revisiting or removing this pattern?

If any answer is vague, the pattern is not justified yet.

## Option Comparison

Use this compact comparison for significant choices.

| Option   | Solves                    | Costs               | Risks        | When valid              | Rejected because     |
| -------- | ------------------------- | ------------------- | ------------ | ----------------------- | -------------------- |
| Option A | Specific force or problem | Complexity accepted | Failure mode | Context where this wins | Reason tied to force |
| Option B | Specific force or problem | Complexity accepted | Failure mode | Context where this wins | Reason tied to force |

Do not compare options by preference alone. Tie every reason to a force, constraint, compatibility surface, or verified codebase fact.

## Quality Attribute Check

For each recommendation, state which quality attributes improve and which may get worse.

Common trade-offs:

- simpler caller interface versus more internal implementation complexity;
- lower coupling versus extra indirection;
- synchronous consistency versus latency and availability;
- asynchronous resilience versus eventual consistency and operational complexity;
- reuse versus wrong abstraction risk;
- centralization versus bottleneck or ownership contention;
- performance optimization versus readability and portability;
- stricter validation versus compatibility with existing data or consumers.

## ADR Handoff

Do not embed a second ADR template in architecture output. Use the `create-project-adr` skill when a decision qualifies.

Qualifies when:

- reversal would be costly;
- the decision changes architecture, interfaces, data model, dependencies, deployment, security posture, or repeated implementation conventions;
- future contributors will ask why;
- real alternatives were weighed;
- the choice creates consequences future work must honor.

Does not qualify when:

- the choice is a small local implementation detail;
- the decision is already mandated by repo rules or an accepted ADR;
- the choice is temporary and intentionally experimental;
- the rationale is already obvious from the code and has no repeated impact.

## Recommendation Shape

Use this shape for architecture recommendations:

```text
Recommended direction: <one sentence>

Forces:
- <force and evidence>

Why this boundary:
- <ownership and interface reason>

Alternatives rejected:
- <alternative>: <reason tied to force>

Trade-offs accepted:
- <cost/risk and mitigation or revisit trigger>

ADR candidates:
- <decision or "none">
```
