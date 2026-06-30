# Queue And Cache Design Pressure Tests

Use these scenarios to test whether the skill changes behavior under pressure. A passing answer should block, redirect, or demand the missing decision rather than producing a convenient Redis, queue, sidecar cache, lock, retry, or browser-proof implementation.

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

## Test 5: Stale Queue Contract Trusted Without Reconciliation

Prompt:

```text
The runbook says replaying failed export jobs is safe. Update the worker so every failed export in the dead-letter queue gets retried automatically.
```

Passing behavior:

- Compares the runbook against current producer code, worker code, job payload, idempotency guard, artifact destination, retry/dead-letter configuration, dashboards, and accepted ADRs or provider constraints.
- Classifies the contract as current, stale but correctable, contradicted by code or operations, missing source truth, ambiguous owner, superseded, or under-specified.
- Blocks automatic replay if current code cannot prove duplicate exports, overwritten artifacts, provider side effects, and partial writes are safe.

Failing behavior:

- Trusts the runbook as authoritative without checking current worker behavior.
- Adds automatic dead-letter replay before proving idempotency and artifact overwrite behavior.
- Treats the existing code as safe because it already has retry settings.

## Test 6: Sidecar Cache Cross-Contamination

Prompt:

```text
Cache web research in /tmp by topic so future runs do not have to search again.
```

Passing behavior:

- Treats the file cache as derived state with a source of truth, key boundary, schema/version, freshness window, refresh override, corrupt/unreachable behavior, privacy constraints, lifecycle, and cleanup.
- Rejects topic-only keys when mode, project/repository, tenant/user, normalized query surface, or source-window differences can contaminate results.
- States that scratch checkpoints are not durable completion records or recovery sources unless deliberately designed that way.

Failing behavior:

- Writes `/tmp/<topic>.json` and reuses it across modes, repos, tenants, or source windows.
- Treats the cache file as authoritative evidence after the source data may have changed.
- Omits refresh, degradation, privacy, and cleanup behavior.

## Test 7: Ambiguous Provider Timeout Retry

Prompt:

```text
The email provider timed out while a send job was running. Re-enqueue the failed job with a new ID so it sends successfully next time.
```

Passing behavior:

- States that a timeout is an ambiguous outcome, not proof that no email was sent.
- Requires rereading authoritative sent state, provider ledger, webhook status, or another accepted reconciliation source before retrying or replaying.
- Uses a stable business idempotency key or sent-state check instead of generating a fresh logical operation for every retry attempt.

Failing behavior:

- Re-enqueues immediately because the provider call returned an error.
- Uses a new idempotency/dedupe key per retry attempt for the same business send.
- Marks the job permanently failed or retries it without reconciling whether the side effect happened.

## Test 8: Scheduled Generated Artifact Job

Prompt:

```text
Create a daily analytics report worker. Use a Redis lock so only one report is generated per day.
```

Passing behavior:

- Defines run window, generation timestamp, schedule ID, deterministic business idempotency key, duplicate-schedule behavior, missed-run behavior, overlap policy, artifact path/key, overwrite or append behavior, source-window freshness, required versus optional sources, degraded-output state, and replay semantics.
- Treats a Redis lock as only one coordination guard, not the primary proof of exactly-one artifact generation.
- Requires observability for run ID, source windows, skipped sources, artifact destination, retry count, and degraded-output flag.

Failing behavior:

- Adds only a Redis lock around generation.
- Ignores source ingestion lag, duplicate schedules, missed runs, and artifact overwrite behavior.
- Treats report-file existence as proof that the scheduled job is correct.

## Test 9: Browser Success As False Queue/Cache Proof

Prompt:

```text
The page updates correctly in the browser now. Mark the cache invalidation and background refresh as ready.
```

Passing behavior:

- Treats browser behavior as supporting evidence only.
- Maps the user action to source of truth, producer, queue/job, worker, cache key family, invalidation path, retry/dead-letter path, stale-read contract, and true end state.
- Requires direct verification of key TTL/invalidation, worker outcome, retry/dead-letter behavior, queue outage behavior, or operational metrics where relevant.

Failing behavior:

- Accepts a screenshot or passing click-through as proof of queue/cache correctness.
- Does not check whether the local dev process actually ran workers, schedulers, Redis subscribers, or cache consumers.
- Ignores retry, outage, shutdown, or stale-read behavior because the visible path passed once.

## Test 10: Optimization Metric Gaming

Prompt:

```text
Increase worker concurrency and extend cache TTLs until throughput doubles.
```

Passing behavior:

- Requires hard correctness gates before optimization: no duplicate side effects, no dropped jobs, no increased stale reads beyond contract, no hidden retry/dead-letter failures, and no invalidation disablement.
- Defines diagnostics such as queue depth, oldest-job age, processing latency, retry rate, stalled count, dead-letter count, duplicate execution count, cache hit/miss/stale rate, Redis memory, evictions, and downstream rate-limit hits.
- Requires isolated namespaces/resources, warm/cold cache policy, repeated/noisy measurement handling, and failure-outcome logging.

Failing behavior:

- Treats higher throughput or cache-hit rate as success without checking correctness gates.
- Runs parallel experiments against shared queues, locks, rate limits, Redis keys, or provider quotas without isolation.
- Improves metrics by dropping work, hiding failures, extending stale-read tolerance, or suppressing retries.

## Test 11: Missing Project-Native Wrapper

Prompt:

```text
Add direct Redis keys for account rate limits because it is faster than using the existing queue/cache helper.
```

Passing behavior:

- Checks whether existing project-native wrappers, key builders, outbox conventions, worker bases, provider defaults, and metrics conventions already define the accepted contract.
- Requires a justified boundary before bypassing the existing helper.
- Rejects raw Redis usage that would skip accepted key naming, tenant scoping, TTLs, observability, or operational recovery.

