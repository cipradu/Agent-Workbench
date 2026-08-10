# Hooks And CI

Load for canonical scripts, lint-staged, Husky, nested workspaces, pre-commit, pre-push, clean installation, or CI.

## Responsibility Chain

| Layer | Responsibility |
| --- | --- |
| Package scripts | Exact commands and aggregate composition |
| lint-staged | Ordered staged-file safe fixes and semantic feedback |
| Husky | Fail-closed Git-hook trigger |
| pre-push | Broader local CI mirror when declared |
| CI | Authoritative clean frozen-install acceptance |

Hooks and workflows call canonical scripts; do not duplicate command bodies.

## lint-staged And Pre-Commit

For TypeScript files, run the project safe Biome/Ultracite fix first and semantic ESLint second so semantic policy sees formatted code. Avoid overlapping globs that rewrite the same file concurrently. Do not send filenames to `tsc`; doing so can change project loading.

Pre-commit runs lint-staged and then the complete `check` that does not rewrite tracked source for the affected repository/workspace. It fails when the declared pnpm executable, installed dependencies, required root, or canonical script is unavailable. Missing prerequisites never yield success.

For a nested workspace, keep one hook tree at the Git root, evaluate the exact staged-path condition, and execute from the owning workspace root. Staged success is feedback only and cannot prove transitive, generated, workspace-wide, or unstaged behavior.

## Pre-Push And CI

When the project declares a broader CI mirror, pre-push invokes one canonical command covering full builds, declarations/package artifacts, integration suites, or other remote acceptance. It supplements rather than delays commit-time gates.

CI must:

- select the exact declared pnpm version and install with `--frozen-lockfile` from a clean checkout;
- run read-only formatting/baseline lint, semantic lint, compiler/projects, tests with coverage, build/declarations/package surfaces, and required integration/E2E scopes;
- keep one compiler-diagnostic owner while retaining distinct build/declaration/reference gates;
- use least-privilege permissions and project-approved action pinning;
- upload failure artifacts only after proving they contain no secrets.

`--no-verify` violates the local validation contract. Because Git cannot make hooks unbypassable, CI repeats every acceptance gate. Full `check` and CI commands do not mutate tracked source.

Failure output: `Not done: hook or CI enforcement is incomplete: <script, staged order, prerequisite, clean install, or missing gate>.`
