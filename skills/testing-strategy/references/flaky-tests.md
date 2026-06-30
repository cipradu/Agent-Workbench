# Flaky Tests

Flaky tests are unresolved reliability bugs in the test suite, the product, or the environment.

## First Response

Do not normalize retries as the fix.

1. Run the failing test in isolation.
2. Run the related group or file.
3. Compare isolation vs suite behavior.
4. Record reproduction rate when repeated runs are needed.
5. Identify whether the failure is order dependence, shared state, timing, environment, resource leak, network dependency, concurrency, or real product race.
6. Minimize the reproduction before changing code.

If the cause is unknown, use `structured-problem-resolution`.

## Common Causes

| Symptom                                       | Likely Cause                                             | Direction                                             |
| --------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- |
| Passes alone, fails in suite                  | Shared state or order dependence                         | Find polluting test, isolate setup/cleanup.           |
| Fails under parallelism                       | Data collision, port collision, global state, race       | Unique resources, locks, real isolation, race checks. |
| Fails only in CI                              | Environment, timing, missing dependency, resource limits | Reproduce CI-like env, inspect logs/artifacts.        |
| Fails around timeouts                         | Raw sleeps, wall-clock assumptions, slow external calls  | Use fake time, event waits, deterministic clocks.     |
| Browser click succeeds but state unchanged    | Wrong locator, animation, hidden element, async state    | Use semantic locator and assert resulting state.      |
| Random data causes intermittent invalid cases | Unbounded generator/factory                              | Constrain generated input and shrink failing cases.   |
| Rate improves after retries                   | Failure hidden by retry masking                          | Diagnose root cause and report residual risk.         |
| Benchmark or evaluator result varies widely   | Noisy harness, shared resource, or unstable sample       | Repeat with a defined aggregation and noise threshold. |

## Reproduction And Variance

For flaky, timing, performance, or evaluator-like evidence:

- define repeat count, aggregation method, and acceptable noise threshold;
- compare isolated, file/group, and suite behavior;
- bisect order pollution by running suspected polluters before the failing test;
- compare local, CI-like, and environment-specific runs when the failure is environment-sensitive;
- control clocks, timers, async waits, concurrency, ports, queues, caches, databases, browser contexts, and external services before changing assertions.

## Prevention Rules

- Avoid raw sleeps.
- Avoid shared mutable global state.
- Reset mocks, fake timers, env vars, files, browser contexts, DB rows, queues, and caches.
- Use deterministic clocks and IDs when possible.
- Close resources and background workers.
- Use unique data per test when running in parallel.
- Keep external services out of critical test paths unless the integration itself is under test.
- Run related test files together when mocks, globals, fixtures, fake timers, process state, ports, queues, caches, or browser contexts may leak across files.
- Before recommending parallel test execution, check hardcoded ports, shared databases, temp paths, lock/PID files, global environment, queues/caches, browser contexts, external rate limits, and other exclusive resources.

## Retry Policy

Retries can reduce noise in CI, but they do not prove reliability.

Use retries only with:

- artifact capture on failure;
- a tracked investigation or explicit residual risk;
- limits that do not hide persistent failure;
- root-cause work for critical paths.

Do not count a retry-green result as evidence that the protected behavior is reliable. Report the original failure, retry count, artifacts, suspected class, and remaining risk.
