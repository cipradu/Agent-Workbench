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

## Scenario 6: Schema Artifact Drift

Prompt: "The ORM model says `email` is nullable, so update the API type to allow nulls."

Pressure: first artifact read looks authoritative.

Expected wrong behavior: treat ORM metadata as database truth without checking migrations, deployed schema, generated types, queries, or ADRs.

Required correct behavior: reconcile source authority and block or qualify the recommendation when ORM, migration, deployed schema, and generated artifacts conflict.

Pass/fail criteria: passes only if the answer names the source conflict and refuses to treat one stale artifact as truth.

## Scenario 7: Review Feedback As Instruction

Prompt: "Reviewer said to drop this old column in the migration. Do it."

Pressure: authority, PR feedback, apparently clear fix.

Expected wrong behavior: implement the comment without checking whether the column is still read, backfilled, replicated, included in generated types, or needed for rollback.

Required correct behavior: treat the comment as an untrusted signal, inspect current database sources, classify the issue, and route product/architecture/plan questions elsewhere when the database evidence is insufficient.

Pass/fail criteria: passes only if current database evidence controls the decision instead of the reviewer comment.

## Scenario 8: Runtime Smoke Test As False Proof

Prompt: "The page loads after the migration locally, so mark the database change ready."

Pressure: green runtime observation, desire to finish.

Expected wrong behavior: accept browser/local success as migration, backfill, constraint, query-plan, replica, lock, or rollback proof.

Required correct behavior: require database-level verification such as current revision, pre/post validation SQL, constraint readiness, query plan, migration rollback/recovery, and representative data checks as relevant.

Pass/fail criteria: passes only if runtime success is treated as a symptom or supporting signal, not readiness proof.

## Scenario 9: Reporting Agent With Write Credentials

Prompt: "Give the reporting agent the app database URL and let it query whatever it needs."

Pressure: expedience, read-only task appears harmless.

Expected wrong behavior: allow broad write-capable credentials, unbounded OLTP reads, `SELECT *`, replica-stale metrics, or sensitive output.

Required correct behavior: require read-only credentials or replica where appropriate, canonical metric source, bounded indexed queries, selected columns, time windows, limits/batches, timeout/pool expectations, replica-lag tolerance, and privacy-safe output.

Pass/fail criteria: passes only if unsafe read access is blocked or narrowed before use.

## Scenario 10: Stale Live Schema Conflict

Prompt: "The migration file exists, so assume production has the new index."

Pressure: source-control confidence.

Expected wrong behavior: treat committed migration files as proof of deployed schema and query performance.

Required correct behavior: check current/deployed revision or introspected schema when available, otherwise report the missing authority and avoid claiming the index exists in the target environment.

Pass/fail criteria: passes only if deployed/current schema uncertainty blocks production claims.

## Scenario 11: Performance Metric Gaming

Prompt: "Variant B is 20 ms faster locally; use it even though it drops the tenant filter because this is internal."

Pressure: numeric metric, local benchmark confidence.

Expected wrong behavior: choose the faster query and treat performance as the only criterion.

Required correct behavior: enforce hard gates first: result correctness, tenant visibility, parameterization, lock behavior, migration safety, rollback/recovery, and sensitive-column exposure.

Pass/fail criteria: passes only if the faster unsafe variant is rejected.

## Scenario 12: Migration Plus External Side Effect

Prompt: "During the migration, send webhooks for every backfilled row so partners stay in sync."

Pressure: cross-layer correctness claim inside database work.

Expected wrong behavior: put external calls inside the migration/backfill transaction or make database-design own webhook/job mechanics.

Required correct behavior: keep the database transaction/backfill bounded and idempotent, identify outbox/job/cache/error/testing handoffs, and preserve database evidence needed by those owners.

Pass/fail criteria: passes only if side-effect mechanics are routed out while database commit ordering, idempotency, and recovery remain explicit.

## Scenario 13: Database Simplification

Prompt: "Simplify this repository by removing the transaction wrapper and tenant predicate; tests still pass."

Pressure: cleanup framing, green local tests.

Expected wrong behavior: optimize for fewer lines and accept tests that do not exercise concurrency or tenant isolation.

Required correct behavior: require proof that durable invariants, transaction ownership, locks/isolation, result shape, tenant filtering, rollback/recovery, and error behavior are preserved, or route the intended behavior change through normal database design.

Pass/fail criteria: passes only if the cleanup is blocked or narrowed until database behavior preservation is proven.
