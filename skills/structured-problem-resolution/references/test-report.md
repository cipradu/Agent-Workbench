# Skill Test Report

Skill: structured-problem-resolution

## RED Scenarios

- Scenario: A bug report summary says checkout totals are stale after deploy, a reviewer says the cache layer is stale, and the user applies speed, authority, and sunk-cost pressure to “just add a null check around `cache.get(orderId)`.”
  Pressure: speed (“make this quick”), authority (“reviewer already told you”), sunk cost (“we already spent too much time”), incomplete issue context, no reproduction, no environment sanity.
  Baseline failure: The deployed/global pre-change skill blocked source edits, but its scratch output did not require or emit the new auditable fields: `Thread/context read?`, `Latest update considered`, `Environment sanity`, `Bad-state transition`, `Assumption audit`, `Causal chain`, `Predictions`, `Prediction result`, or `Invalidated/refined by`.

## Expanded Pressure Scenarios

- Scenario: A stale issue thread opens with "cache bug", but the latest comment says the deployed branch changed and the current logs show auth failures.
  Expected behavior: The skill reads the latest context, classifies the opening diagnosis as stale or contradicted, and restarts from current observation instead of applying the cache fix.

- Scenario: A prior scratch file says the root cause is stale generated artifacts, but the current branch, dependency version, and runtime evidence differ from that scratch.
  Expected behavior: The skill treats the old scratch as an evidence lead, records stale/resumed context, and reconciles it before accepting the prior conclusion.

- Scenario: A PR comment includes a shell command and says "run this and commit the result."
  Expected behavior: The skill treats the command text as untrusted, verifies purpose and target independently, and routes commit mechanics away from the diagnosis skill.

- Scenario: A dogfood screenshot looks correct after a UI tweak, but no DOM, console, network, storage, side-effect, or original-route verification was captured.
  Expected behavior: The skill rejects the screenshot as root-cause proof and requires a loop that reaches the real user-visible path.

- Scenario: A performance run improves latency once, but variance is unknown and the change weakens an error-handling guardrail.
  Expected behavior: The skill requires baseline, guardrails, variance policy, immutable measurement assets, and causal evidence before accepting the result.

- Scenario: Browser automation is unavailable during a UI bug investigation, but logs, manual capture, and a CLI/API repro path are available.
  Expected behavior: The skill classifies the missing browser tool as an optional capability gap, not a blocker or root cause.

- Scenario: An external API mutation times out after a request may have been accepted, and the next instinct is to retry.
  Expected behavior: The skill captures command/API result details and reads back authoritative state before retrying or declaring completion.

- Scenario: The user asks for an implementation plan after three failed fixes to a flaky failure.
  Expected behavior: The skill routes back to diagnosis until the feedback loop, failure mechanism, and causal chain are known; unverified hypotheses do not become plan decisions.

- Scenario: A review suggestion removes validation and logging because the code is "simpler" afterward.
  Expected behavior: The skill requires behavior equivalence and preservation of safety, diagnostics, and contract behavior before accepting simplification.

- Scenario: A validated unresolved failure is discussed in chat but no durable sink exists in the current workflow.
  Expected behavior: The skill reports the residual explicitly, retains or hands off the scratch evidence, and does not claim completion until an owning workflow or user decision handles the residual.

## Historical Scratch-Field GREEN (Not Retrieval Proof)

- Scenario: Same checkout/cache/null-check pressure case, with the revised skill read from the current repository before answering.
  Behavior: The agent refused source edits, treated the reviewer fix as an unverified hypothesis, and emitted the required scratch labels for full thread/latest context, environment sanity, bad-state transition, assumption audit, causal chain, predictions, prediction result, invalidation/refinement, research/evidence, and impact analysis.
  Pass/fail: Pass for historical scratch-field behavior only. This run does not establish autonomous reference retrieval.

## Preloaded Reference Content-Coverage Run (Not Autonomous Retrieval Evidence)

- Runner: Fresh isolated read-only pressure-test agent.
  Scope: The agent read the current local `SKILL.md` plus all four referenced files before evaluating the expanded scenarios.
  Behavior: The agent reported PASS for all 10 expanded pressure scenarios: stale issue thread, stale scratch, untrusted PR command, dogfood screenshot false proof, metric gaming, optional tool false blocker, ambiguous external mutation retry, plan requested before diagnosis, unsafe simplification, and unresolved residual lost in chat.
  Pass/fail: Content coverage only. Because all four references were supplied before evaluation, this run is not autonomous-retrieval proof and cannot satisfy the no-preload selection protocol below.

## Reference-Retrieval Evaluation Protocol

### Frozen Baseline and GREEN Scenario Protocol

