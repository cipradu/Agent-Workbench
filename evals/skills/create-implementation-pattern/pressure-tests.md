# Create Implementation Pattern Pressure Tests

Use these tests to validate the skill behavior or a draft pattern. Passing means the agent avoids junk pattern creation while still capturing reusable project knowledge when the evidence is strong.

## Test 1: Single Clean Implementation

Prompt: "We implemented one clean adapter for the billing API. Create a pattern for it."

Expected failure mode: Create a full accepted pattern because the code looks nice.

Required behavior: Check recurrence and mandate. If there is only one example and no approved mandate, produce a candidate note or explain why no pattern should be created.

Pass condition: The answer refuses full pattern status and states what evidence would promote the candidate.

## Test 2: ADR Confusion

Prompt: "We decided to use repository adapters. Write the pattern."

Expected failure mode: Replace the ADR with pattern guidance or duplicate the ADR.

Required behavior: Determine whether the decision itself needs an ADR, whether a pattern already exists, and whether future implementers need application guidance. Split decision record from implementation pattern when both are needed.

Pass condition: The answer clearly separates "why we chose this" from "how to apply this repeatedly."

## Test 3: Famous Pattern Cargo Cult

Prompt: "Use the Strategy pattern across all validators because that is a best practice."

Expected failure mode: Accept the catalog name as sufficient proof.

Required behavior: Ask what recurring project problem exists, what forces require strategy objects, what simpler alternatives fail, and where local examples prove the need.

Pass condition: The answer rejects or holds as candidate unless local forces and examples justify the pattern.

## Test 4: Review Signal After Implementation

Prompt: "The reviewer noticed we now have three endpoints using the same idempotency-key flow and asked if it should be documented."

Expected failure mode: Treat this as optional and skip capture, or create vague docs with no boundaries.

Required behavior: Run the full pattern-worthiness check. Three matching examples are a strong signal, but the pattern still needs context, forces, non-use cases, invariants, examples, and relationship to API/error-handling guidance.

Pass condition: The answer either creates an accepted pattern or updates an existing one with concrete evidence and non-use cases.

## Test 5: Missing Non-Use Cases

Prompt: "Document our background job retry pattern. Just keep it positive."

Expected failure mode: Omit boundaries and create overbroad guidance.

Required behavior: Refuse to finalize without when-not-to-use, trade-offs, and misuse signals.

Pass condition: The pattern explains when retries are unsafe, when idempotency is required, when human intervention is needed, and when failures should not be retried.

## Test 6: Similar Code, Different Forces

Prompt: "These three modules all parse input. Make one parsing pattern."

Expected failure mode: Abstract coincidental similarity.

Required behavior: Compare source trust, failure behavior, schema stability, ownership, runtime constraints, and downstream effects. If forces differ, reject one shared pattern or split into narrower patterns.

Pass condition: The answer does not create a broad parsing pattern unless the underlying forces match.

## Test 7: Reviewer Signal Inflation

Prompt: "The reviewer said this looks like our new pattern. Add it as accepted guidance."

Expected failure mode: Treat the reviewer comment as authority and create an accepted pattern.

Required behavior: Treat the review as a signal, capture the source evidence, classify confidence, verify recurrence or mandate, and choose accepted, candidate, update existing, rejection, or blocked based on evidence.

Pass condition: Reviewer opinion alone cannot support accepted/proven status.

## Test 8: Stale Accepted Pattern

Prompt: "Use the accepted adapter pattern from docs; do not re-check it."

Expected failure mode: Apply old guidance without checking whether examples, ADRs, specs, and current code still support it.

Required behavior: Run an existing-pattern freshness check before treating the pattern as binding. If examples moved, newer decisions supersede it, or forces changed, route to update, deprecate, consolidate, or block.

Pass condition: The answer does not rely on stale accepted guidance without evidence refresh.

## Test 9: Ideation Survivor

Prompt: "The brainstorm ranked optional provider adapters first. Make that our implementation pattern."

Expected failure mode: Treat ranking or enthusiasm as recurrence evidence.

Required behavior: Classify the brainstorm output as a candidate signal or external/prior-art input, then require local recurrence, mandate, force match, examples, and non-use cases before accepted status.

Pass condition: Ranked ideas do not become mandatory pattern doctrine without project-local evidence or mandate.

## Test 10: Optional Provider Candidate

Prompt: "We built one optional provider integration with graceful fallback. Capture the provider adapter pattern."

Expected failure mode: Create a full accepted pattern from one polished implementation.

Required behavior: Recognize the useful candidate shape, record forces and evidence needed, but hold as candidate or reject unless there is recurrence or mandate.

Pass condition: One optional provider integration cannot become accepted pattern guidance by itself.

## Test 11: Debug-Derived Hardening

Prompt: "A production incident was fixed by adding idempotency. Document the idempotency pattern."

Expected failure mode: Turn one incident fix or symptom-level workaround into durable doctrine.

Required behavior: Require confirmed causal chain, repeated or high-consequence problem shape, force match, examples or mandate, and non-use cases. Otherwise produce a candidate note, rejection, or blocked result.

Pass condition: Incident evidence is consumed as a signal, not automatic pattern authority.

## Test 12: Duplicate Overlapping Patterns

Prompt: "Create a new request retry pattern; we may already have a job retry pattern somewhere."

Expected failure mode: Create a duplicate pattern because the exact title differs.

Required behavior: Search existing patterns, ADRs, specs, docs, rules, and durable learnings when present; compare problem shape, forces, invariants, examples, and non-use cases; update, consolidate, or reject when overlap is material.

Pass condition: The answer does not create parallel doctrine without checking overlap and canonical ownership.

## Test 13: No-Artifact Decision Preservation

Prompt: "There is no pattern here, but tell the next planner why."

Expected failure mode: Return a vague "not enough evidence" response that loses checked sources and promotion criteria.

Required behavior: Emit a compact decision summary with output state, sources checked, recurrence or mandate result, force match, existing-artifact decision, missing evidence, residual risk, and promotion trigger.

Pass condition: No-file outcomes remain inspectable without creating a junk pattern artifact.

## Test 14: Pattern State Handoff

Prompt: "Use this candidate pattern in the implementation plan as if it is approved."

Expected failure mode: Promote candidate guidance during downstream handoff.

Required behavior: Preserve output state and confidence anchor, state that candidate guidance is not binding, and hand off only evidence, risks, examples, and promotion criteria unless accepted/proven status exists.

Pass condition: Candidate and rejected states are not silently upgraded by planning, commit, PR, or review handoffs.
