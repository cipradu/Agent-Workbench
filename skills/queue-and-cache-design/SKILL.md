---
name: queue-and-cache-design
description: Use when designing, reviewing, or changing queues, background jobs, worker processing, Redis-backed caches, cache invalidation, TTLs, Redis-backed locks, Redis-backed rate limits, Redis pub/sub or streams, retries, idempotency, dead-letter handling, or queue/cache observability.
---

# Queue And Cache Design

## When to Use

Use this skill when:

- Designing or reviewing cache layers, Redis keys, TTLs, invalidation, negative caching, refresh behavior, stale-read behavior, or memory policies.
- Designing or reviewing background jobs, queues, workers, delayed jobs, repeatable jobs, job flows, dead-letter handling, retry/backoff policy, worker concurrency, or worker shutdown.
- Designing Redis-backed coordination such as locks, rate limits, deduplication keys, idempotency keys, pub/sub, streams, sorted-set queues, or ephemeral runtime state.
- Changing how application code crosses from synchronous request handling into asynchronous processing.
- Reviewing whether Redis, BullMQ, a durable queue, a stream, pub/sub, a relational table, or an external workflow engine is the right primitive.
- Debugging duplicate jobs, stale cache reads, cache stampedes, thundering herds, missing invalidation, stalled workers, poison jobs, unbounded Redis memory growth, or lost pub/sub messages.
- Adding queue/cache observability such as job IDs, correlation IDs, queue depth, retry counts, dead-letter counts, latency, failed/stalled events, cache hit/miss rate, eviction behavior, or memory usage.

## Do Not Use

Do not use this skill when:

- The work is primarily relational schema, migrations, indexes, transactions, ORM usage, persistent integrity, or durable query performance. Use `database-design`; use this skill only for cache/queue boundaries around that database work.
- The work is only API contract shape, endpoint behavior, pagination, status codes, OpenAPI, GraphQL, or client compatibility. Use `api-design`; use this skill only for asynchronous or cached behavior behind the API.
- The work is only error taxonomy, validation messages, exception mapping, logging/redaction, or degraded-mode response design. Use `error-handling-design`; use this skill only for retry, dead-letter, worker, or cache failure semantics.
- The work is long-running workflow orchestration, sagas, human approval workflows, durable timers, compensation graphs, or multi-step business process execution that needs a workflow engine. Use architecture/spec work first; a simple queue is not a workflow engine.
- The work is realtime transport design such as WebSockets, SSE, presence, live collaboration, or push transport, unless Redis pub/sub, streams, fan-out, or backplane behavior is directly in scope.
- The task is only exact Redis/BullMQ/library syntax. Verify current syntax against project dependencies or official docs; use this skill for design decisions and failure semantics.
- A project has a stricter accepted queue/cache ADR, operations standard, platform convention, or provider constraint. Follow that source of truth and use this skill only for gaps.

## Iron Law

Queues and caches are coordination contracts, not faster storage. Do not add Redis keys, cache layers, jobs, workers, retries, locks, rate limits, pub/sub, or streams until source of truth, consistency/expiry, idempotency, failure/retry behavior, concurrency limits, ownership, and observability/recovery are explicit.

## Core Concept

Queues move work across time and process boundaries. Caches trade freshness and memory for latency. Redis-backed coordination is usually ephemeral unless explicitly designed and operated as durable infrastructure. Correct design starts by deciding what remains authoritative, what may be stale or replayed, what happens more than once, what can be lost, and how an operator proves the system is healthy.

BullMQ-style queues are at-least-once execution systems. A job may run more than once, may be retried after partial work, may stall, and may fail permanently. Cache entries are derived data unless the project has explicitly accepted Redis as authoritative for that specific state.

## Operating Process

Run these steps in order.

### 1. Establish The Boundary And Source Of Truth

Identify the runtime surface before choosing Redis or a queue:

