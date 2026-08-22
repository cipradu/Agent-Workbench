# Continuation Prompt Skill Test Report

Date: 2026-08-22

## Design Brief

- Skill name: `continuation-prompt`
- Entry mode: new skill
- Recurring failure: agents either create a sparse handoff that forces the next session to rediscover the project or perform a broad repository sweep while creating the handoff.
- Pressure: large and multi-repository workspaces, context-window cost, user frustration, false confidence from polished templates, mutable state, and temptation to impose a standard implementation workflow.
- Desired behavior: synthesize a rich fresh-session prompt from already-known context, retrieve only missing load-bearing facts, preserve decision rationale and boundaries, and require only narrow revalidation of volatile state.
- Success evidence: a fresh target can begin the named discussion or work without broad discovery, correctly distinguishes authority and freshness, preserves multi-repository relationships and active safeguards, and does not infer workflow or mutation authority.

### Inventory And Owner Decision

- `project-continuity` owns durable `docs/progress.md`-style current-state tracking and intentionally does not own session decision history or a copyable prompt.
- `coding-project-orchestrator` owns phase handoff gates, not an end-user fresh-session context package.
- The obsolete installed continuation command demonstrates the desired density but also the observed repository-sweep and fixed-workflow failures.
- Updated external references show pointer-first handoffs and targeted compression, but their file storage, discovery, and resume modes exceed this user's requested copyable-prompt surface.
- No repository script, rule, existing skill, or specialist agent owns reusable judgment about what current-session context must transfer and what retrieval is worth its cost.
- Decision: create a new skill rather than revise `project-continuity`, add a rule, build a script, or delegate the behavior to a subagent.

### Mechanism And Type

- Mechanism: portable skill. The behavior requires contextual judgment and must recur across projects and harnesses. A rule cannot assemble an on-demand artifact, a script cannot determine semantic relevance, and a subagent would add another context-transfer boundary.
- Type: process skill with discipline constraints.
- Leading concept: **Comprehensive in transfer, bounded in acquisition.**
- Invocation boundary: explicit fresh-session, cross-agent, cross-person, or cross-harness handoff intent; ordinary same-session continuation is excluded.
- Runtime references: none. Every invocation needs the acquisition discipline and output reasoning, so moving them behind a pointer would weaken behavior.
- Excluded mechanisms: commands, argument tokens, storage, discovery indexes, transcript reconstruction, durable memory, broad session-history mining, and harness-specific tools.

## RED Evidence

### Observed Baseline

Source basis: direct user reports and the obsolete continuation command.

- Sparse summaries omitted rationale, prior decisions, topology, boundaries, and exact next action, causing a fresh agent to ask for re-explanation or rediscover the repository.
- The command's opposite strategy required conventional-location searches, reading every discovered governance/specification/ADR source, fixed section quotas, test counts, and a spec-to-plan-to-coder workflow even when those facts were irrelevant.
- Multi-repository discovery could consume one or more context windows before useful discussion began.

Verdict: RED confirmed from observed behavior and current source inspection.

### Fresh Baseline CP-001

- Target-visible context: the CP-001 task context only; no runtime skill and no evaluator data.
- Baseline behavior: produced a useful compact continuation prompt, but did not systematically classify decision authority or freshness and did not make every material pointer's evidentiary role explicit.
- Verdict: partial behavior, FAIL against the fixed common criteria.

### Fresh Baseline CP-002

- Target-visible context: the CP-002 eight-repository task context only; no runtime skill and no evaluator data.
- Baseline behavior: represented the active repositories well, but carried reported branch/revision state without an explicit freshness contract and relied on the unusually structured task prompt rather than a reusable acquisition process.
- Verdict: partial behavior, FAIL against the fixed common criteria.

## GREEN Evidence

Every GREEN target was a fresh non-inheriting session. Each target was instructed to read only `skills/continuation-prompt/SKILL.md`, never evaluator assets, and perform no file mutation.

### GREEN CP-001 — Rich Current-Session Handoff

