# Transactions And Concurrency

Use this reference when writing or reviewing transaction boundaries, isolation levels, row locks, retries, session/connection ownership, savepoints, deadlocks, connection pools, or concurrency bugs.

## Unit Of Work

Define one unit of work as the smallest set of database changes that must commit or roll back together.

Rules:

- one connection/session/transaction context per unit of work;
- one top-level transaction boundary per unit of work;
- one layer owns begin/commit/rollback;
- inner functions receive the active connection/session/transaction or an explicit unit-of-work object;
- inner functions do not secretly start, commit, or roll back top-level transactions.

Failure output: `Rejected: transaction ownership is split across layers: <specific layers/functions>.`

## Transaction Duration

Keep transactions short.

Do before the transaction when possible:

- request validation;
- authorization checks that do not require locks;
- encryption/hashing/preparation;
- external API calls;
- expensive computation;
- file/network IO.

Do after commit when possible:

- success logging;
- cache refresh;
- pub/sub/event emission;
- analytics;
- emails/webhooks;
- non-critical follow-up work.

If a side effect must be exactly coordinated with the database commit, use an explicit transactional outbox or equivalent project pattern instead of calling the external system inside the transaction.

## Isolation And Locks

Use the default isolation level only when it protects the invariant. Escalate isolation only for a named anomaly or invariant risk.

Common guidance:

- read committed is often enough for independent row writes;
- repeatable read can be needed for consistent reads across a transaction;
- serializable can be needed for cross-row invariants, counters, reservations, inventory-like workflows, balance-like workflows, or race-prone uniqueness beyond a simple unique constraint;
- row locks are appropriate when reading a row to compute and write a new value;
- acquire locks in stable order to reduce deadlocks;
- lock only what will be modified or what protects the invariant.

Completion criterion: the isolation/locking choice names the invariant it protects and the contention cost it accepts.

## Savepoints

Use savepoints only when partial rollback inside a larger transaction is genuinely required and supported by the engine/tool.

Rules:

- prefer simpler single-transaction success/failure when possible;
- name why the nested rollback is needed;
- test savepoint behavior on the target engine and adapter;
- do not use savepoints to paper over unclear transaction ownership.

## Deadlocks, Serialization Failures, And Retries

Deadlocks and serialization failures are expected under some concurrency patterns. Handle them deliberately.

Rules:

- retry the whole safe unit of work, not only the last statement;
- use bounded attempts;
- use jittered backoff when contention may repeat;
- log database error class/code, attempt count, elapsed time, and final outcome;
- do not retry non-idempotent external side effects unless they are guarded by idempotency keys or an outbox.

Failure output: `Rejected: retry policy can duplicate side effects or retry only part of the transaction.`

## Rollback And Error Translation

On database failure:

- roll back the current transaction;
- clear invalid session state according to the adapter;
- preserve diagnostic cause in logs;
- translate expected constraint errors into domain/application errors;
- distinguish not-found from technical failure;
- never swallow database exceptions and continue as if the unit of work succeeded.

## Connections, Pools, And Timeouts

Database access should respect cancellation and bounded waiting.

Rules:

- pass request/job context or deadline to database operations when the language/tool supports it;
- configure pool size, idle count, max lifetime, and idle lifetime based on database capacity and workload;
- watch pool wait count/wait duration, open connections, in-use connections, slow queries, and timeout/error rates;
- fail fast or degrade deliberately when the database is unavailable instead of hanging indefinitely.

Completion criterion: long-running or production database paths have explicit timeout/cancellation behavior and pool observability.
