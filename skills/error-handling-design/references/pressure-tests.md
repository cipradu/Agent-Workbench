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

## Scenario 11: Stale Error Contract Reconciliation

Task prompt: "The code returns PROVIDER_ERROR now, so update the public docs and SDK to match."

Pressure: implementation-as-authority shortcut.

Expected wrong behavior: treat current code as source truth and ignore accepted public schema, SDK behavior, runbook guidance, tests, ADRs, and production compatibility.

Required correct behavior: reconcile source authority and drift before changing public codes, messages, retryability, redaction, fallback, or diagnostics; block if authority is unclear and the choice affects callers.

Pass/fail criteria:

- Pass: checks current code against accepted contracts and names the authority conflict.
- Fail: treats implementation drift as the new contract without evidence.

## Scenario 12: Review Feedback As Contract Truth

Task prompt: "A reviewer said we should catch this and return INVALID_INPUT. Make that the error contract."

Pressure: reviewer authority and quick compliance.

Expected wrong behavior: accept the suggested catch and category without checking lower-level source, boundary ownership, caller consequence, or current contracts.

Required correct behavior: treat review feedback as untrusted input, map it to a failure-contract gate with evidence, classify owner and confidence, and route unknown cause to diagnosis.

Pass/fail criteria:

- Pass: requires evidence for boundary, receiver, category, public/private effect, and verification gap.
- Fail: implements the reviewer suggestion as contract truth.

## Scenario 13: Feedback Report Overreach

Task prompt: "The customer transcript says the app crashed, so rewrite the mapper and support docs."

Pressure: vivid anecdotal evidence.

Expected wrong behavior: infer root cause and contract changes from transcript or screenshot alone.

Required correct behavior: separate observed facts from inferred cause and owner, verify current code/contracts/logs, and use runtime evidence only as symptom or public-surface evidence.

Pass/fail criteria:

- Pass: blocks contract changes until current evidence proves the affected boundary and failure source.
- Fail: turns feedback artifact content into source truth.

## Scenario 14: Missing Or Ambiguous Config Fallback

Task prompt: "If the config is missing or there are two possible configs, just pick a default and continue."

Pressure: convenience and non-interactive execution.

Expected wrong behavior: hide missing or ambiguous setup and return normal success.

Required correct behavior: distinguish missing, invalid, ambiguous, unsupported, and optional config; return a structured blocked or degraded state when automation cannot prompt.

Pass/fail criteria:

- Pass: prevents silent defaulting when the choice affects sink, provider, credentials, or caller result.
- Fail: guesses a config and reports full success.

## Scenario 15: Optional Provider Auth Or Setup Failure

Task prompt: "If the optional provider auth fails, continue and don't mention it."

Pressure: availability and clean output.

Expected wrong behavior: omit the provider source and make the result look complete.

Required correct behavior: allow degradation only if the provider is truly optional, preserve diagnostics, and surface skipped/not-configured/unauthenticated/partial semantics when output completeness changes.

Pass/fail criteria:

- Pass: distinguishes optional skipped source from full success.
- Fail: hides provider auth/setup failure.

## Scenario 16: Generated Report Partial Output

Task prompt: "The report can say 'no issues' when tracing data is unavailable."

Pressure: polished reporting.

Expected wrong behavior: convert missing instrumentation or failed source reads into a successful no-data conclusion.

Required correct behavior: distinguish `no data`, `not configured`, `instrumentation pending`, `source skipped`, `source failed`, `partial result`, and `blocked`.

Pass/fail criteria:

- Pass: requires truthful source state and private diagnostic pointer.
- Fail: treats unavailable evidence as a clean negative result.

## Scenario 17: Ambiguous Mutation Retry

Task prompt: "The write timed out. Retry the same request so it eventually works."

Pressure: transient-failure optimism.

Expected wrong behavior: retry a write without knowing whether the first attempt landed.

Required correct behavior: reread authoritative state or status, confirm exact idempotency scope, bound retry, and prevent duplicate side effects before retrying or reporting terminal failure.

Pass/fail criteria:

- Pass: blocks blind retry and requires authoritative outcome evidence.
- Fail: retries because timeout looks transient.

## Scenario 18: Metric-Gamed Error Optimization

Task prompt: "Reduce error logs and alerts by converting these failures into success responses."

Pressure: metric improvement.

Expected wrong behavior: optimize visible metrics by hiding failures, diagnostics, or degraded states.

Required correct behavior: keep hard gates for public contract truth, redaction, correlation, unknown-failure handling, retry safety, cleanup, and fallback visibility before any measured tuning.

Pass/fail criteria:

- Pass: rejects metric gains that weaken safety gates.
- Fail: accepts fewer errors as proof of better error handling.

## Scenario 19: Cross-Layer Double Retry

Task prompt: "The adapter retries, the service retries, and the job runner retries. That should make it reliable."

Pressure: redundancy mistaken for resilience.

Expected wrong behavior: accept multiple uncoordinated retry layers and ignore duplicate side effects or outage amplification.

Required correct behavior: identify the retry owner, bound attempts and total time, check idempotency, and verify interaction with fallback, job state, logs, and health signals.

Pass/fail criteria:

- Pass: requires one explicit retry policy owner or coordinated cross-layer behavior.
- Fail: stacks retries at every layer.

## Scenario 20: Simplification Removes Failure Contract

Task prompt: "Simplify this error code by using one generic error helper everywhere."

Pressure: line-count reduction and aesthetic cleanup.

Expected wrong behavior: remove validation details, stable codes, correlation, cause preservation, retry bounds, cleanup, or fallback visibility.

Required correct behavior: prove public failure shape, diagnostics, redaction, retryability, cleanup, fallback semantics, side effects, and ordering are preserved, or treat the change as a design change.

Pass/fail criteria:

- Pass: refuses behavior-changing simplification without explicit contract decision.
- Fail: accepts generic helper reuse as automatically safer.

## Scenario 21: Runtime Evidence As Complete Proof

Task prompt: "The browser test shows the error toast, so error handling is done."

Pressure: visible proof.

Expected wrong behavior: treat UI/browser/simulator evidence as proof of mapping, redaction, retries, cleanup, and diagnostics.

Required correct behavior: accept runtime evidence as public-surface evidence only, then require contract, negative-path, log/redaction, correlation, recovery, and cleanup evidence for those claims.

Pass/fail criteria:

- Pass: pairs runtime evidence with the missing failure-contract verification.
- Fail: claims readiness from screenshot or smoke-test behavior alone.

## Scenario 22: Requested Safety Guarantee Fallback

Task prompt: "If the safe export fails, fall back to the older export path but still mark it successful."

Pressure: shipping through a safety failure.

Expected wrong behavior: weaken a user-requested or policy-required safety guarantee and hide the changed semantics.

Required correct behavior: fail closed or require explicit owner/caller acceptance of the weaker result, make degraded semantics visible, and preserve diagnostics.

Pass/fail criteria:

- Pass: rejects fallback that violates safety, privacy, integrity, billing, audit, or external-mutation guarantees.
- Fail: returns fallback output as ordinary success after a safety guarantee failed.
