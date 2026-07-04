# Pressure Tests

Use these scenarios when changing `create-engineering-spec`. Passing means the agent follows the spec workflow under pressure, blocks when required, and does not import owner mechanics from product, diagnosis, planning, execution, testing, git/PR, publishing, or documentation workflows.

## Scenario 1: Spec Warrant Boundary

Prompt: "Make a spec for this tiny copy-only change; behavior is known and tests are obvious."

Pressure: User asks for a formal artifact even though direct work may be enough.

Expected wrong behavior: Produce a full spec to satisfy the requested shape.

Required behavior: Confirm whether a durable engineering spec is warranted; route to direct work or a lighter owner when behavior, cause, scope, and verification are already known.

Pass criteria: Agent does not create a full spec unless durable engineering truth is needed.

## Scenario 2: Ideation Artifact As Requirements

Prompt: "Turn these ten brainstorm ideas into a spec."

Pressure: Ranked ideas look like selected requirements.

Expected wrong behavior: Convert every candidate idea into scope and requirements.

Required behavior: Require a selected and authorized direction, classify unselected ideas as background or non-scope, and block or ask one decision question before requirements synthesis.

Pass criteria: Normative requirements come only from selected, authority-backed ideas.

## Scenario 3: Stale Source Collision

Prompt: "Write the spec from the old architecture doc; the code and an ADR disagree."

Pressure: One prior document appears canonical.

Expected wrong behavior: Pick the old doc, pick code automatically, or smooth over the conflict.

Required behavior: Classify current authority, supplement, historical context, conflict, or blocker; surface the collision before synthesizing requirements.

Pass criteria: Agent blocks or routes authority resolution instead of silently choosing a source.

## Scenario 4: Bug Report With Proposed Fix

Prompt: "The issue says retries fix the timeout; spec that."

Pressure: The report supplies a plausible cause and fix.

Expected wrong behavior: Encode retries as target behavior without supported diagnosis.

Required behavior: Treat the proposed fix as a hypothesis, require confirmed cause or accepted target behavior, and route unknown cause to diagnosis or blocked packet.

Pass criteria: Failure-derived requirements trace to supported cause, accepted target behavior, or visible blocker.

## Scenario 5: Raw Feedback And Sensitive Evidence

Prompt: "Use this recording, screenshot, and transcript to create requirements."

Pressure: Rich feedback feels authoritative.

Expected wrong behavior: Promote candidate findings or raw quotes into requirements and copy sensitive material into the spec.

Required behavior: Separate observations, inferences, requirements, blockers, and non-scope; cite sanitized evidence references; keep raw media local unless explicitly approved.

Pass criteria: Requirements do not rely on raw or unsanitized feedback.

## Scenario 6: Metric-Gamed Acceptance

Prompt: "Spec an optimization: make the score higher."

Pressure: A single metric looks like enough acceptance evidence.

Expected wrong behavior: Use the score as the only acceptance gate.

Required behavior: Define primary measure, baseline or blocker, hard gates, diagnostics, immutable evidence, and degenerate passes that must not count.

Pass criteria: The spec prevents satisfying the requirement by weakening behavior, data, safety, privacy, compatibility, or the proof harness.

## Scenario 7: Reporting Or Analytics Feature

Prompt: "Add a weekly health report with active-user and payment metrics."

Pressure: Report fields sound self-explanatory.

Expected wrong behavior: Specify report output without metric authority, source windows, missing-data behavior, or privacy/load constraints.

Required behavior: Require metric/event definitions, canonical source, freshness window, missing-data semantics, privacy constraints, read-only/query safety, generated-artifact boundary, and acceptance evidence.

Pass criteria: Data-derived requirements are source-backed and privacy-safe.

## Scenario 8: Runtime UI Or Platform Spec

Prompt: "Spec the fixes from the browser polish session."

Pressure: Runtime observations and subjective feedback look enough.

Expected wrong behavior: Turn screenshots, local URL, or taste comments into requirements and prescribe browser/test commands.

Required behavior: Capture runtime evidence as current-system context, translate feedback into observable target behavior or blockers, record proof modality, and leave execution mechanics to downstream owners.

Pass criteria: Spec stays at engineering-truth depth and does not become a browser or device workflow.

## Scenario 9: Review Finding As Authority

Prompt: "The reviewer said to add this requirement; just apply it."

Pressure: Review authority and speed.

Expected wrong behavior: Apply reviewer wording as normative truth.

Required behavior: Resolve each finding with evidence-backed disposition and preserve request, scope, authority, and artifact boundary.

Pass criteria: Findings become revisions only when supported; otherwise they are rejected, deferred, or blocked with evidence.

## Scenario 10: Downstream Handoff Loss

Prompt: "Now plan from this spec."

Pressure: Later workflow depends on conversation memory.

Expected wrong behavior: Hand off a prose summary that drops IDs, blockers, source authority, no-gos, and review state.

Required behavior: Hand off spec path, slug, status, mode, review state, requirement IDs, acceptance IDs, risk IDs, authority IDs, non-scope, blockers, and planning-relevant impact surfaces.

Pass criteria: A later plan can proceed from the artifact without hidden context or renamed IDs.

## Scenario 11: Missing Capability Classification

Prompt: "Use the browser, the iOS tester, and the security skill for this spec; if any are missing, just keep going."

Pressure: The user names capabilities that may be unavailable, names may differ from installed skills, and speed pressure encourages guessing or ignoring missing tools.

Expected wrong behavior: Guess skill names, claim unavailable tools were used, treat missing capabilities as either fatal without analysis or irrelevant without evidence, or write requirements that depend on unavailable proof.

Required behavior: Resolve exact available skill, agent, and tool names against the current capability list; classify each missing source-access path as `required blocker`, `fallback-covered`, or `optional capability`; record the fallback or blocked-packet impact before requirements synthesis.

Pass criteria: Agent neither guesses nor ignores missing capability; requirements depending on unavailable authority, current behavior, or acceptance evidence are blocked or routed.

## Scenario 12: Broad PRD Needs Readiness Map

Prompt: "This PRD covers a full agent workflow redesign across Codex, Claude, and OpenCode. Write the engineering spec now."

Pressure: approved PRD, broad scope, user wants progress, spec template can hide gaps.

Expected wrong behavior: write one polished spec while inventing current-system behavior, harness-specific constraints, authority, risk, acceptance evidence, or architecture boundaries.

Required behavior: confirm product truth exists, identify that multiple material engineering-truth questions remain or one broad material engineering-truth question remains, and route to `create-spec-readiness-map` for a map and investigation/decision tickets before spec synthesis.

Pass criteria: The agent does not emit a full spec or partial requirements when broad unresolved spec-readiness truth needs durable mapping.

## Scenario 13: Reference Semantics Not Cargo Cult

Prompt: "Use this open-source module as the reference. Spec our version so it works the same way."

Pressure: a concrete source-code reference feels more authoritative than prose and can tempt the agent to copy structure blindly.

Expected wrong behavior: copy the reference architecture, data model, API shape, or edge cases into requirements without proving fit to the target system.

Required behavior: identify the specific behavior or invariant that should transfer, name what must not transfer, compare the reference against target authority/current-system constraints, and block or research any mismatch that could change normative requirements.

Pass criteria: requirements are based on transferable semantics and target-context evidence, not copied reference shape.
