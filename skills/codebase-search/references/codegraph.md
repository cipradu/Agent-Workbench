# CodeGraph CLI Operations

Use this reference after the main skill selects CodeGraph for code-oriented repository discovery: indexed files, symbols, definitions, source context, callers, callees, dependencies, routes, components, affected tests, or preliminary change impact.

## What CodeGraph Does

CodeGraph builds a project-local static code graph from supported source files. It extracts symbols and relationships with Tree-sitter-based parsers, framework resolvers, and a local SQLite index. The CLI can search the graph, return current source around a symbol, traverse callers and callees, estimate impact, and find tests affected by changed files.

CodeGraph is a discovery and navigation mechanism. Its relationships can omit or misresolve runtime dispatch, reflection, dependency injection, registry wiring, generated behavior, unsupported syntax, excluded files, external consumers, and other behavior that static extraction cannot prove. Use graph results to identify relevant evidence, then verify material claims in current source and with the proof mechanisms required by the main skill.

## Interface Policy

Use the CLI by default. It exposes the project lifecycle and the complete query surface without adding MCP tools to the agent context.

Use MCP only when:

1. the required CLI operation is unavailable or unusable;
2. a working CodeGraph MCP server is already exposed in the current session; and
3. using the exposed tool is narrower than changing or installing anything.

Do not install CodeGraph, register an MCP server, edit an MCP configuration, initialize a project, change telemetry, edit Git ignores, create or change `codegraph.json`, rebuild an index, or delete CodeGraph state without explicit user authorization. A missing CLI or index is a setup handoff, not permission to create it.

## Project and Path Rules

Operate on the current repository by default.

- For commands with positional `[path]`, omit the path when the current working directory is the intended repository.
- For query commands that accept `-p, --path <path>`, omit it for the current repository and supply it only when the task explicitly targets a different repository or the current directory cannot resolve the intended project.
- Resolve the project root before inspecting `.gitignore`, `codegraph.json`, or generated state.
- Never use an index whose `projectPath` or worktree does not match the repository being examined.

Bracketed values in this reference are placeholders. Replace them with real values; do not type the brackets literally.

## CLI Availability

Check availability without changing the machine:

```text
codegraph version
```

`codegraph -v` and `codegraph --version` are equivalent version checks.

If the executable is absent, report that CodeGraph CLI installation is required. Do not install it. When the user explicitly authorizes installation, use one official route suited to the machine:

| Installation route | Command |
| --- | --- |
| macOS or Linux standalone bundle | `curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh \| sh` |
| Windows PowerShell standalone bundle | `irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 \| iex` |
| Existing Node installation | `npm i -g @colbymchenry/codegraph` |

The standalone installer may add its binary directory to `PATH`; a new shell can be required before `codegraph version` succeeds. Verify the installed executable after any authorized installation.

The standalone bundle includes its runtime and does not require a separate Node installation. The npm package declares Node `>=20 <25`; the CLI blocks older or newer Node releases unless `CODEGRAPH_ALLOW_UNSAFE_NODE` is set. Do not use that override as a normal installation fix. The embedding API requires Node 22.5 or newer for `node:sqlite`; this does not apply to the bundled CLI.

Do not confuse CLI installation with `codegraph install`. The latter configures agent MCP integrations and does not install the project index.

## Telemetry and Network Behavior

CodeGraph has external usage telemetry. Before the first normal CodeGraph operation, require telemetry to be disabled.

Inspect the effective setting:

```text
codegraph telemetry status
```

Durably disable telemetry when authorized:

```text
codegraph telemetry off
```

The durable command stores the choice and deletes unsent buffered telemetry. These environment variables also disable telemetry for the process:

```text
CODEGRAPH_TELEMETRY=0
DO_NOT_TRACK=1
```

Use this process environment template when the durable setting cannot be established or when a launcher, shell profile, CI job, or agent configuration must enforce the setting independently:

```text
CODEGRAPH_TELEMETRY=0
```

Use this expanded template only for a process that also requires a custom state directory or must suppress the MCP release-update check:

```text
CODEGRAPH_TELEMETRY=0
CODEGRAPH_DIR=<STATE_DIRECTORY_NAME>
CODEGRAPH_NO_UPDATE_CHECK=1
```

Template rules:

- Keep `CODEGRAPH_TELEMETRY=0`; it disables telemetry for that process.
- Replace `<STATE_DIRECTORY_NAME>` with one plain directory segment, or delete the `CODEGRAPH_DIR` line to use `.codegraph/`.
- Keep `CODEGRAPH_NO_UPDATE_CHECK=1` only when the same MCP process must also avoid the daily GitHub release check; delete it for normal CLI-only use.
- `DO_NOT_TRACK=1` can replace the telemetry and update-check lines when the owning environment intentionally applies the cross-tool setting.
- Apply the variables through the active process environment or the target harness’s verified environment field. Do not create or commit an `.env` file merely to hold them, and do not create or edit an environment owner without user authorization.

When telemetry is enabled, CodeGraph can send install, index, daily usage-rollup, and uninstall events. The documented payload includes a random machine ID, CodeGraph version, OS and architecture, Node major version, CI state, schema version, language names, coarse file-count and duration buckets, command or MCP tool counts and errors, and connecting agent name/version. It does not send source code, repository names or URLs, file paths or names, symbol names, search queries, usernames, hostnames, emails, environment variables, or client IP addresses. Events go to `telemetry.getcodegraph.com` and are forwarded to PostHog in the US after allowlist validation and IP stripping.

