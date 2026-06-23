---
name: error-handling-design
description: Use when designing, changing, or reviewing application error handling, runtime validation failures, error taxonomies, result envelopes, exception mapping, sanitized messages, retryability, fallback/degraded-mode behavior, error aggregation, cleanup, correlation IDs, logging, or redaction behavior.
---

# Error Handling Design

## When to Use

Use this skill when:

- Designing or reviewing application error handling for services, APIs, jobs, CLIs, workers, integrations, scripts, agents, UI actions, or domain workflows.
- Defining runtime validation failures, field errors, parse failures, malformed input behavior, domain validation behavior, or boundary rejection behavior.
- Creating or changing error taxonomies, machine-readable codes, public messages, private diagnostic fields, retryability semantics, or failure categories.
- Choosing between exceptions, typed errors, result/outcome values, protocol responses, job status records, dead-letter records, or user-facing failure states.
- Mapping unknown exceptions, dependency failures, database constraint failures, timeout/cancellation failures, or validation library errors into safe application errors.
- Designing fallback, graceful degradation, partial success, error aggregation, retry exhaustion, rollback, cleanup, or dead-letter behavior after a failure.
- Deciding what gets shown to users or clients, what gets logged, what gets redacted, and how request/correlation IDs connect reports to diagnostics.

## Do Not Use

Do not use this skill when:

- The problem cause is unknown, a test/build/runtime failure is being diagnosed, or prior fixes failed. Use `structured-problem-resolution` first.
- The task is only to run, configure, or fix formatter/linter/typechecker/static-analysis commands. That belongs to project tooling, CI, coder workflow, or reviewer workflow, not this skill.
- The task is only API style, endpoint design, pagination, versioning, OpenAPI, GraphQL, REST status policy, or client compatibility. Use `api-design`; load this skill only for the error/failure branch.
- The task is only database transaction ownership, constraint design, deadlocks, migrations, or backfills. Use `database-design`; load this skill only for translating database failures into application errors.
- The task is only test design, regression evidence, coverage, mocks, fixtures, or CI evidence. Use `testing-strategy`.
- A project already has a stricter accepted error standard, ADR, public API style guide, framework convention, compliance policy, or generated contract source of truth. Follow that source and use this skill only for gaps.
- The work needs exact library syntax, such as a specific validation framework, web framework, logger, tracing SDK, or language exception API. Verify that syntax against current project dependencies or official docs.

## Iron Law

Error handling is failure contract design, not catch-block decoration. Do not add or accept error handling until the failure source, validation boundary, public contract, private diagnostic path, retry/recovery behavior, redaction policy, and verification evidence are explicit.

## Core Concept

Every failure has at least two audiences: the caller that must decide what to do next, and the operator or maintainer that must diagnose what happened. Good error handling gives each audience enough information without leaking secrets, internal implementation, or accidental control flow. The normal path should stay readable, invalid states should be prevented where possible, and unavoidable failures should be classified, mapped, recovered from or failed safely, logged, and verified deliberately.

## Operating Process

Run these steps in order. Load only the references needed for the current branch.

### 1. Establish Failure Context

Identify the failure surface before choosing a pattern:

- caller or consumer: user, browser UI, public API client, internal service, job runner, CLI caller, queue consumer, operator, agent, or test harness;
- boundary crossed: user input, HTTP/RPC/event/file/config/env/database/cache/third-party response, background job, UI form, command line, scheduler, or internal domain call;
- source of truth: project convention, API/schema, ADR, spec, local code pattern, compliance rule, existing production behavior, or framework contract;
- failure modes: malformed syntax, invalid data, missing data, unauthorized/forbidden action, not found, conflict, dependency failure, timeout, cancellation, quota/rate limit, invariant violation, programmer bug, or unknown exception;
- consequence: user correction, retry, backoff, fallback, degraded mode, partial success, rollback, compensation, dead-lettering, escalation, alerting, support lookup, or fail-fast behavior.

Completion criterion: the design can name who receives the failure, what boundary produced it, what action the receiver can safely take, and where maintainers find the private cause.

Failure output: `Blocked: error-handling design depends on missing failure context: <specific missing fact>.`

### 2. Classify Failure Semantics

Classify the failure by meaning, not by implementation exception name.

Load [Error Taxonomy](references/error-taxonomy.md) when creating, revising, or reviewing categories, codes, retryability, permanence, or public/private fields.

Rules:

