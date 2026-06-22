# Ceremony Calibration

Use this reference to choose the lightest sufficient workflow. The goal is not maximum process. The goal is enough evidence and control for the work at hand.

## Contents

- [Ceremony Levels](#ceremony-levels)
- [Calibration Questions](#calibration-questions)
- [PRD Calibration](#prd-calibration)
- [Diagnosis Calibration](#diagnosis-calibration)
- [Engineering Spec Calibration](#engineering-spec-calibration)
- [Implementation Plan Calibration](#implementation-plan-calibration)
- [Review Calibration](#review-calibration)

## Ceremony Levels

| Level             | Use when                                                                                                                                                                                | Required behavior                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Direct            | Work is local, reversible, understood, and concretely verifiable                                                                                                                        | Implement narrowly, verify, and report evidence                                         |
| Diagnostic        | Something is failing or disputed and cause is not proven                                                                                                                                | Run structured problem resolution before choosing fix/spec/plan                         |
| Definition        | Product or engineering truth is missing                                                                                                                                                 | Confirm explicit PRD/product-definition intent before PRD, or create engineering spec when engineering truth is missing |
| Planned execution | Implementation has multiple surfaces, dependencies, handoff needs, or meaningful blast radius                                                                                           | Create or use implementation plan before execution                                      |
| High assurance    | Wrong behavior would be hard to reverse, difficult to detect, broadly impactful, trust-affecting, data-affecting, permission-affecting, externally visible, or control-surface changing | Require stronger discovery, traceability, concrete verification, and independent review |

High assurance is not a domain label. It is a property of consequence, reversibility, detectability, blast radius, and trust.

## Calibration Questions

Ask these before selecting a path:

- What changes if the agent is wrong?
- How quickly would the wrong result be noticed?
- Can the change be reversed without data loss, compatibility damage, or user-visible fallout?
- Which existing behavior, contracts, data, permissions, runtime wiring, generated artifacts, or automation might be affected?
- Is the desired behavior already authoritative, or is it being invented?
- Is the cause known, or are we guessing?
- Can one verification check prove the work, or do we need layered evidence?
- Does another agent or future maintainer need an artifact to preserve context?

## PRD Calibration

Use PRD when the user explicitly asks for a PRD, project definition, product definition, product brief, or equivalent product-scope artifact, and product/workflow truth must be established or changed.

When product truth is missing but PRD/product-definition intent is not explicit, do not invoke PRD. Ask one targeted question or report a blocker before engineering spec, planning, or implementation.

Signals:

- new project, product surface, major capability, or user-facing workflow;
- unclear beneficiary, problem, current workaround, success evidence, scope, or non-goal;
- multiple plausible product shapes;
- product constraints must be preserved before engineering spec.

Do not use PRD when:

- product truth is already explicit and the work is engineering translation;
- PRD/product-definition intent is not explicit;
- the change is local and does not alter product/workflow scope;
- the PRD would only restate implementation details.

## Diagnosis Calibration

Use diagnosis before spec/plan when:

- the issue is a failure, regression, intermittent behavior, test failure, review claim, or bug report;
- the cause is unknown;
- previous fixes failed;
- the proposed fix comes from an unverified diagnosis;
- the symptom may reveal deeper design or compatibility issues.

Diagnosis may lead to direct implementation, engineering spec, architecture analysis, or user decision. It should not be bypassed by writing a confident spec around a guessed cause.

## Engineering Spec Calibration

Use engineering spec when:

- required behavior or acceptance evidence must be stabilized;
- constraints, authority, invariants, contracts, risks, compatibility, or data/state implications matter;
- current codebase behavior must be reconciled with requested behavior;
- implementation would otherwise depend on assumptions.

Do not use engineering spec when:

- an approved/current spec or equivalent implementation contract already exists;
- the work is direct, local, and fully understood;
- the only missing item is execution sequencing, which belongs in the plan.

## Implementation Plan Calibration

Use implementation plan when:

- an approved/current spec or equivalent contract exists;
- execution has multiple units or dependencies;
- target and non-target boundaries matter;
- blast radius needs analysis;
- implementation will be delegated;
- verification and review must be mapped before editing.

Do not use implementation plan when:

- engineering truth is still unsettled;
- the work is a direct local change with concrete verification;
- the plan would be a thin task list with no useful guardrails.

## Review Calibration

Independent review is required when:

- implementation is non-trivial;
- changed artifacts affect runtime behavior, public contracts, persistent state, permissions, generated outputs, commands, agents, skills, rules, prompts, templates, or workflow/control surfaces;
- acceptance depends on more than the implementer's own claim;
- prior findings, failed checks, or user-facing risk exist.

Review depth scales with risk. Direct work can still need review when the changed surface controls future behavior.