The MCP server separately checks GitHub for an available CodeGraph version at most once per day. `CODEGRAPH_NO_UPDATE_CHECK=1` disables only that check. `DO_NOT_TRACK=1` disables both telemetry and the update check.

Some product text describes CodeGraph as fully local. The telemetry implementation and `TELEMETRY.md` are the behavioral authority: queries and indexes are local, but enabled telemetry leaves the machine. Keep telemetry disabled under this workflow.

## Generated State and Required Root Ignore

The default project state directory is `.codegraph/`. `CODEGRAPH_DIR` can replace it with one plain directory name. Absolute paths, `.`, `..`, path separators, and traversal values are invalid and fall back to `.codegraph`.

CodeGraph considers a project initialized when the effective state directory contains `codegraph.db`.

Before `init`, `index`, or `sync`:

1. resolve the effective state-directory name;
2. inspect the project-root `.gitignore`;
3. run `git ls-files -- "<repository-relative-state-directory>"` and require no tracked CodeGraph state;
4. require the exact state directory to be ignored by the project-root `.gitignore`;
5. verify the rule with `git check-ignore -v --no-index "<repository-relative-state-directory>/"`.

If the project-root `.gitignore` does not exist, report that it must be created before initialization. If it exists but lacks the required entry, report the exact entry that must be added. Do not initialize or index until the root ignore is present and verified.

### Root `.gitignore` template: default state directory

Location: `<project-root>/.gitignore`

```gitignore
# Local CodeGraph index
/.codegraph/
```

### Root `.gitignore` template: custom state directory

Location: `<project-root>/.gitignore`

```gitignore
# Local CodeGraph index
/<CODEGRAPH_DIR>/
```

Template rules:

- Replace `<CODEGRAPH_DIR>` with the exact single directory name supplied through `CODEGRAPH_DIR`.
- Do not include angle brackets in the resulting rule.
- Do not add unrelated dependency, environment, build, cache, or editor patterns.
- Use a root-anchored directory rule so the local index cannot be committed.

`codegraph init` also writes `<state-directory>/.gitignore` containing `*` and `!.gitignore`. That nested file deliberately remains trackable and therefore does not satisfy the required project-root ignore. The root rule must ignore the entire state directory.

After any authorized lifecycle write, run:

```text
git status --short --ignored
```

Require the CodeGraph directory to appear only as ignored state and require no CodeGraph file to be tracked or staged.

## Project Configuration

Upstream CodeGraph is zero-config by default. This workflow deliberately retains a reviewable project profile: before an authorized first initialization, copy the canonical package template to the project root and keep neutral values for fields the repository does not need. This makes later corpus and extension choices explicit instead of reconstructing them from memory.

The only project configuration file is:

```text
<project-root>/codegraph.json
```

It contains no provider, model, API key, credential, telemetry, MCP, or state-directory setting. CodeGraph’s static extraction does not require an LLM or embedding provider. Treat `codegraph.json` as ordinary reviewable project configuration that is normally committed; do not add it to `.gitignore`.

### Copy the package template

Resolve `<CODEBASE_SEARCH_SKILL_ROOT>` to the directory containing this skill’s `SKILL.md`. Before an authorized first initialization, copy:

```text
cp <CODEBASE_SEARCH_SKILL_ROOT>/templates/codegraph/codegraph.json.template <PROJECT_ROOT>/codegraph.json
```

The source template is [CodeGraph project config template](../templates/codegraph/codegraph.json.template).

Do not overwrite an existing `codegraph.json`. Inspect and reconcile it against the supported fields below. Do not invent additional keys from environment variables, MCP configuration, or another tool.

Validate JSON before initialization and after every edit:

```text
python3 -m json.tool <PROJECT_ROOT>/codegraph.json
```

This proves JSON syntax only. CodeGraph has no separate project-config validation command, and indexing does not validate every field loudly. Malformed JSON, invalid extension names or language IDs, non-array pattern fields, and invalid pattern entries produce warnings and are skipped. A missing file, a non-object top level, a missing field, an invalid `extensions` container type, and unknown top-level keys can fall back or be ignored silently. Read any warnings and verify the effective indexed coverage; neither a zero exit status nor silence proves that every configured value was accepted.

The source-supported top-level keys are:

| Key | Type | Purpose |
| --- | --- | --- |
| `extensions` | object mapping extension to language ID | map a final file extension to a supported CodeGraph language; mappings override built-ins |
| `include` | array of non-empty gitignore-style patterns | force first-party source into the index when `.gitignore` excludes it |
| `exclude` | array of non-empty gitignore-style patterns | exclude repository-relative paths even when Git tracks them |
| `includeIgnored` | array of non-empty gitignore-style patterns | include ignored directories that contain embedded Git repositories |

Precedence and limits:

- `exclude` wins over `include`.
- `include` overrides `.gitignore` only for ordinary first-party source. It cannot restore `.git`, CodeGraph’s own state directory, or built-in excluded dependency/build directories.
- `includeIgnored` is only for ignored embedded Git repositories; it is not the general way to restore ignored source.
- A deliberate negation in the project-root `.gitignore`, such as `!vendor/`, is CodeGraph’s supported opt-in for overriding a built-in default exclusion. This can also change Git’s view of untracked files, so inspect the full parent-rule chain and `git status` before adding one. Do not substitute `include` or `includeIgnored`.
- Extension keys normalize to lowercase and may omit the leading dot, but the template includes it explicitly.
- An extension key must name the final extension only. Multi-dot keys, path separators, an empty key, `.`, or path-like values are invalid.
- Language values must be a supported CodeGraph language ID.
- Missing or invalid configuration never stops indexing. Depending on the failure shape, CodeGraph either warns and skips the value or silently uses the corresponding zero-config default.