- Separate expected business or validation failures from unexpected system failures.
- Separate malformed input from syntactically valid input that violates domain rules when callers need different behavior.
- Separate authentication, authorization, not-found, and disclosure-policy choices deliberately; do not leak resource existence by accident.
- Define disclosure policy for credential validity, authorization failure, ownership failure, and not-found behavior across public messages, status/category choice, validation detail, and timing-sensitive differences.
- Separate retryable/transient failures from permanent failures; never mark validation or authorization failures as retryable.
- Prefer stable, caller-actionable codes over implementation names like ORM errors, SQL constraints, SDK exception classes, or stack frame names.
- Do not create a new code for every message variation. Codes are contract categories; messages and details carry instance context.

Completion criterion: every material failure mode has category, public code, retryability, public visibility, private diagnostic handling, and owner.

Failure output: `Rejected: failure semantics are unclear or implementation-shaped: <specific issue>.`

### 3. Define Runtime Validation Boundaries

Validate data where trust changes or where external facts enter the system.

Load [Runtime Validation](references/runtime-validation.md) when handling user input, request bodies, query params, headers, webhooks, third-party responses, configuration, environment variables, files, cache reads, database outputs, CLI args, or generated artifacts.

Rules:

- Treat external input and external responses as untrusted until parsed and checked.
- Validate shape, type, required fields, bounds, enums, formats, cross-field rules, normalization, and business plausibility where the owning layer has authority.
- Do not rely on TypeScript types, generated clients, UI controls, documentation, or caller promises as runtime validation.
- Do not duplicate validation everywhere. Parse once at the boundary, pass trusted values inward, and keep durable invariants enforced by the owning persistence or policy layer.
- Field-level validation errors should be structured enough for correction, not just a single generic message.
- Never echo secrets or sensitive values in validation messages.

Completion criterion: each boundary states what is parsed, what is normalized, what is rejected, what is allowed through, and how field/domain failures are represented.

Failure output: `Rejected: runtime validation boundary is missing, duplicated, or unsafe: <specific boundary>.`

### 4. Choose Error Shape And Delivery Mechanism

Choose how failures move through the system from caller needs and local conventions.

Load [Error Shapes And Delivery](references/error-shapes.md) when choosing exceptions, typed errors, result/outcome envelopes, response bodies, field errors, CLI exits, job status, dead-letter records, partial success, or user-facing states.

Rules:

- Use the existing project convention when it is safe and accepted.
- Use exceptions for truly exceptional or framework-owned flow when that matches the language/framework; do not use exceptions as routine validation control where a typed result is clearer.
- Use typed results/outcomes when expected failures are normal branches and callers must handle them explicitly.
- Use aggregate or per-item results when multiple independent failures can occur and the caller needs the complete set to correct input or recover work.
- Use one public error shape per boundary unless the protocol or project convention deliberately distinguishes validation, domain, and system failures.
- Keep public error shapes serializable. Do not expose raw `Error` objects, stack traces, dates/objects that cannot cross the target boundary, ORM exceptions, or SDK payloads.
- Include stable code, safe message, optional field/domain details, retry/remediation hints where safe, and request/correlation ID location when available.

Completion criterion: the chosen shape can be serialized across the target boundary and gives the caller one clear handling path.

Failure output: `Rejected: error shape is inconsistent, non-serializable, or not actionable: <specific issue>.`

### 5. Map Exceptions And Lower-Level Failures

Centralize translation from lower-level failure to application meaning.

Load [Exception Mapping](references/exception-mapping.md) when mapping thrown exceptions, validation-library errors, framework errors, database constraint errors, dependency failures, timeouts, cancellations, or unknown failures.

Rules:

- Map known lower-level failures to stable application categories at the boundary that owns the abstraction.
- Preserve private cause, stack, error class/code, dependency name, and correlation context in logs or diagnostics, not in the public error.
- Unknown failures become sanitized generic public errors and detailed private diagnostics.
- Do not swallow exceptions and continue as if work succeeded.
- Do not catch broadly unless the boundary immediately maps, logs or propagates, and preserves enough cause for diagnosis.
- Do not wrap the same failure at every layer; one clear mapping boundary is better than nested generic wrappers.

Completion criterion: known failures have explicit mappings, unknown failures have a safe fallback, and diagnostic cause is preserved privately.

Failure output: `Rejected: exception mapping hides cause, leaks internals, or changes success semantics: <specific issue>.`

### 6. Define Logging, Redaction, And Correlation

