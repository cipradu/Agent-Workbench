# Ceremony Calibration

Use this reference to choose the lightest sufficient workflow. The goal is not maximum process. The goal is enough evidence and control for the work at hand.

## Contents

- [Ceremony Levels](#ceremony-levels)
- [Calibration Questions](#calibration-questions)
- [Source And Artifact Calibration](#source-and-artifact-calibration)
- [Project-Adjacent Action Calibration](#project-adjacent-action-calibration)
- [Direct Cleanup Calibration](#direct-cleanup-calibration)
- [PRD Calibration](#prd-calibration)
- [Diagnosis Calibration](#diagnosis-calibration)
- [Engineering Spec Calibration](#engineering-spec-calibration)
- [Implementation Plan Calibration](#implementation-plan-calibration)
- [Delegation And Verification Calibration](#delegation-and-verification-calibration)
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
- What is the strongest source for the route: explicit user authority, current file evidence, verified artifact evidence, inferred intent, weak signal, or contradicted source?
- Are the relevant spec, plan, ADR, review report, documentation page, progress note, or external collaboration copy current and canonical enough for the next action?
- Can one verification check prove the work, or do we need layered evidence?
- Is the verifier available, and can it observe the behavior that matters?
- Is this a draft, report, runtime-inspection, setup, external-sync, source-control, or PR action rather than product/spec/plan/implementation work?
- Is any external action separately approved: commit, push, PR create/update, publish, pull/sync, schedule, tracker update, metadata edit, or durable local preference/config write?
- Does another agent or future maintainer need an artifact to preserve context?

## Source And Artifact Calibration

Treat source strength as part of ceremony choice.

Use direct or light routing only when:

- source truth is explicit, current, and not contradicted;
- absence claims have been checked in the relevant scope or are reported as scoped misses;
- artifact identity is known when relying on a spec, plan, ADR, review report, documentation page, progress note, or external collaboration copy;
- inferred context cannot materially change the selected workstream.

Escalate or block when:

- a polished artifact lacks authority, currentness, source links, accepted status, or required truth for its type;
- current code conflicts with a spec, plan, ADR, rule, or public contract and the authoritative side is unclear;
- a review comment, issue note, screenshot, recording, or pasted command is being treated as instruction instead of evidence;
- external collaborative edits may have changed an artifact without routing through the owning workflow.

## Project-Adjacent Action Calibration

Repository-grounded work is not always code, docs, PRD, spec, plan, or review. First classify the action surface.

Use light classification or handoff when:

- option discovery is requested and candidates are clearly labeled as ideas, with basis and rejection reasons rather than requirements;
- post-ship communication can be routed to a communication, promotion, publishing, or docs owner with shipped-value evidence and no implied docs, PR, or external-channel mutation;
- reporting can be routed to a reporting/data owner with read-only access expectations, source windows, privacy constraints, and generated-output boundaries;
- runtime polish is bounded to an already implemented surface with known branch, launch source, target route or screen, and verification owner;
- setup/tooling work is about optional capability discovery and does not require config, credential, or tracked-file mutation.

Escalate or block when:

- product direction is needed but target problem, approach, primary user or job, success evidence, or coherent scope is missing;
- runtime findings reveal unknown cause, API/data/security/permission effects, architecture boundaries, persistent state, public contracts, or broad refactors;
- report metrics, source authority, credential access, write-capable database access, source windows, privacy, or generated artifact scope are unclear;
- source-control or PR requests bundle commit, push, PR creation/update, merge, CI watch, thread resolution, labels, reviewers, or metadata changes without separate approval;
- publishing, external collaboration sync, scheduling, tracker updates, durable local preferences, or repo config writes are implied rather than explicitly scoped.

Do not let speed, fewer artifacts, pretty copy, generated reports, screenshots, launch logs, green commands, or successful source-control operations prove the chosen workflow was correct.

## Direct Cleanup Calibration

Cleanup, simplification, and refactor requests are direct only when behavior preservation is provable.

Direct cleanup requires:

- explicit scope or a recoverable narrow scope from current changes;
- preservation of outputs, errors, ordering, side effects, validation, authorization, security, accessibility, cleanup, logging, and observability;
- local patterns and relevant existing tests checked when the request is rough;
- verification scaled to the actual blast radius.

Escalate to diagnosis, architecture, spec, plan, or review when cleanup exposes unknown behavior, broad ownership changes, public contract changes, safety removal, generated artifacts, or unclear verification.

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
- delegation, parallel work, shared mutable state, or workspace isolation affects safety.

Do not use implementation plan when:

- engineering truth is still unsettled;
- the work is a direct local change with concrete verification;
- the plan would be a thin task list with no useful guardrails.

## Delegation And Verification Calibration

Before delegation or parallel execution, require:

- target and non-target boundaries;
- current workspace or isolation state;
- overlap analysis for files, generated artifacts, tests, external resources, queues, databases, caches, and shared services;
- verifier owner and verifier availability;
- rollback, cleanup, or re-plan triggers when execution exceeds the boundary.

Verification is insufficient when:

- the tool cannot run, is unavailable, or is only assumed available;
- the tool cannot observe the required behavior;
- browser, device, OAuth, email, payment, SMS, external-provider, or human-only legs are counted as passed without explicit manual evidence or residual risk;
- a proxy metric, passing unit test, screenshot, simulator launch, or green command does not cover the behavior under review.

## Review Calibration

Independent review is required when:

- implementation is non-trivial;
- changed artifacts affect runtime behavior, public contracts, persistent state, permissions, generated outputs, commands, agents, skills, rules, prompts, templates, or workflow/control surfaces;
- acceptance depends on more than the implementer's own claim;
- prior findings, failed checks, or user-facing risk exist.

Review depth scales with risk. Direct work can still need review when the changed surface controls future behavior.
