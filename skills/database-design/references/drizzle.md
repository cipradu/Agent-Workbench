# Drizzle

Use this reference when applying the database-design skill in a TypeScript project that uses Drizzle ORM or drizzle-kit.

Always apply the general database rules first. This reference covers the adapter layer only.

## Core Rules

- Define schema in TypeScript using the dialect-specific table helpers for the target engine.
- Derive types from tables with `typeof table.$inferSelect` and `typeof table.$inferInsert`; do not hand-maintain duplicate DTO types as the database source of truth.
- Use Drizzle query APIs for normal repository/query code.
- Do not use driver-level raw SQL strings in repositories.
- Treat Drizzle `sql` as an escape hatch, not the default path.
- Runtime uses of non-trivial `sql` fragments require explicit justification and explicit user approval before implementation.
- Generate and apply migrations through the project's drizzle-kit workflow.
- Keep transactions short and free of external network calls.
- Enforce soft delete filters by default in the query layer, with explicit include-deleted behavior where needed.
- Use prepared statements for hot paths where the target driver and project convention support them.

## Schema And Types

Rules:

- choose the correct dialect package for the target engine;
- define constraints and indexes in schema/migration code where the tool supports it;
- keep database column names stable and explicit;
- derive select/insert types from the table definition;
- map database rows to API/domain contracts instead of returning table types everywhere by default.

Completion criterion: Drizzle schema, inferred types, and public contracts do not drift independently.

## Migrations

Rules:

- review generated migrations before accepting them;
- keep one logical change per migration where practical;
- do not rely on generated output to decide operational safety;
- handle partitioning, specialized indexes, constraints, or engine-specific DDL through reviewed migrations/scripts when Drizzle schema cannot express the operation safely;
- verify migration commands and config against the project's installed Drizzle/drizzle-kit version before asserting exact CLI syntax.

Failure output: `Blocked: Drizzle migration behavior needs project-version verification: <specific command/config/API>.`

## Transactions

Rules:

- put only required database work inside the transaction callback;
- perform external calls before or after the transaction;
- do not hide nested transactions inside helper functions unless the project has a tested savepoint/unit-of-work pattern;
- translate constraint and driver errors into project error contracts without losing logs.

## Raw SQL Escape Hatch

Use raw SQL only when:

- the query/DDL cannot be expressed safely by Drizzle;
- the engine feature is required and documented;
- user-controlled values remain parameterized;
- identifiers are static or allowlisted;
- the migration/runtime blast radius is explicit;
- the user explicitly approves the escape hatch.

Failure output: `Rejected: Drizzle raw SQL escape hatch lacks justification, parameterization, or explicit approval.`
