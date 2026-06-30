# MySQL And MariaDB

Use this reference when applying the database-design skill to MySQL, MariaDB, or InnoDB-specific schema, query, migration, index, locking, replication, pooling, or operational behavior.

Always apply the general database rules first. This reference covers MySQL/MariaDB-specific consequences and gotchas.

## Version And Engine Check

Start by identifying:

- MySQL versus MariaDB;
- exact version;
- storage engine, usually InnoDB for transactional application data;
- hosting platform restrictions;
- replication topology;
- migration/online DDL tooling.

MySQL and MariaDB diverge in SQL details. Do not assume syntax or behavior is portable without checking the target engine and version.

When project artifacts disagree, prefer current MySQL/MariaDB evidence for engine-specific behavior: exact server family/version, InnoDB settings, deployed constraints/indexes, migration history, DDL algorithm support, replication topology, and hosting restrictions. Treat copied MySQL examples, stale ORM metadata, generated schema output, and generic SQL assumptions as untrusted until checked against the target engine.

Failure output: `Blocked: MySQL/MariaDB version or engine behavior must be verified before use: <specific feature>.`

## Schema Defaults

Common defaults:

- use InnoDB for transactional application tables;
- use `utf8mb4` character sets/collations, not legacy `utf8`/`utf8mb3`;
- use `BIGINT UNSIGNED AUTO_INCREMENT` for write-heavy internal OLTP primary keys unless a different key strategy is justified;
- avoid random UUID values as clustered primary keys on hot tables because InnoDB stores rows by primary key order;
- if externally opaque IDs are needed, consider a secondary unique `BINARY(16)` UUID/UUIDv7/ULID-style value while keeping the clustered primary key narrow and monotonic;
- use `DECIMAL(p, s)` for exact values such as money or billing quantities, not `FLOAT`/`DOUBLE`;
- use `DATETIME` for application timestamps stored in UTC when avoiding `TIMESTAMP` timezone conversion and 2038 limits matters;
- prefer lookup tables or constrained string/status tables over `ENUM` when values change often.

Completion criterion: primary key, charset/collation, timestamp, and exact numeric choices account for MySQL/InnoDB behavior.

## Indexing

Rules:

- composite indexes follow the leftmost-prefix rule;
- equality columns generally come before range/sort columns;
- a range predicate can stop use of later columns in a composite index;
- secondary indexes include the primary key value, so wide primary keys make every secondary index larger;
- use prefix indexes for long strings only when the prefix is selective enough;
- for frequently queried JSON paths, expose generated columns and index those columns;
- confirm with `EXPLAIN`, and use `EXPLAIN ANALYZE` only when it is safe because it executes the query.

EXPLAIN signals to investigate:

- `type: ALL` on a large table;
- `key: NULL` when a selective predicate exists;
- very high `rows` estimates for interactive paths;
- `Using temporary`;
- `Using filesort`;
- broad `Using where` on large scans.

Failure output: `Rejected: MySQL index/query change is not tied to EXPLAIN evidence or leftmost-prefix behavior.`

## Query Patterns

Avoid:

- `SELECT *` in hot paths;
- deep `OFFSET` pagination;
- N+1 query loops;
- functions on indexed columns in predicates;
- JSON for relational ownership, foreign keys, tenant keys, lifecycle state, or heavily filtered fields;
- full-text search when the requirements need typo tolerance, advanced ranking, multi-table facets, or language features beyond MySQL built-ins.

Prefer:

- explicit selected columns;
- keyset pagination with an index matching the cursor;
- generated columns for indexed JSON paths;
- `UNION ALL` when deduplication is unnecessary;
- batched inserts/updates sized for lock time and replication impact.

## Transactions, Locks, And Isolation

Rules:

- keep transactions short;
- do external API calls before opening the transaction;
- lock rows in deterministic order across code paths;
- index predicates used by `UPDATE`, `DELETE`, and locking reads;
- on deadlock, roll back and retry the whole transaction with a bounded retry budget;
- capture InnoDB deadlock diagnostics soon after the deadlock when possible because the diagnostic state is overwritten by later events.

InnoDB isolation guidance:

- `REPEATABLE READ` is the default and is often correct for OLTP, but next-key/gap locks can surprise applications;
- switch to `READ COMMITTED` only with a measured reason such as confirmed gap-lock contention, and prefer per-session scope over global changes;
- avoid `READ UNCOMMITTED`;
- use `SERIALIZABLE` only when the project explicitly accepts the contention cost;
- use `SKIP LOCKED` only for queue-like workloads where skipping locked rows is acceptable. It is not a general consistency mechanism.

Failure output: `Rejected: MySQL transaction plan ignores gap locks, deterministic lock order, or whole-transaction retry.`

## Online DDL And Migrations

Not all `ALTER TABLE` operations are equally safe.

Rules:

- check whether the operation is `INSTANT`, `INPLACE`, or `COPY` for the target version/table;
- request safe algorithms/lock levels where supported so unsafe fallback fails loudly;
- test large-table DDL on realistic data or replicas first;
- account for metadata locks at the start/end of DDL;
- consider online schema-change tooling for huge or high-write tables when native DDL is not safe;
- include replication lag impact in the rollout plan.

Failure output: `Rejected: MySQL migration does not account for DDL algorithm, metadata locks, or replication impact.`

During review, explicitly look for hidden metadata-lock and gap-lock risk when a diff changes large tables, indexes, predicates used by `UPDATE`/`DELETE`, online DDL options, isolation settings, or migration ordering. A migration that is harmless on an empty local database can still block production writes or replicas.

## Replication And Read Consistency

MySQL replication is commonly asynchronous. Reads from replicas may be stale.

Rules:

- do not route read-your-own-write paths to replicas immediately after writes;
- keep checkout, permission checks, idempotency-key reads, and user-visible consistency reads on primary unless an explicit lag-wait/sticky-read strategy exists;
- monitor replica SQL thread health, IO thread health, and lag;
- large transactions and blocking DDL can cause replica lag spikes;
- check version-specific terminology and commands before standardizing diagnostics.

Failure output: `Rejected: replica read strategy can return stale data for a consistency-sensitive path.`

For read-only reporting or operational observers:

- prefer read-only users and replicas only when stale reads are acceptable;
- keep checkout, permission, idempotency, and read-your-own-write paths on primary unless a lag-wait/sticky-read strategy exists;
- bound queries by indexed predicates, time windows, limits, or batches;
- select only required columns and avoid sensitive verifier or payload fields;
- account for long reads and large transactions that can increase replication lag.

Failure output: `Rejected: MySQL read-only observer path ignores replica lag, privileges, query bounds, or sensitive data exposure.`

## Pooling, Timeouts, And Security

Rules:

- size pools from workload and server capacity, not copied constants;
- keep application pool recycling below server idle timeouts where applicable;
- use pre-ping/health checks when the driver supports it and stale connections are possible;
- require TLS when traffic crosses hosts or networks;
- store credentials in the platform secret manager, not repository files;
- separate migration/admin users from runtime users;
- grant runtime users only the permissions required for normal application operations.

## Verification Checklist

- Engine and version are known, including MySQL versus MariaDB.
- InnoDB/charset/collation/PK choices are deliberate.
- MySQL/MariaDB syntax differences are checked for upserts, locks, generated columns, JSON, and diagnostics.
- Indexes follow leftmost-prefix and primary-key-size implications.
- DDL algorithm/lock behavior is known for production migrations.
- Gap locks, deadlocks, and retry behavior are addressed.
- Replica lag and read-after-write paths are addressed.
- Runtime and migration privileges are separated.
