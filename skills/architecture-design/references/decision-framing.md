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

## Source Basis

Separate constraints from background before comparing options.

| Source class        | Use in architecture reasoning                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------- |
| Constraint          | Accepted ADR, approved spec, public contract, compliance/security rule, compatibility promise, or project rule. |
| Current evidence    | Current code, tests, schemas, configs, runtime behavior, diagrams verified against code, or operational facts.  |
| Candidate evidence  | Review comments, generated findings, old docs, prior learnings, issue themes, metrics, screenshots, or reports. |
| Inference           | Agent reasoning from forces when source evidence is incomplete.                                                 |
| Background          | External prior art, examples, Slack notes, issue discussion, or product context not accepted as authority.      |

Normative architecture decisions can rely on constraints and current evidence. Candidate evidence, inference, and background can guide option discovery, but they need verification or owner acceptance before they become binding.

## Pattern Proof

Before accepting a pattern, answer all five questions.

1. What specific problem does this pattern solve in this system?
2. What simpler alternative would also work?
3. What new complexity, coupling, runtime cost, or maintenance cost does the pattern add?
4. What evidence says the complexity is needed now rather than later?
5. What would trigger revisiting or removing this pattern?

If any answer is vague, the pattern is not justified yet.

## Option Discovery

Use option discovery when the prompt is broad, solution-shaped, pattern-attached, or expensive to reverse.

Generate materially different candidates across relevant axes:

- ownership model;
- boundary placement;
- interface depth and caller obligations;
- seam timing: now, deferred, or compatibility shim;
- policy/mechanism split;
- data, persistence, queue, cache, or external-state authority;
- migration and compatibility path;
- operability, reliability, security, privacy, or performance posture.

Each candidate should state its basis:

- `direct`: source-backed by current project evidence or accepted constraints;
- `external`: grounded in current outside behavior, protocol, vendor, standard, or operational prior art;
- `reasoned`: inferred from forces and trade-offs, with uncertainty named.

Reject candidates before the final recommendation when they fail an architecture gate: missing force, ambiguous ownership, shallow interface, boundary leak, unjustified pattern, brownfield gap, compatibility risk, unacceptable caller burden, weak verification, or unresolved source authority.

## Option Comparison

Use this compact comparison for significant choices.

| Option   | Solves                    | Costs               | Risks        | When valid              | Rejected because     |
| -------- | ------------------------- | ------------------- | ------------ | ----------------------- | -------------------- |
| Option A | Specific force or problem | Complexity accepted | Failure mode | Context where this wins | Reason tied to force |
| Option B | Specific force or problem | Complexity accepted | Failure mode | Context where this wins | Reason tied to force |

Do not compare options by preference alone. Tie every reason to a force, constraint, compatibility surface, or verified codebase fact.

## Force-To-Decision Trace

For significant choices, connect the reasoning chain explicitly:

```text
Force or constraint:
<what matters and source basis>

Decision:
<boundary, owner, seam, adapter, pattern, or trade-off>

Rejected alternative:
<alternative and why it failed>

Verification:
<evidence that would prove the decision survived implementation>
```

Use this trace in handoffs to specs, implementation plans, ADRs, reviews, commits, and PRs. The trace preserves architecture reasoning; it does not create implementation units or source-control instructions.

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

When measurement materially shapes the decision, state the baseline, evidence source, hard gates, diagnostics, and stopping condition. Treat metrics as supporting evidence, not authority over missing forces, ambiguous ownership, shallow interfaces, boundary leaks, uncharacterized brownfield behavior, security/privacy gates, or public compatibility.

Proxy metrics can mislead. Fewer files, shorter code, lower latency, higher coverage, or cleaner folder shape can still be worse architecture if caller burden, coupling, ownership ambiguity, stale authority, or policy/mechanism leakage increases.

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

Handoff:
- <architecture facts downstream owners must preserve, or "none">
```