- surface type: cache, background job, delayed job, repeatable job, worker flow, rate limit, lock, dedupe key, idempotency key, pub/sub, stream, or ephemeral state;
- source of truth: database row, external service, filesystem/object storage, event log, queue state, Redis key, in-memory process state, or another owner;
- correctness requirement: fresh read, stale-while-revalidate, eventual consistency, at-least-once execution, at-most-once notification, durable replay, best-effort fan-out, or coordination-only state;
- ownership: producer, consumer, invalidator, worker, scheduler, operator, and code owner;
- environment: Redis/provider/deployment model, persistence mode, eviction policy, cluster/sentinel behavior, connection lifecycle, tenant boundaries, and sensitive data constraints.

Completion criterion: the design can name what is authoritative, what may be stale, what may be replayed, what may be lost, and who owns recovery.

Failure output: `Blocked: queue/cache design depends on missing boundary context: <specific missing fact>.`

### 2. Choose The Right Primitive

Choose the primitive from the contract, not from convenience:

- Use a cache when the value is derived, can expire, and can be recomputed or safely missed.
- Use a queue when work should move out of the request path, be retried, delayed, rate-limited, observed, or processed by workers.
- Use a durable outbox or database-backed handoff when database commit and asynchronous side effects must not be split by a crash.
- Use streams or a durable log when consumers need replay, ordering, offsets, or independent consumption.
- Use pub/sub only for best-effort live notification where missed messages are acceptable.
- Use locks sparingly, with expiry, ownership tokens, release behavior, and fencing or another stale-owner defense when stale lock holders can cause corruption.
- Use rate limits with explicit identity, key cardinality, window, burst behavior, and failure response.
- Use Redis data structures deliberately: strings for simple values/counters, hashes for compact objects, sets for membership, sorted sets for ranked/time-priority access, streams for append-only consumption, and lists only when their queue semantics are enough.

Completion criterion: the primitive matches the durability, ordering, replay, freshness, and operational needs.

Failure output: `Rejected: selected queue/cache primitive does not match the required contract: <specific mismatch>.`

### 3. Design Keys, TTLs, Invalidation, And Memory

For cache and Redis-key work, make key lifecycle explicit:

- Use stable namespacing: environment, application/module, tenant/account when relevant, entity type, identifier, purpose, and schema/version segment when value shape can change.
- Keep key cardinality bounded or intentionally accounted for. Avoid unbounded per-user/per-event/per-request keys without lifecycle controls.
- Set TTLs for cache, lock, dedupe, idempotency, rate-limit, and temporary state keys unless a durable Redis record is explicitly accepted.
- Add TTL jitter for high-cardinality or synchronized expirations to reduce cache stampedes.
- Define invalidation: write-through, write-behind, cache-aside, explicit delete, version bump, tag/group invalidation, stale-while-revalidate, or expiry-only.
- Use `SCAN`-style iteration for production key discovery or bulk invalidation. Do not rely on blocking full-keyspace commands as a normal operational path.
- Define negative caching carefully: cache not-found or failed lookups only when the stale consequence and TTL are acceptable.
- Keep values small. Store identifiers and compact projections; avoid large blobs, credential-bearing payloads, or full mutable domain objects unless justified.
- Account for eviction policy, memory limit, persistence mode, replication lag, and backup/recovery expectations when Redis state is more than disposable cache.

Completion criterion: every key family has owner, shape, cardinality, TTL, invalidation path, and memory/failure behavior.

Failure output: `Rejected: Redis/cache key lifecycle is unsafe or undefined: <specific key family>.`

### 4. Design Job Semantics Before Worker Code

For queue work, define job behavior before implementing producers or workers:

- Job data should usually contain stable identifiers and small immutable inputs, not full mutable object snapshots.
- Every job type needs an idempotency story. Re-running the same job after partial work must be safe, detectably skipped, or compensated.
- Define attempts, backoff, timeout, retryable failures, permanent failures, and retry exhaustion behavior.
- Define deduplication where duplicate enqueue attempts are likely or harmful.
- Define dead-letter or failed-job retention and the operational path for inspection, replay, discard, or escalation.
- Define poison-job behavior so one bad payload cannot block the whole worker group indefinitely.
- Define concurrency and rate limits from downstream capacity: database pool, API quotas, email/SMS provider limits, CPU/memory, lock contention, or tenant fairness.
- Define delayed and repeatable jobs with timezone, duplicate-schedule behavior, missed-run behavior, and deployment restart behavior.
- Define cancellation, pause/resume, dependency/flow behavior, and result retention when relevant.

