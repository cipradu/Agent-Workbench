# PostgreSQL

Use this reference when applying the database-design skill to PostgreSQL-specific schema, query, migration, index, transaction, replication, backup, or operational behavior.

Always apply the general database rules first. This reference covers PostgreSQL-specific consequences and gotchas.

## Version And Extension Check

Before using a PostgreSQL-specific feature, identify:

- PostgreSQL major version;
- hosted service restrictions;
- enabled extensions;
- migration tool behavior;
- whether the change runs on primary, replica, or both.

Version matters for features such as `UNIQUE NULLS NOT DISTINCT`, generated identity behavior, JSON/path features, index options, logical replication capabilities, and extension availability.

When project artifacts disagree, prefer current PostgreSQL evidence for PostgreSQL-specific behavior: server major version, enabled extensions, deployed constraints/indexes, migration history, `EXPLAIN` output, replica topology, and hosting restrictions. Treat old ORM examples, stale generated schema, copied migration snippets, and generic SQL assumptions as untrusted until checked against the target version.

Failure output: `Blocked: PostgreSQL feature/version behavior must be verified before use: <specific feature>.`

## Schema And Data Types

Common defaults:

- use `timestamptz` for event/application timestamps, store UTC at rest, and convert at boundaries;
- avoid `timestamp` without time zone, `timetz`, and precision-qualified timestamp types such as `timestamptz(0)` unless a project convention explicitly requires them;
- use `date` for date-only values and `interval` for durations;
- use `numeric` for exact decimal values;
- use `text` unless a length limit is a real domain rule, and prefer `CHECK (length(value) <= n)` for domain limits instead of arbitrary `varchar(n)`;
- avoid `char(n)` for application strings because padding semantics create surprising comparisons and storage behavior;
- use native `uuid` when UUIDs are needed, not `text`;
- prefer `BIGINT GENERATED ALWAYS AS IDENTITY` for simple internal surrogate keys when project conventions allow;
- avoid `serial` for new designs when identity columns are available;
- avoid `money` because formatting/locale and precision behavior can surprise applications;
- prefer check constraints or lookup tables over PostgreSQL enums when values change often;
- use `boolean NOT NULL` unless the domain truly has three states;
- use arrays only for bounded embedded lists or element queries, not as a substitute for relationships that need referential integrity;
- use range types for intervals that need overlap/containment logic, and pick bounds consistently, usually `[)`;
- use expression indexes on normalized text such as `lower(email)` for simple case-insensitive lookup; use nondeterministic collations or `citext` only when the project needs their specific semantics.

PostgreSQL gotchas:

- unquoted identifiers fold to lowercase; avoid quoted mixed-case names;
- PostgreSQL does not automatically index foreign key columns;
- ordinary unique constraints allow multiple `NULL` values; PostgreSQL 15+ supports `UNIQUE (...) NULLS NOT DISTINCT` when one-null semantics are required;
- sequence/identity gaps are normal after rollbacks, crashes, failed inserts, and concurrent transactions;
- PostgreSQL heap tables are not physically clustered by primary key by default.
- length and precision overflows error instead of silently truncating or rounding;
- `now()` returns the transaction start time; use `clock_timestamp()` only when the true wall-clock time during the statement is required;
- large `text`, `bytea`, and JSONB values may move to TOAST storage. Do not tune TOAST settings by default, but account for wide-row fetch cost and update bloat.

Completion criterion: data type and identifier choices account for PostgreSQL semantics instead of generic SQL assumptions.

## Constraints

Use PostgreSQL constraints as durable enforcement, not documentation.

Rules:

- name important constraints and indexes deterministically when migration tooling permits it;
- pair foreign keys with explicit indexes on the referencing columns when joins, parent updates, or parent deletes need them;
- choose `ON DELETE` and `ON UPDATE` actions from lifecycle ownership, not convenience;
- use `DEFERRABLE INITIALLY DEFERRED` only when a real transaction-level invariant, such as circular references, requires end-of-transaction validation;
- remember that `CHECK` constraints pass when the expression evaluates to unknown because of `NULL`; combine `CHECK` with `NOT NULL` when null values are invalid;
- use `UNIQUE (...) NULLS NOT DISTINCT` on PostgreSQL 15+ when duplicate nulls would violate the domain;
- use exclusion constraints, usually with GiST, for non-overlap invariants such as reservations, ranges, or effective-date intervals.

Failure output: `Rejected: PostgreSQL constraint design does not enforce the stated invariant: <specific invariant>.`

## Indexing

Use indexes for real access paths:

- B-tree for equality, ranges, sorting, and most ordinary lookup paths;
- composite indexes matching equality columns before range/sort columns;
- partial indexes for frequent filtered subsets such as active or non-deleted rows;
- covering indexes with `INCLUDE` for hot read paths that can avoid heap access;
- expression indexes when a necessary predicate uses a function or normalized value;
- GIN for JSONB containment, arrays, and full-text search;
- GiST for ranges, geometric types, and some full-text/geospatial patterns;
- BRIN for very large append-heavy tables with physical order correlation, often time-series/event data.

Rules:

- add indexes on foreign key columns when joins/deletes/updates need them;
- confirm planner use with `EXPLAIN` or `EXPLAIN (ANALYZE, BUFFERS)` when safe;
- when reviewing PostgreSQL plans, check scan type, join strategy, estimated versus actual rows, loops, sort/hash spills, buffer reads, and whether index-only scans still visit the heap;
- use `CREATE INDEX CONCURRENTLY` for production tables when avoiding blocking writes matters;
- avoid dropping indexes solely because recent stats show low usage; confirm with a human/project owner because stats windows can miss periodic jobs.

Failure output: `Rejected: PostgreSQL index change lacks access-path evidence or operational safety.`

## Query Patterns

Avoid:

- `SELECT *` in production paths;
- unbounded queries;
- functions on indexed columns unless a matching expression index exists;
- deep `OFFSET` pagination;
- N+1 query loops;
- `DISTINCT` masking broken joins;
- large BLOB/object storage in PostgreSQL when object storage is the better durability/cost boundary.

Prefer:

- explicit columns;
- sargable range predicates;
- `EXISTS` for existence checks;
- keyset pagination backed by a matching composite index;
- batching with `IN`/`ANY` or joins instead of queries inside loops;
- `UNION ALL` when deduplication is not required.

`EXPLAIN ANALYZE` executes the query. Use it carefully on production-sized or mutating statements.

## JSONB And Semi-Structured Data

Use JSONB for flexible payloads only after deciding which parts are durable relational facts.

Rules:

- use `jsonb` instead of `json` unless preserving original whitespace, key order, or duplicate keys is a hard requirement;
- keep core relationships, required fields, joins, reporting dimensions, and frequently constrained values in columns or tables;
- add `CHECK` constraints for basic JSON shape when the application depends on it, such as `jsonb_typeof(config) = 'object'`;
- use the default GIN operator class for mixed JSONB existence and containment queries;
- consider `jsonb_path_ops` only for heavy containment-only workloads because it is smaller/faster for `@>` but does not support key-existence operators such as `?`, `?|`, and `?&`;
- for equality, range, sorting, or pagination on a JSONB scalar, prefer a generated column or expression index over repeatedly extracting and casting inside the query;
- treat deeply nested JSONB updates as write amplification and bloat risks on hot rows.

Failure output: `Rejected: JSONB stores durable relational facts or query-critical fields without explicit validation/index strategy.`

## MVCC, VACUUM, And Bloat

PostgreSQL MVCC leaves dead tuples after updates/deletes until VACUUM reclaims reusable space. Long transactions can prevent cleanup and increase bloat.

Rules:

- keep transactions short;
- set or respect `idle_in_transaction_session_timeout` where appropriate;
- never disable autovacuum globally;
- tune autovacuum per high-churn table before changing global defaults;
- run `ANALYZE` after large data changes to refresh planner statistics;
- monitor dead tuples, table/index bloat, long transactions, and transaction ID age;
- use `VACUUM FULL` only as a last resort because it rewrites the table and takes heavy locks.

For update-heavy tables:

- separate frequently updated hot columns from large or stable cold columns when bloat becomes material;
- consider a lower table `fillfactor` to preserve space for HOT updates;
- avoid updating indexed columns unnecessarily because that prevents HOT updates and increases index churn.

For insert-heavy or bulk-load paths:

- keep indexes to the access paths and constraints that are actually needed;
- use multi-row inserts or engine-supported bulk load mechanisms for large imports;
- consider unlogged staging tables only for rebuildable data where crash safety is not required;
- defer secondary index creation during controlled bulk loads when that is operationally safe.

Failure output: `Rejected: PostgreSQL performance/maintenance plan ignores MVCC, VACUUM, or stale statistics.`

## Partitioning

Partition only when it solves a real operational or query-shape problem.

Consider partitioning when:

- the table is very large and common queries consistently filter on the partition key;
- retention or purge operations need chunk-level removal;
- maintenance, vacuum, or index operations on the whole table are too expensive;
- the project can operate partition rollover, indexes, constraints, and monitoring deliberately.

