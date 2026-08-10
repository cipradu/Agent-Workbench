# Turborepo

Load for Turborepo task graphs, dependencies, caching, inputs, outputs, environment hashing, filters, package configuration, persistent tasks, or watch behavior.

Turborepo owns task orchestration and caching. pnpm owns packages, workspace links, dependency declarations, and the lockfile. The application settings owner loads runtime configuration; Turbo only declares the files and environment inputs that affect task hashes.

## Task Ownership And Graph

- Package scripts own task logic. Root scripts delegate through `turbo run <task>`; root-only task logic is exceptional.
- Persisted scripts and CI use the explicit `turbo run` form supported by the installed major, not interactive shorthand.
- `^build` means the task on declared package dependencies; `build` means the same package; `package#build` names an exact package task.
- Dependency ordering follows manifest edges. An undeclared workspace dependency makes both import ownership and task order incomplete.
- Do not chain dependency builds manually, use `prebuild` to reconstruct the graph, or pass `--parallel` to bypass dependency order.
- Shared application code belongs in a package; one application does not import another application's source tree.

## Inputs, Outputs, And Cache Correctness

Inspect the real command before declaring cache behavior.

- File-producing tasks declare exact outputs, including declarations, source maps, bundles, reports, and `*.tsbuildinfo` when incremental/composite TypeScript writes it.
- Non-file tasks do not invent outputs solely to make caching look configured.
- Environment values that affect a task are declared in the installed major's hashed environment surface. Values required only at runtime/CI but not affecting output use the appropriate pass-through mechanism.
- `.env` files that affect a task are declared as inputs. Turbo never reads them for the application and never becomes a second settings owner.
- Prefer task-level inputs/environment over broad global dependencies that invalidate every cache entry.
- Paths outside a package use the installed major's repository-root token rather than `../` traversal.
- Package-specific task differences live in package Turbo configuration instead of a root file full of package overrides.

Cache correctness depends on the real dependency graph and complete inputs/outputs. A cache hit is not proof when those declarations are incomplete.

## Environment And Lifecycle

Use strict environment filtering for production/CI. Declare every task-required variable in the correct hashed or pass-through surface; loose mode is not the default.

Watch/dev graphs distinguish one-shot dependency preparation from persistent servers. Persistent tasks declare their lifecycle and do not become dependencies of finite tasks in a way that can never complete. Use transit nodes when tasks may execute in parallel but cache invalidation must still follow dependency-source changes.

## Filters And Verification

Use Turbo filters for task execution and pnpm filters for package management. Confirm the installed major's exact filter syntax before persisting it.

When task edges, inputs, outputs, or environment hashing change, delete `.turbo`, TypeScript incremental state, and affected output, then run the uncached canonical graph and the complete check. Do not accept a warm cache as proof of the new declaration.

Failure output: `Blocked: Turborepo graph is incomplete: <task owner, dependency edge, input, output, environment, cache, or lifecycle>.`
