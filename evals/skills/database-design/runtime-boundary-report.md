# Database Design Runtime Boundary Report

Owner: `database-design`

Checkpoint: CP-002

Fixture ID: CP2-DB-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` version 0.4. The target result record was appended after the target run completed.

Runtime skill entry point: `skills/database-design/SKILL.md`

Evaluator suite: `evals/skills/database-design/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one path — trigger basis per selected operational reference, or none applicable>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply database-design to review a PostgreSQL zero-downtime backfill that adds a tenant-scoped unique column under concurrent writes using SQLAlchemy and Alembic. Cover schema constraints, transaction and locking behavior, migration and backfill safety, indexes and query-plan verification, and stack-specific mechanics. Do not edit files.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/database-design/references/schema-design.md`
- `skills/database-design/references/transactions-and-concurrency.md`
- `skills/database-design/references/migrations-and-backfills.md`
- `skills/database-design/references/indexing-and-performance.md`
- `skills/database-design/references/postgres.md`
- `skills/database-design/references/sqlalchemy-alembic.md`

Expected unselected operational references:

- `skills/database-design/references/mysql.md`
- `skills/database-design/references/drizzle.md`
- `skills/database-design/references/go-database.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/database-design/ or none>
Selector basis: <one path — trigger basis per selected operational reference, or none applicable>
```

## PASS Criteria

- `References read` reports exactly the expected selected operational references and no expected unselected operational references.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for each selected operational reference.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, or the checkpoint summary.
- Target reports no file edits.

## Target Result Record

Target run status: `COMPLETED`

Target source identity: `/root/cp2_db_target`

Target output:

````text
Conclusion: Not ready to claim zero downtime as stated. No migration artifact or production profile was supplied, so this is a design-level review. The safe design is an expand-contract rollout; a single Alembic revision that adds a required column, backfills it, and creates uniqueness is rejected because it can hold long transactions, block concurrent writes, and break rolling deployments.

Assumptions and unresolved facts:

- PostgreSQL major version, hosting restrictions, SQLAlchemy/Alembic versions, table size, write rate, replica topology, deployed revision, and existing indexes/constraints must be confirmed. The production table size/write profile is the fact most likely to change batch sizes, lock budgets, and whether “zero downtime” is credible.
- Define the invariant precisely: whether the value is required, how it is normalized, whether deleted rows participate, and whether uniqueness means `(tenant_id, new_column)`.
- If the final column remains nullable, ordinary PostgreSQL uniqueness permits multiple nulls. PostgreSQL 15+ can provide `NULLS NOT DISTINCT`, but that behavior and rollout must be version-verified. If the column becomes `NOT NULL`, transitional nulls are acceptable during expansion.
- Reconcile the deployed schema, SQLAlchemy models, Alembic revisions/heads, and cataloged constraints/indexes before migration.

Schema and deployment sequence:

1. Add the new column as nullable, without a per-row volatile default. Use a short metadata operation with a lock timeout; even additive DDL needs a lock, so “zero downtime” means fail-fast/retry and measured non-disruption, not zero locking.
2. Before any application or backfill writes non-null values, create a unique composite index on `(tenant_id, new_column)` with `CREATE UNIQUE INDEX CONCURRENTLY`. Legacy nulls allow this transitional index to build while it begins enforcing every non-null value.
3. Run the concurrent index build outside the normal Alembic migration transaction, preferably in a dedicated revision/operational step. Review the installed Alembic version’s concurrent-index mechanism rather than accepting an autogenerated blocking unique constraint. Check for an invalid leftover index before retrying.
4. Attach the valid index as a named unique constraint using the index if constraint metadata is required. This still needs a brief table lock; use a lock budget and representative-volume rehearsal. Retaining the valid unique index temporarily is safer than allowing a long blocking attach.
5. Deploy SQLAlchemy code that always supplies the new value for new writes in the same unit-of-work transaction while readers tolerate legacy nulls.
6. Run the legacy-row backfill separately in bounded, resumable batches.
7. Verify completeness and uniqueness. If required, add a `CHECK (new_column IS NOT NULL) NOT VALID`, validate it online, then set `NOT NULL` with a bounded lock attempt. Deploy readers that require the value only after validation; remove compatibility behavior later.

Transaction, locking, and backfill safety:

- Each batch gets one SQLAlchemy session and one top-level `session.begin()` boundary. Helpers receive that ambient session and must not begin or commit independently.
- Select a bounded set of null rows in stable primary-key order and lock only those rows. Multiple workers may use SQLAlchemy row-lock support equivalent to `FOR UPDATE SKIP LOCKED`, but a persisted high-water mark must not permanently skip locked rows; perform wraparound/reconciliation until the null count is zero.
- Update only rows still satisfying `new_column IS NULL`, generate values deterministically and idempotently, and commit between batches. Record key range, affected count, duration, retries, and failures.
- A unique violation is evidence of bad derivation or conflicting source data, not a transient error to retry with a random replacement. Roll back the batch and preserve the collision for investigation.
- Retry deadlocks or serialization failures only as bounded retries of the whole idempotent batch. Keep external calls, logging, and other side effects outside the transaction.
- Concurrent index creation does not block ordinary DML, but it can wait for long transactions and adds CPU/IO/WAL pressure. Monitor lock waits, long transactions, dead tuples, replication lag, autovacuum, error rate, and batch latency.
- Large updates create MVCC churn and stale planner statistics. Tune batches from observed lock/WAL/replica pressure and run `ANALYZE` after the backfill.

Index and query-plan verification:

- Inspect existing constraints and indexes first; do not add a redundant tenant/value index.
- Verify the real lookup shape is tenant-bound, for example `WHERE tenant_id = :tenant_id AND new_column = :value`, so the composite index order supports both isolation and lookup.
- Before index creation, check derived-value duplicates grouped by tenant and establish null/count baselines. Afterward, verify the named constraint/index, PostgreSQL index readiness/validity, zero unexpected nulls, zero duplicates, row counts, and representative value mappings.
- Use `EXPLAIN` and, where safe, `EXPLAIN (ANALYZE, BUFFERS)` on representative read-only lookup queries. Check scan type, estimated versus actual rows, loops, buffers, and heap visits; merely seeing the index name is insufficient.
- Run concurrency tests showing two writers cannot create the same tenant/value pair and that old/new application versions tolerate every rollout state.

Rollback and recovery:

- A failed concurrent build may leave an invalid index; inspect and remove it safely before retrying.
- Do not automatically downgrade by dropping the column once deployed writers depend on it. Pause the backfill, retain compatible nullable schema, and roll application behavior back first.
- Treat generated backfill data as potentially irreversible. Define roll-forward recovery, pre-change snapshot/restore expectations, and tested upgrade/downgrade behavior against representative data.
- Verify Alembic has the expected deployed revision and a single head unless an explicit merge workflow exists.

References read: skills/database-design/references/schema-design.md, skills/database-design/references/transactions-and-concurrency.md, skills/database-design/references/indexing-and-performance.md, skills/database-design/references/migrations-and-backfills.md, skills/database-design/references/sqlalchemy-alembic.md, skills/database-design/references/postgres.md
Evaluator assets read: none
Selector basis: skills/database-design/references/schema-design.md — tenant-scoped unique column and schema constraints; skills/database-design/references/transactions-and-concurrency.md — concurrent writes, transactions, and locking; skills/database-design/references/indexing-and-performance.md — index design and query-plan verification; skills/database-design/references/migrations-and-backfills.md — zero-downtime migration and backfill safety; skills/database-design/references/sqlalchemy-alembic.md — SQLAlchemy and Alembic mechanics; skills/database-design/references/postgres.md — PostgreSQL-specific uniqueness, MVCC, locking, and concurrent index behavior
````

Reported audit lines:

```text
References read: skills/database-design/references/schema-design.md, skills/database-design/references/transactions-and-concurrency.md, skills/database-design/references/indexing-and-performance.md, skills/database-design/references/migrations-and-backfills.md, skills/database-design/references/sqlalchemy-alembic.md, skills/database-design/references/postgres.md
Evaluator assets read: none
Selector basis: skills/database-design/references/schema-design.md — tenant-scoped unique column and schema constraints; skills/database-design/references/transactions-and-concurrency.md — concurrent writes, transactions, and locking; skills/database-design/references/indexing-and-performance.md — index design and query-plan verification; skills/database-design/references/migrations-and-backfills.md — zero-downtime migration and backfill safety; skills/database-design/references/sqlalchemy-alembic.md — SQLAlchemy and Alembic mechanics; skills/database-design/references/postgres.md — PostgreSQL-specific uniqueness, MVCC, locking, and concurrent index behavior
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: target-reported/procedural read evidence, not filesystem capability isolation.