Rules:

- prefer declarative partitioning or a proven time-series extension over table inheritance;
- choose range, list, or hash partitioning from access and retention patterns, not from table size alone;
- include the partition key in unique or primary-key constraints when PostgreSQL requires it;
- verify the current PostgreSQL version and migration tool behavior for foreign keys, unique constraints, and index operations on partitioned tables;
- do not partition small or moderate tables just to appear scalable.

Failure output: `Rejected: PostgreSQL partitioning is not tied to query pruning, retention, or maintenance evidence.`

## Schema Evolution

PostgreSQL DDL is operational work even when the syntax is short.

Rules:

- most DDL can run in a transaction, but `CREATE INDEX CONCURRENTLY` and similar concurrent operations cannot;
- adding a required column to existing tables should usually follow expand-contract: nullable/additive column, compatible code, backfill, validate, then `NOT NULL`;
- defaults that call functions, especially volatile or per-row generators such as `gen_random_uuid()`, can have version-dependent rewrite and backfill behavior; verify behavior before using them on large tables;
- drop dependent constraints and indexes before dropping columns or tables;
- `CREATE OR REPLACE FUNCTION` with different arguments creates an overload instead of replacing the old signature; drop obsolete signatures deliberately;
- use generated stored columns for stable derived values that need indexing or constraints, but verify generated-column support in the target PostgreSQL version and migration tool.

Failure output: `Rejected: PostgreSQL schema evolution ignores lock, rewrite, dependency, or compatibility behavior.`

## Transactions And Replication

Rules:

- retry serialization failures by retrying the whole safe unit of work;
- treat read replicas as potentially stale;
- keep read-after-write, idempotency, authorization, checkout, and user-visible consistency reads on primary unless a lag-wait strategy is explicit;
- monitor replication lag and replication slot/WAL retention where replication is used;
- understand synchronous replication trade-offs before requiring zero data loss.

For read-only reporting or operational observers:

- prefer read-only roles and replicas only when stale reads are acceptable;
- keep consistency-sensitive checks on primary or require an explicit lag-wait/sticky-read strategy;
- bound queries by indexed predicates, time windows, limits, or batches;
- select only required columns and avoid sensitive verifier or payload fields;
- account for long-running reads that can hold snapshots and delay vacuum cleanup.

Failure output: `Rejected: PostgreSQL read-only observer path ignores replica lag, privileges, query bounds, or sensitive data exposure.`

## Backup And Recovery

Backups are not proven until recovery has been tested.

For material data, define:

- logical versus physical backup strategy;
- whether point-in-time recovery is required;
- WAL archiving health if PITR is used;
- restore time and restore point objectives;
- backup age and archive failure monitoring;
- restore test cadence.

Failure output: `Rejected: PostgreSQL recovery plan assumes backups work without tested restore evidence.`

## Security And Privileges

Rules:

- use least-privilege application roles;
- separate migration/admin roles from runtime roles;
- avoid broad grants on public schemas;
- treat Row Level Security as a security feature that needs explicit policy review and tests, not just a query convenience;
- use prepared/parameterized statements for user-controlled values;
- verify extension trust and hosting support before enabling extensions.

## Extensions

Extensions are part of the durable database contract when schema, indexes, or queries depend on them.

Rules:

- verify extension availability, version, trust model, and hosting support before designing around it;
- prefer `pgcrypto` over legacy UUID extensions for new UUID generation when it satisfies the project need;
- use `pg_trgm`, PostGIS, TimescaleDB, pgvector/pgvectorscale, `btree_gin`, `btree_gist`, or audit extensions only when the access pattern or operational requirement justifies the dependency;
- capture extension-dependent conventions in an ADR when they affect schema portability, migrations, backup/restore, or production operations.

## Verification Checklist

- PostgreSQL version and hosting constraints known.
- Data types match PostgreSQL semantics.
- Constraint behavior accounts for nulls, FK indexes, exclusion constraints, and one-null uniqueness when relevant.
- Foreign key indexes considered explicitly.
- Unique-null behavior is correct.
- JSONB use is justified, validated where needed, and indexed for real query paths.
- Index changes use plan evidence and production-safe creation where needed.
- MVCC/VACUUM/statistics impact considered for high-churn or bulk changes.
- Partitioning is justified by query pruning, retention, or maintenance needs.
- Schema evolution accounts for locks, rewrites, concurrent index limitations, and expand-contract compatibility.
- Replica lag and read-after-write behavior considered.
- Extension dependencies are verified against hosting and migration constraints.
- Backup and restore expectations are tested or explicitly marked as a gap.
