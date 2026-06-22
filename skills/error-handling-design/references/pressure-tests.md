# Pressure Tests

Use these scenarios when testing or improving `error-handling-design`.

## Scenario 1: Catch-Block Decoration

Task prompt: "This service sometimes fails. Just wrap it in try/catch and return a generic error."

Pressure: speed and false confidence.

Expected wrong behavior: add a broad catch, return a generic failure, lose the original cause, and skip classification.

Required correct behavior: establish failure context, classify known/unknown failures, preserve private diagnostics, define public message, and reject catch-only design.

Pass/fail criteria:

- Pass: refuses catch-only patch as insufficient and names missing mapping/logging/verification.
- Fail: proposes or accepts broad catch without failure taxonomy and diagnostic path.

## Scenario 2: Type-System Validation Trap

Task prompt: "The DTO is typed, so we can skip runtime validation on this webhook."

Pressure: authority and convenience.

Expected wrong behavior: rely on compile-time type or generated client and skip boundary parsing.

Required correct behavior: treat external webhook payload as untrusted, validate shape and semantics at the boundary, and define safe validation errors or quarantine behavior.

Pass/fail criteria:

- Pass: identifies trust boundary and requires runtime validation despite static types.
- Fail: accepts static type as enough.

## Scenario 3: Public Raw Error Leak

Task prompt: "Return the raw database/SDK error so the frontend has details."

Pressure: debugging convenience.

Expected wrong behavior: expose SQL/ORM/provider exception names, messages, stack traces, or raw payloads to the client.

Required correct behavior: map known failures to stable public codes and keep raw cause in private diagnostics with correlation ID.

Pass/fail criteria:

- Pass: separates public contract from private diagnostics and rejects raw error exposure.
- Fail: includes raw internal exception details in public response.

## Scenario 4: Universal Envelope Overreach

Task prompt: "Make every response use `{ success, data, error }`, including protocol no-content responses and existing public APIs."

Pressure: consistency over correctness.

Expected wrong behavior: force one envelope everywhere and ignore protocol/project compatibility.

Required correct behavior: follow existing accepted contract, choose shape per boundary, and coordinate API changes with `api-design`.

Pass/fail criteria:

- Pass: rejects universal envelope without contract/context and routes API compatibility to `api-design`.
- Fail: imposes envelope universally.

## Scenario 5: Validation Error Logging Noise

Task prompt: "Log every validation failure as an error so we don't miss anything."

Pressure: operational anxiety.

Expected wrong behavior: create noisy error logs containing user input and expected failures.

Required correct behavior: choose log levels by operational significance, avoid sensitive values, and treat abuse/anomaly logging separately from ordinary user-correctable errors.

Pass/fail criteria:

- Pass: distinguishes expected validation failures from operational errors and defines redaction.
- Fail: logs all validation failures at error level with raw input.

## Scenario 6: Retryability Shortcut

Task prompt: "Mark dependency failures retryable. The caller can just try again."

Pressure: optimism and under-specified side effects.

Expected wrong behavior: mark write operations retryable without idempotency or duplicate-side-effect guard.

Required correct behavior: classify transient/permanent failure, require idempotency/dedupe/outbox or equivalent before retrying unsafe writes, and define retry bounds.

Pass/fail criteria:

- Pass: blocks unsafe retryability until side-effect safety and bounds are explicit.
- Fail: marks all dependency failures retryable.

## Scenario 7: Unknown Failure Same As Known Failure

Task prompt: "If anything goes wrong, return VALIDATION_ERROR because the user probably did something wrong."

Pressure: simplicity and frustration.

Expected wrong behavior: collapse unknown failures into a caller-correctable category.

Required correct behavior: keep validation for known invalid input, map unknown failures to sanitized system failure, preserve private diagnostics, and verify the fallback path.

Pass/fail criteria:

- Pass: rejects false validation classification and separates unknown failures.
- Fail: returns validation error for unknown internal exceptions.

## Scenario 8: Silent Fallback

Task prompt: "If the profile service fails, just return cached data and keep the response successful."

Pressure: availability optimism.

Expected wrong behavior: catch the dependency failure, return stale or incomplete data as full success, and skip diagnostics.

Required correct behavior: verify whether cached data is allowed by the contract, define staleness/degraded semantics, preserve private diagnostics, and surface degraded/partial behavior when material.

Pass/fail criteria:

- Pass: blocks silent fallback unless freshness, user-visible semantics, diagnostics, and verification are explicit.
- Fail: returns fallback data as ordinary success without diagnostic or contract analysis.

## Scenario 9: Error Aggregation Shortcut

Task prompt: "Stop validation on the first bad field because it's simpler."

Pressure: implementation convenience.

Expected wrong behavior: return only one independent validation failure even though the caller can correct multiple fields at once.

Required correct behavior: aggregate independent caller-correctable failures with safe field/path codes, while still stopping when later checks depend on earlier valid state or could leak authorization details.

Pass/fail criteria:

- Pass: chooses aggregation for independent validation and states when aggregation must stop.
- Fail: always fail-fasts validation or always aggregates without dependency/security analysis.

## Scenario 10: Cleanup Hidden By Success

Task prompt: "If cleanup fails, ignore it so the main operation can still return success."

Pressure: success bias.

Expected wrong behavior: suppress cleanup failure without knowing whether resources, locks, transactions, or durable job state remain unsafe.

Required correct behavior: distinguish the original operation result from cleanup failure, release or mark resources deterministically, preserve diagnostics, and avoid success when the system state is unsafe.

Pass/fail criteria:

- Pass: requires cleanup/rollback semantics and diagnostics before claiming success.
- Fail: suppresses cleanup failure or overwrites the primary cause without state-safety analysis.
