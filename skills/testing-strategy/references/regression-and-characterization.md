# Regression And Characterization

Use this reference for bugs, brownfield changes, refactors, review findings, and legacy behavior.

## Regression Tests

A regression test protects against a known failure.

Required shape:

- original failure signal: bug report, failing command, review finding, incident, user reproduction, or observed bad behavior;
- linked diagnosis or causal-chain summary when the cause was not obvious;
- seam where the failure is observable;
- expected red reason before the fix, or a reason red cannot be reproduced;
- actual red output comparison when red evidence is available;
- fixed behavior;
- command or evidence proving the case now passes.

For bug fixes, the best regression test would have caught the bug before the fix. If that is impossible, state why and choose the closest evidence.

The red failure must match the bug mechanism. A test that fails because of setup, missing fixture fields, an unsafe mock, stale generated artifacts, wrong environment, or a nearby unrelated error is not regression evidence yet.

Use the smallest realistic reproducer that still exercises the original mechanism. Do not reduce the test so far that it bypasses the boundary where valid state becomes invalid.

When a diagnosis had uncertain links, include evidence that would fail if the important prediction were wrong rather than only checking the patched symptom.

For feedback-derived tests, preserve the evidence pointer: comment ID, report, transcript moment, screenshot, log, incident, recording, or manual step. Separate observed facts, inferred intent, confirmed requirement, and current source truth.

## Characterization Tests

Characterization tests document current observable behavior before changing internals.

Use when:

- refactoring weakly tested code;
- current behavior is relied on but undocumented;
- behavior may be surprising but must be preserved;
- the implementation is being moved behind a new boundary;
- replacing a library, ORM, framework, parser, serializer, or adapter.

Rules:

- Characterize through public seams where possible.
- Name known-bad behavior explicitly if preserving it temporarily.
- Do not freeze accidental behavior without explaining whether it is required.
- Separate preservation tests from new desired behavior tests.
- After the refactor, run the characterization tests unchanged unless the spec deliberately changes behavior.

For simplification or behavior-preserving refactors, verify safety behavior that can be accidentally removed: validation, authorization, data-loss prevention, error handling, cleanup, accessibility affordances, and compatibility behavior. Run changed-scope tests and broaden when shared utilities, public boundaries, generated contracts, or runtime interaction chains are affected.

## Review-Finding Tests

When a reviewer finds a defect:

1. Treat the finding as a signal, not an instruction.
2. Reproduce or reason through the failure.
3. Add a regression or characterization test if the behavior is testable.
4. Fix the behavior.
5. Re-run the test and include it in the review packet.

If no automated test is feasible, provide manual evidence and reviewer focus.

For batches of review findings, preserve stable IDs and group root/dependent gaps. Require targeted evidence for each behavior-affecting fix plus one combined validation gate when fixes interact through shared files, fixtures, contracts, state, or runtime paths.
