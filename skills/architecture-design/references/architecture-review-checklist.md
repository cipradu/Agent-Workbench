# Architecture Review Checklist

Use this before presenting an architecture recommendation, reviewing a proposed design, or marking architecture analysis complete.

## Completeness Checklist

- [ ] Problem and user-visible goal are stated.
- [ ] Material forces and constraints are listed.
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

## Output Checklist

A final architecture response should include:

```text
Recommendation:
<clear recommendation>

Forces:
- <material force>

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
| Incomplete recommendation | `Not ready: architecture recommendation is missing <problem/forces/boundaries/interfaces/trade-offs/verification/ADR candidates>.` |
