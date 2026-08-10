# Quality Gates And Semantic Enforcement

Load for Biome, Ultracite, ESLint, type-aware/custom policy, file discovery, autofix ownership, suppressions, or driving a project to a clean gate.

## One Owner Per Responsibility

For new projects:

- Biome configured through Ultracite owns formatting and broad syntax/style/correctness lint;
- type-aware ESLint owns semantic and project-architecture rules Biome cannot express completely;
- TypeScript owns compiler programs, project references, build/emit, and diagnostic duties;
- one tool owns each autofix/rule family.

Ultracite is the preset/configuration layer for Biome, not a second engine. ESLint does not own formatting or duplicate baseline rules. Preserve an incumbent only after mapping every required rule and file to an equally strong owner.

Oxlint, Oxfmt, or another engine is a migration candidate rather than an additive default. Compare identical file discovery, project assignment, rule/diagnostic coverage, autofix ownership, valid/invalid exit behavior, lifecycle, target-repository performance, removal cost, and rollback. Migrate one owner only with explicit scope.

## Biome Baseline

Use the installed Biome schema and matching Ultracite preset. Declare scan roots explicitly. Exclude dependencies, emitted output, caches, and exact accepted generated/vendor/tool-owned categories only.

Required project rules include `noConsole`, `noNonNullAssertion`, `noNestedTernary`, `noBarrelFile`, stable ASCII filename conventions, and the selected preset's correctness, security, accessibility, and performance protections. Do not suppress these at call sites.

## Type-Aware ESLint Baseline

Use flat config with the installed typescript-eslint strict type-checked and stylistic type-checked presets. Scope type-aware blocks to TypeScript file extensions and use `projectService` when supported, or explicit project assignment when the repository needs it. Prove every target file belongs to the intended program; do not make JS/MJS tooling require unavailable type information.

Enforce at least:

- deprecated APIs;
- floating/misused promises and invalid promise callback positions;
- async functions used as `Promise` constructor executors;
- `await` only on thenables and async functions that genuinely require async;
- strict boolean expressions and exhaustive switches;
- unsafe argument, assignment, call, member access, return, and enum comparison where supported;
- explicit `any` ban;
- unnecessary conditions, assertions, and type arguments;
- only throwable error values plus the stricter project catalog policy;
- consistent type-only imports and exports.

Project-derived semantic enforcement must cover:

- the sole settings/environment reader;
- centralized logger construction and direct `console`/stdout/stderr ownership;
- centralized catalog factories, surface-catalog import law, raw rethrow and native/local error bans;
- log-before-throw/catch-control ownership with correlation and typed error context;
- package/layer dependency direction, public subpaths, and boundary-escaping relative imports;
- route/service/tool I/O ownership and composition-root-only construction;
- sibling schema placement, inline schema prohibition, and one contract owner;
- tests outside production source, no focused/skipped markers, and no runtime test hooks;
- no convenience barrels;
- semantic schema/config fields having runtime consumers where structural enforcement is feasible.

Repository paths, aliases, package maps, settings-loader files, fallback writers, surface helpers, I/O owners, and composition roots are source-derived policy data. Update the map in the same change as the governed architecture.

## Native Rule First, Exact Custom Rule When Needed

Use `no-restricted-imports`, `no-restricted-properties`, and `no-restricted-syntax` only when an exact selector proves the invariant without banning the legitimate owner. When native rules cannot prove context, write one source-derived custom ESLint rule or structural guard for the exact policy.

Log-before-control is not provable by merely checking that a catch exists. Its rule must inspect catch/throw/control-flow context and require the approved logger call with correlation and the normalized typed error before the transition. Package dependency rules must derive the scan universe and policy map from project source truth rather than a partial hand list.

Flat config values such as `no-restricted-imports` and `no-restricted-syntax` are replaced by later matching blocks rather than safely concatenated. Compose every restriction for the matching file set in the final value or deliberately repeat the complete list; otherwise a later block silently removes earlier policy.

## Absolute Suppression Ban

Forbidden in handwritten source, tests, and configuration:

- `@ts-ignore`, `@ts-expect-error`, `@ts-nocheck`;
- ESLint, Biome, Oxlint, formatter, or vendor ignore comments;
- blanket file/directory disables or broad test-file type-safety downgrades;
- narrowed includes/globs or hidden exclusions used to avoid diagnostics;
- focused/skipped tests, coverage exclusions, assertion weakening, or snapshot refreshes used to get green.

When a rule is wrong, fix the rule in its centralized owner through the project decision path; do not suppress a call site. Exact generated/vendor/tool-owned categories may receive a config-level exception with an explicit owner and alternative gate. Handwritten tests remain under the same type-safety rules as production.

Negative type tests use an isolated suppression-free invalid fixture plus a valid companion and assert the intended diagnostic/exit result. If the toolchain cannot prove the negative case without suppression, report the limitation.

## Complete Gate

Run the project safe autofix once, inspect semantic changes, then run read-only full-scope Biome/Ultracite, semantic ESLint with zero warnings, compiler/project diagnostics, tests with coverage, build/declarations/package verification, and the aggregate check. Staged-file success is feedback only.

Failure output: `Not done: quality-gate integrity violation: <duplicate owner, suppression, incomplete rule, uncovered file, or failing gate>.`
