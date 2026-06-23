# Queue And Cache Design Pressure Tests

Use these scenarios to test whether the skill changes behavior under pressure. A passing answer should block, redirect, or demand the missing decision rather than producing a convenient Redis or queue implementation.

## Test 1: Cache With No Invalidation

Prompt:

```text
Add Redis caching for user account summaries so the dashboard loads faster.
```

Passing behavior:

- Names the authoritative source for account summaries.
- Asks or establishes freshness tolerance, TTL, invalidation trigger, key namespace, tenant/account scoping, value shape, and negative-cache behavior.
- Rejects a cache with no TTL or invalidation story.
- Handoffs to `database-design` if the real bottleneck is query/index shape rather than cache design.

Failing behavior:

- Adds `get/set` cache calls immediately.
- Uses permanent keys.
- Stores full mutable user/account objects without a schema/version or sensitivity check.

## Test 2: Queue Without Idempotency

Prompt:

```text
Move invoice sending into BullMQ with retries because the provider times out sometimes.
```

Passing behavior:

- States that queue execution is at least once.
- Requires idempotency, provider dedupe key or sent-state check, retryable/permanent failure categories, timeout, backoff, concurrency/rate limits, dead-letter handling, and operator replay/discard behavior.
- Checks transaction timing so invoice state and enqueue do not split across a crash.
- Handoffs to `error-handling-design` for public failure state and dead-letter semantics when needed.

Failing behavior:

- Adds a worker that sends the invoice on every retry.
- Stores full invoice payload in the job.
- Treats successful enqueue as successful invoice delivery.

## Test 3: Pub/Sub Used As Durable Eventing

Prompt:

```text
Use Redis pub/sub to publish order events so other services can process them later.
```

Passing behavior:

- Rejects pub/sub if consumers must process events later or recover missed messages.
- Recommends streams, a durable queue, outbox, or event log depending on replay, ordering, and consumer independence requirements.
- Names source of truth, replay behavior, ordering expectations, consumer ownership, failure handling, and monitoring.

Failing behavior:

- Implements `PUBLISH`/`SUBSCRIBE` as if disconnected consumers can replay events.
- Does not discuss loss, replay, offsets, or consumer failure.

## Test 4: Distributed Lock As Race Fix

Prompt:

```text
Prevent duplicate report generation by adding a Redis lock around the report worker.
```

Passing behavior:

- Checks whether idempotency, unique durable state, or job deduplication is the better primary control.
- If a lock remains appropriate, requires expiry, owner token, release check, stale-owner behavior, fencing or durable status checks, timeout behavior, and operator recovery.
- Rejects a lock with no TTL or release ownership check.

Failing behavior:

- Uses `SETNX` with no expiration.
- Deletes the lock without checking ownership.
- Assumes the lock alone prevents duplicate external effects after expiry.

## Skill Test Report

Skill: `queue-and-cache-design`

Test method: fresh isolated RED run without this skill, followed by fresh isolated GREEN run with this skill attached. No repository files were mutated during either run.

RED scenarios:

- Scenario: Cache with pressure.
  Pressure: "Keep it quick; we can figure out invalidation later."
  Baseline failure: The response accepted Redis caching with a short TTL and said to skip complex invalidation for the first pass. It recognized a possible weakness afterward, but the actionable recommendation still allowed cache implementation before the freshness/invalidation contract existed.
- Scenario: Queue with pressure.
  Pressure: "The senior engineer said idempotency is overkill for now. Just get the worker running."
  Baseline failure: The response moved invoice sending into BullMQ with retries, backoff, status logging, and health checks, but only noted idempotency as a weakness afterward. It did not block the retrying worker design before idempotency was defined.
- Scenario: Pub/sub with pressure.
  Pressure: "We already wrote most of the publisher, so don't redesign it."
  Baseline failure: The response finished the Redis pub/sub publisher and documented that pub/sub is best-effort, but still proceeded even though the user required services to process events later.
- Scenario: Distributed lock with pressure.
  Pressure: "Keep it simple with SETNX and delete the key when done."
  Baseline failure: The response improved `SETNX` into tokenized `SET NX EX` with safer release behavior, but still treated a Redis lock as the main answer before checking whether idempotency, queue dedupe, durable uniqueness, lease renewal, fencing, or duplicate-result prevention was the real control.

GREEN result:

- Scenario: Cache with pressure.
  Behavior: The response refused to add Redis caching until freshness tolerance, source of truth, key shape, invalidation triggers, TTL, stampede protection, and observability were defined.
  Pass/fail: Pass. It rejected "figure out invalidation later" as a correctness risk.
- Scenario: Queue with pressure.
  Behavior: The response refused to move invoice sending into BullMQ retries until idempotency, stable job IDs, retry/backoff, dead-letter handling, provider reconciliation, and durable handoff were defined.
  Pass/fail: Pass. It treated idempotency as a hard gate for retrying invoice delivery.
- Scenario: Pub/sub with pressure.
  Behavior: The response rejected Redis pub/sub for events other services must process later and redirected to a durable stream, queue, event log, or outbox-backed event design.
  Pass/fail: Pass. It caught the durability/replay mismatch and did not preserve the wrong primitive because work had already started.
- Scenario: Distributed lock with pressure.
  Behavior: The response rejected plain `SETNX` plus unconditional delete, required TTL, owner token, compare-and-delete release, stale-owner handling, and asked whether queue dedupe, durable uniqueness, or idempotent report state should be the primary duplicate-prevention control.
  Pass/fail: Pass. It treated the lock as a coordination tool rather than a complete correctness guarantee.

Refactor changes:

- Observed loophole: The baseline often added reasonable mechanics while leaving the central correctness decision unresolved.
  Skill change: The skill's Iron Law, operating process, rationalization table, and red flags explicitly gate source of truth, TTL/invalidation, idempotency, retry/dead-letter behavior, pub/sub durability, and lock ownership/fencing before implementation.
  Retest result: GREEN run passed all four scenarios.

Residual risk:

- Trigger language includes broad terms such as `rate limits`, `pub/sub`, and `streams`. The Do Not Use section narrows this by excluding general realtime transport and non-queue/cache API concerns unless Redis, queues, workers, cache lifecycle, or related coordination behavior is directly in scope.
