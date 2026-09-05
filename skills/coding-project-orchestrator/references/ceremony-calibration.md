# Ceremony Calibration

Use this reference to choose the lightest sufficient workflow. The goal is not maximum process. The goal is enough evidence and control for the work at hand.

## Contents

- [Consequence Lanes And Gate Warrants](#consequence-lanes-and-gate-warrants)
- [Scope Envelope Calibration](#scope-envelope-calibration)
- [Calibration Questions](#calibration-questions)
- [Source And Artifact Calibration](#source-and-artifact-calibration)
- [Project-Adjacent Action Calibration](#project-adjacent-action-calibration)
- [Direct Cleanup Calibration](#direct-cleanup-calibration)
- [Instrumental Discovery And Standard Implementation Calibration](#instrumental-discovery-and-standard-implementation-calibration)
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

## Scope Envelope Calibration

Bind `Outcome`, `Non-goals`, `Target boundary`, `Acceptance proof`, and `Expansion or re-plan triggers` before using consequence to select ceremony. Consequence changes control depth; it does not enlarge the accepted outcome.

Trace every proposed capability, abstraction, file, test, artifact, compatibility path, and workflow phase to the accepted outcome, a current named risk or invariant, a required compatibility obligation, or cleanup directly caused by the change. Remove an item that has no trace. When new evidence creates a real need outside the envelope, return it to the orchestrator for scope and gate reclassification rather than silently expanding a spec, plan, implementation, or review.

Prefer existing code, helpers, patterns, dependencies, and test setup. A new abstraction needs a current evidenced force: real duplication, an established local pattern, a domain invariant, a changing external or security boundary, or a test seam required to prove accepted behavior. A second caller is strong evidence, not a universal prerequisite. Minimal scope must still deliver the complete outcome and retain every applicable safeguard.

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

- What exact outcome, non-goals, target boundary, acceptance proof, and expansion triggers constrain this work?
- Which accepted outcome, current risk or invariant, compatibility obligation, or change-caused cleanup justifies each proposed addition?
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

## Instrumental Discovery And Standard Implementation Calibration

Use bounded instrumental discovery when current repository facts are needed to classify the requested outcome. Fully load applicable governing instructions, owning skills and selected references before their dependent decisions. Inspect evidence that can change lane, gate, scope, clarification, verification or next action; follow relevant dependencies or authority beyond the initially named target. Such examples guide judgment rather than limit valid expansion. End routing discovery when its evidence requirements are satisfied, then preserve downstream loading, diagnosis, impact and acceptance obligations. Do not read unrelated source bodies or repeat searches solely for ceremony; do not use bounded discovery to skip required context or an unresolved proof gap.

After inspection, ask one targeted question only when two materially different complete outcomes remain and no safe authorized default exists. Start with the user's action and observable consequence, then explain the missing fact or conflict, exact blocked work and unaffected work, and one recommended resolution with its exact approved change, material effect, material cost and risk, and no-change outcome. Show alternatives only when their behavior, cost, risk, authority, or future obligation differs; merge choices with the same practical result. Ask before a specification, plan, or implementation; those artifacts cannot supply user-owned truth. The question fails this gate when the next action is unchanged regardless of the answer or when the user must understand internal identifiers to choose.

Use standard implementation when:

- direct proof remains incomplete and no concrete high-assurance trigger applies;
- the user request plus current repository evidence and any necessary clarification are sufficient as the implementation contract;
- target and non-target boundaries, permission, verification, and stop conditions are known enough to act safely;
- every diagnosis, spec, plan, delegation, review, and final-gate warrant has been decided independently, and each required precondition is satisfied.

Do not use standard implementation to bypass unresolved product behavior, unknown failure cause, durable engineering truth, architecture ownership, permission, destructive/external-action authority, or acceptance evidence. Do not withhold standard implementation merely because the change is durable, affects tooling or configuration, spans multiple files, or does not satisfy the stricter direct checklist.

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
- a standard implementation contract is sufficient from the user request, current repository evidence, and any necessary clarification, with no durable engineering truth left to decide;
- the only missing item is execution sequencing, which belongs in the plan.

## Implementation Plan Calibration

Use implementation plan when:

- an approved/current spec or equivalent implementation contract exists;
- multiple dependent units, real ordering constraints, multiple executors, shared mutable state, migration or rollout, material rollback concerns, or a boundary that must be crossed safely requires durable sequencing.

Do not use implementation plan when:

- engineering truth is still unsettled;
- the work is inside a proven direct lane under current governing repository policy;
- standard implementation has no real dependency order, shared state, migration/rollout, multiple-executor coordination, material rollback, or safe-boundary-crossing need;
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

Then classify the current changed surface. A `document-only` delta changes only ADRs, specs, plans, READMEs, reader-facing docs, progress or scratch notes, or other prose records; it excludes code, tests, executable configuration, schemas, migrations, generated contracts or artifacts, commands, hooks, CI, and behavior-changing agents, skills, rules, or prompts. A prose-formatted control artifact is not document-only. Mixed deltas use their actual non-document surfaces. Risks described by a document are future implementation context, not current review triggers.

Decide review warrant, cadence, depth, and semantic lanes independently:

- Warrant review for an explicit request, an applicable scoped repository floor, a changed surface whose consequence needs independent acceptance, unresolved semantic judgment, or another named acceptance gap.
- Cadence is `none`, `single_final`, or `checkpoints`; checkpoints require a boundary where review can change the next action.
- Depth is `not_applicable`, `quick`, `standard`, or `deep`; depth controls rigor inside the exact target and causal halo, never repository-wide breadth by itself.
- Semantic lanes activate only from changed surfaces or evidence. Security, performance, concurrency, operations, pattern, and adversarial lanes do not run by artifact label.

A standard lane can have no review, one review at any justified depth, or checkpoints. High assurance can have one final review when intermediate review cannot change an action. A direct lane can still have review when its independent warrant passes. Generic semantic/non-trivial/control-surface labels, file count, configuration status, generated artifacts, or delegation do not warrant review.

Document-only deltas have a hard review ceiling: `quick` or `standard`, never `deep`, and never a fresh validator or nested review chain. Use `single_final` for the complete document deliverable when review is warranted. Do not create a checkpoint because a unit produces a document or because that document discusses auth, security, regulated or sensitive data, migration, public contracts, production, release, or deployment. An explicit current user request may add a distinct review event but does not remove the depth or validator prohibition.

## Final Complete-Gate Calibration

Record `Final complete gate warranted: yes` only when repository policy assigns a complete gate to the changed artifact, high-assurance acceptance needs it, shared or cross-boundary behavior can escape targeted checks, or an acceptance predicate requires it. Record `no` for non-semantic prose or an isolated artifact with complete deterministic validation and no applicable repository gate.

Run the complete gate once after the final mutation of the logical deliverable. Reuse fresh evidence tied to the exact state; any covered mutation invalidates it. Do not run a gate whose result cannot change the next action.
