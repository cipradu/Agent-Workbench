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
  opencode/
harness-instructions/
  claude/
  codex/
  opencode/
skills/
```

This repository currently has no public tracked `docs/` tree. Local ignored `docs/` material may exist for references, skill analysis, or project progress notes. Local `.agents/` material may exist for disposable visual artifacts or project-local skill experiments, but the reusable source assets live under tracked top-level directories. The README is the front door for the asset set.

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

Each harness may need a different file format, but the role intent should stay aligned across Codex, Claude, and OpenCode.

### Harness Instructions

`harness-instructions/` holds durable operating instructions that sit at a project boundary. These files define routing, delegation, safety gates, artifact attribution rules, workflow expectations, and completion discipline.

## How To Use

Copy assets selectively. This repository does not provide an installer, so use the locations your target harness or project already reads:

1. Copy the relevant `skills/` directories into the target harness skill directory.
2. Copy the matching specialist agent definitions from `agents/<harness>/`.
3. Copy the relevant project instruction file from `harness-instructions/` or `harness-instructions/<harness>/`.
4. Keep project-specific rules in the target project unless the rule is broadly reusable.
5. Validate behavior with pressure scenarios before trusting a new or changed skill.

The generic `harness-instructions/AGENTS.md` is a portable source file. Use the harness-specific instruction file when deploying to Claude, Codex, or OpenCode.

## Acknowledgements

This project draws inspiration from the following public work:

- [mattpocock/skills](https://github.com/mattpocock/skills), for focused, behavior-oriented skill examples.
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin), for planning, review, and structured execution workflows.
- [github/awesome-copilot](https://github.com/github/awesome-copilot), for a broad catalog of Copilot instructions, agents, prompts, and skill examples.

## License

This repository uses the [MIT License](LICENSE.md).
