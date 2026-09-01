# Verification Harness Lifecycle

Use this reference when creating, maintaining, repairing, or auditing a reusable project verification harness. A harness is a project-owned capability that can repeatedly launch a real target, diagnose prerequisites, drive supported scenarios, capture decisive evidence, and clean its owned state.

The portable owner defines lifecycle and evidence semantics. Project-local adapters define exact commands, tool syntax, selectors, credentials or role provisioning, fixtures, temporary-state mechanics, and authoritative cleanup operations. Do not assume a browser product, CLI driver, device runner, service manager, or harness API.

## Modes And Entry Gate

Choose the mode from current project and task evidence before changing verifier state:

| Mode | Entry condition | Required outcome |
| --- | --- | --- |
| `bootstrap` | A user-facing or operational product has a runnable first vertical slice, no adequate verifier exists, reusable live proof is required, and project mutation plus live actions are authorized | Minimum adequate project-native capability, discovery pointer, truthful feature map, one mapped live proof, cleanup readback, and exact `changed` return |
| `use` | An adequate verifier and affected mapped path are current | Run the applicable mapped path, preserve source/build and evidence identity, clean owned state, and return evidence to the requesting workflow |
| `maintain` | Product source, launch/control/observer mechanics, evidence identity, or a prior support claim may have changed | Mark affected claims stale, classify the cause, repair only verifier-owned drift through project implementation ownership, rerun proof and cleanup, and return `clean`, `changed`, or `blocked` |
| `not_applicable` | No runnable surface exists, work is document-only or read-only, the first slice is not runnable, or sufficient deterministic evidence closes the task without reusable live control | Return to the ordinary testing path without creating a feature map, wrapper, helper, package, schedule, or extra phase |

Planning may reserve verifier work at project inception when later runtime proof will require it. Do not instantiate project mechanisms or feature claims until a real runnable slice supplies launch, drive, observer, evidence, and cleanup facts. Do not treat repository age, elapsed time, a generic application label, or possible future reuse as an entry condition.

## Project-Native Capability Contract

The capability shape follows the project. It can compose existing commands, tests, scripts, developer tools, framework adapters, or a project-owned helper. It is not required to be a skill, CLI, package, manifest, browser adapter, or single executable.

The minimum capability provides:

- a project-designated discovery pointer in an already-used project instruction or developer entry surface when one exists, otherwise an exact canonical project-local location returned for future project intake;
- one truthful feature map with user-facing or operational paths, source pointers, verifier entry points, evidence states, and known bounds;
- project-native ways to perform applicable Launch, Doctor, Drive, Evidence, and Cleanup stages;
- exact source/build identity, evidence artifacts or readback, state ownership, and cleanup contract;
- a stable invocation path that later work can compose without reconstructing throwaway control logic.

Reuse existing project mechanisms first. A new wrapper, CLI, helper, adapter, or skill-shaped package requires a named missing reusable seam, a current project owner, bounded write authority, and proof that composition alone cannot supply the lifecycle. Do not copy another harness's directory shape, commands, provider assumptions, cloud execution, swarm topology, schedule, or media requirements.

## Bootstrap Ownership And Handoff

`testing-strategy` defines the capability and acceptance contract. The normal project implementation owner creates or changes project-local files and commands. A verifier-specific owner is optional and may be used when the project already has one; it is never a bootstrap prerequisite.

Before the implementation handoff, discover and provide:

- accepted feature scope and user-visible behavior;
- canonical project root, composition-root launch path, and current source/build identity;
- existing launch, health, test, drive, inspection, evidence, and cleanup mechanisms to reuse;
- missing control or observer seams, with evidence that each is necessary;
- allowed target paths and non-target boundaries;
- authority for project mutation, local/live actions, credentials, external reach, and destructive behavior;
- required discovery pointer, feature-map fields, invocation return, evidence artifacts, state isolation, and cleanup readback;
- exact first mapped journey and its accepted result.

The implementation return must name changed paths, reused and added mechanisms, feature-map and discovery locations, invocation entry points, source/build identity, allowed-write inventory, cleanup contract, unsupported coverage, deviations, and resulting state identity. Consume the returned fields; do not accept a zero exit code, generated file, or implementer completion claim as lifecycle proof.

