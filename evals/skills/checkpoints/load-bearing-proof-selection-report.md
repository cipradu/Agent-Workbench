# Load-Bearing Proof Selection Report

Status: `PASS`

## Decision Claim

The existing search, diagnosis, and testing owners must identify the one or two safety facts that carry acceptance, preserve the bounded evidence scope, and stop at the lowest proof level that can decide each fact. Source evidence must not be presented as runtime proof. Executable or live proof must not be added when bounded source or unreachability evidence already settles the claim.

## Evaluation Contract

- Source basis: `docs/skill-analysis/cursor-plugins-exhaustive-skill-analysis.md`, Step 2.
- Scenario count: three materially distinct owner cases and no additional convenience cases.
- Maximum fresh RED runs: three, one per owner.
- GREEN runs: only for owners that fail RED, one rerun per changed owner.
- Focused correction maximum: one per failing owner.
- Reviewers: none by default.
- Completion reserve: retain enough context and time to apply and verify one focused correction per failing owner and complete the aggregate Unit 2 gate.
- Optional-evidence downshift order: model comparison, additional target, extra scenario, independent review.
- Expansion trigger: only a new result that changes the causal hypothesis or exposes a distinct consequential owner boundary.
- PASS stop: the target meets every criterion for its scenario without evaluator data.
- CORRECT stop: a target blocks because the prompt lacks a fact that is genuinely required and cannot be discovered from the allowed context.
- FAIL stop: one or more fixed criteria fail.
- INFRASTRUCTURE stop: the target cannot load the named runtime skill or inspect the permitted repository source; the run does not count as behavior evidence.

## Target Context Boundary

Each target receives normal harness and repository instructions, the named runtime skill entry point, the scenario prompt, and ordinary read-only repository access. It receives no evaluator assets, expected behavior, pass/fail criteria, prior target output, or report summary. It must not edit files, dispatch another agent, or read any path under `evals/`.

## Scenario LBP-SEARCH-01 — Bounded Absence Handoff

Owner: `codebase-search`

Source label: `provisional external-pattern gap`

Prompt:

```text
Apply codebase-search to this impact-analysis handoff. Do not edit files.

We plan to remove a compatibility branch in a parser. The acceptance decision depends on this claim: no in-repository caller can pass `legacy_mode=true` to `parse_config`. Current source inspection has found the only definition, its direct callers, a string-key configuration registry, and one reflective dispatcher. The exact search covered tracked source and tests, but excluded generated artifacts and external consumers. The direct callers pass `false`; the registry has no `legacy_mode` entry; the reflective dispatcher resolves names from runtime plugin metadata that is not present in the repository.

State what the current repository evidence proves, what it does not prove, and the smallest handoff needed before the branch can be removed safely. Keep the answer bounded to this claim.
```

Required behavior:

- Names the load-bearing claim and the bad case that would invalidate it.
- Records the searched boundary and exclusions.
- Uses the strongest supportable search proof label; it does not call the claim globally absent or runtime-proven.
- Distinguishes the source-settled direct-caller path from the unresolved reflective metadata path.
- Hands off only the unresolved observer or evidence need instead of requesting a full repository test suite or live end-to-end reproduction by default.

Target: `/root/lbp_search_red`

Source identity: `5eafc84a347bda969011528aa68513097c1d726637a6a4ddaab6a39a9e7ada75`

Observed result: The target labeled the overall absence claim `not proven absent`, bounded the evidence to tracked source and tests, separated the verified direct callers and registry miss from unresolved reflective metadata, and requested only the authoritative runtime plugin-metadata set plus argument trace.

Verdict: `PASS`

## Scenario LBP-DIAG-01 — Cheapest Decisive Proof Ladder

Owner: `structured-problem-resolution`

Source label: `provisional external-pattern gap`

Prompt:

```text
Apply structured-problem-resolution to choose verification for this already diagnosed, bounded correction. Do not edit files.

Root cause: `normalize_options` retains a deprecated fallback when `mode` is absent. The proposed fix removes that fallback. Impact search found two acceptance-critical facts. First, every in-repository caller supplies `mode`, and the bounded exact search covered tracked source, tests, configuration registries, and generated call sites with no unresolved dynamic dispatch. Second, the CLI adapter forwards its parsed `--mode` value through a runtime registration table, so source inspection confirms the wiring shape but cannot prove the registered path executes with the intended value.

Choose the proof needed for each fact and state where verification stops. The repository has a focused CLI integration test seam. No repository policy requires the full suite for this bounded change.
```

Required behavior:

- Names no more than the two supplied load-bearing claims and the bad case for each.
- Stops the first claim at bounded source or unreachability proof.
- Escalates the second claim only to the focused CLI integration seam because source inspection leaves runtime registration unresolved.
- Does not require a full suite, live manual reproduction, reviewer, or repeated proof after each claim is decided.
- States the unresolved question that justifies the second claim's escalation.

Target: `/root/lbp_diag_red`

Source identity: `8797488c96a12ba463ddd9beb5194ce25b30291e98d467ec1bbd0d30d37a2880`

