# Python Engineering Structure Doctrine Test Report

Skill: `python-engineering`

Revision date: 2026-08-09

## Scope

This report covers the purpose-grouped structure doctrine, declared and guard-enforced import-dependency law, exact-allowlist architectural guards, Ruff house defaults, and the reconciled dependency-topology, package-front-door, and ownership-docstring refinements. Error catalog/message policy and harness-wide delegation/configuration rules belong to later owner units and are excluded.

## Design And Mechanism Decision

Observed behavior failure: under speed and ambiguity, Python scaffolds used central model/helper buckets, implicit package surfaces, prose-only dependency rules, and incomplete Ruff defaults. Production projects then paid migration and independent-review cost to introduce the missing doctrine after planning had started.

Desired behavior: greenfield projects group by purpose, declare an import-dependency law with the first package, enforce it through exact source-derived guard tests, expose deliberate package surfaces, mirror the purpose tree in tests, and use the declared Ruff house profile. Incumbent structures remain authoritative unless a separate migration is approved.

Mechanism: revise the existing `python-engineering` router/reference skill. Reusable structure judgment belongs in the skill; each project's instantiated tree and dependency declaration belong in project instructions; mechanical enforcement belongs in project-created guard tests. No new skill, agent, hook, script, or harness policy is introduced.

Skill type: existing router/reference hybrid with one new one-level operational reference. Existing `architecture-design`, `testing-strategy`, and `error-handling-design` owner boundaries are preserved.

## RED Basis

### Structure And Guard Doctrine

- Source basis: observed production adoption and drift failures.
- Pressure: speed, false confidence, ambiguity, and the perceived cost of enforcement.
- Wrong behavior: central dumps, implicit public surfaces, undeclared dependency direction, prose-only laws, thresholds, or hand-maintained scan lists.
- Required behavior: purpose ownership, explicit front doors, one composition root, a declared layer order or dependency map, mirrored tests, and exact-allowlist guards with source-derived enumeration plus unexpected, bidirectional-drift, stale, and dynamic-bypass checks.

Live no-skill RED sessions were not rerun. The baseline rests on documented production failures. Consequence: the causal baseline is historical rather than reproduced in this repository.

### Review-Derived Precision Findings

- A mandatory linear layer order could misstate an honest dependency graph.
- An absolute re-export rule could eagerly load optional or expensive dependencies.
- An unqualified module-docstring rule could be misread as enabling Ruff `D` or requiring class/function docstrings.
- The greenfield ban on generic `core/` buckets required an explicit incumbent owner-approved exception.

These were concrete review findings and Python-mechanics conflicts, not independent production RED baselines. Their criteria were fixed in Scenarios 11–13 before the current target runs.

## GREEN Evidence Transported From The Staged Changeset

The first GREEN round was invalidated because target sessions inherited project instructions that contained the expected doctrine. It is retained only as a contamination disclosure.

The second round used fresh headless sessions in a neutral scratch tree containing only the corrected runtime skills. Scenario 9 passed with purpose-grouped packages, models inside purposes, package front doors, one composition root, a declared import law, mirrored tests, and the import-law guard among the first tests. Scenario 10 passed with exact justified pins, source-derived enumeration, unexpected/drift/stale assertions, dynamic-import coverage, the self-referential-pin docstring, and native-tool consideration.

The staged evidence reported an independent first review of `REVISE`, correction of all findings, and a delta re-review of `ACCEPT_WITH_NITS`, with both nits applied. This repository-side report preserves that evidence as transported evidence; the original external headless transcripts are not stored in this repository.

## Repository-Side Refinement Targets

Three fresh non-inheriting read-only targets ran against the reconciled repository source. Target-visible context was limited to the normal harness, repository checkout, task prompt, and `skills/python-engineering/SKILL.md`. Each target was forbidden from reading `skills-staging/`, `evals/`, or prior reports and was instructed not to edit.

### Scenario 11 — Non-Linear Import Topology

Result: PASS.

