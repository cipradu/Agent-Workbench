# Research Planning

Research is driven by decomposition. Do not research the whole universe. Research what can change requirements, authority, constraints, risks, acceptance evidence, or fit.

## Research Categories and Order

Run categories in order. Later categories depend on earlier findings.

| Order | Category                                    | Use when                                                                                     | Output                                                                    |
| ----- | ------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1     | Domain research                             | domain terms, rules, workflows, norms, or failure modes are unclear                          | domain glossary, common patterns, risks, and authority candidates         |
| 2     | Authority hunt or existing-system discovery | source of truth is unknown; greenfield needs authority, brownfield needs system truth        | authority map or existing-system evidence                                 |
| 3     | Library/protocol/vendor research            | requirements depend on current APIs, protocols, libraries, frameworks, vendors, or standards | options, supported behavior, limitations, versions/dates, caveats         |
| 4     | Compliance/risk research                    | external obligations or high-consequence constraints may apply                               | applicable regimes/policies/standards and verification needs              |
| 5     | Constraint validation                       | goals, constraints, and options may conflict                                                 | compatibility matrix: satisfied, conflicting, blocked, or decision needed |

## Stop Conditions

| Category                  | Stop when                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Domain research           | two consecutive targeted searches add no new material fact                                                                        |
| Authority hunt            | each material data concept/rule has an authority or explicit blocker                                                              |
| Existing-system discovery | current behavior, owners, contracts, dependencies, tests, consumers, and impact surfaces are known enough for spec-level fit      |
| Library/protocol/vendor   | each serious option has current support status, target-environment fit, limitation notes, and at least one alternative considered |
| Compliance/risk           | each applicable constraint has source, owner/authority, and verification implication                                              |
| Constraint validation     | each material goal/constraint/option conflict is answered yes, no, blocked, or decision-needed                                    |

## Evidence Logging

Record material evidence when discovered, not at the end. Each evidence item should include:

- claim;
- source;
- date or version when relevant;
- confidence;
- how it affects the spec.

## Question Rule

Ask only when research cannot resolve the decision or when user authority is required. Every question must include:

- decision needed;
- options considered;
- recommended default;
- what changes based on the answer.

## Over-Research Guard

Stop when new searches only confirm known facts, when every material claim has authority, or when remaining unknowns require user/owner decision rather than more research.
