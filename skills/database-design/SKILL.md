---
name: database-design
description: Use when designing, reviewing, or changing relational database schemas, migrations, transactions, indexes, backfills, query behavior, ORM/database access patterns, soft deletes, tenancy, or database performance/concurrency.
---

# Database Design

## When to Use

Use this skill when:

- Designing or reviewing relational schema, tables, columns, keys, constraints, relationships, soft deletes, audit fields, retention, or tenant scoping.
- Creating, reviewing, or planning migrations, rollback paths, data backfills, online changes, destructive changes, or schema versioning.
- Designing or debugging transactions, isolation levels, locking, deadlocks, session/connection ownership, savepoints, retries, or "transaction already in progress" failures.
- Adding or reviewing indexes, query shapes, pagination, partitioning, connection pools, batch processing, or database performance changes.
- Working specifically with PostgreSQL, MySQL, or MariaDB behavior that affects schema, query, migration, locking, pooling, replication, backup, or operational safety.
- Working with database access through an ORM, query builder, driver, repository, migration tool, or generated schema layer.
- Reviewing database code for SQL injection risk, unsafe raw SQL, missing parameterization, missing context/timeouts, connection leaks, or missing error translation.

## Do Not Use

Do not use this skill when:

- The task is only product definition, workflow design, UI behavior, or application architecture with no persistence, query, migration, or data integrity decision. Use the relevant PRD, spec, architecture, or implementation planning skill instead.
- The user needs a full security scan or vulnerability validation. Use security-specific scanning/review skills for that work, and use this skill only for database-specific design or implementation concerns.
- The task is a one-line data lookup or one-off SQL answer with no design, migration, safety, or correctness implication.
- The project has a stricter local database standard or accepted ADR that directly supersedes this skill. Follow the project source of truth and use this skill only for gaps.
- The necessary database engine, version, data volume, access pattern, ownership, or deployment constraint is unknown and would materially change the recommendation. Stop and get the missing fact instead of defaulting.
- The task is provider provisioning only, such as creating a Railway, Prisma Postgres, PlanetScale, Neon, Supabase, or cloud database resource. Use a provider-specific workflow if one exists; use this skill only for the database design and safety decisions around that resource.

## Iron Law

Database work is integrity, concurrency, and operations discipline, not table-shape decoration. Do not design or change schema, transactions, migrations, indexes, query behavior, or ORM usage until the invariants, access patterns, data volume, concurrency behavior, deployment path, and rollback/verification strategy are explicit.

## Core Concept

The database is the final enforcement point for durable truth. Application validation improves user experience, but database constraints, transaction boundaries, migration safety, and query/index design determine whether the system remains correct under concurrency, retries, partial deploys, production data volume, and operational failure.

## Operating Process

Run these steps in order. Load only the references needed for the current branch.

### 1. Establish Database Context

Collect the facts that materially shape the database decision:

- database engine, version, hosting model, migration tool, ORM/query builder/driver, and local conventions;
- business invariants that must remain true even under concurrency or application bugs;
- entities, relationships, lifecycle states, tenancy model, retention needs, audit needs, and data sensitivity;
- current and expected data volume, write/read ratio, hot paths, pagination needs, reporting/analytics needs, and access patterns;
- concurrency pressure, contention points, idempotency requirements, retry behavior, and consistency requirements;
- deployment model, migration windows, rollback expectations, backup/restore expectations, and environments that must be supported.

Completion criterion: the recommendation can name the database context and the forces it optimizes for.

Failure output: `Blocked: database decision depends on missing context: <specific missing fact>.`

### 2. Model Integrity First

Design durable invariants in the database before relying on application code.

Rules:

- Enforce identity, uniqueness, referential integrity, required fields, valid ranges, and state constraints with primary keys, foreign keys, unique constraints, not-null constraints, and check constraints where supported.
- Use application validation to provide clear errors and preflight checks, not as the only integrity boundary.
- Choose normalization, denormalization, keys, JSON/storage shape, soft delete semantics, tenant scoping, audit fields, and retention based on real invariants and access patterns.
- Keep persistence models from leaking blindly across application boundaries. Map database rows to explicit contracts when crossing policy, API, or UI boundaries.

Load [Schema Design](references/schema-design.md) when designing or reviewing tables, columns, relationships, constraints, tenancy, soft deletes, timestamps, retention, or JSON/structured storage.

Completion criterion: every critical invariant has an enforcement location, and all database-only, application-only, and shared enforcement choices are explicit.

Failure output: `Rejected: data integrity is not enforced at the durable boundary: <specific invariant>.`

### 3. Define Transaction And Concurrency Behavior

Decide how writes stay correct when requests overlap, fail, retry, or partially complete.

Rules:

- Use one top-level transaction boundary per unit of work, owned by one layer. Inner functions should participate in the ambient transaction, not secretly begin/commit/rollback.
- Keep transactions short. Do validation, encryption, external calls, network IO, cache refresh, pub/sub, and success logging outside the transaction unless the database operation itself requires it.
- Lock only the rows or ranges that must be protected, acquire locks in a stable order, and document the isolation level when the default is insufficient.
- Retry deadlocks and serialization failures only as bounded retries of the whole safe unit of work.
- Roll back on failure, clear invalid session state, and translate database errors into domain/application errors without hiding the original cause from logs.

Load [Transactions And Concurrency](references/transactions-and-concurrency.md) when writing/reviewing transactions, locking, isolation, retries, session/connection ownership, savepoints, connection pools, or concurrency bugs.

Completion criterion: transaction owner, isolation/locking strategy, retry policy, rollback behavior, and side-effect timing are known.

Failure output: `Rejected: transaction/concurrency behavior is unsafe or undefined: <specific issue>.`

### 4. Design Query Shape, Indexes, And Performance From Evidence

Optimize from query behavior, not from guesses.

Rules:

- Start from actual or expected access patterns: filters, joins, sorts, grouping, pagination, uniqueness checks, and hot-path frequency.
- Use parameterized queries or safe query-builder APIs for all user-controlled values. Dynamic identifiers require allowlists.
- Add indexes only for known access paths or constraints, and account for write overhead, lock cost, migration cost, and redundancy.
- Prefer keyset/cursor pagination for large or deep result sets. Offset pagination is acceptable only when bounded and known to be small enough.
- Use `EXPLAIN`/query plans, slow query logs, database statistics, or representative tests before claiming an optimization.

Load [Indexing And Performance](references/indexing-and-performance.md) when adding/reviewing indexes, optimizing queries, choosing pagination, checking N+1 behavior, partitioning large tables, tuning connection pools, or reviewing performance-sensitive SQL.

Completion criterion: query shape, index strategy, pagination strategy, and verification evidence are explicit.

Failure output: `Rejected: database performance change is not tied to a proven query/access pattern: <specific gap>.`

### 5. Plan Migrations And Backfills As Operational Changes

Treat schema and data changes as deployable operations, not static file edits.

Rules:

- Prefer additive and reversible changes. Use expand-contract sequencing for breaking changes: add new shape, deploy compatibility, backfill, verify, switch reads/writes, then remove old shape later.
- Keep migrations small and focused. One logical schema change per migration unless the project convention requires a different unit.
- Make rollback behavior explicit. If a migration cannot be fully reversed, document why and define the operational recovery path before implementation.
- Backfill in bounded, resumable batches with progress logging, verification queries, and safe transaction boundaries.
- Test migrations both ways against a representative schema/data copy when data volume, locking, or compatibility risk is material.

Load [Migrations And Backfills](references/migrations-and-backfills.md) when creating/reviewing migrations, destructive changes, online changes, backfills, rollback plans, migration ordering, or migration graph hygiene.

Completion criterion: deployment sequence, rollback/recovery, data verification, operational window, and migration tests are known.

Failure output: `Rejected: migration/backfill plan is not operationally safe: <specific gap>.`

### 6. Apply Stack-Specific Adapter Rules Only After The General Design

Use stack references to apply the general database decision safely in the local toolchain. Do not let an ORM, migration generator, or driver decide the data model, transaction semantics, or operational risk for you.

Load the relevant adapter reference:

- [Drizzle](references/drizzle.md) for TypeScript Drizzle ORM, drizzle-kit, `$inferSelect`/`$inferInsert`, Drizzle transactions, and `sql` escape-hatch decisions.
- [SQLAlchemy And Alembic](references/sqlalchemy-alembic.md) for Python SQLAlchemy sessions, async transaction boundaries, row locks, Alembic migrations, and Alembic graph hygiene.
- [Go Database Access](references/go-database.md) for Go `database/sql`, `sqlx`, `pgx`, context propagation, row scanning, nullable columns, pool configuration, and Go database tests.
- [PostgreSQL](references/postgres.md) for PostgreSQL-specific data types, identifiers, indexes, MVCC/VACUUM, `CREATE INDEX CONCURRENTLY`, replication lag, backup/recovery, extensions, RLS, and operational gotchas.
- [MySQL And MariaDB](references/mysql.md) for MySQL/InnoDB/MariaDB-specific primary keys, data types, character sets, online DDL, isolation/gap locks, replication lag, and version differences.

If the current stack is not covered, infer only the general database rules from this skill and verify current tool-specific behavior against official documentation or project-local references before asserting exact API calls or commands.

Completion criterion: the implementation uses the local database toolchain without weakening the general integrity, transaction, migration, or performance rules.

Failure output: `Blocked: stack-specific database behavior needs verification: <tool/version/API detail>.`

### 7. Verify The Database Recommendation Or Change

Before presenting database work as ready, verify:

- invariants are enforced in the database or explicitly justified elsewhere;
- transaction owner, isolation, locking, retries, and side-effect timing are explicit;
- migrations are ordered, reversible where possible, tested, and safe for the deployment model;
- backfills are batched, resumable, observable, and verified;
- indexes match query shapes and do not duplicate or blindly optimize;
- queries are parameterized, bounded, and shaped to avoid N+1, unsafe `SELECT *`, and unbounded scans;
- soft deletes, tenancy, auditing, retention, and UTC timestamp policy are handled where relevant;
- backup/restore, rollback, monitoring, and failure recovery are named when operational risk is material.

Completion criterion: a future implementer can preserve correctness and operate the change without guessing.

Failure output: `Not ready: database design is missing <specific integrity/concurrency/migration/performance/operational criterion>.`

## Output Contract

For database design or review, include:

- database context and assumptions;
- invariants and where they are enforced;
- schema/relationship/key/tenant/soft-delete choices, when relevant;
- transaction and concurrency behavior, when relevant;
- migration/backfill/deployment sequence, when relevant;
- query/index/pagination/performance evidence, when relevant;
- stack-specific adapter notes, when relevant;
- verification steps and residual risks.

When blocked, emit the failure output from the failed step and name the smallest missing fact or next verification action.

## Reference Loading

| Situation                                                                                                                           | Load                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Tables, columns, relationships, constraints, tenancy, timestamps, soft deletes, JSON/structured data                                | [Schema Design](references/schema-design.md)                               |
| Transactions, isolation, locking, deadlocks, savepoints, sessions/connections, retries                                              | [Transactions And Concurrency](references/transactions-and-concurrency.md) |
| Migrations, rollback, data backfills, destructive changes, online changes                                                           | [Migrations And Backfills](references/migrations-and-backfills.md)         |
| Indexes, query optimization, pagination, partitioning, N+1, connection pools                                                        | [Indexing And Performance](references/indexing-and-performance.md)         |
| Drizzle ORM or drizzle-kit                                                                                                          | [Drizzle](references/drizzle.md)                                           |
| SQLAlchemy or Alembic                                                                                                               | [SQLAlchemy And Alembic](references/sqlalchemy-alembic.md)                 |
| Go `database/sql`, `sqlx`, or `pgx`                                                                                                 | [Go Database Access](references/go-database.md)                            |
| PostgreSQL-specific table design, indexing, MVCC, VACUUM, extensions, RLS, replication, backup, or `CREATE INDEX CONCURRENTLY`      | [PostgreSQL](references/postgres.md)                                       |
| MySQL or MariaDB-specific schema, InnoDB, clustered primary keys, online DDL, gap locks, read replicas, or version-dependent syntax | [MySQL And MariaDB](references/mysql.md)                                   |
| Testing or improving this skill                                                                                                     | [Pressure Tests](references/pressure-tests.md)                             |

## ADR Handoff

Use `create-project-adr` when a database decision changes a durable project convention, would be costly to reverse, affects persistent data shape, chooses a database/ORM/migration strategy, establishes tenancy/soft-delete/audit policy, or sets a repeated transaction/query/migration pattern future maintainers will question.

## Rationalization Table

| Temptation                                           | Reality                                                                                           | Required action                                                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| "The ORM schema is enough."                          | ORM types do not replace database constraints, migration safety, or operational rollback.         | State the database invariants, migrations, and runtime behavior explicitly.                      |
| "We can add the index because the query feels slow." | Indexes add write cost and migration risk, and may duplicate existing access paths.               | Prove the query shape and inspect existing indexes or query plans first.                         |
| "Just make the column NOT NULL."                     | Existing rows, concurrent deploys, and old application versions may break.                        | Use expand-contract or prove the table is empty/small and deploy compatibility is safe.          |
| "Transactions are handled by the framework."         | Hidden or nested transaction ownership causes partial writes, leaked state, and concurrency bugs. | Name the transaction owner and one top-level unit of work.                                       |
| "Soft delete is just a nullable timestamp."          | Restore behavior, uniqueness, default visibility, indexes, and retention all change semantics.    | Define query defaults, uniqueness strategy, indexes, retention, and include-deleted escape path. |
| "Raw SQL is faster."                                 | Raw SQL can bypass parameterization, type mapping, query builders, and local safety conventions.  | Use safe APIs first; justify and approve any raw escape hatch.                                   |
| "Rollback can be figured out later."                 | A migration without recovery is an operational bet, not a plan.                                   | Define rollback or recovery before implementing.                                                 |

## Red Flags

- A schema recommendation appears before invariants, relationships, access patterns, and volume are known.
- Application validation is the only enforcement for durable uniqueness, relationship, state, or range constraints.
- A migration combines behavior change, schema change, destructive cleanup, and data backfill in one unverified step.
- A transaction includes external network calls, long computation, or logging that can safely happen after commit.
- A query optimization is proposed without a query shape, plan, statistics, or representative workload.
- `SELECT *`, string-built SQL, dynamic identifiers without allowlists, or unbounded queries appear in production paths.
- Soft-deleted or tenant-scoped data can leak because default predicates are optional or duplicated manually.
- A tool-specific feature is asserted without checking the project version, official docs, or local convention.
