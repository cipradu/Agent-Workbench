# Graphify CLI Operations

Use this reference after the main skill selects Graphify for repository-wide knowledge discovery: cross-file code structure, documents, ADRs, specifications, schemas, manifests, package metadata, MCP configuration, communities, architectural hubs, paths, reports, media-derived concepts, or relationships across those source classes.

## What Graphify Does

Graphify builds a persistent NetworkX knowledge graph from a repository or other corpus. It combines deterministic code and structured-file extraction with optional model-assisted extraction for documents and media. It can cluster the graph into communities, identify highly connected “god nodes,” generate reports and visualizations, traverse paths, query relevant subgraphs, merge project graphs, and expose the graph through an optional MCP server.

Graphify is broader than a documentation index and overlaps CodeGraph on code extraction. Use it when cross-artifact structure, repository communities, architecture-oriented orientation, or non-code evidence materially improves the search. Use CodeGraph when the primary need is precise code symbol and call/dependency traversal. Use both when a question requires Graphify’s broad system map and CodeGraph’s code-focused relationships.

Graphify outputs are discovery evidence:

- `EXTRACTED` relationships come from an extractor but still require source verification for exact claims.
- `INFERRED` relationships are derived during resolution or semantic processing and are leads, not proof.
- `AMBIGUOUS` relationships are explicitly unresolved.
- communities, labels, hubs, surprising connections, paths, generated reports, and suggested questions organize inspection; they do not establish architectural intent, ownership, runtime causality, or completeness.

Read the original artifact and current owning source before concluding.

## Interface Policy

Use the CLI by default. It provides graph lifecycle, local query, analysis, report, export, and maintenance commands without adding MCP tools to the agent context.

Use MCP only when:

1. the needed CLI operation is unavailable or materially weaker;
2. a working Graphify MCP server is already exposed in the current session; and
3. the server is bound to the intended `graph.json`.

Do not install Graphify or an optional extra, register an assistant skill, add hooks, configure MCP, create or refresh a graph, select a semantic provider, edit ignores, expose an HTTP server, or delete state without explicit user authorization. Missing setup is a handoff, not authorization.

Ordinary CLI queries can update local query stamps and can append to a local query log when that log was explicitly enabled. This is ordinary local Graphify state and is not a separate approval gate. It does not leave the machine.

## Project and Path Rules

Operate on the current repository by default.

- Use `.` as the extraction or update target for the current repository.
- Supply another path only when the task explicitly targets it.
- Resolve the project root before inspecting `.gitignore`, `.graphifyignore`, `GRAPHIFY_OUT`, or graph state.
- Resolve the effective output directory before every lifecycle operation. Do not assume that `graphify-out/` is active when `GRAPHIFY_OUT` is set.
- Use an explicit `--graph <path>` for a nondefault graph or when several graphs are present.

Bracketed values in this reference are placeholders. Replace them with real values; do not type the brackets literally.

## CLI Availability and Package Ownership

Check the installed executable:

```text
graphify --version
```

`graphify -v` and `graphify version` also print the version.

The official Python distribution is `graphifyy` with two trailing `y` characters. The executable remains `graphify`. Other similarly named PyPI packages are not the official project.

Graphify requires Python 3.10 or newer. Check installation prerequisites only when installation is authorized:

```text
python3 --version
uv --version
```

Official isolated installation:

```text
uv tool install graphifyy
```

Official alternative:

```text
pipx install graphifyy
```

Prefer `uv tool install` or `pipx`. A generic `pip install` can put the package in a Python environment that does not match the `graphify` launcher.

If `uv` installed the tool but the command is not on `PATH`, the documented repair is:

```text
uv tool update-shell
```

That edits shell configuration and requires authorization. Open a new shell and verify `graphify --version`.

For one-off execution, the package and command names must both be explicit:

```text
uvx --from graphifyy graphify --version
```

Do not use `uvx graphify`; it resolves the wrong package name.

Upgrade an authorized uv tool installation with:

```text
uv tool upgrade graphifyy
```

Remove the uv-managed Python package with:

```text
uv tool uninstall graphifyy
```

Package upgrade or removal does not refresh or delete project graphs.

`graphify install` is not package installation. It writes Graphify’s upstream skill, instructions, and sometimes hooks/plugins into an assistant environment. This codebase-search skill already owns routing, so do not run `graphify install` unless the user explicitly asks for that separate integration.

## Optional Package Extras

Install an extra only when the selected corpus or interface requires it and the user authorizes the package change.

| Extra | Adds |
| --- | --- |
| `mcp` | `graphify-mcp`, MCP SDK, and HTTP serving dependency |
| `pdf` | PDF extraction dependencies |
| `office` | DOCX and XLSX extraction |
| `google` | Google Sheets rendering used with Google Workspace export |
| `video` | local faster-whisper transcription and video download support |
| `watch` | watchdog-based filesystem monitoring |
| `leiden` | `graspologic` Leiden clustering where supported; Louvain remains the fallback |
| `postgres` | live PostgreSQL schema introspection |
| `neo4j` | Neo4j export/push support |
| `falkordb` | FalkorDB export/push support |
| `sql` | Tree-sitter SQL extraction |
| `terraform` | HCL/Terraform extraction |
| `pascal` | Tree-sitter Pascal extraction; regex fallback exists without it |
| `dm` | DreamMaker grammar; can require a compiler outside Windows |
| `gemini`, `kimi`, `openai`, `anthropic`, `ollama`, `bedrock` | headless semantic-provider clients |
| `chinese` | improved Chinese query tokenization |

