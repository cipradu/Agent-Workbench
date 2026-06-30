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
- Designing or reviewing sidecar/file caches, build/research/agent caches, scratch checkpoints, generated artifact caches, or other non-Redis derived state.
- Changing how application code crosses from synchronous request handling into asynchronous processing.
- Reviewing an existing queue/cache system where producers, consumers, workers, schedulers, keys, dashboards, runbooks, ADRs, or prior incidents may disagree.
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
- The work is generic root-cause diagnosis, code-review orchestration, browser testing, simulator testing, setup, commits, pushes, PRs, CI watch, tracker filing, or release mechanics. Use the owning diagnosis, testing, review, setup, git, PR, or workflow skill.
- A project has a stricter accepted queue/cache ADR, operations standard, platform convention, or provider constraint. Follow that source of truth and use this skill only for gaps.

## Iron Law

Queues and caches are coordination contracts, not faster storage. Do not add Redis keys, cache layers, jobs, workers, retries, locks, rate limits, pub/sub, or streams until source of truth, consistency/expiry, idempotency, failure/retry behavior, concurrency limits, ownership, and observability/recovery are explicit.

## Core Concept

Queues move work across time and process boundaries. Caches trade freshness and memory for latency. Redis-backed coordination is usually ephemeral unless explicitly designed and operated as durable infrastructure. Correct design starts by deciding what remains authoritative, what may be stale or replayed, what happens more than once, what can be lost, and how an operator proves the system is healthy.

BullMQ-style queues are at-least-once execution systems. A job may run more than once, may be retried after partial work, may stall, and may fail permanently. Cache entries are derived data unless the project has explicitly accepted Redis as authoritative for that specific state.

File caches, scratch checkpoints, generated reports, and local runtime artifacts are still cache-like derived state when they can be reused across requests, runs, users, tenants, repositories, or time windows. Treat them with the same source-of-truth, keying, freshness, privacy, lifecycle, and degradation discipline as Redis-backed caches.

Existing queue/cache systems are evidence, not automatic authority. Before changing a brownfield system, reconcile current code/configuration with accepted ADRs, specs, worker conventions, scheduler definitions, key inventories, dashboards, alerts, runbooks, tests, provider constraints, and recent incidents.

## Operating Process

Run these steps in order.

### 1. Establish The Boundary And Source Of Truth

Identify the runtime surface before choosing Redis or a queue:

- scope synthesis: stated requirement, inferred consistency assumptions, explicitly out-of-scope guarantees, and unresolved facts that would change primitive choice;
- surface type: cache, background job, delayed job, repeatable job, worker flow, rate limit, lock, dedupe key, idempotency key, pub/sub, stream, or ephemeral state;
- source of truth: database row, external service, filesystem/object storage, event log, queue state, Redis key, in-memory process state, or another owner;
- correctness requirement: fresh read, stale-while-revalidate, eventual consistency, at-least-once execution, at-most-once notification, durable replay, best-effort fan-out, or coordination-only state;
- ownership: producer, consumer, invalidator, worker, scheduler, operator, and code owner;
- existing-system evidence: producer paths, worker paths, scheduler definitions, key families, queue names, wrapper clients, provider defaults, retry/dead-letter configuration, metrics, dashboards, runbooks, ADRs, and tests that currently define behavior;
- environment: Redis/provider/deployment model, persistence mode, eviction policy, cluster/sentinel behavior, connection lifecycle, tenant boundaries, and sensitive data constraints.