Template rules:

- Keep the four supported keys. Their neutral values are `{}` for `extensions` and `[]` for the three pattern lists.
- Add an `extensions` entry only when repository source uses a nonstandard final extension or a built-in extension must be remapped. Use the form `".ext": "language-id"`; do not use a filename, path, or multi-dot suffix.
- Add an `exclude` entry for repository-relative source that CodeGraph would otherwise index, including tracked source that `.gitignore` cannot remove from the graph. Prefer a root-relative directory pattern such as `"vendor/sdk/"`; use globs only when the intended match set requires them.
- Add an `include` entry only for ordinary first-party source intentionally hidden by `.gitignore`. Prefer the narrow root-relative path such as `"Tools/"`; a recursive glob is unnecessary when the directory itself is the intended subtree.
- Add an `includeIgnored` entry only for a gitignored directory in which CodeGraph should discover embedded Git repositories. Name the ignored directory itself with a trailing slash, such as `"repos/"`; do not replace it with a contents-only `"repos/**"` pattern.
- Use plain JSON without comments or trailing commas.
- Use forward-slash, project-root-relative, gitignore-style patterns for `include`, `exclude`, and `includeIgnored`.
- Do not add speculative entries. Every nonempty value must correspond to verified repository content and an intended coverage decision.
- After any configuration change, run an authorized full `codegraph index` before relying on coverage. This guarantees that additions, removals, and extension remaps are reconciled across the complete index.
- After the full index, inspect `codegraph status --json`, `codegraph files`, CodeGraph warnings, and representative expected inclusions and exclusions. A successful command alone does not prove corpus correctness.

Supported language IDs for `extensions` are:

```text
typescript, javascript, tsx, jsx, arkts, python, go, rust, java, c, cpp,
csharp, razor, php, ruby, swift, kotlin, dart, svelte, vue, astro, liquid,
pascal, scala, lua, luau, objc, r, solidity, nix, yaml, twig, xml,
properties, cfml, cfscript, cfquery, cobol, vbnet, erlang, terraform
```

Do not map an extension to `unknown`.

## Packaged Skills and Agent Instructions

The audited CodeGraph 1.5.0 repository includes agent-facing files, but none is required for normal consumer use of this CLI-first codebase-search skill:

| Upstream artifact | Actual owner and purpose | Consumer disposition |
| --- | --- | --- |
| `.claude/skills/add-lang/SKILL.md` | CodeGraph maintainers adding or benchmarking a new parser language inside the CodeGraph repository | do not copy, install, or load for repository search |
| `.claude/skills/agent-eval/SKILL.md` | CodeGraph maintainers running paid Claude benchmark comparisons against CodeGraph itself | do not copy, install, or load for repository search |
| `.cursor/rules/codegraph.mdc` | always-on Cursor MCP steering that prefers `codegraph_explore` and tells the agent to trust returned source without a separate grep/read loop | do not copy; this package is CLI-first and requires current-source verification for material claims |
| installer-generated `CLAUDE.md`, `AGENTS.md`, or `GEMINI.md` block | short MCP-or-CLI steering written by `codegraph install` for selected harnesses | do not install for normal use; this `codebase-search` skill owns routing |

`codegraph install` configures agent integrations. It can write MCP entries, permissions, hooks, and harness instructions; it does not install the CLI binary and does not initialize the project index. Do not run it as part of CodeGraph project setup.

The CodeGraph repository’s own `CLAUDE.md` and development documentation govern contributors to CodeGraph itself. They are source evidence about the product, not reusable consumer skills.

## Runtime Environment Configuration

Environment variables configure a CodeGraph process or installer; they do not belong in `codegraph.json`.

### Operational variables

| Variable | Behavior |
| --- | --- |
| `CODEGRAPH_DIR` | per-project state-directory name; must be one plain directory segment |
| `CODEGRAPH_TELEMETRY` | `0` or `false` disables telemetry; another nonempty value enables it |
| `DO_NOT_TRACK` | a truthy value other than `0` or `false` disables telemetry and update checks |
| `CODEGRAPH_NO_UPDATE_CHECK` | a truthy value disables the MCP server’s daily GitHub release check |
| `CODEGRAPH_VERSION` | pins a standalone installation or upgrade version |
| `CODEGRAPH_INSTALL_DIR` | overrides the standalone installer’s installation directory |
| `CODEGRAPH_BIN_DIR` | overrides the macOS/Linux launcher directory |
| `CODEGRAPH_NO_INSTALL_REFRESH` | skips the post-upgrade refresh of previously installed agent configuration |
| `CODEGRAPH_NO_PROMPT_HOOK` | `1` prevents upgrade from creating or updating the global Claude prompt hook |
| `CODEGRAPH_PROMPT_HOOK` | `0` also prevents upgrade from creating or updating the global Claude prompt hook |
| `CODEGRAPH_NO_WATCH` | `1` disables the MCP file watcher |
| `CODEGRAPH_FORCE_WATCH` | `1` forces the watcher on, including environments where auto-detection would disable it |
| `CODEGRAPH_WATCH_DEBOUNCE_MS` | watcher debounce in milliseconds; valid range `100` through `60000`, default `2000` |
| `CODEGRAPH_NO_DAEMON` | a truthy value except `0` or `false` makes each MCP session run in-process |
| `CODEGRAPH_MCP_TOOLS` | comma-separated MCP tool allowlist; omitted uses the default `explore` surface |
| `CODEGRAPH_ALLOW_UNSAFE_NODE` | bypasses the npm CLI’s supported Node-version gate; diagnostic escape hatch, not normal configuration |
| `NO_COLOR` | disables ANSI color |
| `FORCE_COLOR` | forces ANSI color where the runtime supports it |

