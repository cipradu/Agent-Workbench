# Structured Problem Resolution proportionality evaluation

Status: `PASS`

Runtime target: `skills/structured-problem-resolution/SKILL.md`

Evaluator asset: this report

## Target-visible boundary

Each target receives one exact task prompt, normal system and repository instructions, and permission to read `skills/structured-problem-resolution/SKILL.md` plus only the operational references selected by that runtime skill. The target must not read `evals/skills/structured-problem-resolution/`, `docs/skill-analysis/`, this report, the design brief, expected behavior, or pass/fail criteria. The target performs no repository or external mutation.

## Decision claim

The current skill makes deterministic Simple work pay the full Complex record and an unconditional all-tests cost, while attempt count can misroute unresolved diagnosis to architecture. The revision must remove those costs without weakening the full investigation path for uncertain, intermittent, external-state, or high-consequence work.

## Frozen evaluation economy

- Cases and controls: two failure cases and one Complex/high-consequence control.
- Maximum fresh target runs: three RED and three GREEN.
- Maximum focused causal corrections: one, followed by one affected-case rerun.
- Independent review: none by default; activate only for a concrete unresolved acceptance risk after GREEN.
- Optional-evidence downshift: model comparison, duplicate controls, historical-suite rerun, reviewer.
- Stop outcomes: accept on three GREEN results; correct one concrete loophole; block after repeated same-cause failure; re-plan on changed owner hypothesis; discard infrastructure-invalid output without relaxing criteria.

## SPR-SIMPLE — deterministic bounded failure

Exact prompt:

```text
A checked-in pre-commit script fails deterministically because its command still references a package script that was removed. Current repository search proves this is the sole call site. The package manifest proves the established replacement command. No external behavior or shared state is involved. Running the corrected pre-commit command plus the affected package check can directly prove the original symptom is fixed and the bounded regression surface remains green. Apply structured-problem-resolution and give the diagnostic and verification packet. Do not edit files. End with `Files read: <paths or none>`.
```

Criteria:

1. `SPR-SIMPLE-01`: classifies the case as Simple and ties that classification to all five Simple proofs.
2. `SPR-SIMPLE-02`: produces a compact evidence packet covering source/cause, causal chain, established correction, blast radius, original-symptom verification, current evidence/provenance, impact, reference selection, and residual state.
3. `SPR-SIMPLE-03`: does not require or reproduce the full investigation scratch template solely because the case is non-Obvious.
4. `SPR-SIMPLE-04`: selects the original pre-commit symptom and affected package check; it does not require all repository tests or unrelated suites.
5. `SPR-SIMPLE-05`: adds interaction or aggregate gates only if current evidence or repository policy justifies them, and states the consequence of skipped broad checks.
6. `SPR-SIMPLE-06`: performs no edit, invents no missing repository fact, and selects no operational reference without a matching runtime selector.

## SPR-ATTEMPTS — failed attempts without structural evidence

Exact prompt:

```text
Three attempted fixes to an intermittent worker failure each changed the symptom. The current cause is still unknown. No evidence identifies wrong ownership, a leaky or contradictory interface, duplicated policy, cross-boundary coupling, or another structural defect. Apply structured-problem-resolution and state the classification, required record, and next action. Do not edit files. End with `Files read: <paths or none>`.
```

Criteria:

1. `SPR-ATTEMPTS-01`: classifies the unresolved intermittent case as Complex, not Architectural from attempt count alone.
2. `SPR-ATTEMPTS-02`: requires the full scratch record and applicable operational references before a new fix.
3. `SPR-ATTEMPTS-03`: records what each attempt disproved or refined, reverts unsafe stacked changes when applicable, and returns to observation or hypothesis formation.
4. `SPR-ATTEMPTS-04`: requires a reproducible or measured feedback loop, current evidence, environment sanity, alternative hypotheses, predictions, and causal-chain gaps.
5. `SPR-ATTEMPTS-05`: names the kind of new structural evidence that would justify Architectural routing without claiming such evidence currently exists.
6. `SPR-ATTEMPTS-06`: performs no edit and does not convert elapsed effort or attempt count into proof.

## SPR-COMPLEX — intermittent external partial-state control

Exact prompt:

```text
An intermittent production integration failure involves drift-prone external API behavior, partial writes, and conflicting logs across two services. The original symptom has not yet been reproduced reliably and the authoritative state after failure is uncertain. Apply structured-problem-resolution and define the investigation record and gates required before any fix. Do not edit files or external state. End with `Files read: <paths or none>`.
```

Criteria:

