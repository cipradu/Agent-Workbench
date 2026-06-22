# Recovery And Degradation

Use this reference when deciding what happens after a failure is detected: stop, retry, fallback, degrade, aggregate errors, roll back, compensate, dead-letter, or continue with partial results.

## Recovery Choice

Choose recovery from caller safety, side-effect safety, and contract truthfulness.

| Choice                           | Use When                                                                                     | Watch For                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Fail fast                        | Continuing would violate an invariant, hide corruption, leak data, or make later work unsafe | Include a clear public failure and private diagnostics                                                             |
| Retry                            | Failure is transient and the operation is idempotent or otherwise duplicate-safe             | Bound attempts, total time, backoff, and retry layer                                                               |
| Fallback                         | Substitute behavior preserves the contract or clearly communicates degraded behavior         | Do not return stale or lower-quality data as if it were primary success                                            |
| Partial success                  | Independent items can succeed/fail separately                                                | Include item identity, ordering, retryability, and final status semantics                                          |
| Error aggregation                | Caller benefits from all independent validation or per-item failures                         | Do not continue dependent work after an invalid prerequisite                                                       |
| Rollback or compensation         | Work changed state before failure                                                            | Roll back the unit of work or define compensating action and residual risk                                         |
| Dead-letter or terminal state    | Async work cannot continue automatically                                                     | Include retry count, terminal reason, recovery owner, and private cause pointer                                    |
| Circuit breaker or degraded mode | Repeated dependency failure threatens caller survival or wider system stability              | Coordinate thresholds, health, metrics, logs, fallback, and reset behavior with observability/operations standards |

Failure output: `Rejected: recovery choice is unsafe or untruthful: <specific issue>.`

## Fallback Rules

Fallback is not success unless the contract says it is.

Rules:

- Name what the fallback replaces and what it cannot provide.
- Surface degraded or partial behavior to the caller when it affects correctness, freshness, completeness, authorization, billing, audit, or user expectation.
- Do not use fallback to hide dependency outages, data-integrity problems, authorization failures, or programmer bugs.
- Do not serve stale cached data unless staleness bounds and caller semantics allow it.
- Log or emit diagnostics for support-relevant fallback activation without leaking sensitive data.
- Test both primary failure and fallback behavior; a fallback path that is never exercised is wishful recovery.

Failure output: `Rejected: fallback hides changed behavior or lacks diagnostics: <specific issue>.`

## Error Aggregation

Aggregate errors when failures are independent and the receiver benefits from a complete correction set.

Good aggregation cases:

- form or request validation where multiple fields can be corrected together;
- import, batch, sync, or bulk operations where items are independent;
- preflight checks where multiple missing prerequisites can be reported safely;
- configuration validation where all missing or invalid settings should be reported before startup fails.

Do not aggregate when:

- the first failure invalidates later checks;
- later checks would require unsafe side effects;
- continuing would multiply dependency load after a systemic failure;
- later errors would reveal unauthorized resources, fields, or policy internals.

Aggregation output should include stable codes, safe messages, field/path or item identity, retryability where relevant, and a single top-level failure status that cannot be mistaken for full success.

Failure output: `Rejected: aggregation loses item identity, leaks details, or makes success ambiguous: <specific issue>.`

## Cleanup And Resource Release

Cleanup is part of the failure contract.

Rules:

- Release locks, file handles, sockets, leases, database connections, temp files, and worker reservations deterministically.
- Roll back the current transaction or unit of work when possible.
- Mark durable job/import/workflow state before retrying, stopping, or handing work to an operator.
- Keep external side effects outside database transactions unless an outbox or equivalent pattern owns the handoff.
- Distinguish cleanup failure from the original cause; do not overwrite the primary diagnostic with a less important cleanup exception.
- Never continue as if the failed step succeeded.

Failure output: `Rejected: cleanup or rollback behavior is missing: <specific resource/state>.`

## Circuit Breaker And Degraded Mode Handoff

Circuit breakers and degraded modes are reliability design, not catch-block decoration.

Use them only when the failure mode is repeated or prolonged dependency/workload failure and the system needs to protect callers, workers, threads, connections, queues, or downstream systems.

Define:

- failure signal and threshold;
- open, half-open, and closed behavior if using a breaker;
- fallback or fast-fail behavior while degraded;
- metrics/logs/health signals and alerting ownership;
- reset behavior and manual override path if applicable;
- interaction with retries so retries do not amplify the outage.

Coordinate with architecture, operations, or observability guidance when those skills or project standards exist.

Failure output: `Blocked: circuit-breaker/degraded-mode behavior needs production-readiness design: <specific missing signal or owner>.`

## Recovery Checklist

- Recovery choice matches failure semantics and caller contract.
- Retry is bounded and side-effect safe.
- Fallback is truthful, visible where material, and verified.
- Independent failures are aggregated when useful; dependent failures stop safely.
- Partial success has item identity, ordering, retry, and terminal-state semantics.
- Cleanup releases resources and preserves the primary diagnostic.
- Degraded mode has diagnostics and does not conflict with retries or health checks.