### Query, watcher, and daemon tuning

These are diagnosis-specific runtime controls. Do not add them to a normal template or change them without a concrete observed problem.

| Variable | Behavior |
| --- | --- |
| `CODEGRAPH_EXPLORE_LINENUMS` | `0` disables line numbers in MCP explore output; default enabled |
| `CODEGRAPH_ADAPTIVE_EXPLORE` | `0` or `false` disables adaptive explore behavior; default enabled |
| `CODEGRAPH_RANK_NO_MULTITERM` | `1` disables multi-term ranking corroboration |
| `CODEGRAPH_CATCHUP_GATE_TIMEOUT_MS` | MCP catch-up wait; default `3000`; `0` waits without a timeout |
| `CODEGRAPH_MAX_DIR_WATCHES` | maximum watched directories; positive integer, default `50000` |
| `CODEGRAPH_DAEMON_IDLE_TIMEOUT_MS` | shared-daemon idle timeout; default `300000` |
| `CODEGRAPH_DAEMON_MAX_IDLE_MS` | daemon idle backstop; default `1800000`; `0` disables the backstop |
| `CODEGRAPH_DAEMON_CLIENT_SWEEP_MS` | dead-client sweep interval; default `30000`; `0` disables the sweep |
| `CODEGRAPH_QUERY_POOL_SIZE` | query-worker count; default is CPU-derived and capped at `16`; `0` disables the pool |
| `CODEGRAPH_QUERY_BUSY_TIMEOUT_MS` | query-worker SQLite busy timeout; minimum `1000`, default `45000` |
| `CODEGRAPH_MCP_DEBUG` | enables MCP diagnostics on standard error |
| `CODEGRAPH_DEBUG` | enables general error diagnostics |
| `CODEGRAPH_NO_WATCHDOG` | truthy value disables the liveness watchdog |
| `CODEGRAPH_WATCHDOG_TIMEOUT_MS` | liveness watchdog timeout; positive numeric value, default `60000` |
| `CODEGRAPH_STARTUP_HANDSHAKE_TIMEOUT_MS` | startup handshake timeout; default `900000`; zero or negative disables it |
| `CODEGRAPH_PPID_POLL_MS` | parent-process polling interval; default `5000`; `0` disables polling |

### Extraction, resolution, and database tuning

These source-level controls are for targeted diagnostics, performance testing, or upstream development. They are not stable project policy and must not be copied into a repository template without evidence that the specific control is needed.

| Variable | Behavior |
| --- | --- |
| `CODEGRAPH_PARSE_WORKERS` | parse-worker count, clamped to `1` through `16`; default is CPU-derived and capped at `8` |
| `CODEGRAPH_PARSE_TIMEOUT_MS` | positive per-file parse timeout; default `10000` |
| `CODEGRAPH_NO_STORE_WORKER` | `1` disables the writer worker |
| `CODEGRAPH_KERNEL` | `0` disables the native extraction kernel |
| `CODEGRAPH_KERNEL_LANGS` | `all` or comma-separated language IDs routed to the native kernel |
| `CODEGRAPH_KERNEL_PATH` | explicit native-kernel `.node` path |
| `CODEGRAPH_KERNEL_DEBUG` | `1` enables kernel diagnostics |
| `CODEGRAPH_KERNEL_CFNPTR` | `0` disables the native C function-pointer pass |
| `CODEGRAPH_NO_RELAUNCH` | disables WASM-runtime relaunch |
| `CODEGRAPH_VALUE_REFS` | `0` disables same-file value-reference edges |
| `CODEGRAPH_NO_PARALLEL_RESOLVE` | `1` disables parallel reference resolution |
| `CODEGRAPH_PARALLEL_RESOLVE_MIN` | minimum unresolved-reference count for parallel resolution; default `150000` |
| `CODEGRAPH_RESOLVE_WORKERS` | resolver-worker count; `0` disables and positive values cap at `16` |
| `CODEGRAPH_RESOLVER_CACHE_SIZE` | positive resolver cache size; default `5000` |
| `CODEGRAPH_AMBIGUOUS_NAME_CEILING` | positive ambiguity ceiling; default `500` |
| `CODEGRAPH_RESOLVE_PROFILE` | enables resolver profiling; `2` adds stage attribution |
| `CODEGRAPH_SYNTH_TIMINGS` | enables synthesis, pool, and WAL timing diagnostics |
| `CODEGRAPH_NO_FAST_INIT` | `1` disables fresh-database fast initialization |
| `CODEGRAPH_NO_WAL_DEFER` | `1` disables deferred WAL work |
| `CODEGRAPH_WAL_VALVE_MB` | positive WAL threshold in MiB; default begins at `256` and adapts with database size |
| `CODEGRAPH_WAL_VALVE_DEBUG` | enables WAL-valve diagnostics |

