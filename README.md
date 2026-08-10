# Agent Workbench

Reusable skills, specialist agents, and harness instructions for AI-assisted coding and knowledge work.

## Status

This repository contains curated `agents/`, `skills/`, `harness-instructions/`, and `evals/` assets. The current asset set covers high-assurance coding orchestration, project continuity, PRD/spec/plan/review gates, implementation-pattern capture, ADRs, documentation/README work, visual engineering artifact companions, graph-backed codebase search, database/API/queue-cache/error/testing design, diagnosis, Python and TypeScript engineering, Microsoft 365 query guidance, team memory, and git commit/PR/conflict discipline.

Skills can be installed directly from this repository with the public `skills` CLI (see [Install Skills With The Skills CLI](#install-skills-with-the-skills-cli)). Agents and harness instructions are copied manually into the harness locations that should use them; this repository ships no installer, exporter, or validator of its own.

## What This Is

Agent Workbench is a portable source repository for agent operating assets: skills, specialist agent definitions, and harness instruction files that can be copied into real projects.

The repository focuses on reusable behavior that can be reviewed, adapted, and improved across projects while preserving structure, safety, and quality gates.

## Core Ideas

- **Behavior over prose**: a useful skill changes what an agent does under pressure.
- **Portable first**: core assets should avoid harness-specific assumptions unless the file is explicitly a harness adapter.
- **High-assurance workflows**: specs, plans, review gates, validation evidence, commit discipline, and PR discipline exist to prevent under-specified execution.
- **Explicit boundaries**: PRDs, engineering specs, implementation plans, architecture design, ADRs, coding, and review are different jobs.
- **No hidden attribution**: generated-by footers, assistant signatures, promotional badges, and AI co-author trailers do not belong in project artifacts.
- **Reviewable changes**: commits and pull requests should be scoped, understandable, reversible, and backed by evidence.

## Repository Layout

The current layout is:

```text
agents/
  claude/
  codex/
  omp/
  opencode/
harness-instructions/
  claude/
  codex/
  omp/
  opencode/
evals/
  skills/
skills/
```

This repository currently has no public tracked `docs/` tree. Local ignored `docs/` material may exist for references, skill analysis, or project progress notes. Local `.agents/`, `.claude/`, `.codex/`, `.opencode/`, and `.omp/` material may exist for disposable outputs, project-local experiments, or deployed harness copies, but the reusable source assets live under tracked top-level directories. Treat untracked working files as local experiments until they are intentionally committed.

## Repository Areas

### Skills

`skills/` holds reusable procedures for recurring agent work. Skills should teach durable behavior, include clear use and non-use boundaries, and avoid project-specific assumptions unless the skill is intentionally scoped.

`skills/<name>/` is deployable runtime skill source: each package contains its `SKILL.md` plus any operational references, scripts, templates, or assets the skill declares. Repository-only evaluator assets for skills live under `evals/skills/<name>/`; those files hold pressure scenarios, criteria, and evaluation evidence or reports, not runtime skill context.

Current skill groups include:

- Orchestration and workflow: `coding-project-orchestrator`, `project-rules`, `project-continuity`, and `implementation-review-workflow`.
- Product and engineering artifacts: `create-project-prd`, `create-spec-readiness-map`, `create-engineering-spec`, `create-implementation-plan`, `create-project-adr`, `create-implementation-pattern`, `create-documentation`, `create-readme`, `create-skills`, and `visual-artifact`.
- Design, diagnosis, and quality: `structured-problem-resolution`, `codebase-search`, `architecture-design`, `api-design`, `database-design`, `queue-and-cache-design`, `testing-strategy`, and `error-handling-design`.
- Engineering mechanics and team memory: `python-engineering`, `typescript-engineering`, and `hindsight-memory`.
- External integrations: `microsoft365`.
- Git workflow: `git-commit`, `git-pull-request`, and `git-resolve-conflicts`.

`codebase-search` routes repository discovery through two optional external CLIs installed separately: CodeGraph for code relationships and impact, and Graphify for cross-artifact and architecture structure. When those tools are unavailable, the skill falls back to direct exact, structural, and type-aware search, so it remains usable without them.

`visual-artifact` creates source-traced HTML projections for existing PRDs, spec-readiness maps, engineering specs, implementation plans, review packets, implementation results, or complex technical artifacts. It uses Mermaid for diagrams by default, keeps evidence and source ownership visible, opens source/evidence links in new tabs, keeps in-page navigation local to the artifact, and writes disposable project-local outputs under `.agents/visual-artifacts/` unless another output path is explicitly chosen.

### Agents

`agents/` holds harness-specific definitions for specialist roles such as `coder`, `implementation-reviewer`, and `research`.

Each harness may need a different file format, but the role intent should stay aligned across Codex, Claude, OpenCode, and Oh My Pi.

The committed agent source formats are:

| Harness | Source files | Format | User/global target used in this setup |
| --- | --- | --- | --- |
| Claude | `agents/claude/*.md` | Markdown agent files with YAML front matter | `~/.claude/agents/` |
| Codex | `agents/codex/*.toml` | TOML agent definitions | `~/.codex/agents/` |
| OpenCode | tracked `agents/opencode/*.md` | Markdown agent files with OpenCode front matter | `~/.config/opencode/agents/` |
| Oh My Pi | `agents/omp/*.md` | Direct Markdown task-agent files with YAML front matter | `~/.omp/agent/agents/` |

`agents/omp/` stores Oh My Pi task-agent source files. OMP agents are direct Markdown files with YAML front matter and prompt body. The source files use the required `name` and `description` contract; `coder` and `implementation-reviewer` also pin their verified OMP `model` and `thinkingLevel` fields. Add other optional OMP fields such as tool allowlists only after verifying the exact field and value shape against current OMP source or runtime behavior. Do not copy Claude, Codex, or OpenCode metadata across without adapting it.

### Harness Instructions

`harness-instructions/` holds durable operating instructions that sit at a project boundary. These files define routing, delegation, safety gates, artifact attribution rules, workflow expectations, and completion discipline.

The harness instruction sources and current user/global targets are:

| Harness | Source file | User/global target |
| --- | --- | --- |
| Portable base | `harness-instructions/AGENTS.md` | Source template only; adapt through a harness-specific file before deployment when the harness has different tool or agent semantics |
| Claude | `harness-instructions/claude/CLAUDE.md` | `~/.claude/CLAUDE.md` |
| Codex | `harness-instructions/codex/AGENTS.md` | `~/.codex/AGENTS.md` |
| OpenCode | `harness-instructions/opencode/AGENTS.md` | `~/.config/opencode/AGENTS.md` |
| Oh My Pi | `harness-instructions/omp/AGENTS.md` | `~/.omp/agent/AGENTS.md` |

Root-level `AGENTS.md` and `CLAUDE.md` files in working projects are ignored here because they are local harness instruction overrides, not reusable source assets for this repository.

## Install Skills With The Skills CLI

Skills in this repository follow the `skills/<name>/SKILL.md` package layout that the open-source [`skills` CLI](https://github.com/vercel-labs/skills) from [skills.sh](https://www.skills.sh/) discovers automatically, so they can be installed straight from GitHub without any registration:

```bash
# Interactive: pick target agents and skills
npx skills add cipradu/Agent-Workbench

# Install specific skills only
npx skills add cipradu/Agent-Workbench --skill codebase-search --skill git-commit

# List available skills without installing
npx skills add cipradu/Agent-Workbench --list
```

The CLI supports 70+ agents (Claude Code, Codex, Cursor, OpenCode, and others), selected interactively or with `-a`/`--agent`. It installs per-project by default and globally with `-g`; installed skills are symlinked by default, with `--copy` available for independent copies. Manage installed skills with `npx skills update` and `npx skills remove`. The CLI collects anonymous usage telemetry by default; set `DISABLE_TELEMETRY=1` to opt out.

Agents and harness instructions are not covered by the skills CLI. Copy those manually as described below.

## Manual Copy

Copy assets selectively into the locations your target harness or project already reads:

1. Copy the relevant `skills/<name>/` directories into the target harness skill directory.
2. Copy the matching specialist agent definitions from `agents/<harness>/`.
3. Copy the relevant project instruction file from `harness-instructions/` or `harness-instructions/<harness>/`.
4. Keep project-specific rules in the target project unless the rule is broadly reusable.
5. Validate behavior with pressure scenarios before trusting a new or changed skill.

Skill deployment by copy uses the selected `skills/<name>/` directory only; do not copy `evals/skills/<name>/` into installed skill locations. In this setup, shared agent skills are copied to `~/.agents/skills/`, Claude Code skills are copied to `~/.claude/skills/`, and Codex-native skills may be copied to `~/.codex/skills/` when the Codex surface should load them directly. Do not rely on symlinked Claude skills unless you have verified that Claude Code loads them in the target environment.

Evaluation may use evaluator assets under `evals/skills/<name>/`, but runtime targets receive only the task prompt and permitted runtime skill context; they do not receive or read evaluator scenarios, criteria, or reports.

The generic `harness-instructions/AGENTS.md` is a portable source file. Use the harness-specific instruction file when deploying to Claude, Codex, OpenCode, or Oh My Pi because each harness has different tool-calling, skill-loading, and task-agent semantics.

Global copy targets for current committed agent and harness sources:

```text
agents/claude/*.md                    -> ~/.claude/agents/
agents/codex/*.toml                   -> ~/.codex/agents/
agents/opencode/*.md                  -> ~/.config/opencode/agents/
agents/omp/*.md                       -> ~/.omp/agent/agents/
harness-instructions/claude/CLAUDE.md -> ~/.claude/CLAUDE.md
harness-instructions/codex/AGENTS.md  -> ~/.codex/AGENTS.md
harness-instructions/opencode/AGENTS.md -> ~/.config/opencode/AGENTS.md
harness-instructions/omp/AGENTS.md    -> ~/.omp/agent/AGENTS.md
```

For Oh My Pi, deploy direct Markdown agent files from `agents/omp/*.md`:

- User/global OMP agents: copy to `~/.omp/agent/agents/`.
- Project-local OMP agents: copy to `<project>/.omp/agents/`.
- User/global OMP instructions: copy `harness-instructions/omp/AGENTS.md` to `~/.omp/agent/AGENTS.md`.

OMP discovers direct `.md` files in those directories; nested folders are not part of the native task-agent discovery path. Do not deploy OMP agents into `.claude/agents`, `.codex/agents`, or `.gemini/agents` and expect OMP to load them.

## Acknowledgements

This project draws inspiration from the following public work:

- [mattpocock/skills](https://github.com/mattpocock/skills), for focused, behavior-oriented skill examples.
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin), for planning, review, and structured execution workflows.
- [github/awesome-copilot](https://github.com/github/awesome-copilot), for a broad catalog of Copilot instructions, agents, prompts, and skill examples.
- [Thariq (@trq212), "A Field Guide to Fable: Finding Your Unknowns"](https://x.com/trq212/article/2073100352921215386), for the known/unknowns framing and HTML artifact patterns that informed the visual artifact workflow.

## License

This repository uses the [MIT License](LICENSE.md).