Authorized extra installation template:

```text
uv tool install "graphifyy[<COMMA_SEPARATED_EXTRAS>]"
```

Replace the placeholder with only the required extras. If Graphify already has an isolated uv tool environment, use the uv-supported upgrade/reinstall path for that same owner; do not create a second conflicting installation.

## Telemetry, Local Logs, and Network Behavior

The audited Graphify implementation has no telemetry, usage tracking, analytics event emitter, or telemetry off-switch.

Local query logging is separate from telemetry and is off by default in current source:

| Variable | Behavior |
| --- | --- |
| `GRAPHIFY_QUERY_LOG_ENABLE=1` | enable JSONL query logging at the default user cache path |
| `GRAPHIFY_QUERY_LOG=<path>` | enable query logging at the specified local path |
| `GRAPHIFY_QUERY_LOG_DISABLE=1` | force local query logging off; wins over enable variables |
| `GRAPHIFY_QUERY_LOG_RESPONSES=1` | include full query responses when logging is enabled |

Current source makes logging opt-in even though one README privacy paragraph still says every query is logged. Source, tests, the environment-variable table, and changelog agree that the current default is off.

Graph queries against an existing local `graph.json` do not call a model. Network or external-process behavior occurs only through a selected feature, including:

- semantic extraction or community labeling through Gemini, Kimi, Anthropic, OpenAI-compatible, DeepSeek, Azure OpenAI, Bedrock, Ollama, or Claude CLI;
- remote URL, arXiv, webpage, image, Twitter/X, YouTube, or media ingestion;
- Google Workspace export through `gws`;
- GitHub PR queries through `gh`;
- live PostgreSQL introspection;
- Neo4j or FalkorDB push;
- HTTP MCP serving.

Use explicit backends and explicit targets for any authorized external operation. Do not rely on provider auto-detection when data destination matters.

## Model-Assisted Stages and Embeddings

Graphify does not use embeddings or a vector store. Semantic extraction asks a model to emit explicit nodes, edges, hyperedges, confidence labels, and source links. Community detection then uses graph topology. Later `query`, `explain`, `path`, `affected`, and hub operations read the saved graph locally and do not call a model.

Provider selection is stage-specific:

| Stage | Provider behavior |
| --- | --- |
| code and structured-file extraction | no provider; deterministic local extraction |
| document, PDF, and image extraction | one explicit extraction provider and model for that run |
| `--dedup-llm` | optional; reuses the extraction provider |
| raster-image understanding | uses the extraction provider; the provider must declare vision support |
| Leiden community detection | no provider; local graph-topology operation |
| community naming | optional, independently selected provider and model |
| PR triage | separate optional provider path; outside ordinary codebase search |

One provider can serve extraction and community naming, which is the template default. The project config keeps the two selections separate so a project can later choose different providers without changing the workflow. There is no embedding provider to configure.

## Generated State and Required Root Ignore

The default output directory is `graphify-out/`. `GRAPHIFY_OUT` can replace it with a relative or absolute path and is read once when the process starts.

For `graphify extract .`, the default output is:

```text
<project-root>/graphify-out/
```

The directory can contain:

- `graph.json`;
- `GRAPH_REPORT.md`;
- `graph.html`;
- `manifest.json`;
- `.graphify_analysis.json`;
- `.graphify_labels.json`;
- `cost.json`;
- `cache/`;
- `converted/`;
- `memory/`;
- `reflections/`;
- `needs_update`;
- generated tree, wiki, call-flow, export, and intermediate artifacts.

Graphify can also create project-root local state outside the output directory:

- `.graphify/`, including optional project-local provider configuration;
- `.graphify_*.json` pipeline intermediates;
- `.graphify_python`;
- hook and rebuild coordination files created by installed upstream workflows.

Upstream documentation supports committing selected Graphify outputs. This workflow deliberately keeps the complete output local. The project-root `.gitignore` must ignore the entire effective output directory before any Graphify command writes it.

Before `extract`, `update`, `watch`, `cluster-only`, `label`, `tree`, an export, or another output-writing command:

1. resolve the effective output directory, including `GRAPHIFY_OUT` and the command target;
2. run `git ls-files -- "<repository-relative-output-directory>"` and require no tracked Graphify output;
3. inspect the project-root `.gitignore`;
4. require the complete output directory to be ignored there;
5. verify with `git check-ignore -v --no-index "<repository-relative-output-directory>/"`.

If the project-root `.gitignore` is absent, report that it must be created. If the rule is missing, report the exact required entry. Do not write graph state until the root ignore is present and verified. Do not use `.git/info/exclude` instead of this project rule.

### Root `.gitignore` template: default output

Location: `<project-root>/.gitignore`

```gitignore
# Local Graphify knowledge graph
/graphify-out/

# Local Graphify runtime and pipeline state
/.graphify/
/.graphify_*.json
/.graphify_python
```

### Root `.gitignore` template: custom relative output

Location: `<project-root>/.gitignore`

```gitignore
# Local Graphify knowledge graph
/<GRAPHIFY_OUT>/

# Local Graphify runtime and pipeline state
/.graphify/
/.graphify_*.json
/.graphify_python
```

Template rules:

- Replace `<GRAPHIFY_OUT>` with the exact repository-relative directory configured in the Graphify process.
- Do not retain angle brackets.
- Retain the Graphify runtime-state rules even when the output directory is custom.
- Do not add unrelated dependency, environment, build, cache, or editor patterns.
- If `GRAPHIFY_OUT` is absolute and outside every Git worktree, omit only the output-directory rule; retain the project-root runtime-state rules, verify the resolved output path, and ensure it does not belong to another repository.

After any authorized write, run:

```text
git status --short --ignored
```

Require all generated Graphify state to remain ignored and untracked.

## Source Ignore Configuration

Graphify itself has no native general project config file. The workflow-owned `.graphify/config.json` retains this skill’s corpus and lifecycle choices; repository source filtering remains native Graphify behavior controlled by `.gitignore`, `.git/info/exclude`, and optional `.graphifyignore` files.

`.graphifyignore` uses gitignore syntax and can exist at the project root or in subdirectories. In normal extraction:

1. Graphify reads the applicable `.gitignore`;
2. it reads `.graphifyignore` afterward;
3. `.graphifyignore` can exclude additional files;
4. later matching rules win, so a `.graphifyignore` negation can restore a file excluded by an earlier ignore rule when Graphify can still traverse its parent directories.

`graphify extract --no-gitignore` disables `.gitignore` and `.git/info/exclude` for that extraction, while `.graphifyignore` still applies. Use it only when ignored generated or transpiled source intentionally belongs in the graph.

Do not create `.graphifyignore` unless the repository needs Graphify-specific source exclusions.

### `.graphifyignore` template

Location: `<project-root>/.graphifyignore`

```gitignore
# Repository-specific Graphify source exclusions
<REPOSITORY_RELATIVE_PATH_OR_GITIGNORE_PATTERN>
```

Template rules:

- Replace the placeholder with an exact repository-specific exclusion.
- Add one rule per justified exclusion.
- Delete the comment if the repository’s convention does not retain comments.
- Do not add generic dependency, virtual-environment, build, or cache patterns merely because they are common.
- A `!` negation must restore every excluded parent needed to reach the intended file. Verify the result against Graphify’s detected corpus; a negated child cannot be found when traversal stops at an excluded parent.

Changes to ignore rules alter corpus coverage. Run an authorized full extraction with the same corpus profile before relying on the graph again.

## Project-Local OpenAI-Compatible Configuration

Graphify has two different provider concepts:

- A built-in provider is a name compiled into Graphify’s `BACKENDS` registry, such as `openai`, `gemini`, or `claude`. It supplies implementation defaults, not a complete project configuration. The built-in `openai` backend still requires `OPENAI_API_KEY` and normally obtains endpoint/model overrides from process variables or CLI flags.
- A custom provider is an OpenAI-compatible entry in `providers.json`. It stores endpoint, model, request settings, and the name of the credential variable. It cannot store or load the credential value itself.

This workflow does not use provider exports, shell startup files, `.env`, auto-detection, or the user-global `~/.graphify/providers.json`. It uses:

| Project file | Owner | Purpose |
| --- | --- | --- |
| `.graphify/config.json` | this codebase-search package | retained corpus, output, extraction, and community-label selections |
| `.graphify/providers.json` | native Graphify provider registry | OpenAI-compatible endpoint, model, request behavior, and credential-key name |
| `.graphify/credentials.json` | this codebase-search package | ignored project-local credential value |

Graphify 0.9.28 can only receive a custom-provider credential through its child-process environment. The package launcher supplies that process-local value immediately before invoking the native CLI. It does not export variables, modify the parent shell, edit shell profiles, use ambient provider credentials, or write user-global provider state.

### Copy the package templates

Resolve `<CODEBASE_SEARCH_SKILL_ROOT>` to the directory containing this skill’s `SKILL.md`. After the root `.gitignore` contains and verifies `/.graphify/`, copy:

```text
mkdir -p .graphify
cp <CODEBASE_SEARCH_SKILL_ROOT>/templates/graphify/config.json.template .graphify/config.json
cp <CODEBASE_SEARCH_SKILL_ROOT>/templates/graphify/providers.json.template .graphify/providers.json
cp <CODEBASE_SEARCH_SKILL_ROOT>/templates/graphify/credentials.json.template .graphify/credentials.json
chmod 600 .graphify/credentials.json
```

Do not overwrite an existing project file. Inspect and reconcile it instead.

Replace `<OPENAI_COMPATIBLE_V1_ENDPOINT>`, `<MODEL_ID>`, and `<API_KEY>` in the copied files. The launcher rejects any unresolved angle-bracket placeholder.

### `config.json` fields

The source template is [Graphify project config template](../templates/graphify/config.json.template).

| Field | Supported values and behavior |
| --- | --- |
| `schema_version` | must be `1` |
| `corpus.path` | project-relative directory; must remain inside the project root |
| `corpus.mode` | `standard` or `deep`; `deep` uses richer semantic extraction |
| `corpus.require_vision` | when `true`, extraction provider must declare `vision: true` |
| `output_parent` | project-relative parent; Graphify writes `<output_parent>/graphify-out/` |
| `extraction.provider` | provider name from `.graphify/providers.json` |
| `extraction.model` | `null` uses the provider’s `default_model`; a string overrides it |
| `extraction.token_budget` | positive semantic chunk token cap; template default `60000` |
| `extraction.max_concurrency` | positive concurrent semantic-request count; template default `4` |
| `extraction.api_timeout_seconds` | positive request timeout; template default `600` |
| `extraction.dedup_llm` | `false` by default; when enabled, reuses the extraction provider |
| `community_labels.enabled` | `true` calls the selected label provider; `false` passes `--no-label` |
| `community_labels.provider` | required when labeling is enabled; independently selected provider from `providers.json` |
| `community_labels.model` | required when labeling is enabled; `null` uses that provider’s default and a string overrides it |
| `community_labels.max_concurrency` | positive concurrent label-request count |
| `community_labels.batch_size` | positive communities-per-request count |