When exactly one missing fact changes the design path, ask or block on that fact only: acceptable staleness, whether missed messages are recoverable, which state is authoritative, what duplicate side effect is dangerous, whether a provider response may be ambiguous, or who owns dead-letter replay.

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
- Use existing project-native queue/cache wrappers, key builders, outbox conventions, worker bases, and metrics conventions when they already provide the accepted contract; do not add raw Redis or queue usage beside them without a justified boundary.
- Treat foreground parallel work as ordinary concurrency when the caller waits for all results. Choose a queue only when work crosses a time/process boundary and needs retry, delay, durability, rate limits, worker lifecycle, or operational recovery.

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
- For sidecar/file caches, include domain or mode, normalized query or focus surface, project/repository discriminator, tenant/user boundary when relevant, schema/version, freshness window, refresh override, corrupt/unreachable behavior, privacy constraints, lifecycle, and cleanup.
- Mark best-effort scratch checkpoints as non-authoritative unless durability, retention, replay, cleanup, and operator semantics are deliberately accepted. Checkpoints must not become hidden queue state, completion records, or recovery sources by accident.
- Define cache degradation: on miss, corrupt entry, unreachable cache, stale source, or incompatible schema, decide whether the system recomputes, bypasses, serves stale, blocks, warns, fails closed, or escalates.

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
- For scheduled or generated-artifact jobs, define run window, generation timestamp, deterministic business idempotency key, duplicate-run behavior, overlap policy, artifact key/path, overwrite/append behavior, source-window freshness, required versus optional sources, degraded-output state, and replay semantics.

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
- After an ambiguous outcome such as timeout, 5xx, lost acknowledgement, worker crash after a side effect, provider pending response, or uncertain dead-letter replay, reread authoritative state, provider ledger, or artifact destination before retrying, replaying, re-enqueueing, or declaring failure. Stable business idempotency keys are not the same as attempt IDs or worker run IDs.

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
- For runtime-impacting changes, name operational validation fields: log queries or search terms, metric/dashboard names, healthy signals, failure signals, rollback or mitigation trigger, validation window, and owner.

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
- existing wrappers, project conventions, ADRs, runbooks, and provider defaults have been checked before claiming a gap;
- ambiguous side effects have an authoritative readback/reconciliation path before retry or replay;
- tests or review evidence cover cache miss/hit/stale behavior, invalidation, repeated job execution, retry, failure, dead-letter/replay, worker shutdown, and queue outage behavior where relevant.

Completion criterion: the design can be implemented and operated without relying on "Redis is fast" or "the queue will handle it" as hidden assumptions.

Failure output: `Not ready: queue/cache design is missing <specific consistency/idempotency/TTL/retry/worker/observability criterion>.`

## Existing-System, Review, And Diagnosis Branches

Use these branches inside the operating process when the prompt is a review, an existing-system change, or a failure symptom.

### Existing-System Reconciliation

Before trusting an existing queue/cache contract, classify the relevant artifacts:

- `current/no change`: code, docs, configuration, operations, and accepted decisions agree.
- `stale but mechanically correctable`: names, paths, metrics, or constants drifted while semantics stayed stable.
- `contradicted by code or operations`: accepted guidance and live behavior disagree.
- `missing source of truth`: no artifact owns freshness, durability, idempotency, retry, or recovery semantics.
- `ambiguous owner`: producer, worker, invalidator, scheduler, operator, or replay owner is unclear.
- `superseded by ADR/provider constraint`: a later accepted decision or provider guarantee changes the local assumption.
- `too under-specified to design safely`: the contract cannot support implementation or review.

Changed delivery guarantees, Redis authority, idempotency model, retry/dead-letter behavior, lock strategy, pub/sub durability expectation, or source-of-truth ownership require design/spec/architecture work. Do not hide those changes as local cleanup.

### Review Findings

Queue/cache review findings need concrete evidence. Include the affected surface type, key family/job type/worker/producer path, source-of-truth impact, observable consequence, cited current-scope or pre-existing evidence, blocker/advisory status, suggested correction, required verification, and residual risk.

Suppress findings when the concern is speculative, load/cardinality evidence is missing, the issue is already handled by project wrappers, middleware, library defaults, accepted configuration, durable uniqueness, or a prior ADR, or the finding is only a generic "consider caching" suggestion without a failure mode.

### Failure-Driven Diagnosis