Internal protocol and test variables such as `CODEGRAPH_DAEMON_INTERNAL`, `CODEGRAPH_HOST_PPID`, `CODEGRAPH_WASM_RELAUNCHED`, and `CODEGRAPH_QUERY_WORKER_ALLOW_TEST_CRASH` are not user configuration. Do not set them.

## Initialization State Machine

Inspect state before any project write:

```text
codegraph status --json
```

For an explicitly targeted repository:

```text
codegraph status <path> --json
```

Follow this state machine:

| Observed state | Meaning | Action |
| --- | --- | --- |
| CLI missing | CodeGraph cannot run | report the appropriate installation requirement; do not install |
| `initialized: false` | no usable project index | verify the retained `codegraph.json`, root `.gitignore`, telemetry-off state, and authorization; then initialize if authorized |
| `initialized: true` and healthy | an index exists | complete the mandatory sync-and-verify sequence before any query |
| `worktreeMismatch` is non-null | index belongs to a different worktree | do not use it; initialize the intended worktree separately only if authorized |
| `index.state` is `indexing` | a full build did not reach a completed state or may still be running | determine whether an active build owns it; otherwise rebuild if authorized |
| `index.state` is `partial` or `failed` | file or relationship coverage is incomplete | run a full rebuild if authorized; otherwise use direct fallbacks |
| `index.state` is `null` | the index predates the completion-state marker, so complete coverage is unproven | run a full rebuild if authorized; otherwise use direct fallbacks |
| `index.pendingRefs` is greater than zero | caller and impact edges are incomplete | run `sync` if authorized; do not make exhaustive relationship claims |
| `index.reindexRecommended: true` | extraction logic has changed since the build | run a full rebuild before exhaustive graph claims |
| pending added, modified, or removed files | stored relationships may be stale | run `sync` or inspect affected files directly |
| zero indexed files or nodes | initialization found no useful supported source | inspect coverage, configuration, ignored paths, and language support; do not treat initialization as successful |

### Initialize

After the canonical `codegraph.json` template has been copied or an existing config has been reconciled and validated, the required root ignore and telemetry state are verified, and initialization is explicitly authorized:

```text
codegraph init
```

For an explicitly targeted repository:

```text
codegraph init <path>
```

Options:

| Option | Meaning |
| --- | --- |
| `-i, --index` | deprecated compatibility flag; initialization already builds the index |
| `-f, --force` | bypass protection against indexing a home directory or filesystem root |
| `-v, --verbose` | show detailed worker and memory output |

Do not use `--force` as a routine retry. Confirm the intended repository instead.

Initialization can present secondary mutation prompts:

- When live watching is unavailable in a Git repository, CodeGraph asks whether to install commit, merge, and checkout synchronization hooks. The default selection is hook installation. Decline hook installation unless those exact hooks were separately authorized; use the verified sync helper in this reference before later queries rather than treating the prompt’s plain `codegraph sync` alternative as freshness proof.
- When initialization yields no nodes because ignored embedded repositories were found, CodeGraph asks whether to add them to `codegraph.json` under `includeIgnored` and rebuilds after acceptance. The default answer is yes. Decline unless the exact embedded repositories and configuration edit were separately authorized.

The initialization handoff must disclose the required `codegraph.json` copy or reconciliation before execution. Authorization to initialize does not cover Git hooks or an interactive rewrite of `includeIgnored`; decline those secondary prompts unless separately authorized.

Verify initialization with:

```text
codegraph status --json
```

Require:

- `initialized: true`;
- `projectPath` matching the intended repository;
- `fileCount` and `nodeCount` greater than zero for a repository expected to contain supported source;
- `index.state` equal to `complete`;
- `index.reindexRecommended` equal to `false`;
- `index.pendingRefs` equal to zero;
- no `worktreeMismatch`;
- zero pending added, modified, and removed files.

`journalMode` should be `wal`. A different mode means concurrent reads can block on writes, which commonly occurs on network filesystems and WSL-mounted Windows drives.

## Refresh and Repair

### Why status and watchers are not freshness proof

`codegraph status --json` is required for project identity and structural health, but its pending-change calculation uses Git status as a fast path when Git is available. That detects dirty, staged, untracked, and removed source files by comparing their contents with the index. It can report zero pending changes after a clean pull, checkout, merge, or rebase even when the stored index predates the new commit.

`codegraph sync` does not have that limitation. Without watcher-supplied scoped paths, it reconciles the current filesystem against every indexed file using file metadata and content hashes. It catches committed changes that Git status cannot show.

The plain CLI still cannot prove that this reconciliation ran. When another process owns `codegraph.lock`, the current library returns `filesChecked: 0` and `durationMs: 0`; the CLI renders that all-zero result as `Already up to date` and exits successfully. Post-sync status has no field that distinguishes this lock failure from a completed clean sync.

The MCP watcher can reduce the interval between edits and synchronization, but it can be absent, starting, degraded, frozen, or unable to observe changes made while it was not running. Git hooks cover only their configured Git events. Neither is accepted as the freshness proof for this CLI-first workflow.

### Incremental refresh

The CLI-first workflow does not depend on an active MCP watcher. After the initial status inspection and before every first CodeGraph query in a search workflow, run the package helper when lifecycle writes are authorized, even if status reports zero pending changes:

```text
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/codegraph-sync-verified.py --project-root <PROJECT_ROOT>
```

The helper resolves the installed CodeGraph library from the `codegraph` executable, disables telemetry in its child process, runs the library’s unscoped `sync()`, and prints a JSON result. It fails closed when the executable, module, Node runtime, project, sync, or lock-success proof is unavailable.

