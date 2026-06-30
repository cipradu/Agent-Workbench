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
- For generated artifacts, assert contract validity, provenance, source window, timestamp consistency, unavailable-data behavior, redaction, and compatibility rather than generated text churn.

## Evidence Strength

Use these labels when reviewing or reporting test evidence:

- `unsupported`: claim exists without current evidence.
- `executes-only`: code path ran, but the assertion would not fail for the protected behavior.
- `red-capable`: test would fail for the intended bug, requirement violation, or contract breach.
- `right-seam`: evidence exercises the boundary where the risk appears.
- `risk-covered`: key happy, boundary, negative, and integration cases are covered for the target.
- `manual-bounded`: manual evidence includes steps, environment, observed result, verifier, artifacts when available, skipped automation reason, and residual risk.
- `independently-reviewed`: evidence was accepted by a separate review workflow or human checkpoint.

## Generated Artifact And Report Checks

For reports, screenshots, traces, logs, exports, generated clients, snapshots, or other persisted artifacts, check what matters for the artifact type:

- source, query, input, or fixture provenance;
- time window, timezone, data freshness, ingestion lag, and missing-data semantics;
- stable path, file name, timestamp, overwrite/append behavior, and contract version;
- omission versus `no data` behavior;
- privacy and redaction of secrets, emails, account IDs, message content, tokens, and other PII;
- content assertions that prove the protected behavior, not only file existence.

## Test-Review Finding Shape

When reporting a test-quality finding, include:

- testing target and source truth;
- protected risk or failure mode;
- current posture and seam;
- assertion weakness or missing case;
- mock or fixture boundary if relevant;
- existing evidence inspected;
- required correction;
- evidence strength and residual risk.

Do not report generic "add more tests" feedback without a named failure mode and evidence that existing tests do not already cover it.

## Safety-Preservation Checks

For refactors, simplifications, generated rewrites, or broad fixture updates, preserve safety behavior as first-class behavior:

- validation and malformed input handling;
- authorization, tenant, role, and security checks;
- data-loss prevention and rollback behavior;
- error shape, retryability, and cleanup;
- accessibility roles, names, focus, keyboard behavior, and visible state.

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