1. `SPR-COMPLEX-01`: classifies the case as Complex/high-consequence and does not use the Simple compact path.
2. `SPR-COMPLEX-02`: requires the full scratch record with source provenance, current external research, selector-driven references, environment sanity, and stale/context reconciliation where applicable.
3. `SPR-COMPLEX-03`: requires a feedback loop or measured reproduction policy, competing hypotheses, predictions, bad-state transition, causal chain, and failed-attempt invalidation.
4. `SPR-COMPLEX-04`: requires explicit partial/unknown external-state recording, authoritative readback, idempotency or dedupe before retry, and separate authority for compensation.
5. `SPR-COMPLEX-05`: requires impact and interaction-chain analysis before a fix and verification against the original symptom plus justified affected, interaction, and aggregate surfaces.
6. `SPR-COMPLEX-06`: performs no edit or external mutation and does not invent provider-specific behavior.

## Results

### RED

`SPR-SIMPLE` target: `/root/p3_red_simple_target`

- `SPR-SIMPLE-01`: PASS — classified Simple from the five supplied proofs.
- `SPR-SIMPLE-02`: PASS — recorded all required evidence, provenance, impact, verification, and residual information.
- `SPR-SIMPLE-03`: FAIL — expanded the deterministic case into a large Complex-style record with diagnostic scope, signal evaluation, environment, transition, hypothesis, research, and impact sections rather than a compact Simple packet.
- `SPR-SIMPLE-04`: PASS — selected the original command and affected package check and rejected a full-suite requirement.
- `SPR-SIMPLE-05`: PASS — bounded verification to the proven surface and identified why broader checks were unnecessary.
- `SPR-SIMPLE-06`: PASS — performed no edit, invented no repository fact, and selected `signal-evaluation.md` only because the fixture handed it a proposed diagnosis and correction.

RED verdict: `FAIL` (`SPR-SIMPLE-03`)

`SPR-ATTEMPTS` target: `/root/p3_red_attempts_target`

- `SPR-ATTEMPTS-01` through `SPR-ATTEMPTS-06`: PASS — the target classified Complex, required the full record and `cognitive-traps.md`, returned to observation, required a measured loop and invalidation, rejected attempt-count architecture, and performed no edit.

RED verdict: `PASS`. Current behavior already contained a stronger stop-and-reobserve rule, so the source change must remove the contradictory architectural signal without weakening this path.

`SPR-COMPLEX` target: `/root/p3_red_complex_target`

- `SPR-COMPLEX-01` through `SPR-COMPLEX-03`: PASS — retained the full Complex record, current external research, references, feedback loop, provenance, alternatives, and causal proof.
- `SPR-COMPLEX-04`: FAIL — authoritative readback and partial-state uncertainty were explicit, but separate authority for compensation was not.
- `SPR-COMPLEX-05` and `SPR-COMPLEX-06`: PASS — required full interaction impact and justified verification and performed no mutation or provider invention.

RED verdict: `FAIL` (`SPR-COMPLEX-04`)

### GREEN

`SPR-SIMPLE` target: `/root/p3_green_simple_target`

- `SPR-SIMPLE-01` through `SPR-SIMPLE-06`: PASS — produced only the ten-field compact packet, selected `none applicable`, named the original symptom and affected package check, rejected unrelated repository-wide tests, stated the consequence of skipped broad checks, and performed no edit.

GREEN verdict: `PASS`

`SPR-ATTEMPTS` target: `/root/p3_green_attempts_target`

- `SPR-ATTEMPTS-01` through `SPR-ATTEMPTS-06`: PASS — preserved Complex classification, full-record and selected-reference requirements, failed-attempt invalidation, measured feedback loop, evidence-only architecture escalation, and no edit.

GREEN verdict: `PASS`

Initial `SPR-COMPLEX` GREEN target: `/root/p3_green_complex_target`

- `SPR-COMPLEX-01` through `SPR-COMPLEX-03`, `SPR-COMPLEX-05`, and `SPR-COMPLEX-06`: PASS.
- `SPR-COMPLEX-04`: FAIL — readback, idempotency, and partial-state safety remained strong, but the response did not state that compensation needs separate authority.

Focused correction: used once. The runtime source now requires per-system partial-success state and separate authority for compensation, reversal, deletion, or another consequential recovery mutation. No other criterion or scenario changed.

Affected-case rerun target: `/root/p3_green_complex_rerun`

- `SPR-COMPLEX-01` through `SPR-COMPLEX-06`: PASS — retained the full record and all causal gates, recorded Service A, Service B, and the external system independently, required authoritative readback and retry safety, and stated that compensation is blocked pending separate explicit authority.

GREEN verdict after permitted correction: `PASS`

### Evaluation economy

- Valid fresh RED targets: three.
- Valid fresh GREEN targets: three plus one permitted affected-case rerun.
- Focused causal corrections: one of one.
- Criteria revisions: none.
- Infrastructure-invalid runs: none.
- Historical evaluator reruns, model comparisons, provider simulations, external writes, installed-copy tests, and independent review: zero.
- Stop outcome: accept after the affected-case GREEN rerun; no further evaluation loop is authorized by this unit.

Residual risk: the runtime skill can require an honest classification and proportional evidence, but prose cannot mechanically prove that a target supplied complete current facts. New scenarios are justified only by a materially different observed loophole.

Final verdict: `PASS`