Design diagnostics with privacy and support lookup in mind.

Load [Logging And Redaction](references/logging-and-redaction.md) when choosing log fields, log levels, correlation IDs, request IDs, trace IDs, redaction policy, stack traces, support identifiers, or public/private message separation.

Rules:

- User/client messages and logs are different artifacts. User messages must be safe and actionable; logs must be diagnostic and access-controlled.
- Every unexpected or support-relevant failure should be findable by request/correlation/trace/job ID.
- Log enough private context to diagnose cause without logging secrets, credentials, tokens, raw sensitive payloads, signed URLs, internal authorization details, or unnecessary personal data.
- Never log raw credential-bearing headers or values, including `Authorization`, `Cookie`, `Set-Cookie`, API key headers, bearer tokens, session identifiers, OAuth codes, one-time codes, signed URLs, password reset tokens, or webhook secrets.
- Expected validation failures usually do not deserve error-level logs. Unexpected system failures usually do.
- Avoid duplicate logging at every layer. Log once at the boundary with enough context unless local recovery needs an additional event.
- Redaction is a last line of defense, not permission to log raw sensitive values.

Completion criterion: the design states public message policy, private diagnostic fields, log level, correlation behavior, redaction rules, and stack-trace visibility.

Failure output: `Rejected: error diagnostics are missing, overexposed, duplicated, or not traceable: <specific issue>.`

### 7. Define Recovery, Degradation, And Cleanup

Decide whether the failed operation should stop, retry, degrade, aggregate failures, roll back, compensate, dead-letter, or continue with a truthful partial result.

Load [Recovery And Degradation](references/recovery-and-degradation.md) when designing fallback behavior, graceful degradation, partial success, error aggregation, cleanup, retry exhaustion, rollback, compensation, dead-lettering, or circuit-breaker handoff.

Rules:

- Fail fast when continuing would hide corruption, violate an invariant, leak data, or make the caller believe work succeeded.
- Use fallback only when the fallback preserves the contract or clearly communicates degraded/partial behavior.
- Aggregate independent validation or per-item failures when complete feedback is more useful than failing at the first item.
- Do not aggregate dependent failures where the first failure invalidates later work or where continuing would create side effects.
- Release resources and roll back the failed unit deterministically before reporting failure or scheduling retry.
- Circuit breakers, bulkheads, health signals, and operational degradation require observability and production-readiness coordination; do not implement them as isolated catch-block behavior.

Completion criterion: the design states stop/retry/fallback/partial-success behavior, resource cleanup, side-effect safety, and how degraded or terminal state is surfaced.

Failure output: `Rejected: recovery behavior hides failure, changes semantics, or lacks cleanup: <specific issue>.`

### 8. Integrate With The Owning Surface

Apply the general failure design to the concrete surface without weakening local contracts.

Rules:

- APIs: coordinate with `api-design` for protocol status, schema, compatibility, versioning, OpenAPI/GraphQL, and client behavior.
- Databases: coordinate with `database-design` for constraint ownership, transaction rollback, retries, deadlocks, serialization failures, and migration/backfill behavior.
- Tests: coordinate with `testing-strategy` for regression, negative-path, boundary, contract, integration, and manual evidence.
- Architecture: coordinate with `architecture-design` when the error mapping boundary changes ownership across controllers, services, adapters, domain modules, jobs, or infrastructure.
- Operations/observability: follow existing logging/tracing/metrics standards when present; do not invent parallel telemetry conventions inside this skill.

Completion criterion: the error design names the owner module/layer, affected surface, related skill/reference, and any local standard it follows.

Failure output: `Blocked: error-handling ownership or related surface contract is unresolved: <specific conflict>.`

### 9. Verify The Error Design Or Change

Before presenting error-handling work as ready, verify:

- failure context, receiver, boundary, and consequence are explicit;
- validation happens at the right boundary and avoids duplicate or missing checks;
- expected failures are distinguishable from unexpected failures;
- public codes/messages/details are stable, safe, and actionable;
- authentication, authorization, not-found, and rate-limit failures follow the chosen disclosure policy and do not reveal credential validity, resource existence, ownership internals, or unsafe quota details;
- private diagnostics preserve cause without leaking sensitive data;
- retryability, idempotency, fallback, degraded mode, partial success, aggregation, rollback, compensation, cleanup, or dead-letter behavior is defined where relevant;
- unknown exceptions become sanitized public failures and diagnosable private records;
- log levels, correlation IDs, and redaction rules match project convention;
- tests or review evidence cover happy path plus validation, domain, dependency, timeout, permission, fallback/degraded mode, cleanup, and unexpected-failure paths where relevant.

