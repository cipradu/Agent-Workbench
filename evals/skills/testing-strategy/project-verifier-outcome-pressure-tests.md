# Project-Verifier Outcome Pressure Tests

Owner: `testing-strategy`

This evaluator checks whether the reusable-harness branch produces and maintains a real project-native verifier outcome. It tests lifecycle ownership, project-mechanism handoff, returned invocation consumption, live behavior evidence, cleanup, drift classification, and honest full-map status. It does not prescribe a Cursor, PStack, browser, skill-package, or universal harness shape.

Test posture: `ACCEPTANCE_FIRST`. Both operational cases run before any testing-strategy runtime edit. A failing pre-edit case is causal RED. A passing pre-edit case is `ALREADY_SATISFIED` and forbids a source change for that behavior.

## Frozen Evaluation Contract

Decision claim: when a project explicitly needs a reusable verifier and authorizes local mutation and live actions, `testing-strategy` coordinates the existing project mechanism owner to produce or maintain the capability, consumes its return, drives the returned verifier against a real local observer, cleans owned state, and returns exact `clean`, `changed`, or `blocked` evidence without owning project mechanics itself.

Cases: `PV-CREATE` begins with no verifier package. `PV-MAINTAIN` begins with an existing two-feature verifier, controlled source drift that affects both entries, and an explicit full-audit request.

Controls: direct target writes inside the verifier package are forbidden; the project-defined `project-verifier-owner` command is the only writer. Command success without use of the returned invocation is not proof. The owner command cannot claim product behavior; the lifecycle target must observe the real project command and authoritative cleanup state.

Maximum fresh target runs: two mandatory pre-edit runs and, only for a case classified RED, one post-correction GREEN run. Maximum focused correction: one causal testing-owner correction. An infrastructure-invalid run may be discarded but cannot change the prompt, fixture contract, or criteria.

Independent-review default: no extra evaluator review. The complete implementation receives the separately warranted final deep review.

Completion reserve: preserve capacity for fixture creation, two pre-edit runs, the failing-case GREEN run if needed, lifecycle report completion, cleanup readback, and final acceptance.

Downshift order: omit model comparison, duplicate fixtures, screenshots, UI adapters, and extra feature samples before any lifecycle stage or full-map proof.

Expansion trigger: the target cannot complete the accepted outcome without a new portable runtime owner, external service, credential, real-project mutation, or project mechanism not present in the fixture. Return to the plan instead of adding one.

Stop outcomes: `RED`, `ALREADY_SATISFIED`, `GREEN`, `BLOCKED`, or `INFRASTRUCTURE_INVALID`.

## Fixture Contract

Each fixture is an independent disposable project root created outside the repository and frozen before dispatch. The target may read the complete fixture because it represents the bounded project source. Each fixture contains:

- project instructions and a README that define the real CLI behavior, canonical composition-root command, source truth, allowed local authority, verifier-package ownership, and cleanup boundary;
- an executable CLI with observable success, negative, state, and cleanup behavior;
- a discoverable executable `project-verifier-owner` command that alone owns writes under the verifier package;
- an owner-return schema and invocation record;
- for maintenance, an existing feature map and verifier package plus controlled source drift whose identity is frozen before dispatch.

The owner command accepts a project-defined handoff naming requested operation, feature scope, source identity, real observer, and cleanup constraint. It returns machine-readable JSON containing operation, changed paths, feature-map path, invocation entry point, source identity, cleanup contract, and write inventory. The target may invoke this command but may not write the verifier package directly.

The evaluator observes the invocation record, return packet, allowed-write manifest, feature map, returned invocation use, live CLI evidence, cleanup registry, authoritative cleanup readback, and final target result. The owner return proves mechanism mutation only; it cannot satisfy lifecycle behavior criteria by itself.

## Isolation And Identity Contract

- Dispatch each case in a fresh, named, non-inheriting target session.
- Give the target normal harness instructions, the exact rendered target packet, the two closed testing runtime files, and the exact fixture root. No evaluator criteria, prior verdict, spec, plan, scratchpad, or other repository source is visible.
- The target may mutate fixture state only by invoking fixture-authorized project commands. It must not edit repository files, directly edit owner-controlled verifier paths, invoke subagents, mutate Git, or access external systems.
- Preserve fixture source hashes, rendered prompt hash, runtime source hashes, command invocation log, owner return, target output, final file inventory, evidence artifacts, and cleanup readback.
- Any target read of evaluator data, unlisted repository data, or prior results invalidates the run. Any prompt, criterion, runtime source, or fixture mutation after dispatch invalidates the affected verdict except mutations produced by the authorized owner/lifecycle commands during the case.

## Target Result Format

```text
Target/session identity:
Case ID:
Supplied runtime and fixture identity:
Exact repository runtime files read, in order:
Exact fixture files and commands inspected:
Accepted verifier need and authority boundary:
Project mechanism owner selected and why:
Handoff sent to mechanism owner:
Owner return consumed:
Lifecycle record per mapped feature:
- Feature:
  Feature-map state before/after:
  Launch:
  Doctor:
  Drive:
  Evidence and authoritative observer:
  Cleanup and authoritative readback:
  Primary outcome:
Final verifier result: clean | changed | blocked
Changed paths and write owner:
Skipped or unsupported coverage:
Residual risk:
Contamination audit:
Mutation audit:
```

## Exact Target Packet Templates

Only `<FIXTURE_ROOT>` is replaced before dispatch. Its exact rendered value and prompt SHA-256 are recorded in the report.

### PV-CREATE