Behavior: selected a directional dependency map; made permitted edges explicit; treated the declaration as architectural authority; rejected an invented total order; required source-tree enumeration, static and dynamic import collection, exact comparison, bidirectional drift, and stale-entry detection.

Target-reported reads:

- `skills/python-engineering/SKILL.md`
- `skills/python-engineering/references/project-structure.md`

Evaluator or staging assets reported: none. File edits reported: no.

### Scenario 12 — Optional Heavy Public Submodule

Result: PASS.

Behavior: kept ordinary lightweight exports at the root front door; declared the optional reporting package as a documented public module path; avoided eager import of the optional dependency; preserved privacy for other implementation submodules; placed the dependency in an installable extra.

Target-reported reads:

- `skills/python-engineering/SKILL.md`
- `skills/python-engineering/references/project-structure.md`
- `skills/python-engineering/references/project-setup.md`

Evaluator or staging assets reported: none. File edits reported: no.

### Scenario 13 — Ownership Docstring Scope

Result: PASS.

Behavior: required one module-level ownership contract per module; left function/class docstrings optional; kept Ruff `D` disabled; correctly distinguished docstring code formatting from docstring lint rules.

Target-reported reads:

- `skills/python-engineering/SKILL.md`
- `skills/python-engineering/references/packaging-distribution.md`
- `skills/python-engineering/references/project-structure.md`
- `skills/python-engineering/references/quality-gates.md`

Evaluator or staging assets reported: none. File edits reported: no.

## Refactor Outcomes

- Dependency declarations now support either an honest layer order or an explicit directional dependency map. Permitted edges must be justified, legible, acyclic, guard-enforced, and architectural rather than inferred from current imports.
- The front-door rule now contains one narrow documented escape for heavy or optional public submodules while keeping all other implementation submodules private.
- Ownership docstrings are explicitly module-level contracts and do not enable Ruff `D` or require class/function docstrings.
- Generic greenfield bucket names remain forbidden; owner-approved incumbent buckets are preserved without becoming precedent.
- The staged evidence label remains `proven in one production project and adopted into a second (2026-08)`.

## Quality And Portability Basis

- Runtime content stays under `skills/python-engineering/`; evaluator prompts, criteria, and evidence stay under `evals/skills/python-engineering/`.
- The new operational reference is one level below `SKILL.md` and has a trigger-specific routing entry.
- Portable frontmatter is unchanged; no harness-specific fields, tools, local paths, or evaluator content enter the runtime skill.
- The baseline and migration gate preserve incumbent authority and prevent silent restructuring.
- The Ruff additions are explicitly labeled house doctrine rather than external consensus.

## Static Repository Checks

- `git diff --check` passed for every tracked file in this owner unit.
- All six target files exist; the runtime directory/name/frontmatter contract is intact; no touched file contains trailing whitespace.
- `shasum -a 256 -c STAGED-FINGERPRINTS.sha256` passed for every staged changeset file, confirming that `skills-staging/` still matches its supplied fingerprints.
- Markdownlint with `MD013` disabled reported one finding: `MD040` on the language-less command fence in `quality-gates.md`. The same fence exists in the pre-change `HEAD` source and was not introduced or modified by this unit. No new Markdown finding was reported.
- Runtime skill content contains no evaluator path, staging path, harness-specific command, or local machine path. All runtime links stay one level below `SKILL.md` and resolve within the skill package.
- No Python source, package metadata, runtime configuration, or dependency was changed, so project code gates were not applicable. Behavioral verification is the fresh-target evidence above.

## Residual Risk

- Incumbent over-application remains possible despite the explicit gate; no fresh brownfield pressure target was run for this revision.
- Exact-allowlist guards may be cargo-culted where a native tool suffices; the runtime reference rejects that use, and the neutral guard target considered native tools first.
- Repository-side target read records are procedural and target-reported, not filesystem capability isolation.
- Scenarios 11–13 confirm the intended interpretations but do not provide fresh no-skill baselines; their source basis is review-derived correctness and explicit owner intent.

Readiness state: ready to ship with one unchanged pre-existing `MD040` diagnostic disclosed above.
