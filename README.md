# Agent Workbench

Reusable skills, specialist agents, and harness instructions for AI-assisted coding and knowledge work.

## Status

This repository contains curated `agents/`, `skills/`, and `harness-instructions/` assets from the working source repository. The current asset set covers high-assurance coding orchestration, project continuity, PRD/spec/plan/review gates, implementation-pattern capture, ADRs, documentation/README work, database/API/error/testing design, and git commit/PR discipline.

Scripts are reserved until install, export, or validation workflows are created intentionally. For now, assets are copied manually into the target harness locations.

## What This Is

Agent Workbench is a portable source repository for agent operating assets: skills, specialist agent definitions, and harness instruction files that can be copied into real projects without carrying project-specific history or private working references.

The goal is not to publish a pile of prompts. The goal is to provide reusable behavior that can be reviewed, adapted, and improved across projects while preserving structure, safety, and quality gates.

## Core Ideas

- **Behavior over prose**: a useful skill changes what an agent does under pressure.
- **Portable first**: core assets should avoid harness-specific assumptions unless the file is explicitly a harness adapter.
- **High-assurance workflows**: specs, plans, review gates, validation evidence, commit discipline, and PR discipline exist to prevent fast but sloppy execution.
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
scripts/
  install/
  validate/
```

The public `docs/` tree is intentionally excluded for now. Curated public documentation can be added later when there is material worth maintaining outside the README.

The `scripts/install/` and `scripts/validate/` directories are placeholders for future automation. They do not currently provide an installer or validator.

## Repository Areas

### Skills

`skills/` holds reusable procedures for recurring agent work. Skills should teach durable behavior, include clear use and non-use boundaries, and avoid project-specific assumptions unless the skill is intentionally scoped.

Current skill groups include:

- Workflow and definition: `coding-project-orchestrator`, `project-continuity`, `create-project-prd`, `create-engineering-spec`, `create-implementation-plan`, `create-implementation-pattern`, and `implementation-review-workflow`.
- Design and quality: `architecture-design`, `api-design`, `database-design`, `queue-and-cache-design`, `testing-strategy`, and `error-handling-design`.
- Documentation and support: `create-documentation`, `create-readme`, `create-project-adr`, `structured-problem-resolution`, `codebase-search`, `create-skills`, `git-commit`, `git-pull-request`, and `project-rules`.

### Agents

`agents/` holds harness-specific definitions for specialist roles such as `coder`, `implementation-reviewer`, and `research`.

Each harness may need a different file format, but the role intent should stay aligned across Codex, Claude, and OpenCode.

### Harness Instructions

`harness-instructions/` holds durable operating instructions that sit at a project boundary. These files define routing, delegation, safety gates, artifact attribution rules, workflow expectations, and completion discipline.

### Scripts

`scripts/` is reserved for install, export, or validation helpers once there is a real repeatable workflow to automate.

## How To Use

Copy assets selectively:

1. Copy the relevant `skills/` directories into the target harness skill directory.
2. Copy the matching agent definition from `agents/<harness>/`.
3. Copy the relevant project instruction file from `harness-instructions/`.
4. Keep project-specific rules in the target project unless the rule is broadly reusable.
5. Validate behavior with pressure scenarios before trusting a new or changed skill.

Common local destinations are:

- `~/.agents/skills/` for portable skills.
- `~/.claude/agents/` and `~/.claude/CLAUDE.md` for Claude.
- `~/.codex/agents/` and `~/.codex/AGENTS.md` for Codex.
- `~/.config/opencode/agents/` and `~/.config/opencode/AGENTS.md` for OpenCode.

The generic `harness-instructions/AGENTS.md` is a portable source file. Use the harness-specific instruction file when deploying to Claude, Codex, or OpenCode.

## Packaging Direction

Agent Workbench is the source of truth. Packaging targets should adapt from it rather than control it.

A Codex plugin may make sense later, but it should be an optional distribution adapter. Claude and OpenCode exports should remain first-class targets too.

## License

This repository uses the [MIT License](LICENSE.md).
