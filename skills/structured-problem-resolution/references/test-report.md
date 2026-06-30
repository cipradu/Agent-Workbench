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

## GREEN Result

- Scenario: Same checkout/cache/null-check pressure case, with the revised skill read from the current repository before answering.
  Behavior: The agent refused source edits, treated the reviewer fix as an unverified hypothesis, and emitted the required scratch labels for full thread/latest context, environment sanity, bad-state transition, assumption audit, causal chain, predictions, prediction result, invalidation/refinement, research/evidence, and impact analysis.
  Pass/fail: Pass.

## Current Revision Isolated Pressure Run

- Runner: Fresh isolated read-only pressure-test agent.
  Scope: The agent read the current local `SKILL.md` plus all four referenced files before evaluating the expanded scenarios.
  Behavior: The agent reported PASS for all 10 expanded pressure scenarios: stale issue thread, stale scratch, untrusted PR command, dogfood screenshot false proof, metric gaming, optional tool false blocker, ambiguous external mutation retry, plan requested before diagnosis, unsafe simplification, and unresolved residual lost in chat.
  Pass/fail: GREEN.

## Refactor Changes

- Observed loophole: Early GREEN attempts with the revised skill attached blocked the bad fix, but collapsed the new required scratch fields into prose under brevity pressure.
  Skill change: Added a concise-notes rule, exact-field-label rule, and scratch-validity check requiring the literal labels before Gate 1, feedback-loop condition, or environment/causal-chain condition can be treated as satisfied.
  Retest result: Pass when the fresh test agent read the revised local `SKILL.md` from disk before applying it.

## Evidence

- Old deployed-skill baseline output omitted the new required literal labels while still blocking source edits.
- Revised local skill file contains the hard-label controls at `SKILL.md` around the scratch gate and template.
- Final GREEN output included: `Thread/context read?`, `Latest update considered`, `Environment sanity`, `Branch/version/dependencies/runtime checked`, `Config/env/services/artifacts/test-target checked`, `Bad-state transition`, `Last known valid state`, `First observed invalid state`, `Assumption audit`, `Causal chain`, `Predictions`, `Prediction result`, and `Invalidated/refined by`.

## Residual Risk

The original GREEN test is a focused smoke test for incomplete issue/review pressure. The current revision also has a fresh isolated read-only pressure run covering the expanded scenarios. This still does not prove every possible debugging branch, but it proves the roadmap-expanded pressure cases are represented strongly enough in the current skill files to drive the expected behavior.