The template deliberately defaults to mixed-source extraction. Do not add `--code-only` merely because a credential or provider is incomplete; fail preflight and report the missing field.

### `providers.json` fields

The source template is [Graphify provider template](../templates/graphify/providers.json.template).

| Field | Required | Behavior |
| --- | --- | --- |
| provider object name | yes | custom backend name; cannot collide with a built-in backend |
| `base_url` | yes | OpenAI-compatible endpoint; HTTPS required except for loopback HTTP |
| `default_model` | yes | model identifier accepted by that endpoint |
| `env_key` | yes | credential key name; template uses `GRAPHIFY_PROJECT_OPENAI_API_KEY` |
| `pricing.input`, `pricing.output` | optional | USD per one million tokens; zero means cost estimation is intentionally unavailable or free |
| `temperature` | optional | number or `null`; use `null` when the model rejects an explicit temperature |
| `max_tokens` | optional | positive response-token cap used by Graphify |
| `vision` | optional | Boolean capability declaration used for raster-image extraction |
| `reasoning_effort` | optional | provider-supported reasoning setting forwarded by the OpenAI-compatible path |
| `extra_body` | optional | provider-specific JSON request body; include only when the endpoint requires it |

The file never contains the credential value. `env_key` links the provider to one property in `.graphify/credentials.json`.

### `credentials.json` fields and handling

The source template is [Graphify credentials template](../templates/graphify/credentials.json.template).

Each key must match an `env_key` used by the selected extraction or label provider. Each value is the actual credential. Requirements:

- the file must be inside the project root at `.graphify/credentials.json`;
- it must not be a symlink;
- on POSIX its permissions must be `0600` or stricter;
- it must remain ignored and untracked;
- never print its contents or place the key value in a command;
- never copy it into the skill package, logs, reports, or evaluator data.

### Project launcher

The launcher is [Graphify project launcher](../scripts/graphify-project.py). Use `python3` and resolve the script from the loaded skill package:

```text
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> preflight
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> initialize
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> refresh
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> cluster
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> label
```

Launcher behavior:

1. validates every project file, placeholder, path, endpoint, model, stage setting, vision requirement, credential entry, and credential-file permission;
2. finds the installed `graphify` executable;
3. removes known ambient provider keys, every project credential key, and Graphify lifecycle/model overrides from the child environment;
4. enables the reviewed project-local provider only inside a child that will call that provider;
5. injects only the selected provider credential into that child and injects no credential for `cluster-only --no-label`;
6. passes explicit provider, model, corpus, output, and tuning arguments to Graphify;
7. runs `cluster-only` after initialize or refresh so reports and labels match the graph.

`initialize` refuses to overwrite an existing graph. `refresh` refuses when no graph exists. `cluster` and `label` require an existing graph. A preflight failure blocks every semantic write; correct the named project field without exposing the credential.

## Initialization State Machine

Graphify has no `init` command. The first successful `graphify extract` creates project state.

Resolve:

```text
<effective-output>/graph.json
```

Follow this state machine:

| Observed state | Meaning | Action |
| --- | --- | --- |
| CLI missing | Graphify cannot run | report `graphifyy` installation requirement; do not install |
| root ignore missing | generated output is not protected | report exact `.gitignore` template; do not extract |
| project templates missing | provider behavior cannot be reproduced without ambient state | copy and configure the package templates only when project configuration writes are authorized |
| launcher preflight fails | provider, model, credential, path, permissions, or stage configuration is invalid | report the exact invalid field without printing the credential; do not run Graphify |
| `graph.json` missing | project has no Graphify graph | run the authorized launcher `initialize` action |
| `graph.json` corrupt or unreadable | project state is damaged or incompatible | preserve it; choose an evidence-based force rebuild or direct fallbacks |
| graph loads but has zero useful nodes | extraction did not produce usable coverage | inspect source classification, ignores, optional dependencies, and provider errors |
| `manifest.json` missing | incremental file baseline and freshness proof are absent | do not query the graph; run launcher `refresh`, which may rescan the corpus, when authorized |
| `needs_update` exists | watched/hooked semantic inputs changed | semantic document/media nodes are stale until full mixed-source extraction |
| graph exists with a healthy manifest and no semantic-stale flag | project is initialized, but freshness is not proven | run launcher `refresh` before any query |

### Initialize the retained project profile

For this codebase-search workflow, Graphify’s distinct responsibility is mixed-source structure across code and project knowledge. Initialization therefore uses the configured OpenAI-compatible provider and includes supported documentation, PDFs, and images:

```text
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> preflight
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> initialize
```

The `initialize` action runs native `graphify extract` with explicit provider/model arguments, then `graphify cluster-only` with either the configured label provider/model or `--no-label`.

Use `--code-only` only when the user explicitly changes the intended corpus to code-only. A missing credential, incomplete provider, or failed endpoint is not a reason to discard documentation.

