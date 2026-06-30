# Mocking And Fixtures

Mocks isolate boundaries. They are not the behavior under test.

## Mocking Rules

- Mock external systems, network calls, time, randomness, filesystem, process boundaries, unsafe side effects, expensive services, and nondeterministic dependencies.
- Prefer real project-owned modules when their behavior is part of the contract being tested.
- Do not mock high-level methods that perform side effects the test depends on.
- Do not assert that a mock exists unless the mock itself is the public contract.
- Do not add production methods used only by tests. Put cleanup and builders in test utilities.
- Before mocking, identify what the real dependency does, what side effects the test needs, and what lower-level boundary can vary safely.

## Incomplete Mock Rule

Mock data must be complete enough to represent the real contract.

Before creating a mock response or fixture:

1. Check the schema, docs, example payload, generated type, or real sample.
2. Include fields downstream code may rely on, not only fields used by the immediate assertion.
3. Preserve important nullability, optionality, status/error variants, pagination metadata, IDs, timestamps, and nested shapes.
4. Add contract/schema validation when drift would be expensive.

## Fixture Freshness

Fixtures, snapshots, generated samples, and mocks drift like code.

Before relying on existing test data:

- check it against the current schema, contract, generated type, source window, or real sample;
- classify stale fixtures as `current/no change`, `stale but correctable`, `contradicted by source truth`, `fixture drift`, `over-mocked`, or `wrong seam`;
- include telemetry/reporting fields such as timestamps, source windows, missing metrics, pagination, IDs, redaction-safe identifiers, and unavailable-data variants when downstream code depends on them;
- update fixtures only when the protected behavior or current contract justifies the change, not merely to make assertions pass.

## Mock Boundary False Positives

Suppress mock-related findings when the mock is a true external boundary and the test has separate evidence for the local behavior. Raise a finding when:

- the code under test or project-owned collaborator is mocked;
- the mock omits fields real downstream code relies on;
- the assertion proves only a call count or mock return;
- the mock hides database, auth, routing, serialization, generated-contract, queue/cache, or browser behavior that is the actual risk;
- shared mocks, globals, fake timers, environment variables, files, queues, caches, or browser contexts can contaminate related tests.

## Fixture Rules

- Prefer factories/builders for varied test data and fixtures for stable shared examples.
- Keep default fixtures valid and minimal; override only the fields relevant to the case.
- Avoid magic IDs unless the ID value is the behavior.
- Use deterministic time, IDs, and randomness where possible.
- Put test-only lifecycle helpers in test utilities, not production classes.

## Red Flags

- Mock setup is larger than the behavior under test.
- The test fails when the mock is removed but production behavior is unchanged.
- The mock omits fields that real responses always include.
- The test asserts `mockFunction` call counts instead of observable behavior.
- The code under test is mocked.
- Cleanup requires production-only methods that should not exist.
- Snapshot or fixture refresh is accepted without checking whether behavior, source truth, or schema changed.
- Related test files pass alone but fail together because shared mocks, globals, fixtures, or fake timers leak.