Completion criterion: the output can show the public failure contract, private diagnostic path, and verification evidence.

Failure output: `Not done: error-handling evidence is missing or unsafe: <specific gap>.`

## Reference Routing

| Need                                                                                                     | Reference                                                          |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Validation at input, config, dependency, file, cache, DB, CLI, or generated-artifact boundaries          | [Runtime Validation](references/runtime-validation.md)             |
| Error categories, codes, permanence, retryability, public/private fields                                 | [Error Taxonomy](references/error-taxonomy.md)                     |
| Exceptions vs typed results, envelopes, response bodies, CLI/job/event failure shapes                    | [Error Shapes And Delivery](references/error-shapes.md)            |
| Mapping lower-level exceptions, dependency failures, validation-library failures, and unknown errors     | [Exception Mapping](references/exception-mapping.md)               |
| Fallbacks, graceful degradation, error aggregation, cleanup, rollback, compensation, dead-letter records | [Recovery And Degradation](references/recovery-and-degradation.md) |
| Logging, redaction, correlation IDs, stack traces, support lookup, public/private message split          | [Logging And Redaction](references/logging-and-redaction.md)       |
| Testing or improving this skill                                                                          | [Pressure Tests](references/pressure-tests.md)                     |

## Rationalization Table

| Temptation                                                     | Reality                                                                                        | Required action                                                               |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| "Just add a try/catch."                                        | Catching without classification often hides the real bug or changes success semantics.         | Classify the failure and decide mapping, logging, and propagation first.      |
| "The type system already validates this."                      | Compile-time types do not validate untrusted runtime input or external responses.              | Validate at trust boundaries and pass parsed values inward.                   |
| "Return the raw error so clients have details."                | Raw errors leak internals and create unstable public contracts.                                | Return stable public codes/messages and keep private cause in diagnostics.    |
| "Everything can use one envelope."                             | A universal envelope can fight protocol semantics, framework behavior, or existing contracts.  | Choose shape per boundary and follow accepted local convention.               |
| "Log everything just in case."                                 | Overlogging leaks data, creates noise, and hides the useful signal.                            | Log structured diagnostic context once at the right boundary with redaction.  |
| "Validation errors are errors, so log them as errors."         | Expected user-correctable failures are often not operational errors.                           | Choose log level by operational significance and abuse/security needs.        |
| "Unknown failures can use the same message as known failures." | Unknown failures need sanitized public output and richer private diagnostics.                  | Map unknowns to generic public errors with correlation support.               |
| "Fallback means the error is handled."                         | A fallback can silently corrupt semantics or hide incidents if it is not truthful and visible. | Define degraded semantics, diagnostics, and verification before accepting it. |

## Red Flags

- Error handling is described only as catch blocks, wrappers, or middleware with no failure taxonomy.
- Public messages include stack traces, SQL/ORM details, SDK payloads, file paths, hostnames, tokens, credentials, signed URLs, or raw sensitive values.
- Validation occurs only in the UI, caller, generated type, or documentation.
- Internal exception names become public error codes.
- Retry behavior is implied but not bounded, idempotent, or classified by failure permanence.
- The same error is logged at multiple layers without adding useful context.
- A broad catch returns success, suppresses rollback, or loses diagnostic cause.
- Fallback or graceful degradation returns stale, incomplete, or substitute data without making the changed semantics visible.
- Multi-item validation stops at the first independent error when the caller needs the complete correction set.
- Field validation errors are collapsed into one vague message when callers need correction details.
- The design changes an API, database, architecture, or test contract without loading the owning skill/reference.
- Verification covers only the happy path or only a generic failure.

## Output Contract

When designing or reviewing error handling, produce:

```markdown
Failure context:
Boundary and receiver:
Validation behavior:
Failure taxonomy:
Public contract:
Private diagnostics:
Exception mapping:
Retry/rollback/recovery:
Logging/redaction/correlation:
Verification evidence:
Residual risk:
```

When reviewing an implementation, lead with findings:

```markdown
Findings:

- <severity> <area>: <failure-contract risk and evidence>

Error-contract assessment:
Diagnostics/redaction assessment:
Verification gaps:
Recommended correction:
```

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when testing or improving this skill.
