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
