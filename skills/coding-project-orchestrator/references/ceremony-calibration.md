# Ceremony Calibration

Use this reference to choose the lightest sufficient workflow. The goal is not maximum process. The goal is enough evidence and control for the work at hand.

## Contents

- [Consequence Lanes And Gate Warrants](#consequence-lanes-and-gate-warrants)
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
- [Final Complete-Gate Calibration](#final-complete-gate-calibration)

## Consequence Lanes And Gate Warrants

| Lane | Positive classification evidence | Required behavior |
| ---- | -------------------------------- | ----------------- |
| `direct` | Known target behavior and cause; bounded scope and blast radius; practical reversibility; no automatic high trigger; deterministic acceptance | Implement inside the proven boundary and satisfy only independently warranted gates |
| `standard` | Complete direct proof is absent and no concrete high-assurance trigger applies | Use the neutral meaningful-work route and activate only gates that resolve a named uncertainty or acceptance gap |
| `high_assurance` | One or more concrete high-assurance triggers are present | Apply every relevant safeguard at sufficient depth without forcing irrelevant artifacts or review lanes |

Diagnosis, definition, planning, delegation, review, re-review, and final complete verification are gate warrants, not additional lanes or a fixed sequence. A lane never expands into a pipeline.

## Assurance Precedence And Configuration Replication

Before de-escalation, evaluate explicit review requests, repository assurance profiles, and automatic high-assurance triggers without coupling unrelated gates.

- An explicit review request sets the review warrant; it does not change the lane or activate spec, plan, or delegation by itself.
- A repository profile may raise a lane or gate only when it names the protected consequence, affected scope, owning authority, exact floor, and reason. Reject a profile based only on semantic/non-trivial labels, artifact type, file count, or configuration status.
- An automatic high-assurance trigger sets `Lane: high_assurance`; gates inside high assurance remain separately warranted.

Bounded configuration replication is one `direct` subtype, not the only direct semantic lane. The authorized source-to-target behavior must be exact, reversible, and deterministically provable. The source, target mapping, target scope, post-activation equivalence, and effective authority must be known. Effective authority comes from actual credentials, runtime controls, reachable data, and enforced permissions; advertised operations are exposure context. The subtype must add no semantics, authority, data reach, permission, dependency, architecture, security boundary, persistence, or side effect. A non-mutating authorized connection check may verify a target; a state-changing check is external mutation.

Direct and high assurance both require positive evidence. When a direct condition or possible high trigger is unknown, run bounded discovery for that named uncertainty and reclassify. Unknown does not mean direct or high assurance.

Concrete high-assurance triggers are: regulated, client, production, or sensitive data; destructive or hard-to-reverse work; migration or persistent-state transformation; authentication, authorization, or security-boundary change; new or expanded write/admin authority or sensitive-data reach; public compatibility or durable external-contract change; release or deployment authority; a broad system-wide control change that changes permission, mutation, or acceptance boundaries; or a source-backed severe consequence with material blast radius, delayed detectability, difficult recovery, trust impact, or operational-continuity impact.

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
- Which named uncertainty or acceptance gap can each proposed phase resolve, and can its result change the next action?
- What are the independent review warrant, cadence, depth, semantic lanes, re-review rule, and final complete-gate warrant?

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

If every direct condition is not affirmatively proven, route standard unless a high trigger applies. Activate diagnosis, architecture, spec, plan, or review only when its independent warrant passes.

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

- durable behavior, constraints, invariants, authority, contracts, or unresolved choices must survive implementation.

Do not use engineering spec when:

- an approved/current spec or equivalent implementation contract already exists;
- the work is direct, local, and fully understood;
- the only missing item is execution sequencing, which belongs in the plan.

## Implementation Plan Calibration

Use implementation plan when:

- an approved/current spec or equivalent implementation contract exists;
- multiple dependent units, real ordering constraints, multiple executors, shared mutable state, migration or rollout, material rollback concerns, or a boundary that must be crossed safely requires durable sequencing.

Do not use implementation plan when:

- engineering truth is still unsettled;
- the work is inside a proven direct lane under current governing repository policy;
- multiple files or delegation are the only reasons proposed;
- the plan would be a thin task list with no useful guardrails.

## Delegation And Verification Calibration

Before delegation or parallel execution, require:

- target and non-target boundaries;
- current workspace or isolation state;
- overlap analysis for files, generated artifacts, tests, external resources, queues, databases, caches, and shared services;
- verifier owner and verifier availability;
- rollback, cleanup, or re-plan triggers when execution exceeds the boundary.

Delegation is warranted only when isolation, parallelism, specialist capability, or context focus materially improves the result relative to its re-derivation cost. Delegation does not create a plan warrant.

Verification is insufficient when:

- the tool cannot run, is unavailable, or is only assumed available;
- the tool cannot observe the required behavior;
- browser, device, OAuth, email, payment, SMS, external-provider, or human-only legs are counted as passed without explicit manual evidence or residual risk;
- a proxy metric, passing unit test, screenshot, simulator launch, or green command does not cover the behavior under review.

## Review Calibration

First classify text edits by semantic effect. Non-semantic typo, formatting, grammar, comment, or wording cleanup does not require independent review when it cannot change trigger selection, routing, ownership boundaries, mandatory or optional behavior, gates, stop conditions, delegation, acceptance criteria, permissions, external/project behavior, or future-agent behavior. Verify those edits with diff/readback evidence and report the non-semantic basis.

Decide review warrant, cadence, depth, and semantic lanes independently:

- Warrant review for an explicit request, an applicable scoped repository floor, a changed surface whose consequence needs independent acceptance, unresolved semantic judgment, or another named acceptance gap.
- Cadence is `none`, `single_final`, or `checkpoints`; checkpoints require a boundary where review can change the next action.
- Depth is `not_applicable`, `quick`, `standard`, or `deep`; depth controls rigor inside the exact target and causal halo, never repository-wide breadth by itself.
- Semantic lanes activate only from changed surfaces or evidence. Security, performance, concurrency, operations, pattern, and adversarial lanes do not run by artifact label.

A standard lane can have no review, one review at any justified depth, or checkpoints. High assurance can have one final review when intermediate review cannot change an action. A direct lane can still have review when its independent warrant passes. Generic semantic/non-trivial/control-surface labels, file count, configuration status, generated artifacts, or delegation do not warrant review.

## Final Complete-Gate Calibration

Record `Final complete gate warranted: yes` only when repository policy assigns a complete gate to the changed artifact, high-assurance acceptance needs it, shared or cross-boundary behavior can escape targeted checks, or an acceptance predicate requires it. Record `no` for non-semantic prose or an isolated artifact with complete deterministic validation and no applicable repository gate.

Run the complete gate once after the final mutation of the logical deliverable. Reuse fresh evidence tied to the exact state; any covered mutation invalidates it. Do not run a gate whose result cannot change the next action.