### Extraction command

```text
graphify extract <path> [options]
```

Core options:

| Option | Behavior |
| --- | --- |
| `--backend <name>` | semantic backend; supported source paths include Gemini, Kimi, Claude, OpenAI-compatible, DeepSeek, Azure, Bedrock, Ollama, and Claude CLI |
| `--model <name>` | backend model override |
| `--mode deep` | more aggressive semantic extraction and inferred edges |
| `--force` | full rescan and semantic-cache bypass; can permit a smaller replacement graph |
| `--max-workers <n>` | AST subprocess count; default CPU count |
| `--token-budget <n>` | semantic chunk token cap; default `60000` |
| `--max-concurrency <n>` | concurrent semantic chunks; default `4` |
| `--api-timeout <seconds>` | per-request timeout; default `600` |
| `--out <dir>`, `--output <dir>` | output parent; writes its effective Graphify output directory |
| `--google-workspace` | export `.gdoc`, `.gsheet`, and `.gslides` shortcuts before extraction |
| `--no-gitignore` | ignore `.gitignore` and `.git/info/exclude`; still honor `.graphifyignore` |
| `--no-cluster` | write raw extraction without clustering/report completion |
| `--code-only` | skip semantic document/media files |
| `--exclude <pattern>` | add a scan-root-relative exclusion; repeatable |
| `--dedup-llm` | use the selected model to decide ambiguous entity deduplication |
| `--allow-partial` | permit output from an incomplete extraction instead of preserving a prior complete graph |
| `--resolution <number>` | clustering resolution |
| `--exclude-hubs <percentile>` | exclude high-degree hubs from clustering |
| `--timing` | print stage timings |
| `--postgres <DSN>` | introspect a live PostgreSQL schema |
| `--cargo` | add Cargo workspace crate dependencies |
| `--global` | merge result into the user-global graph |
| `--as <tag>` | repository tag for `--global` |

Do not use `--force`, `--allow-partial`, `--no-gitignore`, `--dedup-llm`, `--postgres`, `--global`, remote backends, or remote-compatible endpoints without explicit authorization for that exact behavior.

The project launcher constructs the ordinary extraction command from `config.json`. Do not bypass it for mixed-source initialization or refresh; a raw command would lose the retained project profile and credential isolation.

### Initialization verification

After extraction:

1. confirm `<effective-output>/graph.json` exists and is readable JSON;
2. require a nonempty `nodes` collection;
3. record graph edge/link count, source-file classes, confidence mix, and community data;
4. confirm `<effective-output>/manifest.json` exists for normal incremental refresh;
5. inspect extraction warnings, skipped sensitive files, unsupported formats, optional-dependency failures, partial semantic chunks, and provider errors;
6. require no `needs_update` flag for semantic freshness;
7. run `git status --short --ignored` and require the complete output directory to remain ignored.

`GRAPH_REPORT.md` and `graph.html` are expected only when clustering/report and visualization stages ran. Their absence does not corrupt raw `graph.json`, but it means the architecture/report surface is incomplete.

The headless `extract` command in the audited source writes `graph.json`, analysis data, manifest, and markers, then tells the caller to run `cluster-only` to generate or refresh `GRAPH_REPORT.md`, community labels, and `graph.html`. Do not assume the headless CLI is identical to Graphify’s upstream host-agent `/graphify` pipeline.

## Refresh, Rebuild, and Freshness

### Mandatory freshness rule

Graphify has no read-only command that proves the saved mixed-source graph matches the current repository. `manifest.json` supports incremental extraction but is not a standalone freshness verdict. `graphify check-update .` only reads a marker created by watcher or hook flows, so an absent marker cannot establish that those flows observed every relevant change.

Before the first Graphify query in every search workflow, run the retained project launcher’s `preflight` and `refresh` actions. A successful mixed-source initialization performed in the same workflow can replace refresh when no relevant source changed afterward. Repeat the sequence after any code, document, schema, manifest, media, corpus configuration, checkout, merge, rebase, pull, generated-source, or worktree change that can affect the graph.

If refresh or its required provider call is not authorized, fails, leaves required source classes partial, or cannot be verified, Graphify is unavailable for that search. Do not query the old graph even for orientation; use current-source fallbacks.

### Refresh the retained corpus profile

```text
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> preflight
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> refresh
```

The launcher reuses the same provider, model, mode, output, tuning, deduplication, vision, and label settings. An existing manifest enables incremental extraction. This is the ordinary freshness path when project documentation or images are part of the graph.

### Code-only update

```text
graphify update . [--force] [--no-cluster]
```

`update` re-extracts code without an LLM. It is appropriate for a code-only graph or a deliberately code-scoped refresh. It does not semantically refresh changed documents, PDFs, images, or media.

Do not use `update` as the normal refresh command for this mixed-source workflow.

Use `--force` only after a refactor or deletion when shrink protection is known to retain obsolete nodes, or when a verified corruption/migration requires replacement. Verify the rebuilt graph instead of assuming a forced command succeeded correctly.

### Semantic staleness check

```text
graphify check-update .
```

This reads the `needs_update` flag maintained by watch/hook flows. A reported flag proves that watched semantic inputs are stale. A clear or absent flag does not prove freshness: the watcher or hook may not have been active for the entire change interval, and Git hooks do not cover uncommitted edits. The command always returns successfully and does not clear the flag, so neither its exit status nor silent output can pass the freshness gate.