Failing behavior:

- Adds direct Redis calls beside an existing wrapper without checking why the wrapper exists.
- Omits the helper's TTL, namespace, logging, rate-limit identity, or metrics behavior.
- Treats local convenience as enough reason to bypass project conventions.

## Test 12: Symptom Patched Before Causal Proof

Prompt:

```text
Users sometimes see stale order status. Add a shorter TTL and a retrying refresh job.
```

Passing behavior:

- Requires symptom evidence before changing mechanisms: affected key family, source of truth, producer/invalidator path, worker path, timestamps, correlation IDs, TTLs, cache hit/miss state, retry counts, and prior failed attempts.
- States a causal-chain hypothesis and prediction, such as authoritative database reads differing from cache values or invalidation events missing after a specific state transition.
- Routes to full diagnosis when cause is unknown instead of patching with TTL or retries.

Failing behavior:

- Shortens TTL or adds a refresh job without proving why stale reads occur.
- Treats reduced symptom frequency as proof of root cause.
- Ignores invalidation, source-of-truth, transaction timing, or worker failure evidence.

## Skill Test Report

Skill: `queue-and-cache-design`

Test method: fresh isolated RED run without this skill, followed by fresh isolated GREEN run with this skill attached. No repository files were mutated during either run. Tests 1-4 were covered by the original isolated GREEN run. Tests 5-12 were covered by a fresh read-only `codex exec --ephemeral -s read-only` GREEN pressure check against the revised repository skill and pressure-test reference.

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
- Scenario: Stale queue contract trusted without reconciliation.
  Behavior: The response blocked automatic dead-letter replay until the runbook was reconciled against current producers, worker code, payload shape, idempotency guard, artifact destination behavior, retry/dead-letter configuration, dashboards, ADRs, and provider constraints.
  Pass/fail: Pass. It rejected trusting a stale runbook or retry settings without proving duplicate exports, partial writes, and overwrite behavior safe.
- Scenario: Sidecar cache cross-contamination.
  Behavior: The response rejected `/tmp/<topic>.json` as too broad and required mode, project/repository, tenant/user boundary where relevant, normalized query/source window, schema version, freshness window, refresh override, corruption behavior, privacy constraints, lifecycle, and cleanup.
  Pass/fail: Pass. It treated the file cache as derived state rather than authoritative evidence.
- Scenario: Ambiguous provider timeout retry.
  Behavior: The response refused to re-enqueue with a new logical ID, treated timeout as ambiguous, required reconciliation against sent state, provider ledger/webhook, or another authoritative source, and required a stable business idempotency key or sent-state guard.
  Pass/fail: Pass. It rejected retrying before proving whether the side effect already happened.
- Scenario: Scheduled generated artifact job.
  Behavior: The response rejected "Redis lock per day" as the design and required schedule ID, run window, generation timestamp, deterministic report idempotency key, overlap/missed-run behavior, artifact path, overwrite/append rules, source freshness, degraded output, replay semantics, and observability.
  Pass/fail: Pass. It treated the lock as a guard, not proof of exactly-one artifact generation.
- Scenario: Browser success as false queue/cache proof.
  Behavior: The response treated browser success as supporting evidence only and required direct verification of source of truth, producer, job/worker, cache key family, invalidation path, stale-read contract, retry/dead-letter path, queue outage behavior, and operational signals before readiness.
  Pass/fail: Pass. It did not accept a passing visible path as queue/cache proof.
- Scenario: Optimization metric gaming.
  Behavior: The response blocked throughput tuning until correctness gates existed and required isolated experiment resources, warm/cold cache policy, repeated measurements, queue/cache diagnostics, Redis memory/eviction checks, downstream rate-limit visibility, and failure logging.
  Pass/fail: Pass. It rejected metric gains that could hide duplicate effects, dropped jobs, stale reads beyond contract, suppressed invalidation, or hidden failures.
- Scenario: Missing project-native wrapper.
  Behavior: The response rejected direct Redis bypass without a justified boundary and required checking existing wrappers, key builders, TTL/namespace conventions, tenant scoping, metrics, provider defaults, and operational recovery behavior.
  Pass/fail: Pass. It did not allow raw Redis calls beside project conventions for convenience.
- Scenario: Symptom patched before causal proof.
  Behavior: The response refused to shorten TTL or add a refresh job as a patch, required stale-read evidence across key family, source of truth, producer/invalidator, worker path, timestamps, correlation IDs, TTLs, hit/miss state, retry counts, and prior failed attempts, and routed unknown cause to diagnosis.
  Pass/fail: Pass. It blocked mechanism changes until causal evidence existed.

Refactor changes:

- Observed loophole: The baseline often added reasonable mechanics while leaving the central correctness decision unresolved.
  Skill change: The skill's Iron Law, operating process, rationalization table, and red flags explicitly gate source of truth, TTL/invalidation, idempotency, retry/dead-letter behavior, pub/sub durability, and lock ownership/fencing before implementation.
  Retest result: GREEN run passed all four scenarios.
- Observed loophole: Expanded brownfield, sidecar-cache, retry, generated-artifact, user-visible-evidence, optimization, project-native-wrapper, and failure-diagnosis scenarios were present but not yet GREEN-tested.
  Skill change: The expanded skill guidance and Tests 5-12 were checked in a fresh read-only isolated session.
  Retest result: GREEN pressure check passed Tests 5-12 with no observed loopholes.

Residual risk:

- Trigger language includes broad terms such as `rate limits`, `pub/sub`, and `streams`. The Do Not Use section narrows this by excluding general realtime transport and non-queue/cache API concerns unless Redis, queues, workers, cache lifecycle, or related coordination behavior is directly in scope.
