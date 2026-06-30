# Schema Design

Use this reference when designing or reviewing tables, columns, relationships, constraints, keys, tenancy, soft deletes, timestamps, retention, or structured versus semi-structured storage.

## Design From Invariants And Access Patterns

Before proposing a schema, identify:

- entities and lifecycle states;
- relationships and cardinality;
- invariants that must survive concurrency, retries, and application bugs;
- data volume and growth pattern;
- write, read, search, reporting, and pagination paths;
- tenant, ownership, retention, audit, and deletion requirements;
- data sensitivity and fields that should not be exposed broadly;
- compatibility with existing data and consumers.

Use upstream product, strategy, PRD, spec, or workflow artifacts only to extract database-relevant forces such as entity vocabulary, lifecycle states, retention expectations, canonical metrics, reporting paths, access priority, and user-visible consistency expectations. If those artifacts are missing or contradictory, route the product/engineering truth gap to its owner instead of inventing it in the schema.

Completion criterion: each table and relationship exists because it supports an invariant or access pattern, not because the object model happens to look that way.

## Source Authority And Artifact Drift

Database schema truth may be split across migration files, deployed schema, ORM definitions, generated types, schema dumps, current queries, ADRs, runbooks, and production data. Before changing or reviewing schema, check whether the relevant artifacts agree.

Common conflicts:

- ORM model allows nullable data while the database has `NOT NULL`, or the reverse;
- generated types include fields no current query selects;
- migration history differs from the deployed or introspected schema;
- schema docs or ADRs describe a convention that current migrations no longer follow;
- indexes or constraints exist in the database but not in ORM metadata;
- old volume, tenancy, or retention assumptions contradict current usage.

When sources conflict, prefer durable current evidence for safety decisions: deployed/introspected schema and actual constraints for current enforcement, migration history for rollout/recovery, current query code for access paths, ADRs for accepted conventions, and production-like data volume for operational risk. Block when the conflict could change integrity, compatibility, migration safety, tenant isolation, or query behavior.

Failure output: `Blocked: schema source authority conflict must be resolved before design: <specific conflict>.`

## Integrity Enforcement

Use database constraints for durable truth:

- primary keys for identity;
- foreign keys for referential integrity;
- unique constraints for uniqueness;
- not-null constraints for required data;
- check constraints for simple valid ranges, enums, and state combinations where supported;
- default values only when the default is semantically valid, not as a way to hide missing input.

Application validation should still exist for user-facing errors and early rejection, but it is not the final enforcement boundary.

## Normalization And Denormalization

Normalize when:

- data is repeated across rows;
- updates would otherwise require multiple changes;
- relationships have independent lifecycles;
- invariants belong to a separate concept;
- query patterns can join without unacceptable cost.

Denormalize only when:

- the read path is proven important;
- duplicated data rarely changes or consistency lag is acceptable;
- the consistency/repair mechanism is explicit;
- the simpler read model outweighs write and integrity cost.

Rejected shortcut: do not store structured, frequently queried, or constraint-bearing data as opaque JSON merely because it is quicker to write.

## Key Selection

Choose keys by deployment and access needs:

- UUID/ULID-style identifiers fit distributed creation, external exposure, or cross-system references.
- Time-sortable identifiers can help append-heavy or recency-oriented workloads when the engine/index behavior supports it.
- Auto-increment identifiers fit simple single-database systems but may leak ordering and can create coordination concerns across shards or imports.
- Natural keys are valid only when the business value is genuinely stable and accepted as identity; otherwise use a surrogate key and a unique constraint on the natural value.

Completion criterion: the key choice explains uniqueness, external exposure, ordering, import/distribution, and indexing implications.

## Relationships And Deletes

Define relationship ownership before choosing delete behavior:

- restrict/delete prevention when children cannot exist without explicit review;
- cascade only when child lifecycle is truly owned by the parent and deletion blast radius is acceptable;
- set null/default only when orphaned records remain meaningful;
- junction tables for many-to-many relationships, with uniqueness constraints preventing duplicate edges.

For soft deletes:

- define whether soft delete is required or whether hard delete is correct;
- use `deleted_at` or an equivalent state marker consistently;
- make deleted rows invisible by default in application queries;
- provide an explicit include-deleted path for admin, restore, audit, or reconciliation workflows;
- account for uniqueness among active rows, restore conflicts, retention, and purge jobs;
- index common active-row predicates so hidden rows do not degrade hot paths.

## Tenancy And Ownership

For tenant-scoped data:

- choose the tenant boundary explicitly: database, schema, table key, row-level policy, or hybrid;
- include tenant/owner keys in tables that carry tenant-owned data;
- include tenant keys in indexes for common tenant-scoped access paths;
- enforce tenant filtering in repositories/query builders rather than relying on callers to remember it;
- treat row-level security or database policies as an additional enforcement layer only after their operational behavior is understood and tested.

Failure output: `Rejected: tenant boundary is ambiguous or tenant filtering depends on caller memory.`

## Time, Audit, And Retention

Store timestamps in UTC at rest. Use engine-appropriate timestamp types and convert for users at system edges.

Use audit fields when the project needs traceability:

- `created_at`;
- `updated_at`;
- `deleted_at` when soft delete exists;
- `created_by`, `updated_by`, or actor/event tables when actor attribution matters.

Define retention and purge behavior for large, sensitive, temporary, or legally governed data. Retention is part of schema design because it affects indexes, partitions, deletion strategy, and restore expectations.

## Credential And Secret-Derived Data

Do not store reusable secrets as ordinary plaintext data.

Rules:

- Passwords are never stored directly. Store a verifier produced by a project-approved password hashing scheme, plus algorithm/version/parameter metadata when needed for future rehashing.
- API keys, bearer tokens, refresh tokens, webhook secrets, recovery tokens, and one-time codes should be stored as non-reversible verifiers, keyed hashes, token fingerprints, or secret-manager references unless plaintext recovery is explicitly required and protected.
- If plaintext recovery is truly required, state why, encrypt at rest with key-management boundaries outside the application table, and define who or what can decrypt.
- Store display-safe metadata separately from the secret verifier: prefix or last characters for user display, created time, last-used time, expiry, revoked time, owner, tenant, scope, environment, and credential name/label when relevant.
- Model rotation and revocation as lifecycle state, not as an afterthought. Unique constraints and indexes should prevent duplicate active credentials where the domain requires it.
- Do not index or expose raw sensitive values. Index verifier/fingerprint columns only when lookup requires it, and keep response mappers from returning verifier columns.
- Treat credential records as audit-sensitive: define retention, purge, restore, and incident investigation behavior deliberately.

Completion criterion: the schema supports verification, rotation, revocation, display, lookup, audit, and retention without storing or exposing the reusable secret itself.

## Provider, Local-State, And External Output Boundaries

Not every provider session, generated draft, local option, external publication field, or machine preference belongs in the database.

Classify state before persisting it:

- ephemeral provider output can stay transient unless users need shared recovery, audit, or later editing;
- machine-local preferences belong in local config, not shared database state;
- repo-local or project config belongs in tracked config only when it is not secret and must travel with the project;
- user-account settings belong in the database when they must follow the user across devices or collaborators;
- shared product state belongs in the database when other users, jobs, reports, permissions, or recovery paths depend on it.

For provider credentials or provider references, store secret-manager references, non-reversible verifiers, fingerprints, owner, tenant, scope, environment, expiry, revocation, rotation metadata, display-safe labels, last-used time, and audit fields as needed. Do not persist raw provider tokens or full external payloads by default.

Completion criterion: persistence is justified by shared durability, recovery, audit, or access needs, not by convenience.

## JSON And Semi-Structured Data

Use JSON/semi-structured fields when:

- data is truly flexible or externally shaped;
- the application treats the field mostly as an opaque payload;
- versioning the nested structure is easier than relational modeling;
- required indexes and validation are explicit.

Prefer structured columns/tables when:

- fields are filtered, joined, sorted, constrained, or reported on;
- relationships and invariants matter;
- partial updates and consistency rules are important;
- downstream consumers depend on stable shape.

## Backup And Restore

For material persistent data, name the backup/restore expectation:

- restore point objective and restore time objective when relevant;
- whether migrations/backfills need pre-change backups or snapshots;
- whether restore procedures have been tested;
- what operational evidence proves recovery works.

Completion criterion: destructive or high-volume database work has an explicit recovery path.

## Behavior-Preserving Schema Simplification

Treat schema cleanup as a behavior change until proven otherwise. Before simplifying tables, columns, constraints, generated types, mapping code, or ORM definitions, prove that durable invariants, tenant filters, query results, error behavior, credential protections, retention, migration compatibility, and rollback/recovery behavior are preserved or intentionally changed through the normal database workflow.

Rejected shortcut: do not remove a constraint, index, tenant key, soft-delete filter, audit field, display-safe credential field, or generated artifact because it looks redundant without checking the current database source authority and access paths.