Observed result: The target correctly stopped the closed caller claim at bounded exact search, escalated the dynamic registry claim to one focused CLI integration test, and rejected the full suite. It did not preserve the supplied facts as an explicit load-bearing claim → bad case → proof-level handoff. It introduced the ordinary `normalize_options` regression check as a third peer claim instead of separating direct fix verification from the safety claims that justify removal.

Verdict: `FAIL`

## Scenario LBP-TEST-01 — No Redundant Executable Proof

Owner: `testing-strategy`

Source label: `provisional external-pattern gap`

Prompt:

```text
Apply testing-strategy to decide whether more tests are needed for two acceptance claims. Do not edit files.

Claim A is an absence claim. A current exhaustive-in-scope search covered tracked source, tests, registries, generated call sites, and configuration, recorded all exclusions, and proved that no in-repository path can supply the removed enum value. There is no external compatibility promise for that value.

Claim B concerns a dynamically registered CLI adapter. Current source proves registration and value forwarding, but not that the real registry selects the adapter. A focused integration test can invoke the public CLI entry point with the real registry. The full test suite and a live manual run observe no additional behavior relevant to either claim.

Choose the evidence for each claim and explain the stop point.
```

Required behavior:

- Accepts the bounded search evidence as decisive for Claim A and does not add a performative test.
- Selects the focused public-entry integration seam for Claim B.
- Rejects the full suite and live manual run because they add no relevant observation.
- Distinguishes source proof from executable proof and states the residual boundary of each.

Target: `/root/lbp_test_red`

Source identity: `177c964438a556aa47f54acee9c6887a5cfa5b9f3374c2e0bd36406cbd557ba5`

Observed result: The target accepted exhaustive bounded source evidence for Claim A, selected the public CLI entry point with the real registry for Claim B, and rejected both the full suite and live manual run because they add no relevant observation.

Verdict: `PASS`

## Focused Revision Design Brief

Entry mode: existing-skill revision.

Target owner: `structured-problem-resolution`.

Recurring behavior failure: Impact analysis can list a broad blast radius and verification can still choose proportional tests, but the diagnosis handoff does not explicitly preserve which one or two safety facts carry acceptance, the bad case for each, and why a proof level is sufficient. Under pressure, direct fix verification can be mixed with those safety premises, which makes later escalation harder to audit and easier to broaden by habit.

Desired behavior: During impact analysis, identify at most one or two load-bearing safety claims when the correction depends on them. Record the invalidating bad case, the bounded evidence scope for an absence or unreachability claim, and the lowest proof level that can decide it. Verification still covers the original symptom and changed behavior; it separately climbs each safety claim only while an unresolved question remains.

Owner and mechanism decision: Revise the existing diagnosis owner. Search already supplies bounded source and absence evidence. Testing already chooses the right executable observer and stop point. A new skill, shared prose duplicate, script, reviewer, or broad workflow gate would add ownership and cost without fixing the observed handoff gap.

Skill type: Preserve the current discipline/process hybrid. Add one compact impact-analysis decision rule, one proof ladder in verification, and small packet/template fields. Do not change invocation, reference routing, classification, scratch lifecycle, or downstream ownership.

Information placement:

- Phase 4 owns claim identification, bad-case definition, boundary, and provisional lowest proof level.
- Phase 5 owns proof escalation and the stop at the lowest decisive level.
- The Simple packet and Complex scratch template retain the handoff without creating a separate artifact.
- No operational reference changes are needed because the rule applies to every diagnosis branch and is short enough for the main skill.

Failure output: If a proposed correction depends on an unresolved safety claim, do not call the impact gate complete. Name the claim, invalidating bad case, current evidence boundary, and next proof needed.

GREEN criteria: The unchanged `LBP-DIAG-01` scenario must separate ordinary regression verification from exactly the two supplied safety claims, name the invalidating bad case for each, stop the first at bounded source/unreachability evidence, escalate the second only to the focused CLI integration seam, and reject broader or live proof.

## Run Ledger

| Scenario | Source identity | Target identity | Result | Correction | GREEN identity |
| --- | --- | --- | --- | --- | --- |
| `LBP-SEARCH-01` | `5eafc84a...` | `/root/lbp_search_red` | `PASS` | none | not needed |
| `LBP-DIAG-01` | `8797488c...` | `/root/lbp_diag_red` | `FAIL` | one focused diagnosis-owner correction | `/root/lbp_diag_green`; `45b30bd...`; `PASS` |
| `LBP-TEST-01` | `177c9644...` | `/root/lbp_test_red` | `PASS` | none | not needed |

## Unit Verdict

`PASS`

The unchanged GREEN target separated the ordinary correction check from exactly two load-bearing claims. It stopped the closed caller claim at bounded bad-case unreachability, escalated the runtime-registration claim only to the focused CLI integration seam, named the unresolved runtime-selection question, and rejected the full suite and live reproduction.

Fresh runs: `4/4` maximum used: three RED targets and one GREEN rerun for the only failing owner.

Focused corrections: `1/1` maximum used for the failing owner.

Review count: `0`.

Intentionally unchanged owners: `codebase-search` and `testing-strategy`; both passed their frozen RED cases, so changing them would add duplicate policy without evidence.
