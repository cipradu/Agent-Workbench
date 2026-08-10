# Testing Mechanics

Load for runner configuration, Vitest, Playwright, async tests, coverage, type tests, package test helpers/doubles, integration tests, or browser E2E.

`testing-strategy` decides which behavior and risks must be proven. This reference owns strict TypeScript/JavaScript runner, placement, helper, coverage, and execution mechanics.

## Runners And Placement

Preserve a compliant incumbent. New projects use Vitest for unit/integration tests and Playwright for real-browser E2E. Do not add a duplicate runner for convenience.

- All tests, fixtures, mocks, and runner helpers live outside `src`, normally in package/application `tests/`.
- Vitest uses `.test.ts`/`.test.tsx`; Playwright E2E uses `.spec.ts` under `tests/e2e`.
- Unit/integration and browser scopes use separate configs when hosts/lifecycles differ, with explicit canonical scripts and an aggregate test command.
- Runner transforms, module semantics, aliases, and conditions must match the production host closely enough that tests cannot import code production rejects.
- Prove config discovery and source/test membership from the exact root where the command runs.

Production code exposes no test-only branches, flags, reset hooks, mutable registries, alternate dependency paths, or test-framework imports. A source-derived guard scans every production root for test imports and focused/disabled markers and fails closed.

## Deterministic Tests

- No `.only`, `.skip`, conditional silent skip, raw sleep, shared mutable global state, leaked handle, unhandled rejection, or missing await.
- Missing database/browser/service prerequisites fail the applicable integration/E2E job rather than turning it green.
- Await every promise the assertion depends on. Prefer `async`/promise-returning tests; do not use `done` callbacks.
- Restore DOM, spies/mocks, fake time, environment state, database state, connections, contexts, servers, workers, and files after each owner scope.
- Use the runner's controlled clock and restore real time.
- Keep assertions inside `it`/`test` and suite nesting shallow enough to expose ownership/setup.

## Boundary And Contract Tests

Parse realistic unknown input through the public boundary rather than pre-casting fixtures. Endpoint/wire tests parse the actual returned body/envelope with the owning contract schema; asserting only a hand-built literal from the implementation is tautological.

Test success, catalog-backed failures, malformed/missing/extra boundary fields, timeout, cancellation, cleanup, retry/give-up, partial failure, concurrency limits, and each semantic schema/config-field branch when those behaviors exist. Public-surface/export tests import real package subpaths.

## Package-Owned Test Support

Composition roots expose typed factory-injection seams for replaceable external dependencies. Production callers omit overrides; tests inject complete package-owned doubles. A declared central testing-support owner governs shared conventions and only genuinely shared primitives; it does not absorb helpers whose behavior belongs to one package.

A workspace package that needs package-specific test support exposes a deliberate testing subpath containing both:

- a real test factory/config helper for integration tests;
- a structurally complete, spy-capable test double for unit tests.

Test doubles never touch external services. Fake credentials are visibly test-only. Cache/registry reset helpers stay on testing subpaths. Production entry points do not export test support, and package/build checks reject accidental testing-subpath inclusion in production bundles.

Do not `vi.mock` transitive package internals across workspace boundaries when the owning package provides a public factory seam or test double. Mock the dependency you own, not a transitive implementation detail whose identity may differ under pnpm.

## Coverage

Use the stricter existing policy. New projects enforce at least 85% branches, functions, lines, and statements **per file**. Coverage includes every handwritten production file even when no test imports it.

Do not exclude a difficult file, branch, adapter, composition root, or framework shell merely to increase coverage. A complete generated/vendor category may be excluded by exact owner. A handwritten surface may rely on an explicitly named integration/E2E gate only when project policy assigns that gate as its proof; never use exclusion alone as proof.

Verify source maps and transforms attribute coverage to the intended production sources.

## Negative Type Tests

Use a suppression-free diagnostic harness or type-assertion tool. Run an isolated invalid fixture that must fail for the intended diagnostic and a positive companion that must pass. Do not use TypeScript suppression directives in tests.

## E2E Lifecycle

Use locator assertions and auto-waits rather than sleeps. Make environment, server startup/readiness, authentication, browser install, fixtures, artifact retention, and teardown explicit. A page load or zero process exit alone does not prove behavior.

Failure output: `Not done: TypeScript test mechanics are incomplete: <placement, isolation, helper/double, boundary proof, coverage, lifecycle, or command>.`
