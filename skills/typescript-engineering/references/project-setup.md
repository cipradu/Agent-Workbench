# Project Setup And Dependency Management

Load for project creation or changes to pnpm, workspace discovery, manifests, dependencies, catalogs, filters, lockfiles, lifecycle scripts, runtime declarations, or canonical scripts.

## Resolve The Actual Roots

Read the Git root and every applicable nested workspace/package root. Inspect root and package `package.json` files, `packageManager`, `engines`, module `type`, scripts, dependency fields, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `.npmrc`, lifecycle permissions, hook bootstrap, CI install commands, and task-runner config. The Git root may own hooks while a nested workspace owns package commands.

## pnpm Is The Default

- New projects use pnpm and commit one workspace lockfile.
- Root `packageManager` names an exact pnpm version. Use that declaration wherever the executable is selected.
- Install from the workspace root. Use `pnpm add`, `remove`, `update`, `install`, and `exec`; never hand-edit the lockfile or installed tree.
- CI and production use `pnpm install --frozen-lockfile`. Offline install is valid only when the build supplies a complete store.
- Do not use `pnpm dlx` for a tool already declared by the project.
- Preserve another manager only when it provides equivalent explicit manifest, lockfile, workspace, frozen-install, lifecycle-script, and direct-dependency guarantees. Migration is separate approved work.

## Workspace And Direct Dependencies

Declare workspace discovery once with explicit roots. Discovery globs find packages; they do not authorize imports.

Use `workspace:*` for internal dependencies unless the publishing contract needs another workspace protocol. Prefer `link-workspace-packages=false` when the installed pnpm major supports it so local linkage requires an explicit workspace declaration.

Every package declares every external package it imports directly. Do not rely on hoisting, transitive dependencies, root tooling dependencies, or an accumulated local `node_modules`. Root dependencies are repository tooling only; application/package dependencies belong to their consumers.

Use pnpm filters deliberately:

- package name/directory for package-local work;
- `pkg...` for a package plus dependencies;
- `...pkg` for a package plus dependents;
- changed-set filters only when the chosen comparison base is explicit.

Use pnpm filters for package management. Use the task orchestrator's filters for task execution when Turborepo owns the graph.

## Dependency Version Policy

Read and preserve the project's declared dependency-version policy. The committed lockfile provides exact application resolution; library manifests still declare supported consumer compatibility. Do not silently invent exact, caret, tilde, or moving ranges from a generic template.

Manager/runtime/image/CI-action pins, application dependency ranges, library peer compatibility, overrides, and patches are different contracts. A restriction needs a recorded reason such as an API floor, peer constraint, incompatible release, duplicate identity, or security remediation.

## Lifecycle Scripts, Catalogs, Overrides, And Patches

Package lifecycle scripts execute code during installation. Project Setup owns the installed pnpm major's allow/deny configuration mechanics; Security owns the package and script trust decision. Record the exact package, script purpose, and removal condition. Never enable all scripts or bypass the manager's policy to make installation pass.

Catalogs may centralize shared dependency ranges across packages. They do not make a dependency direct: each importing package still declares the catalog entry. Keep one owner for each shared range and avoid named catalogs unless separate compatibility sets are real.

Overrides and patches live in the workspace configuration supported by the installed major. Keep them narrow, state the affected edge and removal condition, and revalidate after the target version changes. Exact overrides may be required to collapse peer-induced duplicate identities; a broad range is not proof of deduplication. Patches are last resort when no compatible upstream release exists.

After dependency-graph changes, remove `*.tsbuildinfo`, emitted output, `.turbo`, and lint/tool caches. Reinstall cleanly, inspect the actual installed graph/symlink resolution, and run the full gate. Incremental green is not dependency proof.

## Canonical Scripts

Expose distinct scripts for safe fix, read-only formatting/baseline lint, semantic lint, compiler/project diagnostics, each required test scope with coverage, build/declarations/package verification, one aggregate `check` that does not rewrite tracked source, and a broader CI mirror when needed. Hooks and CI call these scripts rather than duplicating command bodies.

Failure output: `Blocked: package/dependency ownership is incomplete: <root, manager, workspace link, direct declaration, lifecycle policy, lockfile, override, or script>.`
