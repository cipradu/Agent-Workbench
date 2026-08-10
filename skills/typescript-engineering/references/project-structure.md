# Project Structure And Dependency Law

Load when creating or changing packages, module purposes, transport/service/tool layers, composition roots, centralized owners, imports, shared contracts, or provider adapters.

## Structure By Owned Purpose

Every package/module has one concrete purpose and owns only the code, schemas, types, tests, and adapters for that purpose. Project-specific product topology belongs in project rules; do not copy a sample project's package map.

Avoid generic dumping grounds such as `core`, `common`, `shared`, `misc`, `utils`, `helpers`, `types`, or `services`. A purpose-local file with one of those names is acceptable only when the enclosing owner makes its scope unambiguous.

When the project already contains or explicitly requires these surfaces, apply this responsibility separation:

- routes/controllers own transport parsing, authentication handoff, response mapping, and protocol concerns;
- services own business orchestration and depend on project-owned interfaces;
- tools/clients/adapters own database, filesystem, process, network, SDK, and provider I/O;
- composition roots load complete settings, construct loggers/clients/factories, inject dependencies, install boundaries, and own lifecycle.

This list assigns responsibility to accepted surfaces. It does not authorize inventing packages, layers, purposes, composition boundaries, or dependency edges. Missing topology remains blocked until project instructions or `architecture-design` supplies it.

Services do not reach around an adapter to call a database, SDK, HTTP client, process, or filesystem directly. Leaf modules do not locate settings, loggers, or clients globally.

## Centralized Cross-Cutting Owners

When a concern recurs, it has one narrow owner:

- contracts: cross-surface request/response/event/job/webhook/wire schemas, derived types, and mapping from internal payloads into those external contracts;
- settings: configuration schemas, loading, validation, protected merge, immutable values;
- errors: catalogs, runtime error types, factories, normalizers, and the transport-neutral sanitized error payload;
- logging: factories, serializers, redaction, correlation, sinks, fallback diagnostics;
- persistence: schemas, migrations, and database client/tool mechanics;
- testing support: shared conventions and genuinely shared primitives in the declared central owner; package-specific factories, doubles, and reset helpers on that package's explicit testing subpath.

Feature modules contribute their schema/catalog/redaction/config additions to these owners in the same change. They do not create parallel settings kernels, loggers, error taxonomies, test-helper conventions, persistence writers, or plugin systems.

## Declare Dependency Direction

Project instructions declare the import law beside the package tree: a lowest-first layer order or an explicit dependency map when a single linear order would misstate the graph. It must be legible, acyclic, complete for its scope, and guard-enforced.

- Build order does not grant import permission.
- Cross-package imports use declared workspace names and public subpaths, never relative paths escaping the package.
- Every direct external import has a direct declaration in the importing package.
- TypeScript project references mirror direct workspace dependencies where reference builds apply.
- Aliases and exports point to real owners; they do not create undeclared edges.
- Vendor SDK types stop at adapters. Project-owned contracts cross into services.
- Provider-independent capabilities use project-owned interfaces only when the current project requires provider independence.
- Sole-writer, settings-reader, logger-construction, and surface-catalog decisions are enforced at imports and call sites.

## Enforce The Law

Use a native TypeScript-aware rule when it expresses the complete invariant and covers every target file. Otherwise use a source-derived structural guard that discovers source truth, encodes exact permitted relationships/exceptions, catches dynamic imports and reverse/stale drift, and runs in the canonical gate.

Do not create a dependency map from whatever current imports happen to exist, use threshold-based acceptance, exempt whole directories, or maintain a partial scan list. Architecture defines the allowed graph; the guard proves code conforms to it.

Failure output: `Blocked: package ownership or dependency law is unresolved: <purpose, layer, composition root, centralized owner, public surface, or permitted edge>.`
