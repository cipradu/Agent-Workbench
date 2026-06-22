# Runtime Validation

Use this reference when data crosses a trust boundary or when runtime data can be wrong despite compile-time types.

## Boundary Rule

Validate at the first owned boundary where the system can reject, normalize, or quarantine bad data with enough context.

Common validation boundaries:

- user input: forms, commands, uploaded files, free text, query params, headers, cookies, JSON bodies;
- integration input: webhooks, third-party responses, SDK results, message queues, event payloads, emails, files, scraped data;
- configuration: environment variables, config files, feature flags, secrets metadata, deployment settings;
- persistence and cache: database reads when schema drift or adapter shape is not guaranteed, cache reads, serialized blobs, imported data;
- generated artifacts: codegen outputs, schema-derived clients, migration manifests, agent-produced JSON or markdown consumed by tools.

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

## Validation Checklist

- Boundary is named.
- Source data is treated as untrusted until parsed.
- Owner of each rule is clear.
- Unknown-field behavior is explicit.
- Normalization policy is explicit.
- Field/domain failures have safe structured details.
- Secrets and sensitive values are not echoed.
- Durable invariants are enforced by the owning layer, not only by caller-side checks.
