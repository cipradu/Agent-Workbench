# Go Database Access

Use this reference when applying the database-design skill in a Go project that uses `database/sql`, `sqlx`, `pgx`, or a similar explicit SQL/database driver layer.

Always apply the general database rules first. This reference covers the adapter layer only.

## Access Layer Rules

- Prefer explicit SQL through the project's chosen driver/query helper unless the project already has an accepted ORM convention.
- Use parameterized queries for all user-controlled values.
- Never concatenate user input into SQL.
- Dynamic identifiers such as column names or sort fields require allowlists.
- Pass `context.Context` to database operations through the driver's context-aware methods.
- Use `ExecContext`/equivalent for statements that do not return rows.
- Close rows immediately after successful query creation and check row iteration errors.
- Distinguish not-found from technical failure, for example with `errors.Is(err, sql.ErrNoRows)` when using `database/sql`.
- Wrap database errors with operation context while preserving the original cause.

Failure output: `Rejected: Go database access lacks parameterization, context propagation, row cleanup, or error distinction.`

## Transactions

Rules:

- use a transaction for related multi-statement writes;
- pass the transaction object to helper functions that participate in the unit of work;
- defer rollback immediately after begin where that is the project convention and safe because rollback after commit is a no-op;
- commit once at the end;
- use custom isolation levels only for named invariants;
- use `SELECT ... FOR UPDATE` or engine-equivalent row locks when reading data to compute and write a new value.

## Scanning And Nullable Columns

Rules:

- list columns explicitly instead of relying on `SELECT *`;
- keep struct tags aligned with selected columns when using struct scanning;
- handle nullable columns deliberately with pointers, `sql.NullXxx`/generic nullable types, or explicit query conversion;
- do not accidentally convert `NULL` to a misleading zero value.

## Connection Pool

Configure and observe the pool:

- maximum open connections;
- maximum idle connections;
- max connection lifetime;
- max idle time;
- wait count and wait duration;
- open/in-use/idle connection counts.

Pool settings are workload and database-capacity decisions, not constants to copy blindly.

## Migrations And Tests

Rules:

- use the project's accepted migration tool; do not hand-roll one-off migration execution code;
- migration SQL should be reviewed and versioned;
- unit tests should mock repository contracts or query behavior when no real database is needed;
- integration tests should run against a real database or containerized equivalent when validating SQL correctness, transactions, constraints, nullable round-trips, or migrations;
- never run tests against production databases.
