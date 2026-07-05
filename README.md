# Agent Workbench

Reusable skills, specialist agents, and harness instructions for AI-assisted coding and knowledge work.

## Status

This repository contains curated `agents/`, `skills/`, and `harness-instructions/` assets. The current asset set covers high-assurance coding orchestration, project continuity, PRD/spec/plan/review gates, implementation-pattern capture, ADRs, documentation/README work, visual engineering artifact companions, database/API/error/testing design, diagnosis, and git commit/PR/conflict discipline.

No packaged installer, exporter, or validator is included yet. For now, assets are copied manually into the projects or harness locations that should use them.

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
skills/
```

This repository currently has no public tracked `docs/` tree. Local ignored `docs/` material may exist for references, skill analysis, or project progress notes. Local `.agents/`, `.claude/`, `.codex/`, `.opencode/`, and `.omp/` material may exist for disposable outputs, project-local experiments, or deployed harness copies, but the reusable source assets live under tracked top-level directories. Treat untracked working files as local experiments until they are intentionally committed.

## Repository Areas

### Skills

`skills/` holds reusable procedures for recurring agent work. Skills should teach durable behavior, include clear use and non-use boundaries, and avoid project-specific assumptions unless the skill is intentionally scoped.

Current skill groups include:

- Orchestration and workflow: `coding-project-orchestrator`, `project-rules`, `project-continuity`, and `implementation-review-workflow`.
- Product and engineering artifacts: `create-project-prd`, `create-spec-readiness-map`, `create-engineering-spec`, `create-implementation-plan`, `create-project-adr`, `create-implementation-pattern`, `create-documentation`, `create-readme`, `create-skills`, and `visual-artifact`.
- Design, diagnosis, and quality: `structured-problem-resolution`, `codebase-search`, `architecture-design`, `api-design`, `database-design`, `queue-and-cache-design`, `testing-strategy`, and `error-handling-design`.
- Git workflow: `git-commit`, `git-pull-request`, and `git-resolve-conflicts`.

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

## How To Use

Copy assets selectively. This repository does not provide an installer, so use the locations your target harness or project already reads:

1. Copy the relevant `skills/` directories into the target harness skill directory.
2. Copy the matching specialist agent definitions from `agents/<harness>/`.
3. Copy the relevant project instruction file from `harness-instructions/` or `harness-instructions/<harness>/`.
4. Keep project-specific rules in the target project unless the rule is broadly reusable.
5. Validate behavior with pressure scenarios before trusting a new or changed skill.

Skill deployment is manual. The shared skill source is `skills/`. In this setup, shared agent skills are copied to `~/.agents/skills/`, Claude Code skills are copied to `~/.claude/skills/`, and Codex-native skills may be copied to `~/.codex/skills/` when the Codex surface should load them directly. Do not rely on symlinked Claude skills unless you have verified that Claude Code loads them in the target environment.

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
