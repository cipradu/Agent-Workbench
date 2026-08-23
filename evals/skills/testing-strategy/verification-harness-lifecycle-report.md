# Verification Harness Lifecycle Report

Status: `PASS`

## Decision Claim

`testing-strategy` should own the reusable verification-harness lifecycle when it can define truthful feature coverage, lifecycle states, evidence, authority, and maintenance while project-local adapters own exact launch and drive mechanics. A new skill is justified only if the two surfaces cannot remain coherent behind a branch-specific testing reference.

## Evaluation Contract

- Source basis: `docs/skill-analysis/cursor-plugins-exhaustive-skill-analysis.md`, Step 4.
- Scenarios: one CLI creation case and one UI maintenance case.
- Maximum fresh RED runs: two.
- Maximum focused correction: one existing-owner correction.
- GREEN runs: one unchanged rerun for each failed scenario.
- Reviewers: none.
- Completion reserve: preserve enough context and time to apply one correction, run required GREEN cases, and complete the Unit 4 gate.
- Optional-evidence downshift order: model comparison, extra harness type, additional target, independent review.
- Expansion trigger: only evidence that the lifecycle cannot be expressed coherently through testing strategy plus project-local adapters.
- PASS stop: all fixed criteria pass without evaluator data.
- CORRECT stop: the target blocks on a genuinely missing project fact while still naming the lifecycle and exact missing input.
- FAIL stop: one or more fixed criteria fail.
- INFRASTRUCTURE stop: the target cannot load its permitted runtime skill or selected operational reference; the run is invalid evidence.

## Target Context Boundary

Each target receives normal harness and repository instructions, `skills/testing-strategy/SKILL.md`, its scenario prompt, and ordinary read-only repository access. It may load only operational references selected by the runtime skill. It receives no evaluator assets, expected behavior, pass/fail criteria, analysis report, prior output, or verdict. It must not edit files, dispatch another agent, or perform external research.

## Scenario VH-CLI-01 — Create A Reusable CLI Harness

Source label: `provisional external-pattern gap`

Prompt:

```text
Apply testing-strategy to design a reusable project verification harness for an existing CLI. Do not edit files.

The project has a canonical local launch command and four public commands. Two commands read state; two write files inside a caller-supplied workspace. The harness must work without network access and must never write outside its temporary workspace. Exit zero alone is insufficient because the protected behavior includes exact stdout/stderr, exit class, and filesystem state. One command requires an optional platform binary that is unavailable in CI.

Define the reusable harness lifecycle and the artifact that tells future agents what it can and cannot verify. Keep exact project commands as unresolved project-local adapter inputs rather than inventing them.
```

Required behavior:

- Defines Launch, Doctor, Drive, Evidence, Cleanup, and Feature Map as one lifecycle.
- Separates launch failure, environment/doctor failure, scenario-drive failure, assertion failure, and cleanup failure.
- Names required authority, temporary-state containment, and authoritative filesystem readback.
- Records the optional-binary command as unsupported or environment-limited instead of silently skipping it or claiming full support.
- Leaves exact commands in a project-local adapter/reference and does not assume a universal CLI tool.
- Defines maintenance triggers and retirement for stale commands or unsupported scenarios.

Target: `/root/vh_cli_red`

Source identity: `177c964438a556aa47f54acee9c6887a5cfa5b9f3374c2e0bd36406cbd557ba5`

Observed result: The target produced a strong acceptance harness, truthful capability record, containment controls, evidence schema, and maintenance triggers. It improvised a Preflight/Isolate/Execute/Observe/Assert/Teardown/Aggregate sequence instead of the reusable Launch/Doctor/Drive/Evidence/Cleanup contract and did not classify launch, environment, drive, assertion, and cleanup failures as separate lifecycle outcomes.

Verdict: `FAIL`

## Scenario VH-UI-01 — Maintain A UI Harness

Source label: `provisional external-pattern gap`

Prompt:

```text
Apply testing-strategy to maintain an existing reusable UI verification harness. Do not edit files.

The project changed its canonical dev-server command and login flow. The current harness still launches the old command, reports a screenshot after page load as success, cannot exercise the admin role, and sometimes leaves the server and test account behind after a failed run. The project may expose a browser driver, but no specific browser tool is guaranteed in every harness.

Define how maintenance should update and revalidate the harness without overclaiming support. Keep exact tool syntax and project commands outside the portable lifecycle.
```

Required behavior:

- Re-runs Doctor and lifecycle validation after launch, auth, route, observer, cleanup, or project-command changes.
- Requires behavior evidence beyond a screenshot: true end state plus applicable console, network, log, accessibility, or persisted-state evidence.
- Marks admin-role coverage unsupported or blocked until credentials/fixtures and authority exist.
- Treats cleanup as required even after failure and reports cleanup failure separately without erasing the primary failure.
- Uses a capability-neutral project adapter; it does not assume Playwright, a specific browser driver, or one harness API.
- Updates the feature map and retires or corrects stale commands and scenarios rather than preserving false support.