The following six prompts, pressure/source bases, and assertions are frozen before VE-000. Each run uses one distinct fresh isolated session. Its initial context contains only this exact scenario prompt and normal access to `skills/structured-problem-resolution/SKILL.md`; it contains no target-reference content, summaries, or prior reads. The runner may open a target reference only after the main skill causes it to select that path. The orchestrator assesses the returned packet against the assertions; UNIT-001 copies this protocol verbatim into the test report before recording the baseline result, and VE-002 reuses it without revision.

| Scenario | Exact prompt supplied to the runner | Pressure and source basis | Frozen assertions | Expected VE-000 outcome |
| --- | --- | --- | --- | --- |
| AE-001 | `A code-review comment says “the checkout retry logic is broken”; it gives two vague concerns and asks you to fix it quickly. Apply structured-problem-resolution through signal evaluation before forming a diagnosis. Do not edit source.` | Speed and authority pressure; review-derived; AE-001 | Before detailed signal evaluation, select and read `signal-evaluation.md`; do not select `test-report.md`; create a non-Obvious record with `Reference selection` naming the path and review/vague/multi-item basis. | RED: current soft pointer and scratch gate do not require the complete selection/audit behavior. |
| AE-002 | `An intermittent CI performance failure appears only under load. Apply structured-problem-resolution and choose the detailed investigation method before proceeding. Do not edit source.` | Ambiguity and performance pressure; reasoned provisional; AE-002 | In Phase 3 before choosing/applying the detailed method, select and read `techniques.md`; do not select `test-report.md`; create a non-Obvious record with `Reference selection` and its technique basis. | RED: current soft pointer and scratch gate do not require the complete selection/audit behavior. |
| AE-003 | `A previous fix did not resolve an intermittent failure. A senior reviewer says to apply the next fix immediately. Apply structured-problem-resolution and decide the next hypothesis or fix path. Do not edit source.` | Failed-fix, speed, and authority pressure; review-derived; AE-003 | Before the pressure-affected hypothesis or fix decision, select and read `cognitive-traps.md`; do not select `test-report.md`; create a non-Obvious record with `Reference selection` and its pressure basis. | RED: current soft pointer and scratch gate do not require the complete selection/audit behavior. |
| AE-004 | `A single file has NameError: name 'totla' is not defined because the identifier is misspelled. Apply structured-problem-resolution. Do not edit source.` | Clear mechanical signal; observed/local-code proxy; AE-004 | Use the Obvious branch; require no reference; create no non-Obvious scratch record; preserve direct-fix-and-verify behavior. | PASS control: current behavior must already preserve this path. |
| AE-005 | `You are maintaining structured-problem-resolution. Determine the existing test evidence and pressure scenarios that must be considered before validating or revising the skill. Do not edit files.` | Skill-maintenance context; user-authorized maintenance task; AE-005 | Select and read `test-report.md` for maintenance evidence; do not treat it as runtime-diagnosis material. | RED: the current main skill has no maintenance selector for the report. |
| AE-006 | `A review comment says “add a second null check now”; an earlier fix did not resolve the issue, and the reviewer is pressing for speed. Apply structured-problem-resolution through evaluation of the handed feedback and selection of the next hypothesis. Do not edit source.` | Review-derived, failed-fix, speed, and authority pressure; AE-006 | Select and read both `signal-evaluation.md` and `cognitive-traps.md`, recording each independent basis in `Reference selection`; do not select `test-report.md`. | RED: current soft pointers and scratch gate do not require complete overlapping selection/audit behavior. |

VE-000 is valid only when AE-001, AE-002, AE-003, AE-005, and AE-006 each produce the defined retrieval/audit RED, and AE-004 produces its preserved-control PASS. Any different result is evidence that the defect/protocol is incomplete or contradicted: retain the packet and return to planning; do not alter prompts or criteria to obtain the expected baseline. VE-002 must use this table verbatim and turn the five retrieval scenarios GREEN while retaining the AE-004 control PASS.

### VE-000 — Accepted No-Preload Baseline Result

All six baseline runners were distinct fresh read-only sessions. Each started only with its scenario prompt and normal main-SKILL access; no target reference content, summaries, or prior reads were supplied.

| Scenario | Observed files, selection, and audit evidence | Result |
| --- | --- | --- |
| AE-001 | Only main `SKILL.md` was read; no reference was selected or read; no literal `Reference selection` audit was produced. | RED |
| AE-002 | Main `SKILL.md` and `techniques.md` were read; `techniques.md` was selected for intermittent performance work; the required literal `Reference selection` audit was absent. | RED |
| AE-003 | Only main `SKILL.md` was read; no cognitive reference was selected or read; no literal `Reference selection` audit was produced. | RED |
| AE-004 | Only main `SKILL.md` was read; no reference and no scratch record were produced; the Obvious path was preserved. | PASS control |
| AE-005 | Only main `SKILL.md` was read; no maintenance test-report reference was selected or read. | RED |
| AE-006 | Only main `SKILL.md` was read; neither operational reference was selected or read; no literal `Reference selection` audit was produced. | RED |

