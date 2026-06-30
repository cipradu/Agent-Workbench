# Logging And Redaction

Use this reference when defining what gets logged, what gets shown, what gets redacted, and how failures are correlated.

## Public Message Versus Private Diagnostic

Keep public messages and private diagnostics separate.

Public messages should be:

- safe for the receiver;
- concise and actionable where possible;
- stable enough for support and client behavior;
- free of secrets, stack traces, implementation internals, and raw sensitive payloads.

Private diagnostics should be:

- structured;
- correlated to the request/job/trace/user action where policy permits;
- detailed enough to diagnose cause;
- access-controlled by the logging/error-reporting system;
- redacted by policy and by field choice.

Generated artifacts, reports, support excerpts, review packets, screenshots, transcripts, and provider outputs can become public or widely shared artifacts. Treat them as public unless access control is explicit and verified. Include only safe summaries, redacted identifiers, and correlation pointers; keep raw payloads, internal commentary, prompts, stack traces, and provider diagnostics in private systems.

## Correlation

Every support-relevant failure should connect public output to private diagnostics.

Use project convention for:

- request ID;
- correlation ID;
- trace/span ID;
- job/workflow/import ID;
- tenant/account/user ID where allowed;
- support ticket or incident ID where applicable.

If no convention exists, do not invent a full observability system in this skill. State the minimum needed for the current boundary: a generated request/job/support identifier in public output and the same identifier in logs.

Failure output: `Blocked: support-relevant failure has no correlation path: <surface>.`

For generated reports and automation, correlation may be a report ID, run ID, job ID, source ID, provider request ID, or artifact path plus timestamp. The public artifact should name the support-safe identifier, not embed private logs.

## Log Levels

Choose level by operational significance, not by whether the code path returns an error object.

Common guidance:

- debug: diagnostic detail useful during development or targeted troubleshooting;
- info: expected state transitions or completed recovery with low operational concern;
- warn: expected but noteworthy failure, validation abuse pattern, retryable dependency issue, degraded mode, or recoverable inconsistency;
- error: unexpected failure, failed unit of work, exhausted retry, lost work, invariant violation, or user-impacting dependency failure;
- critical/fatal: process cannot safely continue or core service is unavailable.

Expected user validation failures often do not deserve error logs. Security abuse, repeated malformed traffic, and operational anomaly patterns may deserve warn or security telemetry even when the public response is a validation error.

Startup, setup, dev-server, local-tool, or provider-auth diagnostics are examples of failure surfaces, not proof that the application contract is safe. Treat them like other diagnostics: redact values, include correlation where useful, and avoid turning environmental details into public user-facing messages.

## Redaction Rules

Prefer not collecting sensitive values over collecting and redacting them.

Never log:

- passwords, password reset tokens, API keys, API key headers, `Authorization`, `Cookie`, `Set-Cookie`, bearer tokens, session identifiers, session cookies, private keys, certificates, OAuth codes, one-time passcodes, webhook signing secrets;
- signed URLs or full URLs containing credentials or private tokens;
- raw payment, health, legal, personal, or customer-confidential payloads unless project policy explicitly allows and protects them;
- plaintext secrets from configuration, environment variables, files, or secret managers;
- authorization rule internals that help unauthorized callers enumerate resources.

Be careful with:

- email addresses, phone numbers, names, addresses, IDs, IPs, device IDs, tenant/account IDs, file paths, filenames, query strings, request bodies, provider payloads, generated prompts, and agent transcripts.

When values are needed for diagnosis, prefer stable hashes, truncated identifiers, classification labels, counts, sizes, status codes, provider request IDs, or explicitly approved identifiers.

For generated or review artifacts:

- do not include raw logs beyond the smallest necessary excerpt;
- redact secrets, tokens, signed URLs, cookies, credential-bearing headers, and private paths before sharing;
- avoid provider/internal commentary that reveals prompts, policy internals, moderation details, hidden fields, billing secrets, or customer-confidential payloads;
- summarize failure categories and counts when raw rows are not necessary;
- preserve source/item identity only at the granularity the receiver is authorized to see.

For authentication and authorization diagnostics:

- Log the credential type, failure category, route/operation, trusted principal when known, tenant/account scope when policy permits, and correlation ID.
- Do not log raw credential material, parsed token claims that contain sensitive values, authorization policy internals, or resource ownership details that would help an unauthorized caller enumerate the system.
- Track suspicious patterns as security telemetry when the project has that channel; otherwise use structured warning logs with redacted fields and clear correlation.

## Stack Traces And Cause Chains

Stack traces are private diagnostics, not public messages.

Rules:

- include stack traces for unexpected failures in development, error reporting, or restricted logs when allowed;
- omit stack traces from user/client output;
- preserve cause chains where the language/runtime supports them;
- avoid rethrowing in a way that destroys the original stack/cause;
- avoid logging the same stack at every layer.

## Duplicate Logging

Log once at the boundary that has the most useful context unless local recovery needs a separate event.

Duplicate logging is justified when:

- an adapter logs dependency-level telemetry and a service logs business failure after retries are exhausted;
- a job logs each retry attempt at low severity and terminal failure at higher severity;
- a fallback/degraded-mode event is recorded separately from the terminal failure because it represents a user-visible or operator-relevant state change;
- security telemetry records abuse signals separately from application logs.

Duplicate logging is not justified when every catch block logs the same exception and rethrows it unchanged.

## Public Artifact Boundary

Before writing an error into a public artifact, generated report, README, docs page, issue comment, PR body, review packet, or user-visible transcript, decide whether the receiver needs:

- the public code/message only;
- a redacted diagnostic summary;
- a support/correlation ID;
- source coverage or partial-output state;
- a private-log pointer for maintainers.

Do not paste private stack traces, raw payloads, secrets, provider bodies, or internal authorization facts into public artifacts to make the finding look more evidenced.

Failure output: `Rejected: public artifact includes private diagnostic material: <specific field>.`

## Logging Checklist

- Public message is safe and distinct from private diagnostic.
- Correlation path exists.
- Log level matches operational significance.
- Sensitive fields are not collected or are redacted by design.
- Stack traces stay private.
- Logging happens at the right boundary without noisy duplication.
- Fallbacks, degraded mode, retry exhaustion, and dead-lettering are visible when they matter operationally.
- Security/audit needs are covered by project policy, not improvised in error messages.
- Generated artifacts and review packets preserve public/private separation and correlation without embedding private logs.
