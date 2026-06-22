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