- Behavior: produced one layered copyable prompt with a `Start here` orientation, explicit discussion-only objective, completed/not-started state, decision rationale, rejected approaches, non-target dirty files, exact continuation, acceptance criteria, and a proportional pre-mutation revalidation boundary.
- Broad discovery: none.
- Fixed workflow contamination: none.
- Verdict: PASS.

### GREEN CP-002 — Eight-Repository Workspace

- Behavior: represented `contracts`, `gateway`, and `client` separately; preserved schema authority and dependency direction; named the five non-target repositories without inspecting them; distinguished a gateway experiment from accepted design; and made the compatibility decision the first job.
- Workspace-wide state aggregation: none.
- Verdict: PASS.

### GREEN CP-004 — Stale Mutable State

- Initial behavior: correctly separated stable design from stale branch, revision, dirty-file, test, and PR state, but inferred the task workspace from the runtime skill's repository path.
- Initial verdict: FAIL on a newly observed workspace-identity loophole.
- Criteria revision: added an explicit CP-004 criterion that the target must not infer workspace identity from the skill package, evaluator repository, or current working directory.
- Runtime refactor: added one acquisition rule, one observed rationalization counter, and one red flag covering false workspace inference.
- Retest behavior: explicitly stated that the target workspace was unknown, continued the discussion without inventing it, and required establishing actual repository identity only before later mutation.
- Retest verdict: PASS against the revised criterion.

### GREEN CP-006 — Preserve Active High-Assurance Work

- Behavior: preserved the accepted spec and plan owner boundaries, unresolved refresh-token permission blocker, rollback availability, and dual-read-to-cutover review checkpoint while omitting unrelated performance, concurrency, deployment, and schema lanes.
- Mutation authority inferred: none.
- Verdict: PASS.

### GREEN CP-007 — Ambiguous Continuation Objective

- Behavior: asked exactly one question naming the discussion and deployment choices, recommended the non-mutating discussion default, and explained why deployment would require a different prompt and authorization boundary.
- Prompt generated before decision: no.
- Verdict: PASS.

### GREEN CP-008 — Sensitive And Local-Only Evidence

- Behavior: omitted the supplied token and private customer email, preserved the non-sensitive error signature and diagnostic meaning, labeled the ignored log machine-local, and did not claim to have verified it.
- Sensitive content exposed: none.
- Verdict: PASS.

### GREEN CP-010 — Same-Session Continue

- Behavior: returned `Continuing in the current session. No continuation prompt is needed.`
- Handoff generated: no.
- Verdict: PASS.

## Scenario Coverage Not Run As Separate Fresh Targets

- CP-003 decision-trail behavior was exercised by GREEN CP-001 and the authority/rationale output checks.
- CP-005 workflow contamination was exercised by GREEN CP-001, CP-002, and CP-006.
- CP-009 durable-continuity boundaries are pinned in runtime use/non-use and core-boundary rules but were not run as a separate fresh target.

These are disclosed as non-isolated coverage, not claimed as independent scenario runs.

## Refactor Changes

- Observed loophole: a shared skill's own source repository was mistaken for the handoff target workspace.
- Predicted cause: the runtime process prohibited broad discovery but did not explicitly disqualify ambient skill/cwd identity.
- Skill change: disallow workspace inference from the skill package, evaluator repository, or current directory; omit nonessential identity or ask only when material.
- Retest result: PASS.

No other tested rationalization repeated. No speculative counter was added.

## Portability And Quality Status

- Portable frontmatter uses only `name` and `description`.
- Package directory and `name` match.
- No runtime references or deep reference chains exist.
- No command syntax, argument token, harness-specific tool, provider field, storage path, model, or invocation mechanism is required.
- Evaluator data remains outside the deployable skill package.
- Runtime output is adaptive rather than a fixed quota template.
- Readiness before final static checks and independent review: GREEN behavior proven for the representative and high-risk branches above.

## Residual Risks

- Actual autonomous skill discovery and human invocation behavior in each installed harness is outside these content-only target tests.
- Output quality remains bounded by context the authoring session actually possesses; the skill stops or labels unknowns rather than reconstructing unavailable history.
- CP-003, CP-005, and CP-009 were covered indirectly rather than by isolated fresh targets.
