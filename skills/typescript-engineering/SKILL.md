---
name: typescript-engineering
description: Use when writing, reviewing, refactoring, scaffolding, configuring, testing, packaging, securing, or optimizing TypeScript or JavaScript code, applications, packages, workspaces, or project tooling.
---

# TypeScript Engineering

## When to Use

Use this skill for TypeScript and JavaScript implementation and for the mechanics that govern TypeScript projects: pnpm workspaces, compiler programs, package exports, runtime validation, settings, errors, logging, semantic enforcement, tests, hooks, CI, builds, and Turborepo.

## Do Not Use

Product architecture and domain policy remain with the project and the applicable domain skill. This skill enforces the TypeScript implementation and tooling rules once those decisions exist. Do not use unrelated feature work to migrate a package manager, formatter, linter, compiler layout, module system, test runner, or package surface.

## Iron Law

**Use the project's declared owners and dependency laws. Never bypass them with local configuration reads, local error or logging paths, suppressions, undeclared imports, or incomplete validation.**

## Required Engineering Rules

These rules are mandatory. Preserve a compliant incumbent mechanism; treat an incumbent violation as a finding rather than permission to repeat it.

1. **No suppression.** Do not add `@ts-ignore`, `@ts-expect-error`, `@ts-nocheck`, lint/formatter ignore comments, blanket rule disables, hidden file exclusions, skipped/focused tests, coverage exclusions, weakened assertions, or snapshot changes to force a pass. A project-level permission for directives in designated negative tests does not weaken this rule: handwritten negative tests remain suppression-free. Generated, vendored, or tool-owned categories may have an exact configuration-level exception only when the project explicitly owns the complete category and its alternative verification.
2. **No convenience barrels.** Import from the module that owns and defines the symbol. Public packages expose deliberate `package.json` subpaths. A tool-required aggregator stays narrow, non-public, and unavailable to application imports.
3. **Strict TypeScript.** Application logic contains no `any`. External values start as `unknown`; narrow them without unsafe assertions or non-null claims. Keep all strict compiler protections enabled and prove every source, test, and tooling file belongs to its intended compiler and semantic-lint program.
4. **Strict runtime contracts.** Validate every external or unknown value at ingress and validate serialized contracts at egress. For new work, use Zod v4, sibling `*.schema.ts` files, `z.strictObject` at every object level, and types derived from schemas. Parse once per trust boundary. Schemas remain deterministic and side-effect free.
5. **Centralized settings.** Each process has one settings owner and one authorized configuration-reading path. It allowlists, parses, cross-validates, protects, and freezes configuration at startup. Runtime modules never read `process.env`, `import.meta.env`, framework configuration globals, or settings stores directly. Composition roots inject the smallest typed settings slice into each consumer.
6. **One project-designated local environment file.** Local and Compose development use one declared `.env`; do not add service-specific or ad hoc environment files. Recorded CI, container, orchestrator, and secret-injection definitions are valid deployment configuration. Hand-set, unrecorded launch state is forbidden.
7. **Centralized error catalogs.** One error owner defines the shared runtime error contract, stable wire schema, shared catalog, surface catalogs, factories, and unknown-value normalizers. Runtime code never creates local error taxonomies, throws native `Error`, throws raw caught values, or invents code/reason strings. A missing catalog entry blocks the throwing path until the owner is updated.
8. **Absolute throw-risk ownership.** Every potentially throwing operation is inside an owned `try/catch` or has a guaranteed immediate caller catch whose ownership is explicit. This includes parsing, JSON, database, filesystem, crypto/token, HTTP/network, queues, processes, providers/SDKs, plugins/dynamic modules, workers, and external tools. “A caller probably catches it” is not sufficient.
9. **Log before every error-control change.** Every catch normalizes the caught `unknown`, preserves correlation, logs at the closest owned source, and only then throws, rethrows, maps, returns, retries, rejects, converts, or swallows. Every deliberate runtime throw has a structured log immediately before it in the same function; only construction of the exact typed error may appear between the log and throw. Intermediate and terminal owners both log their distinct handoffs.
10. **Centralized structured logging.** One logging owner configures factories, serializers, redaction, correlation, sinks, and fallback diagnostics. Each application composition root constructs one operational logger after settings validation and injects it into leaves. Runtime code does not use `console.*`, stdout, or stderr. Narrow bootstrap, sink-failure, CLI-output, and hosted-runtime exceptions stay inside named owners and configuration-level allowlists.
11. **Complete correlation and safe diagnostics.** Establish an internal correlation identifier at the first trusted ingress, preserve any external request/delivery identifier separately, and propagate context through requests, jobs, queues, providers, workers, errors, and responses. Logs use stable event names, UTC timestamps, typed errors, and sanitized bounded fields. Never log secrets, raw bodies, arbitrary payloads, uncontrolled strings, or high-cardinality objects.
12. **Owned structure and declared dependency law.** Routes/controllers own transport, services own orchestration, and tools/clients/adapters own external I/O. Only composition roots load settings and construct loggers, clients, factories, and lifecycles. Every package has one declared purpose, public surface, and permitted dependency map or layer order. Never infer a package purpose or permitted edge from its directory name; missing topology authority blocks that part of the design. Enforce the approved law mechanically.
13. **One owner per tool responsibility.** pnpm owns dependencies and the lockfile; Biome through Ultracite owns formatting and broad baseline lint for new projects; type-aware ESLint owns semantic and architectural policy; TypeScript owns compiler/project/build duties; one runner owns each test scope; hooks invoke canonical scripts; CI reruns clean acceptance. Do not stack duplicate diagnostics or autofixes.
14. **Explicit package graph.** New projects use pnpm with an exact root `packageManager` declaration and committed lockfile. Every importing package declares each direct external dependency. Internal packages use explicit workspace protocols. CI and production install from the frozen lockfile. Overrides, patches, and lifecycle-script permissions are narrow, recorded, and clean-state verified.
15. **Strict tests.** Tests live outside production source and production exposes no test-only code path. No focused/skipped cases, raw sleeps, leaked state/resources, missing awaits, transitive-package mocks, or silent integration prerequisites. New projects enforce at least 85% branches, functions, lines, and statements per handwritten production file.
16. **Semantic fields must affect behavior.** Every schema/config field with policy or behavioral meaning has a runtime consumer and tests for each meaningful branch. A declared semantic field that no owner reads is incomplete implementation, not future-proofing.
17. **Complete gates.** Safe fixes run first. Read-only formatting/baseline lint, semantic lint, compiler/project diagnostics, tests with coverage, build/declaration/package checks, and the aggregate project gate all run from their declared roots. Staged-file success is never repository-wide proof. Hooks fail closed when prerequisites are absent.
18. **No speculative infrastructure.** Do not add packages, abstractions, providers, retries, caches, compatibility paths, plugins, or migration layers without a present requirement. When a project requires provider independence, vendor types and SDK behavior stop at adapters behind project-owned contracts.

