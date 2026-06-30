# Architecture Review Checklist

Use this before presenting an architecture recommendation, reviewing a proposed design, or marking architecture analysis complete.

## Completeness Checklist

- [ ] Problem and user-visible goal are stated.
- [ ] Material forces and constraints are listed.
- [ ] Material facts are classified as confirmed, source-backed constraint, inferred assumption, background context, stale or conflicting source, or missing force.
- [ ] Absence claims about ADRs, boundaries, adapters, seams, conventions, dependency direction, or local patterns were verified against relevant sources or labeled as assumptions.
- [ ] Source-authority conflicts among code, ADRs, docs, diagrams, runtime behavior, generated findings, external state, or comments are classified before one source is treated as binding.
- [ ] Existing rules, ADRs, codebase patterns, and relevant domain skills were checked or marked missing.
- [ ] Ownership is clear for policies, invariants, state transitions, data transformations, and side effects.
- [ ] Interfaces state caller obligations, hidden complexity, invariants, errors, ordering, and performance expectations.
- [ ] Seams are justified by variation, testability, ownership, volatility, or observation value.
- [ ] Policy and mechanism are separated.
- [ ] External IO, persistence, SDKs, caches, clocks, queues, and framework lifecycle details are behind appropriate adapters or explicit contracts.
- [ ] Raw database, SDK, framework, and transport objects do not leak across policy boundaries unless they are the deliberate public contract.
- [ ] Named patterns are proven against simpler alternatives.
- [ ] Brownfield behavior, compatibility, and transition risks are characterized when existing code is touched.
- [ ] Accepted trade-offs, risks, mitigations, and revisit triggers are stated.
- [ ] Verification strategy matches the boundary: unit, characterization, integration, contract, migration, observability, or manual review.
- [ ] ADR candidates are identified and routed to the `create-project-adr` skill when recording is requested.
- [ ] Downstream handoff preserves architecture facts for spec, plan, review, commit, or PR owners without importing their mechanics.

## Review Mode

Use this mode when reviewing an existing diff, proposal document, ADR candidate, implementation plan, migration/refactor note, interface sketch, or review comment.

### Artifact Classification

Classify by content shape, not file path.

| Artifact shape                          | Architecture scrutiny                                                                                                              |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Requirements-level architecture note    | Missing forces, ownership ambiguity, trust-boundary omissions, incompatible assumptions, and conflicts with existing capabilities. |
| ADR candidate                           | Decision readiness, alternatives, consequences, reversal cost, source authority, and whether architecture analysis is settled.     |
| Implementation plan                     | Implementable ownership, seams, policy/mechanism split, brownfield compatibility, migration path, verification, and ADR handoff.  |
| Diff or code review                     | Primary changed boundary, secondary touched surfaces, pre-existing architecture debt, concrete caller/operator consequence.        |
| Migration or refactor proposal          | Behavior preservation, compatibility surfaces, smallest useful seam, transition path, rollback or recovery, and verification.      |
| Interface sketch                        | Caller burden, hidden complexity, invariants, error modes, ordering, performance, and variation/test/ownership value.             |
| Review comment or feedback              | Treat as a claim to verify against current sources; route non-architecture work to its owner.                                      |

### Architecture Finding Shape

Architecture review findings should include:

- affected owner, boundary, interface, seam, adapter, pattern, or trade-off;
- source evidence, such as path, section, code symbol, ADR ID, diagram, runtime source, or quoted artifact text;
- downstream consequence for callers, maintainers, operators, future contributors, compatibility, or verification;
- suggested architecture correction or owner route;
- evidence strength and residual risk;
- whether the issue is primary to the change, secondary to a touched surface, or pre-existing context.

Do not report generic pattern preference, style-only diagram complaints, missing implementation sequencing in requirements-level artifacts, theoretical scale risk without a material force, pre-existing unrelated debt, or concerns already answered elsewhere in the artifact.

### Coverage Accounting

Name the surfaces inspected and unverified:

- forces and source authority;
- ownership and boundaries;
- interfaces and seams;
- adapters and policy/mechanism split;
- brownfield behavior and compatibility;
- runtime chain, side effects, and alternate entry points when relevant;
- verification strategy;
- ADR candidates and downstream handoff.

## Review Questions

Ask these questions when something feels architecturally weak.

| Concern           | Question                                                                           |
| ----------------- | ---------------------------------------------------------------------------------- |
| Ownership         | Which module owns this decision, and why does the knowledge belong there?          |
| Locality          | If this concept changes, where are the edit sites?                                 |
| Interface depth   | Does the interface hide meaningful complexity or mostly forward calls?             |
| Caller burden     | What must callers know that they should not need to know?                          |
| Mechanism leakage | Are storage, transport, SDK, framework, or runtime details visible in policy code? |
| Pattern fit       | What specific pain does the pattern solve, and what simpler option was rejected?   |
| Brownfield safety | What current behavior might consumers rely on?                                     |
| Testability       | Can important behavior be tested through the same contract callers use?            |
| Operability       | What fails, retries, times out, rolls back, logs, traces, or alerts?               |
| Reversibility     | What would make this decision expensive to undo?                                   |
| Source authority  | Which source is binding here, and what conflicts or stale evidence were checked?   |
| Runtime impact    | What callbacks, jobs, middleware, persistence, alternate entry points, or IO fire? |
| Handoff           | Which facts must downstream owners preserve, and which mechanics stay out of scope? |

## Output Checklist

A final architecture response should include:

```text
Recommendation:
<clear recommendation>

Forces:
- <material force>

Source evidence:
- <confirmed source, assumption, or conflict>

Ownership and boundaries:
- <owner, responsibility, boundary>

Interfaces and seams:
- <interface, hidden complexity, seam justification>

Policy/mechanism split:
- <policy owner and adapter/tool responsibility>

Alternatives rejected:
- <alternative and reason>

Trade-offs and risks:
- <accepted cost, mitigation, revisit trigger>

Verification:
- <tests, characterization, integration, observability, or review>

ADR candidates:
- <candidate decisions or none>

Downstream handoff:
- <spec/plan/review/commit/PR facts to preserve, or none>
```

## Failure States

Return the matching failure instead of a confident recommendation.

| Failure                   | Output                                                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Missing force             | `Blocked: architecture decision depends on missing force: <specific missing fact>.`                                                |
| Ambiguous ownership       | `Blocked: ownership is ambiguous for <policy/invariant/side effect>.`                                                              |
| Shallow interface         | `Rejected: proposed interface is shallow or leaky: <specific reason>.`                                                             |
| Boundary leak             | `Rejected: policy/mechanism boundary is leaking through <specific object/call/dependency>.`                                        |
| Unjustified pattern       | `Rejected: pattern not justified: <pattern> does not solve a proven problem in this context.`                                      |
| Brownfield gap            | `Blocked: brownfield behavior or compatibility surface is not characterized: <specific gap>.`                                      |
| Source conflict           | `Blocked: architecture source authority is unresolved: <specific conflict>.`                                                       |
| Unsupported review finding | `Rejected: architecture finding lacks boundary consequence or source evidence: <specific gap>.`                                    |
| Incomplete recommendation | `Not ready: architecture recommendation is missing <problem/forces/boundaries/interfaces/trade-offs/verification/ADR candidates>.` |