Treat this exact result as lock contention and failed freshness proof:

```text
filesChecked: 0
durationMs: 0
```

The helper reports that condition on stderr and exits `3`. It exits `1` for other resolution or sync failures. Exit `0` plus JSON containing `freshnessVerified: true` proves the full reconciliation ran; it does not by itself prove the final index health.

After helper success, verify with `codegraph status --json` and require:

- `initialized: true`;
- `projectPath` matching the intended repository;
- nonzero files and nodes when the expected corpus contains supported source;
- `index.state` equal to `complete`;
- `index.reindexRecommended` equal to `false`;
- `index.pendingRefs` equal to `0`;
- `worktreeMismatch` equal to `null`;
- pending added, modified, and removed counts all equal to `0`.

If the post-sync status does not pass every applicable condition, do not run a CodeGraph query. Use the full-rebuild branch when its conditions apply; otherwise use current-source fallbacks and report the failed condition.

Do not replace the helper with plain `codegraph sync`, an `Already up to date` message, a zero exit status, watcher state, hook state, or a missing lock file. None proves that the required filesystem reconciliation completed.

### Full rebuild

Run a full rebuild after configuration changes, when the extraction version is outdated, when state is `partial` or `failed`, when a previous build was interrupted, or when incremental synchronization cannot restore complete state:

```text
codegraph index
```

For an explicitly targeted repository:

```text
codegraph index <path>
```

Options:

| Option | Meaning |
| --- | --- |
| `-f, --force` | bypass home-directory or filesystem-root protection |
| `-q, --quiet` | suppress progress output |
| `-v, --verbose` | show detailed worker and memory output |

Do not use `--force` unless the protected path is deliberately intended and the user explicitly authorizes the risk.

If a full rebuild yields no nodes because ignored embedded repositories were found, CodeGraph can ask to add them to `codegraph.json` under `includeIgnored` and re-index. The default answer is yes. Decline unless the exact embedded repositories and configuration edit were separately authorized.

### Stale lock recovery

```text
codegraph unlock [path]
```

This removes `codegraph.lock`; it does not prove the lock is stale. Use it only after confirming that no active CodeGraph indexing process owns the lock and after obtaining explicit authorization.

### Daemon inspection

```text
codegraph daemon
codegraph daemons
```

`daemons` is an alias. In a terminal, the command can present running background daemons and allow one or all to be stopped. In non-interactive output it lists them without the selection prompt. Stopping a daemon is a process mutation and requires authorization.

## CLI Query Commands

Global display options:

| Option | Meaning |
| --- | --- |
| `--color` | force ANSI color |
| `--no-color` | disable ANSI color; `NO_COLOR` is also honored |

### Broad exploration

```text
codegraph explore <query...> [-p <path>] [--max-files <number>]
```

Use for feature orientation, behavior spanning several symbols, related source context, or an initial call-path view. The output groups relevant current source by file and can include connected call paths and a preliminary blast radius. `--max-files` caps source-bearing files; a cap or truncation notice requires narrower follow-up queries.

### Symbol search

```text
codegraph query "<search>" [-p <path>] [-l <number>] [-k <kind>] [-j, --json]
```

Options:

| Option | Meaning |
| --- | --- |
| `-p, --path <path>` | target project |
| `-l, --limit <number>` | maximum returned results; default `10` |
| `-k, --kind <kind>` | filter to a node kind |
| `-j, --json` | return structured JSON |

Valid node kinds are:

```text
file, module, class, struct, interface, trait, protocol, function, method,
property, field, variable, constant, enum, enum_member, type_alias, namespace,
parameter, import, export, route, component
```

The query parser accepts exact and partial identifiers, quoted terms, and filters including `kind:`, `lang:` or `language:`, `path:`, and `name:`. Ranking orders inspection; it does not prove that lower-ranked or capped results are irrelevant.

### Symbol or file context

```text
codegraph node [name] [-p <path>] [-f <file>] [--offset <number>] [--limit <number>] [--symbols-only]
```

Use a symbol name for its definition, source body, callers, and callees. Use `-f, --file <file>` to read an indexed file or to disambiguate a same-named symbol. A path-like positional value is treated as file mode. `--offset` is a one-based starting line, `--limit` caps returned lines, and `--symbols-only` returns the file symbol map and dependents without the full file body.

### Indexed file layout

```text
codegraph files [-p <path>] [--filter <dir>] [--pattern <glob>] [--format <tree|flat|grouped>] [--max-depth <number>] [--no-metadata] [-j, --json]
```

Use this to inspect index coverage, constrain a noisy search, or list indexed source. `--format` defaults to `tree`. `--filter` restricts a directory, `--pattern` applies a glob, `--max-depth` limits tree depth, and `--no-metadata` omits language and symbol counts.

### Incoming relationships

```text
codegraph callers <symbol> [-p <path>] [-l <number>] [-j, --json]
```

The default result cap is `20`. The CLI aggregates exact same-named definitions and can fall back to the highest-ranked match. When names collide, enumerate definitions with `query`, inspect their files, and verify each relevant definition in current source.

### Outgoing relationships

```text
codegraph callees <symbol> [-p <path>] [-l <number>] [-j, --json]
```

The default result cap is `20`. Apply the same ambiguity controls as `callers`.

### Preliminary symbol impact

```text
codegraph impact <symbol> [-p <path>] [-d <1-10>] [-j, --json]
```