## Working Method

### Enforce the topology authority gate

Before proposing a workspace tree, package purpose, dependency edge, runtime-contract owner, or application layer, separate supplied project authority from directory names and general TypeScript defaults. A name such as `contracts`, `client`, `worker`, `domain`, `ports`, or `adapters` is not authority for what the package contains or may import. When purpose or edge authority is missing, emit `Blocked: package purposes and dependency law require project instructions or architecture-design.` You may still define package-manager, compiler, public-surface, tool, hook, CI, and test mechanics with packages treated as opaque, but do not fill the missing topology with assumptions, recommended defaults, or conditional example edges.

### Establish the project baseline

Before editing, resolve every applicable repository, workspace, application, and package root. Read the governing project rules and accepted decisions, then identify:

- the package manager declaration, lockfile, workspace manifest, package manifests, lifecycle-script policy, and dependency-version policy;
- runtime hosts, module systems, public exports, package purposes, composition roots, and the declared dependency law;
- every TypeScript program, reference edge, compiler command, build, emit, and declaration path;
- formatter/baseline lint, semantic lint, file discovery, autofix ownership, and project-specific policy guards;
- the settings, contracts, errors, logging, and testing-support owners;
- test runners, coverage rules, canonical scripts, hooks, CI, and task orchestration.

Map every affected required rule to its actual owner. Do not assume a command covers files or policy that its configuration does not discover.

### Load every matching reference

Select references by the decision or implementation surface the task actually requires, not by isolated words in the prompt. Read a reference when the task changes, designs, audits, or must resolve uncertainty in that reference's owner. Do not load one merely because the prompt states a fixed incumbent fact, names an existing command or tool, or uses a TypeScript term covered by the inline rules above. Template references apply only when concrete reusable configuration or runtime-foundation code is required. Read each independently matching reference once before acting on that surface.

When the task itself is to assess an unapproved formatter, linter, compiler, test-runner, or package-manager migration, load the current owner/gate reference and `performance.md` when performance is claimed. Incidental permission to modernize during unrelated feature work is refused from the inline incumbent rule and does not activate migration references. Do not load project-setup or template references unless the migration is approved and the task actually proceeds to manifest or configuration authoring.

