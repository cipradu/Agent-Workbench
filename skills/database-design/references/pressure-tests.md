# Pressure Tests

Use these scenarios when testing or improving the database-design skill. They are pressure scenarios, not a complete automated eval harness.

## Scenario 1: Required Column Shortcut

Prompt: "Add a required `account_id` column to the existing orders table. Just make it NOT NULL in the migration."

Pressure: speed, authority, apparently simple schema change.

Expected wrong behavior: create one migration that adds a non-null column without data compatibility, backfill, rollout order, or rollback.

Required correct behavior: block or use expand-contract: add nullable/default-compatible shape, deploy compatible code, backfill, verify, then enforce not-null later.

Pass/fail criteria: passes only if migration safety and existing rows/deployed code compatibility are addressed before implementation.

## Scenario 2: Blind Index

Prompt: "This users page is slow. Add an index on `created_at`."

Pressure: false confidence, common optimization reflex.

Expected wrong behavior: add an index without reading query shape, filters/sorts, existing indexes, or plan evidence.

Required correct behavior: inspect the query shape and current indexes, choose an index only if it matches the access path, and define verification with plan/benchmark evidence.

Pass/fail criteria: passes only if no index is proposed as ready without evidence.

## Scenario 3: Drizzle Raw SQL Escape Hatch

Prompt: "Use raw SQL in this Drizzle repository because it is faster."

Pressure: performance claim, framework frustration.

Expected wrong behavior: use driver-level raw SQL or Drizzle `sql` without justification, parameterization, or approval.

Required correct behavior: prefer Drizzle query APIs; allow raw SQL only with named limitation, parameterization/identifier safety, version/tool check, and explicit approval.

Pass/fail criteria: passes only if the skill rejects unjustified raw SQL.

## Scenario 4: Nested SQLAlchemy Transaction

Prompt: "Fix this SQLAlchemy error by wrapping the helper in its own `session.begin()`."

Pressure: local symptom, plausible-looking fix.

Expected wrong behavior: add nested transaction boundaries and make "transaction already in progress" worse.

Required correct behavior: identify one transaction owner, pass the ambient session/unit of work into helpers, and use savepoints only for a justified nested rollback need.

Pass/fail criteria: passes only if transaction ownership is clarified before code changes.

## Scenario 5: Schema From Object Shape

Prompt: "Create the usage record table from this event JSON object."

Pressure: easy object-to-table mapping, missing production constraints.

Expected wrong behavior: copy object fields into columns without volume, access path, retention, tenant/account scope, uniqueness, timestamp, indexing, or partition considerations.

Required correct behavior: gather or block on material database context before schema design; define invariants and access patterns first.

Pass/fail criteria: passes only if missing data-volume/access-pattern facts block final schema design or are documented as assumptions with explicit risk.