After the return, run the first mapped journey through every applicable lifecycle stage. If the implementation owner cannot produce the bounded capability without new dependencies, external authority, unsupported project surfaces, or a different artifact owner, return the exact blocker or re-plan trigger rather than inventing mechanics inside `testing-strategy`.

## Feature Map

Maintain one project-designated feature map as the truthful front door to the harness. Create or change that project artifact only when repository mutation is authorized. Each entry records:

- feature or scenario and the protected behavior;
- public observer or real seam;
- environment, role, platform, device, service, or optional dependency requirements;
- project-local launch and drive adapter identifiers;
- evidence required for success;
- temporary or external state created and cleanup owner;
- source-of-truth pointer and last validated source/build identity;
- status: `verified`, `manual-bounded`, `blocked`, `unsupported`, or `stale`;
- unsupported gap, skipped automation reason, and residual risk when not `verified`.

Describe features from the user or operator point of view: what the capability does, how to reach it, how the project verifier drives it, and what state or evidence proves it. Keep source truth in code, contracts, and canonical project configuration; the map points to that truth and compresses the navigation path instead of duplicating repository internals.

Do not infer full support from one platform, role, route, browser, command, or happy path. A feature absent from the map is not supported. A stale entry cannot be reported as current evidence.

## Lifecycle

Run the lifecycle for each supported feature or coherent scenario group. Preserve the stage and primary outcome when a later stage also fails.

In `use`, select only affected mapped paths and any causal halo needed for the task. Right-seam automated tests and warranted independent review remain separate evidence owners. The live verifier complements them and its result must be carried to the requesting implementation, diagnosis, plan, or acceptance workflow; a successful run that no consumer uses is incomplete.

### 1. Launch

- Resolve the project-canonical composition-root entrypoint and its source identity through the project-local adapter.
- Name the target environment/build, required authority, network or external-system reach, and all temporary state before starting.
- Isolate mutable state to an authorized workspace, account, tenant, schema, device, process, or other owned boundary.
- Capture process identity, ports, logs, and readiness observer needed for later cleanup.
- Treat readiness as setup evidence, not behavior success.

Failure state: `launch-failed`. Do not continue to Drive when the intended target did not start or its identity is uncertain.

### 2. Doctor

- Check canonical command/tool availability, configuration source, dependencies, services, credentials or roles, fixtures, ports/devices, observer access, and cleanup capability that the mapped feature requires.
- Classify each missing capability as required, optional, CI-only, environment-limited, blocked by authority or credentials, or replaceable by alternate evidence.
- Prove that the harness can observe the real target and can remove every state class it is permitted to create.
- Update the feature status instead of silently skipping an unmet requirement.

Failure state: `doctor-failed`. A healthy generic environment does not override a missing feature prerequisite.

### 3. Drive

- Enter through the public command, route, UI action, API, device action, job trigger, service boundary, or agent surface named in the feature map.
- Use only the authority granted for the scenario. Writes, accounts, messages, external calls, and destructive or irreversible behavior remain separately controlled.
- Exercise the mapped success, boundary, negative, permission, and recovery cases that materially protect the behavior.
- Keep tool syntax and project commands inside the selected project-local adapter.

Failure state: `drive-failed` when setup succeeded but the harness could not complete the intended interaction. Do not relabel a drive failure as an assertion failure.

### 4. Evidence

- Assert the true observable end state and any relevant stdout, stderr, exit class, response, persisted state, filesystem delta, message, log, trace, console, network, accessibility, or device evidence.
- Capture provenance: source/build identity, environment, role/account, steps, observer, timestamp or source window, artifacts, and skipped checks.
- Read authoritative state back when exit status, screenshot, response, or mutation result cannot prove the protected behavior.
- Treat screenshots, file existence, page reachability, and exit zero as supporting evidence only unless one is itself the complete accepted contract.

Failure state: `assertion-failed` when Drive completed but observed behavior did not match the accepted result. Preserve the exact mismatch and artifacts.

### 5. Cleanup