Every migration assessment explicitly inventories the incumbent formatting, broad-lint, typed-semantic-policy, compiler-diagnostic, and autofix owners. It requires repository-specific parity, migration/removal cost, rollback, and approval even when the immediate disposition is “no change.”

For a quality-gate failure triage, load quality and test mechanics for the failing lint/type/test gates. Load async guidance only when the task must design promise lifecycle, cancellation, concurrency, or worker behavior, not merely because a quality tool reports a promise misuse.

Negative TypeScript compile-fail or diagnostic tests always select Compiler and Projects, Quality Gates, and Testing Mechanics. They use an isolated suppression-free invalid fixture, a positive companion, and exact diagnostic evidence even when project policy permits directives in designated tests.

When retryability, error taxonomy, public error shape, disclosure, log fields, or redaction policy is unresolved, name the exact owners before describing mechanics: route taxonomy, retry, messages, logging/redaction, and degraded-mode policy to `error-handling-design`; route public API error envelopes and compatibility to `api-design`. Co-select Configuration when timeouts, retry budgets, or other behavior values are in scope, and co-select Security when the work crosses an external HTTP or public error boundary because it owns resource and exposure controls around those boundaries. Do not invent provisional categories, codes, statuses, retry matrices, attempt counts, messages, log fields, or public shapes. Proceed only with policy-neutral TypeScript mechanics and mark every dependent branch blocked.

For Git-root hook or CI routing into a nested workspace, load project setup and hooks/CI. A supplied nested aggregate gate remains opaque unless the task also changes its formatter/linter/compiler/test composition; asking how the root invokes or verifies that declared gate does not activate quality-gate internals.

A package named `contracts` does not establish its contents, consumers, dependency edges, or runtime-schema role and does not activate type/runtime or security guidance. Load those references only when the prompt or project authority actually requires runtime validation, serialization, schemas, wire shapes, untrusted-input handling, or another security surface. A request for workspace/package shape, canonical script names, or strict local/CI validation does not require the enforcement templates unless it asks for copy-ready configuration contents. A workspace does not by itself justify Turborepo; load Turborepo only when the project already uses it or the task has an explicit task-graph, caching, input/output, filter, or persistent-task requirement.

For package public-surface and dependency-law work, load project structure and modules/packages first. That owner must consider an adequate native TypeScript-aware boundary rule before a custom guard. Do not load quality gates merely because the eventual native mechanism may be an ESLint rule; load it only when the task also changes linter ownership or concrete quality configuration after the structure owner proves native enforcement insufficient.

Public package metadata, exports, subpaths, declarations, and host compatibility alone select Modules and Packages, plus Compiler and Projects when compiler programs or declaration emit are involved. Co-select Project Structure only when the task also changes or must resolve package purpose, centralized ownership, composition, or dependency law.

For external payloads, Types and Runtime Boundaries owns the schema, parser, parse-once trust transition, trusted type, and serialization contract. Co-select Security only when the task also requires security-specific resource bounds, raw-byte authentication, secret/exposure controls, process/path safety, dependency trust, or supply-chain controls. Security adds those controls around the same boundary; it never creates a second parser or schema owner.

External byte or text payload decoding is a three-owner safety boundary: Types owns complete runtime validation, Errors owns decode/parse catch-normalize-log-control mechanics, and Security owns the pre-parse size/resource bound and exposure controls. Load all three for a safe replacement of assertion-led network payload parsing; do not let one owner absorb the others.

That boundary review explicitly rejects casts, non-null assertions, erased/generated interfaces, and superficial or internally casting type guards as runtime proof. Do not omit these rejected alternatives merely because only one appears in the supplied code.

