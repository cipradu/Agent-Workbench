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
| 5     | Measurement and verification feasibility    | success depends on metrics, reports, quality, performance, external systems, or human verification | measurement source, baseline need, proof modality, hard gates, diagnostics, blockers |
| 6     | Constraint validation                       | goals, constraints, and options may conflict                                                 | compatibility matrix: satisfied, conflicting, blocked, or decision needed |

## Stop Conditions

| Category                  | Stop when                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Domain research           | two consecutive targeted searches add no new material fact                                                                        |
| Authority hunt            | each material data concept/rule has an authority or explicit blocker                                                              |
| Existing-system discovery | current behavior, owners, contracts, dependencies, tests, consumers, and impact surfaces are known enough for spec-level fit      |
| Library/protocol/vendor   | each serious option has current support status, target-environment fit, limitation notes, and at least one alternative considered |
| Compliance/risk           | each applicable constraint has source, owner/authority, and verification implication                                              |
| Measurement feasibility   | each measurable or externally verified outcome has proof source, modality, baseline or blocker, and hard-gate/diagnostic split   |
| Constraint validation     | each material goal/constraint/option conflict is answered yes, no, blocked, or decision-needed                                    |

## Evidence Logging

Record material evidence when discovered, not at the end. Each evidence item should include:

- claim;
- source;
- date or version when relevant;
- scope: target authority, adjacent impact, historical context, untrusted signal, inferred hint, unsupported;
- confidence: authority-backed, current-system, current-external, verified evidence, weak context, unsupported;
- how it affects the spec.

Every material evidence item must affect at least one requirement, authority-map entry, domain-model decision, risk, acceptance example, non-scope item, or blocker. If it does not affect spec truth, omit it or keep it as background outside the normative path.

## Capability Readiness

Before declaring research blocked by missing tools or skills, classify the missing capability:

- `required blocker`: no adequate source, skill, agent, tool, or access path exists to establish authority, current behavior, current external fact, or acceptance evidence;
- `fallback-covered`: another available skill, direct source inspection, current official docs, or user/owner authority can provide equivalent evidence;
- `optional capability`: would improve confidence or speed but is not required for this spec.

Record the fallback or blocked-packet impact.

## Measurement And Degenerate-Gate Planning

When success depends on performance, quality, cost, reliability, ranking, relevance, generated reports, analytics, or semantic judgment, define:

- primary measure and direction;
- baseline or baseline-discovery need;
- measurement source, dataset, log, telemetry, command, manual review, or rubric;
- hard gates versus diagnostics;
- immutable source evidence, fixtures, contracts, schemas, examples, or rubrics;
- degenerate passes to reject, such as dropping data, narrowing inputs, weakening validation, bypassing security/privacy/compliance, breaking compatibility, changing public contracts, or altering the proof harness.

Use semantic or human judgment only when authoritative hard gates are insufficient, and keep the rubric fixed before planning or implementation.

## Question Rule

Ask only when research cannot resolve the decision or when user authority is required. Every question must include:

- decision needed;
- options considered;
- recommended default;
- what changes based on the answer.

## Over-Research Guard

Stop when new searches only confirm known facts, when every material claim has authority, or when remaining unknowns require user/owner decision rather than more research. Do not research broad candidate ideas, product strategy, or alternatives beyond what can change requirements, authority, constraints, risks, acceptance evidence, or fit.