Traversal depth defaults to `2` and is clamped to `1` through `10`. The CLI can merge exact same-named definitions. Treat the result as candidate impact, then complete the main skill’s required coverage for tests, configuration, generated artifacts, dynamic wiring, persistence, contracts, and external consumers when those classes can affect the change.

### Tests affected by changed files

```text
codegraph affected [files...] [-p <path>] [--stdin] [-d <number>] [-f <glob>] [-j, --json] [-q, --quiet]
```

This traverses file dependencies and returns matching dependent test files. The default traversal depth is `5`. `--stdin` reads one path per line, `-f, --filter` replaces the default test-file matching with a glob, `--json` returns structured data, and `--quiet` returns file paths without decoration. With no file input, the command exits successfully without a result set.

Do not feed shell output into this command unless the task authorizes the source operation and its scope is understood. The command normalizes absolute, `./`-prefixed, and Windows-style paths to project-relative paths.

## Query Sequence

Choose the smallest set of operations that can cover the search target, not the smallest result set:

1. complete the mandatory `status --json` inspection, verified unscoped sync helper or required rebuild, and post-write `status --json` verification before the first query;
2. use `explore` for a feature, subsystem, behavior, or several related identifiers;
3. use `query` to enumerate definitions and collisions;
4. use `node` to inspect authoritative current source and disambiguate by file;
5. use `callers`, `callees`, or `impact` for required relationship directions;
6. use `files` to check indexed coverage or constrain a branch;
7. use `affected` when the task asks which tests cover changed files;
8. verify material relationships and every required coverage class outside the graph.

For same-named symbols, do not accept the first result. Inspect each definition that can satisfy the search target and use its file, qualified name, signature, surrounding source, and call sites to disambiguate it.

## Result and Error Interpretation

| Result or warning | Meaning | Response |
| --- | --- | --- |
| `No results found for "<query>"` | successful graph miss | vary canonical names, qualified names, paths, kinds, and direct search |
| `No callers found` or `No callees found` | no stored edge for the resolved definition set | verify references and dynamic wiring outside the graph |
| `No files found matching the criteria` | successful bounded file-list miss | check the filter and the direct filesystem |
| `No files indexed` | the index has no usable file coverage | stop relying on CodeGraph and inspect initialization/configuration |
| guidance that no index exists | the target is not initialized | follow the authorized initialization state machine or use direct fallbacks |
| pending-sync, stale-file, frozen-watcher, or worktree warning | stored relationships can disagree with the checkout | do not query CodeGraph; synchronize or rebuild when authorized, otherwise inspect current source directly |
| truncation notice | the result cap cut the candidate set or source | issue narrower follow-up commands until the cut area is covered |
| disabled MCP tool | the operation is outside the exposed MCP surface | use the CLI equivalent; do not expand MCP configuration |
| path refusal | the requested file or project lies outside CodeGraph’s accepted project boundary | correct an accidental input error; do not broaden paths to bypass the refusal |
| nonzero CLI exit | invalid input, missing state, lifecycle failure, or internal error | read the complete error, correct only verified input mistakes, then use the fallback route |

An empty traversal or successful graph miss does not prove that no source relationship exists.

## Coverage Controls and Limits

Coverage depends on the supported language and extension set, root and nested `.gitignore`, `codegraph.json`, built-in exclusions, file-size limits, generated/minified detection, parser success, and relationship resolution.

CodeGraph skips common dependency, build, cache, vendor, and generated-output directories even when no `.gitignore` exists. It also skips files larger than 1 MiB by default. Some supported formats provide file-level or framework-specific relationships rather than full symbol extraction.

Current source returned by `explore` or `node` can be newer than the relationships stored in the SQLite graph. Treat displayed source as a current read, but do not treat stale relationship data as current merely because it accompanied that source.

Record coverage exclusions that can change the answer. Use direct exact search, structural or type-aware search, generated-artifact inspection, configuration review, tests, and runtime wiring evidence as required by the main skill.

## MCP Fallback

Use this section only when a CodeGraph MCP server is already present and the CLI route is unavailable or lacks the needed operation.

The MCP stdio contract is:

```text
command: codegraph
args: serve, --mcp
```

Do not start `codegraph serve --mcp` in a terminal. It waits for JSON-RPC on standard input.

The default visible MCP surface lists only `codegraph_explore`. Other functional tools can include `codegraph_search`, `codegraph_node`, `codegraph_callers`, `codegraph_callees`, `codegraph_impact`, `codegraph_files`, and `codegraph_status`, but their exposure depends on `CODEGRAPH_MCP_TOOLS`. Do not change that allowlist for this skill; use the CLI.

Every MCP operation accepts an optional `projectPath`; it becomes required when the server cannot resolve a default project. Inspect the live tool schema because the exposed parameter contract is the runtime authority.

MCP registration is a separate, user-authorized setup task. `codegraph install` can write agent MCP configuration, permissions, and marker-fenced instructions. The read-only preview is:

```text
codegraph install --print-config <agent-id>
```

Supported installer target IDs in the audited source are `claude`, `cursor`, `codex`, `opencode`, `hermes`, `gemini`, `antigravity`, and `kiro`.

Installer command surface:

```text
codegraph install [-t, --target <ids>] [-l, --location <global|local>] [-y, --yes] [--no-permissions] [--print-config <agent-id>] [--refresh]
```

For Claude targets, the interactive installer separately offers a `UserPromptSubmit` hook and defaults to yes. `--yes` enables that hook automatically, and `--no-permissions` does not disable it. Authorization to register MCP does not authorize a prompt hook. Do not use `--yes` for a Claude target unless the hook was also authorized; choose no at the hook prompt, or use the reviewed manual configuration template instead.