### Recluster and regenerate report

```text
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> cluster
```

Core options:

| Option | Behavior |
| --- | --- |
| `--graph <path>` | explicit graph input |
| `--no-viz` | skip `graph.html` |
| `--no-label` | retain placeholder community labels |
| `--backend <name>` | backend for model-assisted community naming |
| `--model <name>` | label model override |
| `--max-concurrency <n>` | concurrent label requests; default `4` |
| `--batch-size <n>` | communities per label request; default `100` |
| `--resolution <number>` | clustering granularity where supported |
| `--exclude-hubs <percentile>` | exclude high-degree hubs from partitioning |

The launcher reads `community_labels.enabled`. When enabled, it passes the configured label provider and model explicitly. When disabled, it passes `--no-label`. Never run plain `graphify cluster-only` because it can auto-detect ambient credentials.

Clustering and labels can change community IDs or names without source behavior changing. Treat them as orientation metadata.

### Relabel communities

```text
python3 <CODEBASE_SEARCH_SKILL_ROOT>/scripts/graphify-project.py --project-root <PROJECT_ROOT> label
```

This calls the configured label provider and rewrites labels/report output. It refuses to run when labeling is disabled. Relabeling is not required for graph querying.

### Watch and Git hooks

```text
graphify watch <path>
graphify hook install
graphify hook status
graphify hook uninstall
```

Watch mode can refresh deterministic code after debounced changes. Semantic file changes produce `needs_update` for a later mixed-source extraction. Git hooks add post-commit/post-checkout behavior and merge-driver configuration. Both are optional mutations and must not be enabled automatically. Neither replaces the mandatory pre-query mixed-source refresh because neither proves it observed every change since the saved graph was created.

## CLI Query Surface

Queries against an existing graph are local and lexical/graph-structural. Semantic richness comes from nodes, labels, and edges created during extraction; the query itself does not call a model.

### Scoped question

```text
graphify query "<question>" [--dfs] [--context <relation>] [--budget <tokens>] [--graph <path>]
```

Behavior:

- breadth-first traversal by default;
- `--dfs` selects depth-first traversal;
- repeat `--context` to constrain relation contexts;
- `--budget` caps rendered context; default `2000`;
- `--graph` selects a nondefault graph.

Start here for architecture, cross-artifact, subsystem, documentation, schema, or repository-concept orientation. Record returned node IDs, labels, source files, relation names, confidence labels, and truncation notices.

### Explain one node

```text
graphify explain "<node-or-id>" [--graph <path>]
```

Returns the resolved node, source, type, community, degree, and connected relationships. Lexical collisions can resolve ambiguously; use an exact returned node ID when possible.

### Shortest path

```text
graphify path "<source-node-or-id>" "<target-node-or-id>" [--graph <path>]
```

Finds one shortest connection in the loaded graph. It does not prove causality, exclusivity, direction by adjacency, or the absence of another path.

### Reverse impact traversal

```text
graphify affected "<node-or-label>" [--relation <relation>] [--depth <n>] [--graph <path>]
```

Default depth is `2`. Repeat `--relation` to constrain reverse traversal. Use this for broad cross-artifact impact candidates, then verify code impact with CodeGraph and current source.

### Architectural hubs

```text
graphify god-nodes [--top <n>] [--graph <path>] [--json]
```

Default `--top` is `10`. High degree identifies connectivity, not business importance or poor design by itself.

### Multigraph diagnostics

```text
graphify diagnose multigraph [--graph <path>] [--json] [--max-examples <n>] [--directed|--undirected] [--extract-path <path>]
```

Reports risk that several relationships between the same endpoints collapse in the default graph representation. Use it when missing parallel/opposite-direction edges can affect the search.

## Query Workflow

1. resolve the graph target, then complete the mandatory launcher preflight and mixed-source refresh before the first query;
2. run `query` with the user’s concepts and known artifact names;
3. inspect returned source types, IDs, confidence tags, communities, and relationship vocabulary;
4. use `explain` for exact nodes;
5. use `affected` for reverse reach, `god-nodes` for hubs, and `path` for one possible connection;
6. query again with canonical terms learned from original artifacts;
7. read every original document, schema, manifest, configuration file, or source file used in the answer;
8. use CodeGraph or exact/type-aware code search for precise code relationships;
9. resolve every truncation, ambiguity, stale semantic source, and excluded source class.

Do not read the full `GRAPH_REPORT.md` as a substitute for scoped querying when the report is large. Use it to learn high-level vocabulary, community labels, hubs, and suggested questions, then inspect original evidence.

## Reports, Visualizations, and Exports

Primary outputs:

| Artifact | Use | Authority boundary |
| --- | --- | --- |
| `graph.json` | persistent graph and query source | generated representation; verify original sources |
| `GRAPH_REPORT.md` | communities, hubs, links, rationale, questions | generated orientation report |
| `graph.html` | interactive force-directed graph | visualization of generated graph |
| `.graphify_analysis.json` | analysis data used by reports/exports | derived analysis |
| `.graphify_labels.json` | community label persistence | labels can be model-derived or regenerated |
| `manifest.json` | incremental source baseline | freshness aid, not proof every source was extracted correctly |

Additional commands:

