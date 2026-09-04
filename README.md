# Agent Workbench

Reusable skills, specialist agents, and harness instructions for AI-assisted coding and knowledge work.

## Status

This repository contains curated `agents/`, `skills/`, `harness-instructions/`, and `evals/` assets. The current asset set covers consequence-calibrated coding orchestration, ordered solution-sufficiency gating, project continuity, independently warranted PRD/spec/plan/review gates, implementation-pattern capture, ADRs, documentation/README work, visual engineering artifact companions, graph-backed codebase search, database/API/queue-cache/error/testing design, diagnosis, bounded author-side hygiene, caller-first interface analysis, reusable verification-harness design, historical-rationale evidence discipline, Python and TypeScript engineering, Microsoft 365 query guidance, team memory, and git commit/PR/conflict discipline.

Skills can be installed directly from this repository with the public `skills` CLI (see [Install Skills With The Skills CLI](#install-skills-with-the-skills-cli)). Agents and harness instructions are copied manually into the harness locations that should use them; this repository ships no installer, exporter, or validator of its own.

## What This Is

Agent Workbench is a portable source repository for agent operating assets: skills, specialist agent definitions, and harness instruction files that can be copied into real projects.

The repository focuses on reusable behavior that can be reviewed, adapted, and improved across projects while preserving structure, safety, and quality gates.

## Core Ideas

- **Behavior over prose**: a useful skill changes what an agent does under pressure.
- **Portable first**: core assets should avoid harness-specific assumptions unless the file is explicitly a harness adapter.
- **Consequence-calibrated assurance**: Direct, Standard, and High Assurance lanes scale safeguards to reversibility, blast radius, data, permissions, external effects, public contracts, and uncertainty.
- **Independent workflow warrants**: diagnosis, specifications, plans, delegation, review, re-review, and final gates run only when each resolves a named uncertainty or acceptance gap.
- **Improvement before proliferation**: adapt useful mechanisms into the existing owner when they fit; create a new skill only when repeated evidence shows that current composition cannot own the behavior coherently.
- **Bounded proof, complete outcomes**: satisfy the full accepted goal while using the cheapest decisive evidence and stopping checks, agents, and review cycles when they can no longer change the result.
- **Explicit boundaries**: PRDs, engineering specs, implementation plans, architecture design, ADRs, coding, and review are different jobs.
- **No hidden attribution**: generated-by footers, assistant signatures, promotional badges, and AI co-author trailers do not belong in project artifacts.
- **Reviewable changes**: commits and pull requests should be scoped, understandable, reversible, and backed by evidence.

## Assurance Model

The coding workflow separates consequence classification from process selection. A lane calibrates assurance depth; it does not activate a fixed pipeline.

| Lane | Qualification | Execution shape |
| --- | --- | --- |
| Direct | Target behavior and, for failures, cause are known; scope is bounded and reversible; no high-assurance trigger applies; deterministic checks can prove acceptance | Inspect the bounded target, change it, verify it, and report |
| Standard | Ordinary meaningful work where complete Direct proof is absent and no high-assurance trigger applies | Use only the specification, planning, delegation, review, and final-gate steps that have an independent warrant |
| High Assurance | Security, permissions, sensitive or persistent data, migrations, destructive work, public compatibility, release authority, or another source-backed severe consequence is present | Apply every relevant safeguard at sufficient depth without forcing unrelated artifacts or review lanes |

Specifications preserve durable behavior and contracts when needed. Plans preserve real sequencing, dependency, shared-state, rollout, rollback, or multi-executor decisions. Neither is required merely because code changes, multiple files are involved, or implementation is delegated.

Approved plans execute through a coordinator-held cursor: the coordinator authorizes exact unit batches, treats the rest of the plan as context rather than blanket implementation authority, advances only units whose required evidence passed, and stops at declared review checkpoints. The originally accepted outcome stays controlling until current evidence proves it; a downstream artifact, passing check, or owner-local completion claim cannot silently redefine completion. Document-only deliverables cap independent review at standard depth with a single final review and no validator chains.

When Standard work warrants independent review, the normal cadence is one review after the complete deliverable. Review findings are returned and corrected as a batch. A further review requires an explicit trigger, a material acceptance-boundary change, uncertain proof, or a reviewer-stated need; mechanically decidable corrections may close through reviewer-authored contingent acceptance. Completed specs, plans, and reports remain valid historical artifacts even when later judged unnecessary and are not deleted without authority.

## Integrated Engineering Practices

Several practices are deliberately integrated into existing owners instead of exposed as standalone skills:

- The portable harness instructions, all four harness adapters, and the Claude, Codex, OpenCode, and Oh My Pi coder adapters run an ordered solution sufficiency gate before constructing a new custom implementation of a capability: does it need to exist at all, does the project already provide it, does the language, standard library, runtime, framework, platform, or database provide it, does an already-installed dependency provide it — stopping at the first level that fully satisfies the requirement, including its validation, error-handling, security, compatibility, accessibility, and verification floors. When a lower level covers the core capability and only a bounded residual gap remains, only that gap is built. Explicitly accepted solution shapes are built without re-arguing, contrary sufficiency evidence returns to the owning artifact as a changed premise, and local consistency with existing custom components is not by itself a reason to build custom. The implementation reviewer's maintainability lane reports new custom implementations that a named existing facility demonstrably satisfies.
- The Claude, Codex, OpenCode, and Oh My Pi coder adapters run one bounded final-delta hygiene pass before diagnostics and verification. The pass removes agent-introduced residue without turning cleanup into an independent review loop or widening scope into pre-existing code.
- `structured-problem-resolution` identifies the one or two facts that carry a correction's safety when such facts exist, then uses the lowest decisive proof level: current source, bounded bad-case unreachability, execution at the nearest real seam, or live reproduction only when lower levels cannot settle the question.
- `architecture-design` uses disposable caller-first usage sketches to expose placeholders, sequencing burden, invalid combinations, mechanism leakage, and error-handling cost before an interface is accepted. Repeated same-shape caller friction can reopen the design; one subjective awkward call cannot.
- `testing-strategy` owns the portable lifecycle for reusable project verification harnesses: feature mapping, Launch, Doctor, Drive, Evidence, Cleanup, maintenance, and retirement. Exact commands, selectors, credentials, fixtures, and mutation mechanics remain project-local.
- `codebase-search` classifies historical-rationale findings as direct evidence, inference, hypothesis, contradiction, null source, or gap while keeping current live source authoritative for current behavior.

These changes use frozen, bounded RED/GREEN pressure cases: first reproduce a specific behavioral gap, make one focused owner correction, rerun the unchanged case, and stop when the acceptance criteria pass. The evaluation contract reserves enough cost to finish and verify the accepted work; it does not justify shortcutting the goal, spawning agents by habit, or repeating broad tests and reviews after the relevant question is settled.

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
  agents/
  skills/
skills/
```

This repository currently has no public tracked `docs/` tree. Local ignored `docs/` material may exist for references, skill analysis, or project progress notes. Local `.agents/`, `.claude/`, `.codex/`, `.opencode/`, and `.omp/` material may exist for disposable outputs, project-local experiments, or deployed harness copies, but the reusable source assets live under tracked top-level directories. Treat untracked working files as local experiments until they are intentionally committed.

## Repository Areas

### Skills

`skills/` holds reusable procedures for recurring agent work. Skills should teach durable behavior, include clear use and non-use boundaries, and avoid project-specific assumptions unless the skill is intentionally scoped.

`skills/<name>/` is deployable runtime skill source: each package contains its `SKILL.md` plus any operational references, scripts, templates, or assets the skill declares. Repository-only evaluator assets live under `evals/skills/<name>/` for skills and `evals/agents/<name>/` for specialist agents; those files hold pressure scenarios, criteria, and evaluation evidence or reports, not runtime skill or agent context.

Current skill groups include:

- Orchestration and workflow: `coding-project-orchestrator`, `project-rules`, `project-continuity`, `continuation-prompt`, and `implementation-review-workflow`.
- Product and engineering artifacts: `create-project-prd`, `create-spec-readiness-map`, `create-engineering-spec`, `create-implementation-plan`, `create-project-adr`, `create-implementation-pattern`, `create-documentation`, `create-readme`, `create-skills`, and `visual-artifact`.
- Design, diagnosis, and quality: `structured-problem-resolution`, `codebase-search`, `architecture-design`, `api-design`, `database-design`, `queue-and-cache-design`, `testing-strategy`, and `error-handling-design`.
- Engineering mechanics and team memory: `python-engineering`, `typescript-engineering`, and `hindsight-memory`.
- External integrations: `microsoft365`.
- Git workflow: `git-commit`, `git-branch`, `git-tag`, `git-pull-request`, `git-resolve-conflicts`, `github-actions`, and `github-release`.

`codebase-search` routes repository discovery through two optional external CLIs installed separately: CodeGraph for code relationships and impact, and Graphify for cross-artifact and architecture structure. When those tools are unavailable, the skill falls back to direct exact, structural, and type-aware search, so it remains usable without them.

`visual-artifact` creates source-traced HTML projections for existing PRDs, spec-readiness maps, engineering specs, implementation plans, review packets, implementation results, or complex technical artifacts. It uses Mermaid for diagrams by default, keeps evidence and source ownership visible, opens source/evidence links in new tabs, keeps in-page navigation local to the artifact, and writes disposable project-local outputs under `.agents/visual-artifacts/` unless another output path is explicitly chosen.

### Agents

`agents/` holds harness-specific definitions for specialist roles such as `coder`, `implementation-reviewer`, and `research`.

Each harness may need a different file format, but the role intent should stay aligned across Codex, Claude, OpenCode, and Oh My Pi.

Project-owned agent adapters do not pin models or effort levels. The invoking harness selects them or inherits them from its active runtime context.

The committed agent source formats are:

| Harness | Source files | Format | User/global target used in this setup |
| --- | --- | --- | --- |
| Claude | `agents/claude/*.md` | Markdown agent files with YAML front matter | `~/.claude/agents/` |
| Codex | `agents/codex/*.toml` | TOML agent definitions | `~/.codex/agents/` |
| OpenCode | tracked `agents/opencode/*.md` | Markdown agent files with OpenCode front matter | `~/.config/opencode/agents/` |
| Oh My Pi | `agents/omp/*.md` | Direct Markdown task-agent files with YAML front matter | `~/.pi/agent/agents/` |

`agents/omp/` stores Oh My Pi task-agent source files. OMP agents are direct Markdown files with YAML front matter and prompt body. The source files use the required `name` and `description` contract. Add other optional OMP fields such as tool allowlists only after verifying the exact field and value shape against current OMP source or runtime behavior. Do not copy Claude, Codex, or OpenCode metadata across without adapting it.

### Harness Instructions

`harness-instructions/` holds durable operating instructions that sit at a project boundary. These files define routing, delegation, safety gates, artifact attribution rules, workflow expectations, and completion discipline.

The harness instruction sources and current user/global targets are:

| Harness | Source file | User/global target |
| --- | --- | --- |
| Portable base | `harness-instructions/AGENTS.md` | Source template only; adapt through a harness-specific file before deployment when the harness has different tool or agent semantics |
| Claude | `harness-instructions/claude/CLAUDE.md` | `~/.claude/CLAUDE.md` |
| Codex | `harness-instructions/codex/AGENTS.md` | `~/.codex/AGENTS.md` |
| OpenCode | `harness-instructions/opencode/AGENTS.md` | `~/.config/opencode/AGENTS.md` |
| Oh My Pi | `harness-instructions/omp/AGENTS.md` | `~/.pi/agent/AGENTS.md` |

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

Skill deployment by copy uses the selected `skills/<name>/` directory only; do not copy `evals/skills/<name>/` into installed skill locations. In this setup, shared agent skills, including repository-owned skills used by Codex, are copied to `~/.agents/skills/`, while Claude Code skills are also copied to `~/.claude/skills/`. Keep `~/.codex/skills/` for Codex-managed `.system` skills; do not deploy repository-owned skills there. Do not rely on symlinked Claude skills unless you have verified that Claude Code loads them in the target environment.

Evaluation may use evaluator assets under `evals/skills/<name>/`, but runtime targets receive only the task prompt and permitted runtime skill context; they do not receive or read evaluator scenarios, criteria, or reports.

The generic `harness-instructions/AGENTS.md` is a portable source file. Use the harness-specific instruction file when deploying to Claude, Codex, OpenCode, or Oh My Pi because each harness has different tool-calling, skill-loading, and task-agent semantics.

Global copy targets for current committed agent and harness sources:

```text
agents/claude/*.md                    -> ~/.claude/agents/
agents/codex/*.toml                   -> ~/.codex/agents/
agents/opencode/*.md                  -> ~/.config/opencode/agents/
agents/omp/*.md                       -> ~/.pi/agent/agents/
harness-instructions/claude/CLAUDE.md -> ~/.claude/CLAUDE.md
harness-instructions/codex/AGENTS.md  -> ~/.codex/AGENTS.md
harness-instructions/opencode/AGENTS.md -> ~/.config/opencode/AGENTS.md
harness-instructions/omp/AGENTS.md    -> ~/.pi/agent/AGENTS.md
```

For Oh My Pi, deploy direct Markdown agent files from `agents/omp/*.md`:

- User/global OMP agents: copy to `~/.pi/agent/agents/`.
- Project-local OMP agents: copy to `<project>/.pi/agents/`.
- User/global OMP instructions: copy `harness-instructions/omp/AGENTS.md` to `~/.pi/agent/AGENTS.md`.

OMP discovers direct `.md` files in those directories; nested folders are not part of the native task-agent discovery path. Do not deploy OMP agents into `.claude/agents`, `.codex/agents`, or `.gemini/agents` and expect OMP to load them.

## Acknowledgements

This project draws inspiration from the following public work:

- [cursor/plugins](https://github.com/cursor/plugins), including PStack, `poteto-mode`, and related first- and third-party plugin examples, for mechanisms around author-side hygiene, bounded proof, caller-first design, reusable verification, and historical-evidence discipline. These sources were analyzed as design input; justified mechanisms were adapted to existing owners rather than importing plugins or skills wholesale.
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), for the ordered solution-sufficiency ladder, its never-simplify floors, and the agentic benchmark method that informed this repository's solution sufficiency gate and its RED/GREEN pressure scenarios. The reference was analyzed as design input; justified mechanisms were adapted into existing owners rather than installing the plugin or copying its files.
- [mattpocock/skills](https://github.com/mattpocock/skills), for focused, behavior-oriented skill examples.
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin), for planning, review, and structured execution workflows.
- [github/awesome-copilot](https://github.com/github/awesome-copilot), for a broad catalog of Copilot instructions, agents, prompts, and skill examples.
- [Thariq (@trq212), "A Field Guide to Fable: Finding Your Unknowns"](https://x.com/trq212/article/2073100352921215386), for the known/unknowns framing and HTML artifact patterns that informed the visual artifact workflow.

## License

This repository uses the [MIT License](LICENSE.md).