Target: `/root/vh_ui_red`

Source identity: `177c964438a556aa47f54acee9c6887a5cfa5b9f3374c2e0bd36406cbd557ba5`

Observed result: The target correctly rejected screenshot-only proof, designed true-end-state evidence, bounded unsupported admin and browser capability, separated portable lifecycle from project-local commands, and required unconditional cleanup. It did not maintain a named feature map, did not use the shared lifecycle states, and did not preserve cleanup failure as a separate outcome alongside the primary launch/doctor/drive/assertion failure.

Verdict: `FAIL`

## Focused Revision Design Brief

Entry mode: existing-skill revision.

Target owner: `testing-strategy`.

Recurring behavior failure: When asked to create or maintain a reusable project verification harness, the current testing owner can produce good scenario-level evidence design but invents a case-specific lifecycle and support artifact. Future agents then lack one stable contract for launch, environment diagnosis, driving, evidence, cleanup, supported features, unsupported gaps, failure classification, freshness, and retirement.

Desired behavior: Select one branch-specific lifecycle for reusable harness work: Feature Map, Launch, Doctor, Drive, Evidence, Cleanup, and Maintenance. Keep exact commands, selectors, browser/CLI drivers, credentials, fixtures, and mutation mechanics in project-local adapters. Report launch, doctor, drive, assertion, and cleanup failures separately; cleanup must run after failure and must not erase the primary outcome.

Mechanism decision: Improve `testing-strategy` with one operational reference. The main skill already owns behavior targets, seams, risk, evidence, and residual risk. A conditional reference can add the lifecycle without bloating ordinary test design. A new autonomous skill, create/maintain split, universal tool, or harness generator is not justified by these cases.

Skill type: Preserve the current process/discipline owner. Add one selector and one branch-specific process reference.

Information placement:

- `skills/testing-strategy/SKILL.md` adds the trigger and sharp selector.
- `skills/testing-strategy/references/verification-harness-lifecycle.md` owns lifecycle states, feature-map truth, failure taxonomy, maintenance, portability, and stop conditions.
- Project repositories own exact adapter commands and stateful tool mechanics; browser/computer/CLI tools remain adapters.

Failure output: `Not done: verification harness cannot claim <capability>: <launch/doctor/drive/evidence/cleanup/feature-map gap>.`

GREEN criteria: Both unchanged scenarios must use the shared lifecycle and feature map, preserve project-local adapter boundaries, report unsupported states honestly, classify failures by lifecycle stage, retain primary and cleanup outcomes, and avoid universal tooling assumptions.

## Owner-Coherence Test

The existing owner remains coherent if one conditional reference can express both cases while:

- the main skill keeps evidence-selection semantics and a sharp selector;
- the reference owns lifecycle states, feature-map truth, maintenance, and stop conditions;
- project-local adapters own exact commands, browser/CLI tooling, credentials, and mutation mechanics;
- no separate autonomous trigger is required for ordinary testing work.

A new skill remains unjustified unless RED/GREEN evidence proves this split cannot guide both cases without bloating or contradicting the testing owner.

## Run Ledger

| Scenario | Source identity | Target identity | RED verdict | Correction | GREEN identity |
| --- | --- | --- | --- | --- | --- |
| `VH-CLI-01` | `177c9644...` | `/root/vh_cli_red` | `FAIL` | one focused existing-owner correction | `/root/vh_cli_green`; `fdd64d9c...`; `c9d2ea61...`; `PASS` |
| `VH-UI-01` | `177c9644...` | `/root/vh_ui_red` | `FAIL` | same focused correction | `/root/vh_ui_green`; `fdd64d9c...`; `c9d2ea61...`; `PASS` |

## Unit Verdict

`PASS — improve existing owner; do not create a new skill.`

Both unchanged GREEN targets used Feature Map plus Launch, Doctor, Drive, Evidence, Cleanup, and Maintenance; classified lifecycle failures; preserved primary and cleanup outcomes; bounded unsupported or blocked capability; kept project commands and tool syntax in project-local adapters; and avoided universal CLI/browser assumptions.

Owner-coherence result: `testing-strategy` remains coherent. The main skill gained one sharp selector and the branch-specific lifecycle lives in one operational reference. Ordinary test-design invocations do not load the lifecycle. Project adapters retain exact mechanics. A new skill or separate create/maintain skills would duplicate the existing evidence owner without a distinct proven trigger.

Fresh runs: `4/4` maximum used: two RED and two GREEN.

Focused corrections: `1/1` maximum used.

Review count: `0`.
