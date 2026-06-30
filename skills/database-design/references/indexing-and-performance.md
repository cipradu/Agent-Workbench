# Indexing And Performance

Use this reference when adding/reviewing indexes, optimizing queries, choosing pagination, partitioning large tables, diagnosing N+1 behavior, reviewing connection pools, or changing performance-sensitive SQL.

## Evidence Before Optimization

Start from evidence:

- exact query shape, including filters, joins, grouping, sorting, limits, and selected columns;
- expected and current data volume;
- frequency and latency target;
- existing indexes and constraints;
- execution plan or representative benchmark when available;
- write-path cost and migration/locking cost.

For measured database optimization, separate hard gates from diagnostics.

Hard gates that metrics cannot override:

- result correctness and selected-column shape;
- tenant/permission/soft-delete visibility;
- parameterization and identifier safety;
- transaction, lock, and isolation behavior;
- migration/backfill safety and rollback/recovery;
- replica/read-after-write consistency where relevant;
- credential and sensitive-column exposure rules.

Diagnostics may include latency, throughput, query plan shape, buffer reads, rows scanned, lock wait, pool wait, CPU, IO, memory, and replication lag. Diagnostics support a recommendation only after hard gates pass.

When reading an execution plan, capture the details that explain behavior, not just whether an index appears:

- scan type and whether the table size makes that scan acceptable;
- join strategy and whether it matches expected row counts;
- estimated rows versus actual rows when actual execution data is safe to gather;
- loops, sort/hash operations, memory or disk spill indicators, and buffer/cache reads when the engine reports them;
- whether an index-only plan still needs heap/table reads;
- before/after plan evidence for material optimization claims, or the explicit reason plan evidence is unavailable.

Failure output: `Rejected: optimization is not backed by query shape, data volume, or plan evidence.`

## Measured Optimization Evidence

Use a lightweight evidence table when comparing query/index/pool/batch variants:

| Candidate | Primary metric | Baseline | Workload/fixture | Plan/stat evidence | Hard gates | Noise/residual risk |
| --- | --- | --- | --- | --- | --- | --- |

Rules:

- choose one primary metric before comparing variants;
- use representative data and stable fixtures where possible;
- keep validation queries or result checks immutable across candidates;
- account for warm cache, cold cache, concurrent load, and background jobs when they materially change results;
- do not run competing database experiments against the same shared state in parallel unless isolation is proven;
- look for prior project learning, ADRs, incidents, or runbooks before repeating a risky experiment;
- require explicit approval before adding extensions, engine settings, new infrastructure, or persistent operational complexity.

Rejected shortcut: do not optimize for a proxy such as local page load, smaller diff, clean PR state, or a single lucky query run when the database workload and hard gates are not represented.

## Index Selection

Index candidates:

- columns used in common `WHERE` predicates;
- join keys;
- foreign key columns when the engine does not index them automatically;
- uniqueness constraints;
- columns used for common `ORDER BY` or pagination;
- partial/filtered predicates for hot subsets;
- specialized structures for JSON, full-text, geospatial, vector, range, or array queries when the engine supports them and the query path is real.

Composite index guidance:

- equality columns usually come before range columns;
- the index order should match the query predicate and sort pattern;
- account for selectivity and left-prefix behavior in the target engine;
- avoid maintaining multiple indexes that serve the same access path.

Rejected shortcut: do not add broad indexes "just in case." Every index taxes writes, storage, backups, and migration operations.

## Query Shape

Common anti-patterns:

- `SELECT *` in production paths, especially on wide or sensitive tables;
- unbounded queries without `LIMIT` or a streaming/batch strategy;
- functions on indexed columns in `WHERE` clauses that prevent index use;
- N+1 query loops;
- `DISTINCT` hiding incorrect joins;
- `COUNT(*)` for existence checks when `EXISTS` or a limited query is sufficient;
- dynamic SQL built by string concatenation;
- dynamic identifiers without allowlists;
- offset pagination on deep or large datasets.

Better patterns:

- select only required columns;
- use parameterized values;
- use range predicates that preserve index use;
- batch related lookups or join when appropriate;
- use keyset/cursor pagination for large/deep pages;
- order deterministically when paginating;
- use `EXPLAIN` or engine-specific plan tools before and after major changes.

## Pagination

Offset pagination is acceptable when:

- result sets are small or bounded;
- users will not navigate deep pages;
- latency is acceptable at expected offsets;
- ordering is deterministic.

Use keyset/cursor pagination when:

- tables are large;
- pages can be deep;
- stable performance matters;
- inserts/deletes can happen while paginating;
- a suitable indexed cursor column or composite cursor exists.

Completion criterion: the pagination strategy names ordering, cursor/offset behavior, and index support.

## Partitioning And Retention

Consider partitioning when:

- a table is very large and mostly queried by time, tenant, region, or another natural partition key;
- retention/purge operations need to drop chunks efficiently;
- operational maintenance on the whole table is too expensive;
- query plans can prune partitions reliably.

Do not partition by default. Partitioning adds operational procedures, constraint/index implications, rollover jobs, and tooling complexity.

## Connection Pools And Batches

Connection pools must match database capacity and workload. Monitor:

- open connections;
- in-use connections;
- idle connections;
- wait count and wait duration;
- timeouts;
- slow query counts;
- connection churn after failover/redeploy.

Batching rules:

- avoid row-by-row work when a bounded batch is safe;
- avoid giant batches that hold locks, consume memory, or exceed timeout windows;
- tune batch size from row size, query cost, lock time, and database load;
- make batch jobs resumable when they touch durable data.

## Verification Checklist

Before accepting a performance change:

- query shape and access path are documented;
- existing indexes checked;
- plan/statistics or representative benchmark reviewed when material, including before/after evidence for claimed improvements;
- write overhead and migration cost considered;
- N+1 and unbounded scans checked;
- pagination is deterministic and indexed;
- sensitive/wide columns are not fetched unnecessarily;
- connection/pool impact is monitored when relevant;
- measured optimization evidence includes baseline, workload, hard gates, before/after evidence, and residual risk when performance claims are material.
