# Configuration And Settings

Load for environment values, `.env`, runtime settings stores, secret delivery, startup validation, behavior-affecting values, settings access, or dependency injection.

## One Settings Owner Per Process

Every process has one settings package/module and one authorized path for reading configuration sources. It must:

1. project an explicit allowlist before parsing;
2. parse raw strings into domain types;
3. validate required fields and cross-field invariants;
4. classify and protect bootstrap/security/connectivity keys;
5. reject invalid or forbidden overrides;
6. produce immutable typed settings;
7. emit a sanitized catalog-backed bootstrap diagnostic and fail startup on invalid configuration.

No other runtime module reads `process.env`, `import.meta.env`, framework globals, browser build globals, or a runtime settings database directly. Environment type declarations are compile-time hints, not deployed-value validation.

Use configuration-scoped enforcement to allow the one settings reader. Do not place an inline lint suppression in the authorized reader.

## Source Categories And Delivery

Keep these sources distinct:

- build-time public values embedded into an artifact;
- process-start runtime values and secrets;
- validated runtime overrides from an approved settings store;
- request/job/correlation context;
- browser-safe public settings.

Local and Docker Compose development use one project-designated `.env`, normally at the repository or application root. Commit a safe `.env.example`; never commit live values. Do not create service-local or task-local `.env` files that establish competing settings owners.

Recorded CI definitions, container specifications, service-manager/orchestrator manifests, and secret-injection manifests are project-designated configuration. Ad hoc, unrecorded environment values added at process launch—including `PYTHONPATH`-style path changes or JavaScript runtime equivalents—are forbidden.

Unknown keys are discarded or rejected according to the settings contract; they never flow automatically into effective settings. Secrets have no convenience defaults and never enter browser bundles, logs, errors, snapshots, fixtures, or generated files.

## Behavior-Value Test

A value belongs in settings when an operator may change it per deployment and the change alters security, data selection, routing, resource use, or policy. This includes timeouts, retry/backoff budgets, limits, concurrency, polling, cache TTL, flags, provider selection, bind settings, auth policy, thresholds, and resource policy.

UI or query values also belong in settings when they change selected data, thresholds, resource use, or operator policy. Intrinsic presentation constants remain source constants.

Protocol constants, domain-separation tags, stable product identity, compile-time discriminants, and deliberately code-fixed security allowlists can remain in source. If such a value bounds persisted or security-sensitive input, enforce it at the write/security boundary even though it is not configurable.

When a needed behavior setting is missing, add it to the centralized schema/catalog, validate it, document its delivery, wire it at the composition root, inject the smallest typed slice, and cover startup/configuration behavior before continuing the consumer.

## Two-Phase Settings

When runtime overrides exist:

1. load and validate bootstrap/local-authority values;
2. inspect the raw override key names for protected keys before parsing or merging;
3. fail with a logged, catalog-backed startup error if a protected key is present;
4. validate the remaining runtime override shape;
5. compose and deeply freeze effective settings.

Protected bootstrap/security/connectivity values cannot be replaced by runtime data. Never silently strip a protected override and continue.

## Access And Injection

Only composition roots may obtain complete settings. They pass narrow readonly configuration objects into factories and services. Leaf packages may import settings types but never a runtime getter, loader, database accessor, or global fallback.

If a singleton is required by the host, initialization is explicit and one-time, access before initialization fails with a logged catalog error, the returned value is immutable, and lazy loading is forbidden. The singleton remains a composition-root mechanism rather than a leaf dependency locator.

Tests construct fresh validated settings or initialize sources before importing the settings owner. They do not mutate process-global settings between cases.

## Required Failure Shape

Bootstrap failure uses the centralized error catalog and a stable bootstrap correlation sentinel. Before the operational logger exists, the settings owner calls the logging package's narrow safe fallback writer with key names, issue paths/codes, and bounded safe metadata only; it then throws the same typed error. Never emit secret values or a raw validation dump.

Failure output: `Blocked: centralized settings contract is incomplete: <source, allowlist, schema, protected key, failure path, or injection owner>.`