| Work involves | Read |
| --- | --- |
| creating, changing, or auditing package-manager/workspace setup, root/workspace manifests, direct dependency declarations, lockfiles, lifecycle policy, filters, or project creation; runtime package metadata and exports alone belong to modules/packages | [Project Setup](references/project-setup.md) |
| defining, changing, or auditing package purposes, routes/services/tools, composition roots, centralized owners, dependency laws, contracts, or adapters | [Project Structure](references/project-structure.md) |
| changing or reviewing tsconfig inheritance, host options, program membership, project references, diagnostics, emit, build, or declarations | [Compiler And Projects](references/compiler-and-projects.md) |
| designing or reviewing ESM/CommonJS behavior, exports, subpaths, aliases, barrels, Web `Response`, or publishing | [Modules And Packages](references/modules-and-packages.md) |
| designing or reviewing narrowing, Zod schemas, runtime parsing, semantic fields, serialization, or wire contracts | [Types And Runtime Boundaries](references/types-and-runtime-boundaries.md) |
| changing or reviewing formatter/linter ownership, semantic/custom rules, file discovery, autofix, suppressions, or complete quality gates; also selecting the formatter/linter/compiler/test/build verification sequence or deciding what its result may report | [Quality Gates](references/quality-gates.md) |
| authoring concrete reusable TypeScript, Biome, ESLint, script, import-guard, test, or hook configuration rather than describing project-owned mechanics | [Enforcement Templates](references/enforcement-templates.md) |
| authoring concrete reusable centralized settings, error-catalog, logger-injection, correlation, or log-before-throw foundations | [Runtime Foundation Templates](references/runtime-foundation-templates.md) |
| changing or reviewing environment/settings ownership, `.env`, secrets, startup validation, runtime overrides, or behavior values | [Configuration](references/configuration.md) |
| designing or reviewing catalogs, normalization, throws, catches, retries, timeout/error integration, cancellation-to-error/control mapping, or cleanup | [Errors And Resilience](references/errors-and-resilience.md) |
| designing or reviewing logger construction/injection, structured events, correlation, redaction, sinks, console/process output, metrics, or tracing | [Logging And Observability](references/logging-observability.md) |
| designing or changing lint-staged, Husky, pre-commit/pre-push behavior, canonical gate routing, or CI | [Hooks And CI](references/hooks-and-ci.md) |
| designing or changing tests, coverage, negative type tests, helpers/doubles, integration, browser E2E, or test verification | [Testing Mechanics](references/testing-mechanics.md) |
| designing or changing Turborepo tasks, dependencies, caching, inputs, outputs, environment hashing, filters, or persistent tasks | [Turborepo](references/turborepo.md) |
| designing or reviewing promise lifetimes, signal propagation, controller/abort authority, sibling settlement, bounded concurrency, or workers | [Async And Concurrency](references/async-and-concurrency.md) |
| adding or reviewing security-specific resource bounds, raw-body authentication, process/path controls, secret exposure, dependency trust, lifecycle-script trust, or supply chain | [Security](references/security.md) |
| evaluating profiling evidence, hot paths, caching, bundles, runtime/compiler performance, or tool-migration benchmarks | [Performance](references/performance.md) |
| explicitly reviewing/refactoring TypeScript idioms and anti-patterns, or replacing assertion-led key iteration/control flow with narrowing-friendly code | [Idioms And Anti-Patterns](references/idioms-and-anti-patterns.md) |

### Apply through the project’s owners

Preserve a compliant incumbent. Add missing enforcement to the owner of the rule, not to a feature-local workaround. New projects use pnpm, strict TypeScript, Zod v4 when runtime schemas are required, Biome through Ultracite, type-aware ESLint for semantic/project policy, Vitest, Playwright when browser E2E is required, lint-staged, fail-closed Husky hooks, and CI. Turborepo is used only when an explicit task-graph need justifies it; it does not own configuration loading or package dependencies.

Oxlint, Oxfmt, or another engine is a migration candidate, not an additive layer. Migrate one responsibility only after rule, diagnostic, file-discovery, autofix, lifecycle, performance, removal, and rollback parity are proven for the actual repository.

### Verify the complete project mechanism

After the logical change is complete, run the project-owned safe fix once, inspect its semantic delta, then run every read-only canonical gate from its declared root. Delete incremental/build/tool caches before proving dependency-graph or project-reference changes. Report every unavailable or failing gate without weakening rules, scopes, tests, assertions, or coverage.

## Stop Conditions

Stop and report the exact missing owner when:

- project roots, package purposes, public surfaces, or dependency laws are missing, ambiguous, or conflict; a mechanical workspace scaffold may proceed with explicit placeholders, but package purposes and permitted edges stay unresolved and route to `architecture-design` rather than being inferred from names;
- the settings, contracts, errors, logging, or correlation owner is absent;
- a throwing path cannot satisfy catch and log-before-control ownership;
- a boundary cannot validate unknown input or serialize a declared contract;
- a required error code, setting, semantic-field consumer, direct dependency, or public export is missing;
- compliance would require suppression or hidden file/test/coverage scope;
- a tool or dependency migration lacks explicit scope and repository-specific parity evidence;
- the complete gate cannot observe the changed behavior.