- Register each harness-owned process, account, file, workspace, database row, queue item, browser context, device state, or other resource when it is created.
- Run cleanup from unconditional finalization after success, launch/doctor/drive/assertion failure, timeout, cancellation, or interruption whenever any owned state exists.
- Remove only validated harness-owned state. Cleanup authority does not extend to pre-existing or unrelated resources.
- Verify cleanup through the authoritative state owner; command success alone is insufficient.
- Aggregate cleanup errors and preserve `cleanup-failed` separately from the primary outcome. Cleanup failure never turns the primary failure into success or erases its evidence.

The final run record contains `primary outcome` and `cleanup outcome`. A feature cannot remain `verified` when required cleanup is failed or unverified.

## Maintenance And Retirement

Enter `maintain` and revalidate affected feature-map entries when current evidence shows any of these changed or may have changed:

- launch command, composition root, runtime, build, configuration, dependency, or optional platform tool;
- route, command, selector, login flow, role, permission, fixture, API/schema/contract, or expected output;
- browser/device/CLI adapter, observer, evidence requirement, temporary-state boundary, or cleanup operation.

An explicit full-audit request or source evidence that can invalidate entries beyond the affected set expands maintenance to the complete map. Elapsed time, repository activity, or a universal daily schedule does not. A scheduler or automation may call this lifecycle only when another authorized system owns that mechanism and supplies a valid evidence-based trigger; this portable contract does not create one.

For each affected entry:

1. mark it `stale` before relying on prior evidence;
2. inspect current product source and live behavior to classify product failure, verifier-owned drift, or environment/authority blockage before mutation;
3. route verifier-owned adapter, feature-map, discovery, or helper repair through the normal project implementation owner without inventing commands;
4. rerun Launch and Doctor, then the mapped Drive, Evidence, and Cleanup path;
5. restore `verified` only from current decisive evidence;
6. use `manual-bounded`, `blocked`, or `unsupported` when current automation or authority cannot prove the feature;
7. retire commands, scenarios, fixtures, and support claims that no longer map to current behavior.

Do not split creation and maintenance into separate lifecycle owners. Do not auto-expand feature coverage because a project changed. New scenarios need a protected behavior, source truth, authority boundary, observer, and cleanup contract.

When a mapped journey fails during feature or bug work, preserve the before state and causal classification. Change product code only for a source-backed product failure. Change verifier-owned mechanisms only for drift. Keep environment and authority blockers explicit. After an authorized repair, run the same affected user path and record before/after source/build and evidence identity.

## Harness Failure Record

Record every run with:

```text
Feature:
Source/build identity:
Feature-map status before run:
Launch: passed / launch-failed / not reached
Doctor: passed / doctor-failed / not reached
Drive: passed / drive-failed / not reached
Evidence: passed / assertion-failed / not reached
Primary outcome:
Cleanup: passed / cleanup-failed / not required / unverified
Artifacts and authoritative readback:
Skipped or unsupported coverage:
Residual risk:
```

Do not collapse all failure states into `test failed`. The stage controls the next action: fix launch ownership, repair the environment, correct the adapter interaction, investigate product behavior, or recover owned state.

## Lifecycle Return

Return the result to the workflow that requested proof:

```text
Mode: bootstrap / use / maintain
Applicability reason:
Project capability and discovery pointer:
Feature-map path and affected entries:
Source/build identity:
Implementation owner and changed paths:
Reused mechanisms:
Added mechanisms and proven missing seam:
Lifecycle record per mapped feature:
Primary result: clean / changed / blocked
Cleanup result and authoritative readback:
Evidence artifacts and consumer:
Unsupported or retired coverage:
Next evidence-based maintenance trigger:
Residual risk:
```

`bootstrap` cannot return `clean`. `use` with no current live proof is incomplete. `maintain` cannot return `clean` when any affected verified claim remains stale, cleanup is unverified, or authority/observer access is missing. `not_applicable` returns to the ordinary testing result and does not use this lifecycle return.

## Completion And Failure

The harness lifecycle is complete when the selected mode was justified, the capability is discoverable, the feature map matches current project truth, every affected `verified` entry passes Launch, Doctor, Drive, Evidence, and required Cleanup through its real observer, all other affected entries state an honest bounded status, exact project mechanics remain with project implementation ownership, and the requesting workflow receives the evidence identity.

Failure output: `Not done: verification harness cannot claim <capability>: <launch/doctor/drive/evidence/cleanup/feature-map gap>.`