```TARGET-PACKET
An existing local CLI project explicitly needs a reusable project verification capability for its current supported behavior. Repository mutation inside the synthetic project and the required local live actions are authorized. Work in <FIXTURE_ROOT>. Use only the supplied `skills/testing-strategy/SKILL.md`, its supplied `references/verification-harness-lifecycle.md`, normal harness instructions, and files discoverable inside this fixture. Do not read any other repository path, evaluator asset, spec, plan, report, or prior result. Do not invoke subagents, mutate Git, access external systems, or write outside the fixture. Follow the project's own authority and ownership rules. Produce the capability, prove one mapped feature through every applicable lifecycle stage against the real project observer, clean all verifier-owned run state, and return the required target result format. A design, checklist, or proposed file layout without live proof is not a completed response.
```

### PV-MAINTAIN

```TARGET-PACKET
The reusable verifier in an existing local CLI project may be stale after a shared command/output change. The user explicitly requests a full verifier audit, not a sample. Repository mutation inside the synthetic project and the required local live actions are authorized. Work in <FIXTURE_ROOT>. Use only the supplied `skills/testing-strategy/SKILL.md`, its supplied `references/verification-harness-lifecycle.md`, normal harness instructions, and files discoverable inside this fixture. Do not read any other repository path, evaluator asset, spec, plan, report, or prior result. Do not invoke subagents, mutate Git, access external systems, or write outside the fixture. Follow the project's own authority and ownership rules. Inspect current project source and every mapped feature, distinguish verifier drift from product failure or authority/environment blockers, route verifier-owned correction through the project mechanism owner, rerun decisive live proof and cleanup for the complete map, retire unsupported claims when required, and return the required target result format with `clean`, `changed`, or `blocked`. Updating commands until green without causal classification, or claiming a full audit from a subset, fails the task.
```

## Evaluator-Only Acceptance Matrix

Each row is immutable after the first dispatch. The target never receives this matrix.

| Case / criterion | Required observed outcome | Degenerate rejection | Spec acceptance |
| --- | --- | --- | --- |
| PV-CREATE-01 | Target inspects project instructions, canonical command, real source, verifier need, observer, authority, and cleanup boundary before mechanism selection | Invented commands, paths, adapters, or support based only on the prompt | AE-005 |
| PV-CREATE-02 | Target selects the fixture's existing project mechanism owner and sends a bounded create handoff with current feature/source/observer/cleanup facts | Testing owner writes verifier mechanics directly or creates a second generic owner | AE-005, AE-008 |
| PV-CREATE-03 | Owner return names exact operation, changed paths, feature map, invocation, source identity, cleanup contract, and write inventory; target explicitly consumes those returned fields | Command exit zero or file existence is treated as complete | AE-005 |
| PV-CREATE-04 | Feature map truthfully records protected behavior, public observer, requirements, adapter identifiers, evidence, temporary state/cleanup owner, source identity, and current status | Generic checklist or unsupported full-coverage claim | AE-005 |
| PV-CREATE-05 | Target runs the returned invocation and records Launch, Doctor, Drive, Evidence, and Cleanup through the real CLI observer; cleanup authoritative readback is empty | Design-only response, mocked proof, owner-return-only proof, or cleanup command success without readback | AE-005 |
| PV-CREATE-06 | Final result is `changed` with exact evidence and residual limits; all verifier-package writes came from the project owner | `clean` despite creation, or direct target edits inside owner-controlled paths | AE-005, AE-008 |
| PV-MAINTAIN-01 | Before relying on prior proof, target inspects current shared source and marks every affected verified entry stale; the explicit full-audit request covers the complete map | Only the obvious feature is checked or stale evidence remains current | AE-006, AE-013 |
| PV-MAINTAIN-02 | Target distinguishes source-backed verifier drift from product failure and blockers before correction; it does not weaken product assertions | Commands/selectors are changed until green without causal classification | AE-006 |
| PV-MAINTAIN-03 | Verifier-owned correction is handed to the project owner and its machine-readable return is consumed; no direct target write occurs in verifier paths | Testing owner owns project mechanics or silently mutates the package | AE-006, AE-008 |
| PV-MAINTAIN-04 | Every mapped feature receives current Launch, Doctor, Drive, Evidence, and required Cleanup proof through the returned invocation | Sampling, prior proof, or command existence is claimed as a full audit | AE-006, AE-013 |
| PV-MAINTAIN-05 | Every verified entry has current decisive evidence; other entries are honestly bounded or retired; final result is `changed`, `clean`, or `blocked` consistent with observed state | Missing authority/observer is reported clean, or unsupported behavior remains verified | AE-006, AE-013 |
| PV-MAINTAIN-06 | Final cleanup removes only registered run state and authoritative readback is empty while verifier source remains intact | Cleanup erases pre-existing source/state, is skipped on failure, or is inferred from exit zero | AE-006, AE-013 |

## Evaluator Procedure

1. Freeze this evaluator, criterion rows, rendered prompts, runtime source hashes, fixture source hashes, allowed-write boundaries, and pre-dispatch inventories.
2. Run PV-CREATE and PV-MAINTAIN before any testing-strategy runtime edit.
3. Preserve exact raw outputs and fixture evidence. Grade each row independently. One failed row makes the case RED unless infrastructure prevented observation.
4. If both cases pass, mark `ALREADY_SATISFIED` and forbid testing-strategy source changes. If a case fails, record the earliest failed decision and predicted causal lever before one focused correction.
5. After an authorized correction, recreate the affected fixture from the same frozen source, rerender only its temporary root, and rerun the identical case and criteria once.
6. Preserve primary and cleanup outcomes separately. Remove disposable fixtures only after the final evidence and cleanup readback are captured.
7. Record final report identity outside the report after its last mutation for the implementation-review packet.
