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
- Do not use fallback after a requested safety guarantee fails unless the caller explicitly accepts the weaker result and the output makes the changed guarantee visible.
- Do not serve stale cached data unless staleness bounds and caller semantics allow it.
- Log or emit diagnostics for support-relevant fallback activation without leaking sensitive data.
- Test both primary failure and fallback behavior; a fallback path that is never exercised is wishful recovery.

Failure output: `Rejected: fallback hides changed behavior or lacks diagnostics: <specific issue>.`

## Optional Providers And Local Degradation

Optional providers and local tooling can degrade only when the core contract still holds.

Allowed degradation examples:

- optional provider is absent and the feature is documented as optional;
- provider auth is expired and the user-facing result clearly says the provider source was skipped;
- malformed optional provider output is quarantined and other independent sources still produce a partial result;
- nonessential local preference persistence fails after the primary action completed, with a warning and diagnostic path;
- no configured destination or sink produces a `no_sink` or blocked state instead of silently discarding output.

Fail closed or route to an owner decision when the failure affects required auth, billing, audit, integrity, authorization, external mutation, data deletion, legal/compliance output, or a user-requested safety guarantee.

Failure output: `Rejected: optional-provider degradation changes required semantics: <specific dependency>.`

## Generated Reports And Artifacts

Fallback for reports and generated artifacts must be truthful about source coverage.

Rules:

- `no data` means the source was checked successfully and had no relevant records;
- `not configured` means the source cannot be checked because setup is missing;
- `instrumentation pending` means the signal is not collected yet;
- `source skipped` means the source was intentionally omitted by mode, cost, permission, or scope;
- `source failed` means the source was attempted and failed;
- `partial result` means independent parts succeeded and failed with clear source/item identity;
- `blocked` means a required credential, decision, safety condition, or sink is missing.

Do not fill missing sections with stale, fabricated, or unrelated data unless the artifact clearly labels the substitution and the contract allows it.

Failure output: `Rejected: report fallback hides missing, skipped, failed, or partial source state: <specific source>.`

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

## Retry And Ambiguous Outcome

Retry recovery requires both transient classification and outcome safety.

Before retrying after timeout, network failure, `5xx`, pending async status, sync failure, or commit-ambiguous write:

- reread authoritative state or status when available;
- verify whether the operation landed, partially landed, or is still pending;
- use exact idempotency scope for operation, target, body, key, actor/tenant, and replay window;
- bound attempts, total time, and backoff;
- avoid retrying at multiple layers unless one owner controls the policy;
- surface conflict or state-refresh requirements when the authoritative state changed.

Failure output: `Rejected: retry proceeds without authoritative outcome check or idempotency scope: <specific operation>.`

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

## Measured Recovery Evaluation

Use measurement only to compare recovery variants after safety gates are fixed.

Hard gates before accepting a retry, timeout, fallback, or alert-threshold variant:

- no leaked sensitive data;
- no swallowed unknown failures;
- no unsafe retries or duplicate side effects;
- no missing correlation path for support-relevant failures;
- no false full success for degraded, skipped, partial, blocked, or no-sink results;
- cleanup, rollback, and terminal-state behavior remain intact;
- local conventions and public contracts remain compatible.

Metrics such as fewer logged errors, lower alert volume, faster completion, or higher success count do not justify hiding failures or weakening diagnostics.

## Recovery Checklist

- Recovery choice matches failure semantics and caller contract.
- Retry is bounded and side-effect safe.
- Fallback is truthful, visible where material, and verified.
- Independent failures are aggregated when useful; dependent failures stop safely.
- Partial success has item identity, ordering, retry, and terminal-state semantics.
- Cleanup releases resources and preserves the primary diagnostic.
- Degraded mode has diagnostics and does not conflict with retries or health checks.
- Optional-provider and generated-artifact fallback is truthful about missing, skipped, failed, partial, blocked, and no-sink states.
- Ambiguous mutation outcomes are reread or bounded before retry.
- Measured tuning preserves safety gates before optimizing metrics.