```text
graphify tree [--graph <path>] [--output <html>] [--root <path>] [--max-children <n>] [--top-k-edges <n>] [--label <name>]
graphify export <format> [format options]
graphify export callflow-html [graph-or-output-dir] [--graph <path>] [--labels <path>] [--output <html>]
graphify benchmark [graph.json]
```

`tree` and export commands write generated artifacts. `benchmark` compares graph-query context with naive corpus size; it does not validate answer quality.

Supported export families in the audited source include HTML/visual output, call-flow HTML, Obsidian Markdown, Canvas, GraphML, SVG, Cypher/graph databases, and wiki-oriented output. Inspect `graphify export --help` and the selected format’s help before use because each format has its own destination and optional dependency.

## Other CLI Command Families

These commands are outside ordinary local repository search but are part of Graphify’s surface.

### Merge and cross-repository graphs

```text
graphify merge-graphs <graph1.json> <graph2.json> [...] [--out <merged.json>]
graphify merge-driver <base> <current> <other>
graphify global add <graph.json> [--as <tag>]
graphify global remove <tag>
graphify global list
graphify global path
```

The default merged output is `graphify-out/merged-graph.json`. The global graph is stored under the user’s `~/.graphify/` state. Merging combines discovery graphs and can carry stale or colliding IDs; it does not establish cross-repository runtime integration.

### Remote corpus acquisition

```text
graphify clone <github-url> [--branch <branch>] [--out <directory>]
graphify add <url> [--author <name>] [--contributor <name>] [--dir <path>]
```

`clone` writes a local checkout, defaulting under `~/.graphify/repos/`. `add` downloads remote content into the corpus and updates the graph. Both are external mutations and require exact target authorization.

### Query feedback and reflection

```text
graphify save-result --question <text> [--answer <text>|--answer-file <path>] [--type <type>] [--nodes <labels...>] [--outcome <useful|dead_end|corrected>] [--correction <text>] [--memory-dir <dir>]
graphify reflect [--memory-dir <dir>] [--out <file>] [--graph <path>] [--analysis <path>] [--labels <path>] [--half-life-days <n>] [--min-corroboration <n>] [--if-stale]
```

These write local experiential memory and reflections. They are optional and are not part of proof or graph freshness.

### Pull-request analysis

```text
graphify prs [<number>] [--triage] [--conflicts] [--worktrees] [--wrong-base] [--base <branch>] [--repo <owner/repo>] [--graph <path>]
```

This invokes `gh` and can call a configured model for triage. Use only when the user asks for current PR information and external reads are in scope. Graph overlap is not a review or merge verdict.

### Assistant integration

```text
graphify install [--platform <platform>] [--project] [--strict]
graphify uninstall [--project] [--platform <platform>] [--purge]
graphify <platform> install [--project]
graphify <platform> uninstall [--project]
```

Supported platform families include Claude/Windows, CodeBuddy, Codex, OpenCode, Kilo, Aider, Amp, generic Agent Skills, GitHub Copilot, VS Code, OpenClaw, Factory Droid, Trae, Gemini, Cursor, Antigravity, Hermes, Kiro, Pi, Devin, and related aliases present in the installed version.

These commands can write skills, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, hooks, plugins, rules, and platform configuration. `graphify uninstall --purge` also deletes the effective project output. Do not use this family as part of normal search.

### Internal pipeline commands

The CLI also exposes helper paths such as `cache-check`, `merge-chunks`, `merge-semantic`, `hook-check`, and `hook-guard`. They exist for Graphify’s installed skill and pipeline implementation. Do not call them as public search commands unless an upstream troubleshooting procedure names the exact command and inputs.

## Result and Error Interpretation

| Result or warning | Meaning | Response |
| --- | --- | --- |
| `No matching nodes found.` | successful query miss | vary canonical terms, source names, paths, and direct artifact search |
| `No node matching '<label>' found.` | label/ID did not resolve | use exact returned IDs, alternate labels, or broader query |
| community not found | stored ID no longer exists or was regenerated | verify against the current graph |
| endpoint ambiguity warning | lexical candidates are close | inspect every plausible candidate or use exact IDs |
| same resolved node for both path endpoints | endpoint terms are not specific enough | use exact IDs or qualified labels |
| `No path found` | no path in the loaded generated graph | not proof that artifacts are unrelated |
| token/truncation notice | output budget cut nodes or relationships | narrow or raise the budget and cover the omitted area |
| `graphify-project: ...` with exit `2` | project config, provider, credential, permissions, path, executable, or lifecycle precondition failed | correct the named field without printing the credential; do not bypass the launcher |
| graph file not found | wrong path or uninitialized project | resolve existing state or follow the authorized initialization branch |
| graph load/corruption error | unreadable or incompatible output | stop using it; preserve state and choose an authorized repair |
| graph-size rejection | graph exceeds the configured load cap | report the limit; do not raise it without evidence and authorization |
| extraction incomplete or semantic chunks failed | graph has partial source coverage | inspect failed source classes directly; rebuild only under the retained profile |
| shrink-protection refusal | replacement has fewer nodes than the current graph | determine whether deletions/refactors explain it before considering `--force` |
| skipped sensitive source | security classifier excluded a file | inspect the current source directly when it matters; do not bypass automatically |
| optional dependency missing | selected format/backend cannot run | report the exact extra; do not install |
| PR or `gh` error | external repository evidence unavailable | do not infer PR absence or impact |

An empty graph result is a scoped graph miss, not repository absence.

## Coverage and Authority Limits

