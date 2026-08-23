# Verification Harness Lifecycle

Use this reference when creating, maintaining, repairing, or auditing a reusable project verification harness. A harness is a project-owned capability that can repeatedly launch a real target, diagnose prerequisites, drive supported scenarios, capture decisive evidence, and clean its owned state.

The portable owner defines lifecycle and evidence semantics. Project-local adapters define exact commands, tool syntax, selectors, credentials or role provisioning, fixtures, temporary-state mechanics, and authoritative cleanup operations. Do not assume a browser product, CLI driver, device runner, service manager, or harness API.

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

Do not infer full support from one platform, role, route, browser, command, or happy path. A feature absent from the map is not supported. A stale entry cannot be reported as current evidence.

## Lifecycle

Run the lifecycle for each supported feature or coherent scenario group. Preserve the stage and primary outcome when a later stage also fails.

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

Revalidate affected feature-map entries when any of these changes:

- launch command, composition root, runtime, build, configuration, dependency, or optional platform tool;
- route, command, selector, login flow, role, permission, fixture, API/schema/contract, or expected output;
- browser/device/CLI adapter, observer, evidence requirement, temporary-state boundary, or cleanup operation.

For each affected entry:

1. mark it `stale` before relying on prior evidence;
2. update the project-local adapter or source pointer without inventing commands;
3. rerun Launch and Doctor, then the mapped Drive, Evidence, and Cleanup path;
4. restore `verified` only from current decisive evidence;
5. use `manual-bounded`, `blocked`, or `unsupported` when current automation or authority cannot prove the feature;
6. retire commands, scenarios, fixtures, and support claims that no longer map to current behavior.

Do not split creation and maintenance into separate lifecycle owners. Do not auto-expand feature coverage because a project changed. New scenarios need a protected behavior, source truth, authority boundary, observer, and cleanup contract.

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

## Completion And Failure

The harness lifecycle is complete when the feature map matches current project truth, every `verified` entry passes Launch, Doctor, Drive, Evidence, and required Cleanup through its real observer, all other entries state an honest bounded status, and exact project mechanics remain in their owning adapters.

Failure output: `Not done: verification harness cannot claim <capability>: <launch/doctor/drive/evidence/cleanup/feature-map gap>.`