For duplicate jobs, stale reads, stampedes, stalled workers, poison jobs, lost messages, lock races, retry storms, unbounded Redis growth, or repeated failed fixes, gather symptom evidence before changing mechanisms:

- observed symptom, trigger, affected key family or job type, source of truth, producer path, worker path, provider/Redis mode, relevant timestamps, correlation/job IDs, retry counts, lock owner/token, TTLs, invalidation path, worker concurrency, and prior failed attempts;
- causal chain from trigger to stale data, duplicate work, lost notification, lock corruption, backlog, retry storm, or memory growth;
- prediction for uncertain causes, such as authoritative reads differing under stale-cache theory, repeated business idempotency keys under duplicate-retry theory, lock duration/token evidence under stale-owner theory, or missing replay state under pub/sub-loss theory.

If evidence points to a generic root-cause investigation, route to `structured-problem-resolution` before changing retries, TTLs, invalidation, locks, workers, or primitives.

### Measurement And User-Visible Evidence

Optimization is allowed only after correctness gates are fixed. Before tuning TTLs, worker concurrency, batch size, retry/backoff, lock TTLs, rate-limit windows, cache key shape, or provider settings, define hard correctness gates, diagnostics, isolated queue/cache namespaces or resources, warm/cold cache policy, variance handling, and failure-outcome logging.

Browser, dogfood, simulator, screenshot, report-file, or user-visible success is supporting evidence only. If UI or journey behavior depends on async/cache state, map entry action, producer, queue/job, cache key, source of truth, worker, idempotency guard, retry/dead-letter path, invalidation path, destination, and true end state, then still verify the queue/cache contract directly.

## Output Contract

For queue/cache design or review, include:

- scope synthesis: stated requirement, inferred assumptions, out-of-scope guarantees, and any blocking missing fact;
- boundary and source-of-truth summary;
- chosen primitive and rejected alternatives;
- existing-system reconciliation result when changing or reviewing brownfield behavior;
- key families, TTLs, invalidation, memory, and sensitive-data handling, when relevant;
- job types, payload contracts, idempotency, retries, backoff, timeouts, concurrency, and dead-letter behavior, when relevant;
- producer transaction and side-effect timing, when relevant;
- worker lifecycle, observability, and recovery path, when relevant;
- review finding shape or failure-diagnosis evidence when the prompt is a review or symptom;
- runtime validation fields for operationally meaningful changes;
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
- Use `structured-problem-resolution` when a queue/cache symptom needs full root-cause diagnosis before selecting a mechanism.
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
| "The UI looks right, so the queue/cache works." | One visible journey does not prove retry, replay, idempotency, invalidation, outage, shutdown, or lock behavior. | Use user-visible evidence as a signal, then verify the queue/cache contract directly. |
| "The timeout failed, so retry the job." | Ambiguous provider or worker outcomes may have already produced the side effect. | Reread authoritative state or provider/artifact destination before retrying or replaying. |
| "This is just a temp file cache." | Sidecar caches and scratch checkpoints can leak stale, cross-tenant, cross-repo, or privacy-sensitive state. | Define source of truth, key boundary, schema/version, freshness, degradation, lifecycle, and cleanup. |
| "Current docs say this is safe." | Queue/cache contracts drift across code, workers, schedules, runbooks, dashboards, ADRs, and provider behavior. | Reconcile current artifacts and classify stale or contradicted assumptions before acting. |

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
- Existing producers, workers, scheduler definitions, key inventories, runbooks, dashboards, or ADRs disagree and the design trusts one without reconciliation.
- A review finding recommends caching, higher concurrency, a retry, a lock, or a TTL change without concrete source-of-truth, load, failure, or operational evidence.
- A cache-like sidecar file, scratch checkpoint, build cache, research cache, or generated artifact has no key boundary, schema/version, freshness, privacy, or degradation policy.
- A retry, replay, or dead-letter action follows an ambiguous side effect without first rereading authoritative state or provider/artifact destination.
- Browser, screenshot, simulator, or generated-report success is treated as proof of queue/cache correctness.