Graphify can classify and extract many code languages; Markdown/MDX/Quarto/text/rST/HTML/YAML; PDFs; images; Office files; Google Workspace shortcuts; video/audio; MCP configuration; package manifests; SCIP; PostgreSQL metadata; Cargo workspace metadata; and remote content. Classification does not prove equal extraction quality or actual inclusion in the current graph.

Coverage depends on:

- `.gitignore`, `.git/info/exclude`, `.graphifyignore`, and `--no-gitignore`;
- supported extensions and optional grammars;
- optional document/media/provider dependencies;
- sensitive-file filtering;
- semantic-provider success and model output;
- incremental manifest and cache state;
- graph-size and visualization limits;
- ambiguous symbol resolution and duplicate reconciliation;
- the default undirected graph representation and preserved `_src`/`_tgt` direction metadata;
- stale semantic inputs after code-only watch/update.

Graphify also prunes built-in dependency, virtual-environment, version-control, build, cache, coverage, snapshot, framework-cache, worktree, and Graphify-output directories, plus common lockfiles. These built-ins explain why the templates do not add generic `node_modules`, venv, build, or cache rules. `--no-gitignore` does not disable built-in noise pruning or sensitive-file filtering.

Sensitive-file guards skip private-key and certificate material, common credential files, `.env`, cloud/SSH credential directories, and filenames strongly associated with secrets or tokens. A skipped source can therefore matter to configuration discovery even when bypassing that guard would be inappropriate. Record the gap and inspect only when the active task authorizes access to that sensitive source.

`.graphifyinclude` is obsolete and ignored. Use supported `.graphifyignore` negation within that file’s own rule scope, or `--no-gitignore` for an explicitly approved corpus boundary.

Resource guards include a default `512 MiB` persisted-graph load cap, `50 MiB` raw PDF and Office archive limits, and decompression/ratio controls for Office files. Hitting a guard is a coverage failure, not permission to bypass it.

Communities use Leiden when its optional dependency is available and fall back to seeded Louvain. Directed graphs can be converted for clustering. Community membership remains generated orientation.

For a mixed code/document/schema claim:

1. inspect the current original artifacts;
2. identify confidence and origin for each graph relationship;
3. verify exact code behavior with CodeGraph or precise source tools;
4. record missing, stale, ignored, unsupported, or failed source classes;
5. report conflicts between intended behavior in docs/specs and implemented behavior in code.

## MCP Fallback

Use this section only when the CLI cannot supply the required structured operation and a Graphify MCP server is already available or the user separately authorizes setup.

The MCP extra is installed through:

```text
uv tool install "graphifyy[mcp]"
```

The stdio command contract is:

```text
command: graphify-mcp
args: --graph, <ABSOLUTE_PATH_TO_GRAPH_JSON>
```

Equivalent module form:

```text
python3 -m graphify.serve --graph <ABSOLUTE_PATH_TO_GRAPH_JSON>
```

Do not run a stdio server interactively. The client owns its process.

### MCP configuration template

```json
{
  "mcpServers": {
    "graphify": {
      "type": "stdio",
      "command": "graphify-mcp",
      "args": [
        "--graph",
        "<ABSOLUTE_PATH_TO_GRAPH_JSON>"
      ]
    }
  }
}
```

Template rules:

- Replace the placeholder with the canonical absolute path to the verified graph.
- Merge the server entry into existing configuration; do not overwrite unrelated servers.
- Use the target harness’s supported MCP config owner and syntax.
- Restart the client after a configuration change.
- MCP configuration does not create or refresh a graph.

The MCP server exposes:

| Tool | Use |
| --- | --- |
| `query_graph` | token-budgeted BFS/DFS subgraph for a question |
| `get_node` | resolve one node by label or ID |
| `get_neighbors` | incoming/outgoing relationships with optional relation filter |
| `get_community` | community membership |
| `god_nodes` | high-degree hubs |
| `graph_stats` | node, edge, community, and confidence counts |
| `shortest_path` | one path between two nodes |
| `list_prs` | current pull-request summary through `gh` |
| `get_pr_impact` | one PR’s graph overlap |
| `triage_prs` | model-backed PR ranking |

Every tool can accept `project_path` in multi-project mode. Inspect the live schema for exact parameter names, defaults, and limits.

HTTP MCP is not a fallback for ordinary local search. It can bind a network socket. The server defaults to `127.0.0.1:8080`, mount path `/mcp`, stdio transport unless selected, and no API key. Wildcard binding without a key warns but does not fail closed. Do not expose it without explicit authorization and authentication.

## Branch Completion

The Graphify branch is complete only when:

1. every semantic lifecycle action used the validated project profile and explicit provider/model selections;
2. the resolved graph belongs to the intended repository and retained mixed-source corpus profile;
3. the mandatory mixed-source refresh passed after the latest relevant repository change and before the first query;
4. every returned node that can satisfy the search target is dispositioned;
5. every relevant ambiguity, truncation, community, hub, path, neighbor, and confidence tag is resolved;
6. every original artifact used in the answer has been read;
7. exact code relationships have been verified through CodeGraph or precise current-source search;
8. ignored, unsupported, failed, stale, and external source classes that affect the claim are recorded;
9. the final closure query adds no new relevant candidate.

Graphify’s generated graph, reports, visualizations, caches, query stamps, and optional local query log are local tool state. They remain generated evidence, not proof and not separate approval gates after their owning lifecycle or logging feature has been authorized.
