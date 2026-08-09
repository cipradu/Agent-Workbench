# Error Handling Design Skill Test Report

Date: 2026-08-09

Status: `PASS`

## Scope

This report covers the centralized error vocabulary/catalog split, static catalog-backed messages with structured runtime context, and the anti-speculation vertical-slice constraint added to `error-handling-design`.

Runtime skill entry point: `skills/error-handling-design/SKILL.md`

Operational references under test:

- `skills/error-handling-design/references/error-shapes.md`
- `skills/error-handling-design/references/logging-and-redaction.md`

Evaluator suite: `evals/skills/error-handling-design/pressure-tests.md`, scenarios 23–25.

Skill type: existing router/reference hybrid. The revision adds no new skill owner or runtime mechanism.

Source classification: strong operator convention supported by one production implementation and adoption into a second project. It is a greenfield default, not an external-consensus claim. Incumbent accepted project conventions remain authoritative until an approved change.

## Target Separation

Each target ran in a fresh non-inheriting read-only session. Targets received the runtime skill entry point and one neutral task prompt. They were explicitly prohibited from reading `skills-staging/`, evaluator assets, prior reports, plans, or other target outputs. All targets reported `Evaluator assets read: none` and `Files changed: none`.

## Results

| Target | Pressure | Result | Decisive evidence |
| --- | --- | --- | --- |
| `/root/error_catalog_target` | Per-adapter concrete failure definitions | `PASS` | Kept provider recognition and mapping in adapters while assigning concrete application failures to one enumerable catalog; explicitly rejected generalizing the rule to unrelated logging or audit vocabularies. |
| `/root/error_message_target` | Runtime values interpolated into one operator message | `PASS` | Returned a complete static public message, moved permitted provider/account/path/amount context into governed structured fields, and required authoritative-state checks before payment retry. |
| `/root/error_vertical_slice_target` | Pre-fill a catalog with probable future failures | `PASS` | Rejected all speculative entries and required an implemented path, receiver, mapping site, diagnostic policy, public/private projection tests, and consumer/completeness evidence for each addition. |

Result: 3/3 fresh behavior targets passed.

## Criteria Assessment

- Vocabulary remains dependency-light and broadly importable: `PASS`.
- Concrete failure definitions have one central enumerable owner: `PASS`.
- Provider- or adapter-specific mapping knowledge remains at the owning boundary: `PASS`.
- Central error-catalog doctrine does not spread to unrelated event, audit, or telemetry catalogs: `PASS`.
- Catalog-backed messages remain static and operator-safe: `PASS`.
- Runtime identifiers, paths, amounts, provider details, and payload excerpts stay in governed structured fields: `PASS`.
- Public codes distinguish caller action or disclosure contract rather than message wording: `PASS`.
- Speculative entries without a real vertical slice are rejected: `PASS`.
- Targets preserved incumbent-authority and current-dependency verification boundaries: `PASS`.
- Runtime/evaluator separation and read-only behavior held: `PASS`.

## Residual Limits

- The evidence label intentionally remains “proven in one production project and adopted into a second (2026-08).” It must not rise to “proven in two” until the second implementation lands in accepted code.
- Target isolation is procedural and target-reported; it is not a filesystem sandbox guarantee.
- This evaluation proves skill behavior under the three named pressure cases. It does not validate any project's provider-specific exception classes, public status codes, or retry mechanics.
