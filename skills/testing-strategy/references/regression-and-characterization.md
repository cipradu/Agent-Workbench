# Regression And Characterization

Use this reference for bugs, brownfield changes, refactors, review findings, and legacy behavior.

## Regression Tests

A regression test protects against a known failure.

Required shape:

- original failure signal: bug report, failing command, review finding, incident, user reproduction, or observed bad behavior;
- seam where the failure is observable;
- expected failure before the fix, or a reason red cannot be reproduced;
- fixed behavior;
- command or evidence proving the case now passes.

For bug fixes, the best regression test would have caught the bug before the fix. If that is impossible, state why and choose the closest evidence.

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

## Review-Finding Tests

When a reviewer finds a defect:

1. Treat the finding as a signal, not an instruction.
2. Reproduce or reason through the failure.
3. Add a regression or characterization test if the behavior is testable.
4. Fix the behavior.
5. Re-run the test and include it in the review packet.

If no automated test is feasible, provide manual evidence and reviewer focus.