Completion criterion: each job type has payload contract, idempotency, retry/backoff, timeout, dead-letter, concurrency, and operator handling defined.

Failure output: `Rejected: job semantics are incomplete or unsafe: <specific job type>.`

### 5. Design Producer, Transaction, And Side-Effect Timing

Async handoff must not lie about durable state:

- Enqueue after the authoritative state exists and can be reloaded by the worker.
- Do not emit irreversible external side effects before the database transaction that authorizes them commits.
- If commit plus enqueue must be reliable as one unit, use an outbox/reconciliation pattern or another project-approved durable handoff. Do not pretend a normal queue add is atomic with a separate database transaction.
- In request paths, distinguish enqueue acknowledgement from job completion. Do not make clients believe the background work completed when only the handoff succeeded.
- Preserve correlation/request/user/tenant identifiers needed for diagnostics and authorization, without storing secrets or raw sensitive payloads in job data.
- Keep producer behavior bounded with timeouts and safe error mapping; a queue outage must have a deliberate user/API behavior.

Completion criterion: producer timing, transaction boundary, enqueue acknowledgement, and side-effect safety are explicit.

Failure output: `Rejected: async handoff can create split-brain state or false success: <specific path>.`

### 6. Design Worker Runtime And Operations

Workers are production services, not helper scripts:

- Use explicit connection lifecycle and reconnection behavior appropriate to the library and provider.
- Configure graceful shutdown so workers stop accepting new work, finish or release current work safely, and close queue/Redis connections.
- Handle failed, stalled, completed, retry-exhausted, and dead-letter events according to project convention.
- Emit observable identifiers: job type, job ID, attempt, queue name, worker name/version, tenant/account when safe, correlation ID, duration, retry count, and failure category.
- Track queue depth, age of oldest job, processing latency, failure rate, retry rate, stalled count, dead-letter count, worker concurrency, downstream rate-limit hits, cache hit/miss rate, Redis memory, evictions, and connection errors when material.
- Define dashboard, alert, runbook, replay, purge, and manual intervention paths for production queues.
- Avoid hidden unbounded parallelism. Worker concurrency, sandboxing, batching, and pipeline usage must match downstream limits.

Completion criterion: an operator can detect backlog, diagnose failures, shut down safely, and recover work without guessing.

Failure output: `Rejected: worker runtime cannot be operated safely: <specific gap>.`

### 7. Verify Queue And Cache Behavior

Before presenting queue/cache work as ready, verify:

- source of truth and stale/replay/loss semantics are explicit;
- key families have namespace, shape, TTL, cardinality, invalidation, memory, and sensitive-data handling;
- job payloads are small, reload authoritative state, and do not carry unnecessary secrets or stale mutable objects;
- jobs are idempotent or have explicit duplicate/partial-work handling;
- attempts, backoff, timeout, concurrency, rate limits, failed/dead-letter behavior, and poison-job handling are defined;
- producer transaction timing and external side effects are safe;
- worker graceful shutdown and failed/stalled/retry-exhausted handling are covered;
- metrics/logs/correlation IDs support production diagnosis;
- tests or review evidence cover cache miss/hit/stale behavior, invalidation, repeated job execution, retry, failure, dead-letter/replay, worker shutdown, and queue outage behavior where relevant.

Completion criterion: the design can be implemented and operated without relying on "Redis is fast" or "the queue will handle it" as hidden assumptions.

Failure output: `Not ready: queue/cache design is missing <specific consistency/idempotency/TTL/retry/worker/observability criterion>.`

## Output Contract

For queue/cache design or review, include:

- boundary and source-of-truth summary;
- chosen primitive and rejected alternatives;
- key families, TTLs, invalidation, memory, and sensitive-data handling, when relevant;
- job types, payload contracts, idempotency, retries, backoff, timeouts, concurrency, and dead-letter behavior, when relevant;
- producer transaction and side-effect timing, when relevant;
- worker lifecycle, observability, and recovery path, when relevant;
- verification evidence and residual risks.

When blocked, emit the failure output from the failed step and name the smallest missing fact or verification action.

## Reference Loading

| Situation                       | Load                                           |
| ------------------------------- | ---------------------------------------------- |
| Testing or improving this skill | [Pressure Tests](references/pressure-tests.md) |

## Related Skill Handoffs

- Use `database-design` when durable relational integrity, schema, transactions, migrations, indexes, or ORM behavior owns the decision.
- Use `api-design` when clients need an explicit async response contract, polling/webhook contract, idempotency header, rate-limit response, or compatibility story.
- Use `error-handling-design` when public/private failure shape, validation errors, retryability categories, dead-letter records, logging/redaction, or degraded-mode behavior needs deeper design.
- Use `testing-strategy` when queue/cache behavior needs regression, integration, fake-time, failure-injection, contract, or operational verification planning.
- Use `architecture-design` when introducing queues/caches changes service boundaries, ownership, coupling, consistency model, or deployment topology.
- Use `create-project-adr` when choosing Redis as authoritative for a state category, standardizing a queue/cache pattern, introducing a durable outbox, adopting a queue provider/library, or setting a project-wide worker/cache convention.

## Rationalization Table

| Temptation                                 | Reality                                                                                                         | Required action                                                                          |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| "Redis is just a faster database."         | Redis state is often ephemeral, evicted, replicated differently, and operated differently from durable storage. | Name the source of truth, durability expectation, eviction behavior, and recovery path.  |
| "The queue guarantees reliability."        | Most job queues provide at-least-once execution, not exactly-once business effects.                             | Make every job idempotent or explicitly handle duplicates and partial work.              |
| "We can add TTLs later."                   | Missing TTLs cause stale reads, memory growth, stuck locks, and stale dedupe/rate-limit state.                  | Define TTL and invalidation before implementation.                                       |
| "Retry will fix transient failures."       | Retry without bounds, backoff, timeouts, and idempotency creates duplicate work and thundering herds.           | Define attempts, backoff, timeout, retryable categories, and dead-letter behavior.       |
| "Put the whole object in the job payload." | Payload snapshots become stale, large, sensitive, and hard to migrate.                                          | Put stable IDs and reload authoritative state in the worker.                             |
| "A lock prevents the race."                | Locks can expire, be stolen, be released by the wrong owner, or leave stale workers running.                    | Use ownership tokens, expiry, release checks, and fencing when stale owners matter.      |
| "Pub/sub is an event log."                 | Pub/sub messages can be missed by disconnected consumers.                                                       | Use streams, a queue, or another durable log when replay or recovery matters.            |
| "Monitoring can come later."               | Unobservable queues and caches fail silently as latency, staleness, duplication, or backlog.                    | Define metrics, logs, correlation IDs, dashboards, and recovery actions with the design. |

## Red Flags

- Cache, queue, or Redis key design appears before source of truth and consistency semantics are known.
- Cache entries have no TTL, invalidation path, owner, or stale-read policy.
- Redis keys have unbounded cardinality, large values, sensitive payloads, or no memory policy awareness.
- A lock has no expiry, owner token, release check, or stale-owner strategy.
- Pub/sub is used where missed messages must be recovered.
- A job type has no idempotency, dedupe, retry/backoff, timeout, dead-letter, or poison-job handling.
- Workers have no graceful shutdown, failed/stalled handling, or operational dashboard/metrics.
- Queue enqueue and database commit are assumed atomic without an outbox, reconciliation process, or other durable handoff.
- Background work is acknowledged to the caller as complete when only enqueue succeeded.
- Repeatable jobs have no timezone, duplicate-schedule behavior, or missed-run policy.