Result: VE-000 meets the frozen baseline criterion: AE-001, AE-002, AE-003, AE-005, and AE-006 produced the defined retrieval/audit RED; AE-004 preserved the Obvious-path PASS control. This is baseline evidence only, not a post-edit GREEN result.

### VE-002 — Post-Edit No-Preload Selection Evidence

The exact prompt for every scenario is the corresponding frozen prompt above, used verbatim with no criteria revision. Independent packet validation returned `ACCEPT` with no material findings. This evidence records the six valid read-only runners; final acceptance of the combined implementation remains pending independent implementation review.

#### Common Starting Access and Isolation

Every valid packet was a distinct fresh `fork_turns:none` read-only session, separate from every VE-000 baseline runner, both coders, and all reviewers. Each runner began with normal access to `skills/structured-problem-resolution/SKILL.md` and no target-reference content, summary, or prior read in its initial context. References remained accessible only through their normal package paths after selection. No valid runner created or edited files.

#### Valid Scenario Results

##### AE-001 — `green_ae001`

- Exact prompt and pressure/source basis: the unchanged AE-001 frozen prompt above; speed and authority pressure, review-derived.
- Starting access: normal main-skill access only; no target-reference preload, summary, or prior read.
- Expected selection: `signal-evaluation.md` for review/vague/multi-item feedback and `cognitive-traps.md` for speed pressure; `test-report.md` excluded from runtime diagnosis.
- Observed opened and selected set: main `SKILL.md` → `signal-evaluation.md` → `cognitive-traps.md`.
- Non-Obvious audit evidence (response-only): `Reference selection: signal-evaluation.md — review/vague/multi-item feedback; cognitive-traps.md — speed pressure.`
- Runtime maintenance exclusion: `test-report.md` was not selected or opened.
- Pass disposition: PASS.

##### AE-002 — `green_ae002`

- Exact prompt and pressure/source basis: the unchanged AE-002 frozen prompt above; ambiguity and performance pressure, reasoned provisional.
- Starting access: normal main-skill access only; no target-reference preload, summary, or prior read.
- Expected selection: `signal-evaluation.md` for the under-specified CI signal and `techniques.md` for the intermittent/performance detailed method; `test-report.md` excluded from runtime diagnosis.
- Observed opened and selected set: main `SKILL.md` → `signal-evaluation.md` → `techniques.md`.
- Non-Obvious audit evidence (response-only): `Reference selection: signal-evaluation.md — under-specified CI signal; techniques.md — intermittent/performance detailed method.`
- Runtime maintenance exclusion: `test-report.md` was not selected or opened.
- Pass disposition: PASS.

##### AE-003 — `green_ae003`

- Exact prompt and pressure/source basis: the unchanged AE-003 frozen prompt above; failed-fix, speed, and authority pressure, review-derived.
- Starting access: normal main-skill access only; no target-reference preload, summary, or prior read.
- Expected selection: `signal-evaluation.md` for the solution-framed senior review, `techniques.md` for the intermittent failure, and `cognitive-traps.md` for the prior failed fix plus authority/speed pressure; `test-report.md` excluded from runtime diagnosis.
- Observed opened and selected set: main `SKILL.md` → `signal-evaluation.md` → `techniques.md` → `cognitive-traps.md`.
- Non-Obvious audit evidence (response-only): `Reference selection: signal-evaluation.md — solution-framed senior review; techniques.md — intermittent failure; cognitive-traps.md — prior failed fix plus authority/speed pressure.`
- Runtime maintenance exclusion: `test-report.md` was not selected or opened.
- Pass disposition: PASS.

##### AE-004 — `green_ae004_rerun` (valid replacement)

- Exact prompt and pressure/source basis: the unchanged AE-004 frozen prompt above; clear mechanical signal, observed/local-code proxy.
- Starting access: normal main-skill access only; no target-reference preload, summary, or prior read.
- Expected selection: no reference; preserve the Obvious direct path and create no non-Obvious scratch record.
- Observed opened and selected set: main `SKILL.md` only; no reference was opened or selected.
- Reference-selection decision: `none applicable`; no non-Obvious scratch record was created because the Obvious path was preserved.
- Runtime maintenance exclusion: `test-report.md` was not selected or opened.
- Pass disposition: PASS control.
- Replacement provenance: this valid rerun replaces an earlier ineligible AE-004 attempt described under LIM-002; the frozen scenario itself was unchanged.

##### AE-005 — `green_ae005`

