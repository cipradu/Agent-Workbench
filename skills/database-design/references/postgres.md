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

Failure output: `Blocked: PostgreSQL feature/version behavior must be verified before use: <specific feature>.`

## Schema And Data Types

Common defaults:

- use `timestamptz` for event/application timestamps, store UTC at rest, and convert at boundaries;
- use `numeric` for exact decimal values;
- use `text` unless a length limit is a real domain rule;
- use native `uuid` when UUIDs are needed, not `text`;
- prefer `BIGINT GENERATED ALWAYS AS IDENTITY` for simple internal surrogate keys when project conventions allow;
- avoid `serial` for new designs when identity columns are available;
- avoid `money` because formatting/locale and precision behavior can surprise applications;
- prefer check constraints or lookup tables over PostgreSQL enums when values change often.

PostgreSQL gotchas:

- unquoted identifiers fold to lowercase; avoid quoted mixed-case names;
- PostgreSQL does not automatically index foreign key columns;
- ordinary unique constraints allow multiple `NULL` values; PostgreSQL 15+ supports `UNIQUE (...) NULLS NOT DISTINCT` when one-null semantics are required;
- sequence/identity gaps are normal after rollbacks, crashes, failed inserts, and concurrent transactions;
- PostgreSQL heap tables are not physically clustered by primary key by default.

Completion criterion: data type and identifier choices account for PostgreSQL semantics instead of generic SQL assumptions.

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

Failure output: `Rejected: PostgreSQL performance/maintenance plan ignores MVCC, VACUUM, or stale statistics.`

## Transactions And Replication

Rules:

- retry serialization failures by retrying the whole safe unit of work;
- treat read replicas as potentially stale;
- keep read-after-write, idempotency, authorization, checkout, and user-visible consistency reads on primary unless a lag-wait strategy is explicit;
- monitor replication lag and replication slot/WAL retention where replication is used;
- understand synchronous replication trade-offs before requiring zero data loss.

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

## Verification Checklist

- PostgreSQL version and hosting constraints known.
- Data types match PostgreSQL semantics.
- Foreign key indexes considered explicitly.
- Unique-null behavior is correct.
- Index changes use plan evidence and production-safe creation where needed.
- MVCC/VACUUM/statistics impact considered for high-churn or bulk changes.
- Replica lag and read-after-write behavior considered.
- Backup and restore expectations are tested or explicitly marked as a gap.
