# Runtime Validation

Use this reference when data crosses a trust boundary or when runtime data can be wrong despite compile-time types.

## Boundary Rule

Validate at the first owned boundary where the system can reject, normalize, or quarantine bad data with enough context.

Common validation boundaries:

- user input: forms, commands, uploaded files, free text, query params, headers, cookies, JSON bodies;
- integration input: webhooks, third-party responses, SDK results, message queues, event payloads, emails, files, scraped data;
- configuration: environment variables, config files, feature flags, secrets metadata, deployment settings, optional provider credentials, local preference files, and destination/sink settings;
- persistence and cache: database reads when schema drift or adapter shape is not guaranteed, cache reads, serialized blobs, imported data;
- generated artifacts: codegen outputs, schema-derived clients, migration manifests, agent-produced JSON or markdown consumed by tools, reports consumed by automation, and structured output from language-model or provider calls.

Evidence artifacts are not automatically trusted input. Logs, reports, screenshots, transcripts, review comments, issue text, and bot output can describe symptoms, but the error contract still needs current code, accepted contract, policy, and runtime boundary verification.

## Validation Layers

Use the narrowest owner that has the authority to decide the rule:

| Rule Type                        | Owner                                                                     | Examples                                                                               |
| -------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Syntax and shape                 | boundary adapter, parser, controller, command parser                      | JSON parses, required fields, enum value, string/number/boolean shape                  |
| Format and normalization         | boundary adapter or domain-owned normalizer                               | email casing, phone formatting, URL parsing, timezone normalization                    |
| Cross-field consistency          | domain input model or policy module                                       | start before end, country/postal-code pairing, mutually exclusive fields               |
| Authorization-relevant input     | authorization/policy boundary                                             | tenant ID, account ID, object ownership, requested scope                               |
| Durable invariants               | persistence or domain aggregate plus database constraints where available | uniqueness, foreign keys, balance cannot go negative, valid state transition           |
| Dependency response plausibility | dependency adapter                                                        | content type, expected status, payload schema, required ID, checksum, pagination token |
| Tool/config readiness            | command, setup, or integration boundary                                   | missing provider token, expired auth, ambiguous project root, invalid sink, unsupported mode |
| Generated artifact contract      | artifact producer or consumer boundary                                    | parseable JSON, required section, source coverage, no-data state, partial-result marker |

Do not use one validation layer as an excuse to skip another owner. UI validation improves user experience; server validation protects the system. Database constraints protect durability; domain validation produces caller-actionable failures.

## Validation Failure Shape

Field-level failures are needed when the caller can correct specific input.

Each field/domain failure should define:

- path or field name in the caller's contract language;
- machine-readable validation code;
- safe message;
- expected constraint when useful;
- rejected value only when safe to echo;
- whether the failure is malformed syntax, missing data, invalid shape, invalid format, domain rule failure, or authorization-sensitive rejection.

Do not include secrets, raw tokens, credentials, signed URLs, raw files, internal identifiers that reveal unauthorized resources, stack traces, SQL/ORM details, or dependency payloads in validation messages.

For config, tool, provider, and generated-artifact validation:

- distinguish missing, invalid, expired, ambiguous, unsupported, unauthenticated, unauthorized, malformed response, source skipped, source failed, no data, and partial result states;
- validate provider output with a structured parser or schema when automation consumes it; do not mine prose for contract-critical fields when a structured format is available;
- report field/path names in the consumer's contract language, not provider internals, unless the consumer is an operator diagnostic surface;
- redact secrets and sensitive provider commentary from both public validation output and generated artifacts;
- preserve source/item identity for partial reports, batch results, and multi-source artifacts.

Failure output: `Rejected: generated or provider output validation is missing or prose-derived: <specific boundary>.`

## Evidence Grounding

When validation work starts from feedback, review comments, screenshots, logs, reports, transcripts, or generated artifacts:

- separate observed facts from inferred cause, inferred owner, and proposed fix;
- label owner confidence when the boundary is inferred rather than proven;
- verify current code, accepted schema, local convention, or official dependency docs before accepting the artifact's interpretation;
- treat stale reports, old screenshots, copied logs, and bot-generated summaries as context, not source truth;
- block when the missing current evidence changes public message, retryability, redaction, fallback, or cleanup.

Failure output: `Blocked: validation evidence is not current enough to define the failure contract: <specific gap>.`

## Unknown And Extra Fields

Choose behavior deliberately:

- reject unknown fields for strict contracts, security-sensitive writes, public APIs with generated clients, or inputs where mass assignment is a risk;
- ignore/strip unknown fields when forward compatibility is required and the project convention supports it;
- preserve unknown fields only when they are intentionally part of the contract, such as metadata passthrough or webhook/event extension fields.

Failure output: `Rejected: unknown-field behavior is accidental or unsafe: <specific input>.`

## Normalization

Normalize only when the rule is stable and owned by the current boundary or domain:

- case folding before uniqueness checks;
- trimming whitespace when whitespace has no semantic meaning;
- parsing dates/times into explicit timezone policy;
- canonicalizing IDs, URLs, phone numbers, or emails only under accepted local rules.

Do not normalize away meaningful user input, security-sensitive values, identifiers from another authority, or legally/audit-relevant raw data unless raw and normalized values have a documented storage/audit policy.

## Validation Anti-Patterns

- Casting raw input to a trusted type.
- Trusting generated clients or TypeScript types as runtime validation.
- Re-validating the same parsed value in every layer with inconsistent rules.
- Returning only `"invalid input"` when callers need field-level correction.
- Echoing raw secret or sensitive input in error messages.
- Creating schemas or validators in hot paths when the language/tool allows stable definitions.
- Using validation as authorization or authorization as validation.
- Trusting provider, agent, report, or generated markdown output without structured validation when downstream automation relies on it.
- Recommending exact validation-library issue shapes, coercion behavior, unknown-field defaults, or error formatting from memory instead of current dependency behavior.

## Validation Checklist

- Boundary is named.
- Source data is treated as untrusted until parsed.
- Owner of each rule is clear.
- Unknown-field behavior is explicit.
- Normalization policy is explicit.
- Field/domain failures have safe structured details.
- Secrets and sensitive values are not echoed.
- Durable invariants are enforced by the owning layer, not only by caller-side checks.
- Config/tool/generated-artifact boundaries distinguish absence, ambiguity, invalidity, skipped sources, partial results, and terminal failures.
- Exact validator behavior is verified against current dependencies or official docs when syntax, issue shape, or defaults matter.