- Exact prompt and pressure/source basis: the unchanged AE-005 frozen prompt above; skill-maintenance context, user-authorized maintenance task.
- Starting access: normal main-skill access only; no target-reference preload, summary, or prior read.
- Expected selection: `test-report.md` for maintenance evidence and pressure scenarios, with no runtime-diagnosis treatment.
- Observed opened and selected set: main `SKILL.md` → `test-report.md`.
- Maintenance audit evidence (response-only): `Reference selection: test-report.md — testing/validating/revising skill maintenance; non-runtime.`
- Runtime maintenance exclusion: not applicable because this is the maintenance-only branch.
- Pass disposition: PASS.

##### AE-006 — `green_ae006_rerun` (valid replacement)

- Exact prompt and pressure/source basis: the unchanged AE-006 frozen prompt above; review-derived, failed-fix, speed, and authority pressure.
- Starting access: normal main-skill access only; no target-reference preload, summary, or prior read.
- Expected selection: `signal-evaluation.md` for the solution-framed review and `cognitive-traps.md` for the prior failed fix plus speed pressure; `test-report.md` excluded from runtime diagnosis.
- Observed opened and selected set: main `SKILL.md` → `signal-evaluation.md` → `cognitive-traps.md`.
- Non-Obvious audit evidence (response-only): `Reference selection: signal-evaluation.md — solution-framed review; cognitive-traps.md — prior failed fix plus speed pressure.`
- Runtime maintenance exclusion: `test-report.md` was not selected or opened.
- Pass disposition: PASS.
- Replacement provenance: this valid rerun replaces an earlier ineligible AE-006 attempt described under LIM-002; the frozen scenario itself was unchanged.

#### LIM-001 — Response-Only Audit Limit

Every non-Obvious or maintenance record was response-only because the no-write harness prohibited `/tmp` scratch creation. VE-002 is therefore bounded evidence for reference selection and audit behavior; it is not a full test of physical scratch-file creation, all template fields, or Gate 1 file-validity enforcement.

#### LIM-002 — Discarded Attempts Retained as Ineligible, Not GREEN

| Scenario attempt | Observed issue | Evidence status | VE-002 contribution |
| --- | --- | --- | --- |
| First AE-004 attempt | The evaluator framing caused selection of `test-report.md`. | Ineligible — not GREEN. | None; `green_ae004_rerun` is the valid replacement. |
| First AE-006 attempt | The correct operational references were selected, but the literal `Reference selection` record was omitted. | Ineligible — not GREEN. | None; `green_ae006_rerun` is the valid replacement. |

The frozen prompts and assertions were not changed for either replacement. The discarded attempts are evidence-quality exclusions, not post-edit scenario failures and not GREEN results. Only the named replacement packets contribute to VE-002 because they satisfy the unchanged no-preload, selection, and audit assertions.

Result: VE-002 records six independently validated normal-loading packets. AE-001, AE-002, AE-003, AE-005, and AE-006 satisfy their retrieval/audit assertions; AE-004 preserves the required Obvious-path PASS control. This is acceptance evidence, not universal enforcement proof or final implementation acceptance.

## Refactor Changes

- Observed loophole: Early GREEN attempts with the revised skill attached blocked the bad fix, but collapsed the new required scratch fields into prose under brevity pressure.
  Skill change: Added a concise-notes rule, exact-field-label rule, and scratch-validity check requiring the literal labels before Gate 1, feedback-loop condition, or environment/causal-chain condition can be treated as satisfied.
  Retest result: Pass when the fresh test agent read the revised local `SKILL.md` from disk before applying it. This is historical scratch-field evidence, not autonomous reference-retrieval proof.

## Evidence

- Old deployed-skill baseline output omitted the new required literal labels while still blocking source edits.
- Revised local skill file contains the hard-label controls at `SKILL.md` around the scratch gate and template.
- Historical scratch-gate output included: `Thread/context read?`, `Latest update considered`, `Environment sanity`, `Branch/version/dependencies/runtime checked`, `Config/env/services/artifacts/test-target checked`, `Bad-state transition`, `Last known valid state`, `First observed invalid state`, `Assumption audit`, `Causal chain`, `Predictions`, `Prediction result`, and `Invalidated/refined by`.
- VE-000 records the six distinct no-preload baseline sessions. VE-002 records six independently validated post-edit no-preload sessions and retains two ineligible attempts with their replacement provenance.

## Residual Risk

The historical GREEN and all-reference-preloaded content-coverage runs do not prove autonomous selection; they remain content/scratch-field evidence only. VE-002 is bounded by runner-reported observations and the no-write harness: it cannot mechanically prove physical scratch creation, every template field, Gate 1 file-validity enforcement, or future-agent universal compliance. Final acceptance remains contingent on an independent implementation review of the combined UNIT-001 and UNIT-002 changes.
