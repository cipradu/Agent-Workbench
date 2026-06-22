# Integration, Contract, And E2E Tests

Use this reference when the boundary itself is the risk.

## Integration Tests

Use integration tests when correctness depends on real collaboration between components:

- database SQL, migrations, constraints, transactions, locking, or query behavior;
- framework routing, middleware, serialization, validation, or generated clients;
- filesystem, queues, caches, jobs, schedulers, or background workers;
- authentication/session behavior;
- real parser/serializer behavior;
- service adapters where the local contract must match a real dependency.

Rules:

- Use real dependencies or faithful containers/emulators when the dependency behavior is the point.
- Keep integration tests isolated with clean data, unique IDs, and bounded resources.
- Separate slow/environment-dependent tests from fast unit tests when the project supports that split.
- Assert durable behavior, not just successful calls.

## Contract Tests

Use contract tests when independently changing parties rely on a shared boundary:

- REST/OpenAPI, GraphQL schema, protobuf/gRPC, webhooks, events, SDKs, generated clients, file formats, or database schemas consumed by other services.

Rules:

- Test request/response shape, error shape, status semantics, versioning/compatibility, auth/tenant scoping, pagination bounds, and required/optional fields.
- Validate examples and generated artifacts against the source of truth.
- Include backward-compatibility checks for public or multi-team contracts.

## E2E And Browser/UI Tests

Use E2E tests for critical user journeys and wiring that lower-level tests cannot prove.

Rules:

- Map changed UI files/components/routes to affected user-visible routes or screens.
- Exercise critical interactions, not just page load.
- Check console/runtime errors when browser behavior is in scope.
- Prefer semantic locators: roles, labels, accessible names, visible text, and stable test IDs only when semantic locators are not enough.
- Avoid raw sleeps. Use framework auto-waits, locator assertions, event waits, or explicit state checks.
- Use screenshots, videos, traces, logs, or snapshots as debugging/inspection evidence, not as the only behavioral assertion.
- Human verification is acceptable for external flows such as OAuth, email delivery, SMS, payments, push notifications, device permissions, or third-party services. Minimum evidence is: steps performed, environment/account or role, observed result, verifier, and residual risk; add screenshots, logs, traces, messages, or receipts when available.

## E2E Red Flags

- Test only checks that the page loads.
- Test uses brittle CSS selectors for user-visible controls.
- Test records actions but adds no assertions.
- Test depends on external mutable production data.
- Test silently skips external flows without human evidence.
- Test creates state but never cleans it or uses a sandbox.
