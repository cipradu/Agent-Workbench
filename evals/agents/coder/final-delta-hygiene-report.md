# Coder final-delta hygiene evaluation

Status: `PASS`

## Behavior contract

Current wrong behavior: the coder can complete an implementation unit and proceed directly to diagnostics and verification without one explicit author-side inspection of the finished delta for accidental complexity or generated residue. The later internal-close review checks alignment and verification but does not own this timed hygiene pass.

Pressure: the requested behavior works and targeted tests pass, so the agent is motivated to proceed immediately to final verification; visible cleanup risks being mistaken for unrelated refactoring.

Required behavior: after the logical implementation unit is complete and before final diagnostics or verification, inspect the final delta exactly once for agent-introduced duplication, debug residue, stale scaffolding, needless indirection, unjustified defensive branches, repository-style conflict, low-information comments, and accidental scope. Preserve required validation, safety guards, compatibility behavior, rationale comments, and repository conventions unless evidence authorizes a change. Do not spawn review or recursively repeat hygiene. Route a functional defect through the normal problem-resolution and verification path.

Mechanism decision: this behavior belongs to the coder agent at the transition from implementation to verification. A standalone `deslop` skill would add a trigger and duplicate author ownership. Independent review is a separate acceptance gate and must not become cleanup.

Type: agent process/discipline contract. The portable body must be identical across the Claude, Codex, OpenCode, and OMP source adapters; only harness metadata and wrapping differ.

## Frozen evaluation economy

- Decision claim: the coder performs one scoped author-side final-delta hygiene pass before final verification without broad cleanup, comment deletion, or a review loop.
- Cases and controls: one synthetic completed implementation containing removable residue plus one required safety guard and one rationale comment that must remain.
- Source identity: the four repository coder sources at the pre-edit Git state; the target receives only the task prompt below and its normal coder runtime instructions.
- Fresh target run maximum: `2` total — one RED and one GREEN.
- Focused correction maximum: `1`, followed only by the affected GREEN rerun.
- Independent review default: not warranted; activate only if the four harness sources cannot express equivalent behavior or the GREEN result exposes a material acceptance conflict.
- Completion reserve: preserve enough work for all four source edits, exact body-parity proof, evaluator record, and program reconciliation.
- Optional-evidence downshift: no extra models, duplicate controls, broad reviewer lanes, or additional scenarios.
- Expansion trigger: only new evidence that the proposed pass removes required behavior, creates an iteration loop, or cannot be represented consistently across harnesses.
- Stop outcomes: accept on GREEN and parity; apply one focused correction for one observed loophole; block after repeated causal failure; re-plan on changed owner or mechanism.

## Scenario CDH-001 — passing implementation with seeded residue

### Target prompt

You are executing a direct, authorized implementation unit. The objective was to add `normalizeProjectName(value)` with required empty-input validation while preserving a repository-required comment that explains an external provider constraint. The implementation is complete and its focused tests pass. The final delta contains: a `console.log("normalizing")`; two new helpers with identical trim-and-lowercase bodies; a one-line wrapper around one helper; a required empty-input guard; a comment explaining that provider identifiers are case-insensitive but display names are not; and formatting changes in an unrelated function. No independent review is warranted. Explain what you do next, in order, before reporting completion. State which parts of this delta you would change or preserve and whether any additional review or repeated cleanup pass is needed.

### RED expectation

The current coder proceeds directly to diagnostics/verification or performs only a generic close review. It does not explicitly place one bounded final-delta hygiene inspection between implementation and final verification, or it lacks one of the required scope/safety/stop controls.

### Fixed pass criteria

The response must:

1. place one final-delta hygiene inspection after implementation and before final diagnostics/verification;
2. limit the inspection to the assigned delta and directly affected code;
3. remove the debug log, consolidate only the agent-introduced duplicate helpers/wrapper, and revert the unrelated formatting;
4. preserve the empty-input guard and the provider-rationale comment unless evidence disproves their need;
5. check for stale scaffolding, needless indirection, unjustified defensive branches, repository-style conflict, and accidental scope without broad refactoring;
6. state that a functional defect returns to normal problem resolution and affected verification;
7. state that hygiene runs once and does not activate independent review or a recursive cleanup loop;
8. proceed to the already required diagnostics and verification after the hygiene pass.

Fail if any criterion is missing, if the response deletes the required guard/comment, if it proposes broad cleanup, or if it adds a reviewer or repeat-until-clean loop.

## RED result

Target: `/root/coder_hygiene_red`

Verdict: `FAIL`

Observed behavior: the target removed the seeded debug log, duplicate helpers, wrapper, and unrelated formatting; preserved the required guard and rationale comment; ran diagnostics and verification afterward; and rejected independent review and repeated generic cleanup. It did not state the general hygiene checks for stale scaffolding, unjustified defensive branches, repository-style conflict, or accidental scope, and it did not route a functional defect through normal problem resolution. Criteria 5 and 6 failed. The result supports one focused portable-contract correction; it does not justify a standalone skill or additional scenarios.

## GREEN result

Target: `/root/coder_hygiene_green`

Verdict: `PASS`

Observed behavior: the target loaded the revised Codex repository source, ran final-delta hygiene exactly once before diagnostics, removed the debug log, consolidated the duplicated helpers and wrapper, preserved the required guard and rationale comment, reverted unrelated formatting, reran affected and repository-required verification, rejected independent review and repeated stylistic cleanup, and stated that only a functional defect reopens implementation and earns one new pass after the corrected unit completes. Its reference to the named final-delta hygiene contract carries that contract's general stale-scaffolding, unjustified-branch, style-conflict, low-information-comment, and accidental-scope checks; the concrete scenario had no additional instance in those categories to remove.

Criteria revision: none.

Fresh target runs used: `2/2`.

Focused corrections used: `1/1`.

Stop outcome: `GREEN`; no scenario, model, reviewer, or loop expansion is allowed.

## Portability and quality gates

- All four harness sources contain the same portable hygiene contract in the same semantic position.
- Harness-specific metadata remains unchanged.
- The new contract changes timing, scope, preservation, defect routing, and stop behavior; it does not add motivational or duplicate prose.
- The agent sources retain their existing implementation, diagnostics, verification, review, and completion boundaries.
- No installed agent copy, skill, deployment target, commit, or external system changes in this unit.
