# Migrations And Backfills

Use this reference when creating, reviewing, or planning schema migrations, rollback paths, destructive changes, data migrations, backfills, online changes, migration graph hygiene, or migration verification.

## Classify The Change

Before writing a migration, classify it:

- additive schema change;
- constraint/index change;
- data backfill;
- application compatibility change;
- destructive schema change;
- rename/type change;
- large-table operation;
- migration-tool graph change.

Completion criterion: the deployment sequence reflects the risk class. A destructive or large-table change is not treated like a small additive migration.

## Expand-Contract Sequence

For changes that may break old application versions or existing data, use expand-contract:

1. Add the new compatible shape without breaking existing reads/writes.
2. Deploy code that can write/read both old and new shapes when needed.
3. Backfill existing data in resumable batches.
4. Verify counts, constraints, and application behavior.
5. Switch reads/writes to the new shape.
6. Enforce stricter constraints only after data and deployed code are compatible.
7. Remove the old shape in a later migration after compatibility is no longer needed.

Examples:

- Add required column: add nullable column, deploy writing code, backfill, validate, then add not-null constraint.
- Rename column: add new column, dual-write or map both, backfill, switch readers, remove old column later.
- Change type: add compatible new column/table, backfill with conversion checks, switch, then clean up.
- Remove column/table: stop using it first, deploy, verify no consumers remain, then drop later.

Failure output: `Rejected: migration requires expand-contract but performs the breaking change in one step.`

## Migration File Discipline

Rules:

- one logical change per migration unless project convention says otherwise;
- prefer additive changes first;
- include downgrade/rollback where possible;
- if downgrade cannot restore data, document the irreversible part and operational recovery path;
- use deterministic names for constraints and indexes when the tool/engine supports it;
- create tables/columns before constraints/indexes that depend on them;
- drop dependent constraints/indexes before dropping columns/tables;
- avoid combining schema change, data backfill, behavior switch, and cleanup in one migration.

## Operational Safety

For large or production data:

- test on a representative data copy;
- estimate lock behavior and runtime;
- use online/concurrent mechanisms when supported;
- set statement/lock timeouts where supported;
- choose an operational window when required;
- monitor progress and error rates;
- prepare a pause/resume path.

Do not assume a migration is safe because it works on an empty local database.

## Backfills

Backfills must be bounded, resumable, and verified.

Rules:

- process in batches sized for row width, lock time, and database load;
- use stable ordering and high-water marks such as primary key or timestamp;
- commit between batches unless the invariant requires a larger transaction;
- record progress, affected row count, elapsed time, and failures;
- make retries idempotent;
- verify source/target counts, null rates, orphan rows, constraint readiness, and sample rows;
- avoid `OFFSET` for very large backfills because it becomes slower as the scan advances.

Failure output: `Rejected: backfill is not resumable or does not define verification.`

## Migration Graph Hygiene

Keep the migration graph understandable:

- avoid multiple active heads unless the tool explicitly supports a merge workflow;
- check current revision/head before release;
- merge branches deliberately when required;
- keep generated migrations reviewed, not blindly accepted;
- keep migration files versioned and tied to the release/deployment process.

## Verification Checklist

Before accepting a migration/backfill:

- upgrade path tested;
- downgrade/rollback or recovery path tested/described;
- compatibility with old and new application code considered;
- constraints/index names deterministic where applicable;
- lock/runtime risk understood;
- large-table operations use safe mechanisms;
- backfill is batched, resumable, observable, and idempotent;
- pre/post validation queries exist;
- backup/snapshot/restore plan named when risk is material.
