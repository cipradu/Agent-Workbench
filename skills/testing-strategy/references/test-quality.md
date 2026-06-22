# Test Quality

Good tests constrain behavior. Bad tests constrain implementation.

## Good Test Signals

- Test name states expected behavior in caller/user/domain language.
- Test uses a stable public seam: function API, route, command, UI role, database contract, workflow, or generated contract.
- Assertions would fail for the real regression or requirement violation.
- Test includes meaningful negative, boundary, and error cases for the risk.
- Test can survive behavior-preserving refactors.
- Setup is readable and purposeful.
- Cleanup makes the test independently runnable.

## Weak Test Signals

- Assertion only checks existence: `toBeDefined`, non-null, status present, snapshot exists.
- Test asserts private methods, internal call order, private fields, or implementation-specific collaborators.
- Test name describes how the code works rather than what must happen.
- Test passes if the production behavior is broken but the mock was called.
- Test relies on file order, shared state, wall-clock sleeps, external mutable state, or previous test side effects.
- Test data is unrealistic or omits fields real consumers depend on.

## Assertion Rules

- Assert observable outcomes, not just that code ran.
- For APIs, assert status, shape, stable error code, relevant headers, security-sensitive omissions, and body fields the client relies on.
- For databases, assert durable effects through constraints, transactions, round-trips, uniqueness, filtering, and rollback behavior when relevant.
- For UI, assert accessible/user-visible behavior using roles, labels, text, state, and navigation outcomes.
- For commands/jobs, assert exit behavior, outputs, side effects, idempotency, and failure handling.
- For generated artifacts, assert contract validity and compatibility rather than generated text churn.

## Test Independence

Every test should be independently runnable unless the framework explicitly defines setup dependencies.

Required practices:

- isolate mutable state;
- reset mocks and fake timers;
- clean databases, files, queues, browser contexts, and environment variables;
- avoid dependence on test order;
- use unique IDs or deterministic factories;
- close resources and cancel background work.

## Snapshot Rules

Snapshots are acceptable only when the serialized shape itself is the contract or when visual/markup drift is intentionally reviewed.

Do not use snapshots as a substitute for assertions about behavior, accessibility, errors, permissions, or data integrity.
