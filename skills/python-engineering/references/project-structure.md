# Project Structure: Purpose-Grouped Packages And Enforced Import Law

Load this reference when structuring a new Python package beyond the `src/` decision, adding packages or modules to a purpose-grouped project, declaring or extending an import-dependency law, or turning an architectural rule that no native tool enforces into a guard test.

Provenance: operator house doctrine, not external consensus. Proven in one production project and adopted into a second (2026-08); it is the greenfield default wherever this skill governs. Incumbent structure in an existing project wins under the Step 1 baseline, and restructuring an incumbent is a migration under the migration-approval gate — never a side effect of a feature task.

Owner boundary: cross-service architecture, seams between deployables, and adapter-placement judgment belong to `architecture-design`. Error taxonomy, message policy, and the errors vocabulary/catalog split belong to `error-handling-design`. Test posture and seam judgment belong to `testing-strategy`. This reference owns package-internal structure mechanics and their enforcement.

Leading concept: **structure by purpose; declare the law; let a guard test enforce it.**

## Purpose Grouping

Organize the package by purpose, never by layer-name ceremony. Every purpose is a folder that owns everything belonging to that purpose — its actions, models, and schemas.

- **Models live inside their purpose.** Do not create a package-wide `models.py`, `models/`, `schemas/`, `types.py`, `utils/`, or `helpers/` dump. Purpose-local files may use a precise name such as `types.py` when that name describes their actual ownership.
- **The package root holds only entry files.** Nothing is orphaned at the root. In greenfield work, every package name states a concrete purpose; generic buckets such as `core/`, `common/`, `shared/`, `misc/`, and `services/` are forbidden. An owner-approved incumbent bucket is preserved under the incumbent-structure gate and is not precedent for new work.
- **Composition roots are the only all-knowing modules.** Only an entry point (`__main__.py`, a serving entry, or the project-designated equivalent) may know every package exists. Settings load there and clients are constructed there, after settings.

A neutral example follows. Derive each project's tree from its own purposes; do not copy this tree. The ports/adapters seam is an `architecture-design` decision, not part of this doctrine, and a project with no such need groups its purposes differently.

```text
src/feedsync/
├── errors/          # everything failure — typed failures shared by every package
├── settings/        # all configuration, read once, validated — the only environment reader
├── domain/          # the core model and invariants — pure, no I/O
├── ports/           # capability protocols and their request/result models
├── adapters/        # provider implementations behind the ports — vendor types stop here
├── storage/         # everything persistence
├── ingest/          # the pipeline, one folder per stage
│   └── __main__.py  # composition root: settings, clients, run
└── serving/         # the caller-facing surface
```

## Package Front Doors

- A package's `__init__.py` is its default front door: it re-exports the ordinary public surface, and consumers import those names from the package. A submodule whose eager import would load a material dependency or require an optional extra may instead be named there as a documented public module path. Consumers do not import any other implementation submodules.
- Every module has a module-level ownership docstring stating what it owns, what it deliberately does not own, and any import constraint it lives under. This is an ownership-contract requirement only; per-class and per-function docstrings and Ruff's `D` rules remain opt-in under [quality-gates](quality-gates.md).

## The Import-Dependency Law

Import direction is law, declared per project and enforced by a guard test.

- Each project declares its import-dependency law in its project instructions file, alongside its tree: a layer order (lowest first) where that accurately states the architecture, or a directional dependency map where a single order would misstate it. The declaration is architectural authority, not a graph inferred from current imports; permitted edges are explicit, justified, legible, acyclic, and guard-enforced.
- Imports may follow only relationships the declaration permits. In a layer order, a module imports only strictly lower layers. In a dependency map, a package imports only the packages named as its permitted dependencies. Imports inside one purpose package are exempt unless the project's law says otherwise.
- **The law constrains imports, not build order.** A build-order or verification prerequisite between units never licenses an undeclared import.
- Establish the guard test with the first package and extend it with every package added. Do not retrofit it after violations have already accumulated.

## Guard Tests For Architectural Laws

A project rule is architectural law when no compiler, linter, or type checker enforces it natively: import direction, no provider SDK type in a port signature, only the settings module reads the environment, or a closed defaults set. Violations fail no build and look unremarkable in review, so without enforcement they accumulate until the law is fiction. Enforce each law with an **exact-allowlist guard test**:

1. **One test per law.** It holds the law's exception set as an exact data literal — a per-file count map, dependency map, or field-to-value map — with a justification comment on every entry and a docstring stating that the pins are self-referential. Editing the guard is part of adding a package or a justified exception, not evidence that the guard is wrong.
2. **Enumerate the universe from source truth** through a filesystem walk over the scan roots or model introspection, never through a hand-maintained list of files to check. New files must be covered automatically.
3. **Assert three ways:** nothing outside the allowlist exhibits the construct (*unexpected*); every allowlisted entry matches exactly, so a new use fails until justified and a removed use fails until the pin is lowered (*drift in both directions*); no entry refers to something that no longer exhibits the construct (*stale*).
4. **Collect dynamic bypass channels** where the language offers one. For an import law, collect `ast.Call` nodes targeting `importlib.import_module` with package-prefixed string literals alongside static import statements.

Pins are exact values, never thresholds. "At most N" absorbs drift up to N and goes blind exactly where it matters. Failure output when a proposed guard lacks any of the four properties: `Rejected: guard test is decorative: <missing property>.`

Do not write a guard when a native tool already enforces the rule, the rule is style with no architectural consequence, the law has one call site that its owner's tests can cover directly, or the exception set changes with routine feature work. A daily-edited allowlist stops being read.

Misuse signals: a pin changed without a justification in the same change; an exact pin converted to a threshold "to reduce churn"; a lint suppression where a pinned entry belongs; a whole directory allowlisted; scan roots hand-maintained; a dependency declaration copied from current imports instead of reviewed as architecture.

## Tests Mirror The Tree

The test suite mirrors the purpose tree: `tests/<purpose>/`, or `tests/<type>/<purpose>/` where the project splits by test type. That split is `testing-strategy`'s decision. Shared fixtures live in the nearest `conftest.py`. Cross-cutting guard tests that belong to no single purpose sit at the mirror's root (`tests/test_import_law.py`, or `tests/unit/test_import_law.py` under a type split).

## When Not To Apply

- Single-file scripts (PEP 723) and one-purpose micro-libraries — purpose grouping of one purpose is ceremony.
- Incumbent structures — honor them, including owner-approved incumbent package names; propose restructuring separately under the migration-approval gate.

## Greenfield Scaffold Checklist

Before feature code, in addition to the project-setup checklist: declare the purpose tree and import-dependency law in the project's instructions file; establish the import-law guard test over the first package; put ordinary front-door exports in place; document any heavy or optional public submodule path; add module-level ownership docstrings.

Failure output when structure cannot proceed safely: `Blocked: structure doctrine vs incumbent conflict: <structure found> — restructuring requires migration approval.`

Re-verify: doctrine evidence base on each new adopting project; guard-test mechanics (`ast` surface) on Python majors; verified-as-of 2026-08.