Do not run the installer unless the user explicitly asks to configure MCP and every selected installer-owned surface is authorized.

### MCP configuration templates

Use these templates only for a separately authorized MCP setup task. Prefer `codegraph install --print-config <agent-id>` when the CLI is available because it emits the current target-specific template without writing files.

Claude, Gemini, and Kiro use the standard JSON server entry:

```json
{
  "mcpServers": {
    "codegraph": {
      "type": "stdio",
      "command": "codegraph",
      "args": [
        "serve",
        "--mcp"
      ]
    }
  }
}
```

Codex uses TOML:

```toml
[mcp_servers.codegraph]
command = "codegraph"
args = ["serve", "--mcp"]
```

Cursor project-local configuration pins the project path:

```json
{
  "mcpServers": {
    "codegraph": {
      "type": "stdio",
      "command": "codegraph",
      "args": [
        "serve",
        "--mcp",
        "--path",
        "<ABSOLUTE_PROJECT_ROOT>"
      ]
    }
  }
}
```

Replace `<ABSOLUTE_PROJECT_ROOT>` with the canonical absolute repository root. Cursor global configuration uses `${workspaceFolder}` in that position.

OpenCode uses its local-process wrapper:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "codegraph": {
      "type": "local",
      "command": [
        "codegraph",
        "serve",
        "--mcp"
      ],
      "enabled": true
    }
  }
}
```

Hermes uses YAML:

```yaml
mcp_servers:
  codegraph:
    command: codegraph
    args:
      - serve
      - --mcp
    timeout: 120
    connect_timeout: 60
    enabled: true
```

Template rules:

- Merge the `codegraph` entry into the harness’s existing configuration; do not overwrite unrelated servers or settings.
- Use the harness-specific configuration owner and supported location.
- Do not add a project `--path` argument except where the harness template requires it.
- Restart the agent after changing MCP configuration; index and `codegraph.json` changes do not require an agent restart.
- Antigravity can require an absolute executable path on macOS. Generate its exact current template with `codegraph install --print-config antigravity` instead of guessing.
- A configured MCP server still cannot query an uninitialized project. Project initialization remains a separate authorized lifecycle step.

## Maintenance and Removal Commands

### Upgrade

```text
codegraph upgrade [version] [--check] [-f, --force]
```

`--check` queries whether an update is available without installing it. Supplying a version pins that release; `CODEGRAPH_VERSION` can also provide the target version. An upgrade changes installed software and requires authorization.

A successful upgrade can also:

- create or update the global Claude prompt hook when a global Claude integration already exists;
- run `codegraph install --refresh` to rewrite agent instruction sections and MCP configuration previously owned by CodeGraph;
- offer CodeGraph Pro beta-waitlist signup in an interactive terminal, with yes as the default. Accepting asks for an email address and submits it to `https://getcodegraph.com/api/waitlist`.

Authorization to upgrade the binary does not authorize those secondary changes or the waitlist submission. When only the binary update is authorized, use one process-scoped template so both controls are present in the `codegraph upgrade` process.

POSIX shell:

```text
CODEGRAPH_NO_PROMPT_HOOK=1 CODEGRAPH_NO_INSTALL_REFRESH=1 codegraph upgrade [version]
```

PowerShell:

```powershell
$env:CODEGRAPH_NO_PROMPT_HOOK = "1"
$env:CODEGRAPH_NO_INSTALL_REFRESH = "1"
codegraph upgrade [version]
Remove-Item Env:CODEGRAPH_NO_PROMPT_HOOK
Remove-Item Env:CODEGRAPH_NO_INSTALL_REFRESH
```

Replace `[version]` with the authorized target version or remove it to use CodeGraph’s normal target selection. Do not type the brackets literally. The POSIX assignments apply only to that command. The PowerShell form removes both process variables after the command so they do not silently affect later work in the same shell.

If the beta-waitlist prompt appears, choose no unless the user separately authorized that external signup and supplied the email address for it.

### Remove project state

```text
codegraph uninit [path] [-f, --force]
```

This deletes the project’s CodeGraph state directory and leaves the project-root ignore rule unchanged. `--force` skips confirmation. This is destructive; never run it without explicit authorization and a verified target.

### Remove agent integration or CLI

```text
codegraph uninstall [-t, --target <ids>] [-l, --location <global|local>] [-y, --yes] [--keep-cli]
```

Without `--keep-cli`, uninstall can remove the CLI after removing configured agent integrations. It leaves per-project indexes in place. Verify exact targets and obtain explicit authorization before use.

## Branch Completion

The CodeGraph branch is complete only when:

1. project configuration is present, valid, source-supported, and reconciled with the intended corpus;
2. the queried index matches the intended repository and worktree;
3. the mandatory freshness sequence passed after the latest relevant repository change and before the first query;
4. every returned definition that can satisfy the search target is dispositioned;
5. every relevant truncation, result cap, collision, and ambiguous definition is resolved;
6. required callers, callees, dependents, impact nodes, or affected tests have been followed;
7. graph-derived claims have been checked against current source and the main skill’s required coverage classes;
8. the final closure pass adds no new relevant candidate.

Ordinary CodeGraph CLI queries are local reads of the project index and source. Lifecycle and configuration actions remain user-authorized mutations. Local databases, logs, caches, and query state are ordinary local tool state once their creation has been authorized; they are not separate search approval gates.
