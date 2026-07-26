# Error Handling Design Runtime Boundary Report

Owner: `error-handling-design`

Checkpoint: CP-002

Fixture ID: CP2-ERR-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` version 0.4. The target result record was appended after the target run completed.

Runtime skill entry point: `skills/error-handling-design/SKILL.md`

Evaluator suite: `evals/skills/error-handling-design/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one path — trigger basis per selected operational reference, or none applicable>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply error-handling-design to define an error taxonomy and public HTTP error shape for request validation failures, including sanitized structured logging. No infrastructure exception mapping, retry, fallback, or degraded-mode behavior is in scope. Do not edit files.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/error-handling-design/references/error-taxonomy.md`
- `skills/error-handling-design/references/error-shapes.md`
- `skills/error-handling-design/references/runtime-validation.md`
- `skills/error-handling-design/references/logging-and-redaction.md`

Expected unselected operational references:

- `skills/error-handling-design/references/exception-mapping.md`
- `skills/error-handling-design/references/recovery-and-degradation.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/error-handling-design/ or none>
Selector basis: <one path — trigger basis per selected operational reference, or none applicable>
```

## PASS Criteria

- `References read` reports exactly the expected selected operational references and no expected unselected operational references.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for each selected operational reference.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, or the checkpoint summary.
- Target reports no file edits.

## Target Result Record

Target run status: `COMPLETED`

Target source identity: ephemeral read-only Codex session `019f99ea-23d6-77a1-8760-87862e45902a`

Target output:

````text
## Conclusion

Assume a greenfield HTTP contract; an existing accepted API standard overrides field names and status choices.

**Boundary and receiver:** Validate body, query, path, and relevant headers at HTTP ingress. Parse once, aggregate independent failures, and pass only trusted normalized values inward. Normalization and unknown-field behavior must be explicit in each request schema.

**Taxonomy:**

| HTTP | Public code | Meaning |
|---|---|---|
| 400 | `MALFORMED_REQUEST` | Request cannot be parsed or has an invalid structural shape. |
| 422 | `INVALID_INPUT` | Parsed request contains caller-correctable field, cross-field, or domain validation failures. |

Structured detail codes: `MISSING_REQUIRED_FIELD`, `INVALID_TYPE`, `INVALID_FORMAT`, `OUT_OF_RANGE`, `UNKNOWN_FIELD`, and `DOMAIN_RULE_VIOLATION`. These failures are expected, non-retryable with the unchanged request, and owned by the request-validation boundary.

**Public HTTP shape:**

```json
{
  "error": {
    "category": "validation",
    "code": "INVALID_INPUT",
    "message": "Request validation failed.",
    "details": [
      {
        "path": "email",
        "code": "INVALID_FORMAT",
        "message": "Must be a valid email address.",
        "constraint": "email"
      }
    ],
    "requestId": "req_01..."
  }
}
```

`details` may be omitted for unparseable requests. Paths use public contract names. Messages and constraints must be stable and safe. Rejected values are omitted by default; never expose request fragments, credentials, authorization facts, internal identifiers, stack traces, validator internals, or implementation names.

**Sanitized structured logging:** Emit one event at the HTTP boundary, correlated with the response’s server-generated or strictly validated `requestId`:

```json
{
  "event": "http.request.validation_failed",
  "request_id": "req_01...",
  "method": "POST",
  "route_template": "/users",
  "http_status": 422,
  "error_code": "INVALID_INPUT",
  "validation_codes": ["INVALID_FORMAT"],
  "field_paths": ["email"],
  "error_count": 1
}
```

Use `info` for ordinary validation rejection and `warn` or dedicated security telemetry only for suspicious or abusive patterns; do not use `error` for expected caller-correctable failures. Never log raw bodies, query strings, full URLs, rejected values, cookies, authentication headers, tokens, signed URLs, sensitive headers, personal data, or validator stack traces. Allowlist fields, log route templates rather than raw URLs, and avoid duplicate logging.

Verification must cover malformed input, multiple independent field failures, deterministic safe details, absence of sensitive values in both response and captured logs, matching response/log correlation IDs, appropriate log severity, and exactly one diagnostic event per rejection.

References read: skills/error-handling-design/references/error-taxonomy.md, skills/error-handling-design/references/runtime-validation.md, skills/error-handling-design/references/error-shapes.md, skills/error-handling-design/references/logging-and-redaction.md
Evaluator assets read: none
Selector basis: skills/error-handling-design/references/error-taxonomy.md — taxonomy and public codes requested; skills/error-handling-design/references/runtime-validation.md — request validation boundary requested; skills/error-handling-design/references/error-shapes.md — public HTTP error shape requested; skills/error-handling-design/references/logging-and-redaction.md — sanitized structured logging requested
````

Reported audit lines:

```text
References read: skills/error-handling-design/references/error-taxonomy.md, skills/error-handling-design/references/runtime-validation.md, skills/error-handling-design/references/error-shapes.md, skills/error-handling-design/references/logging-and-redaction.md
Evaluator assets read: none
Selector basis: skills/error-handling-design/references/error-taxonomy.md — taxonomy and public codes requested; skills/error-handling-design/references/runtime-validation.md — request validation boundary requested; skills/error-handling-design/references/error-shapes.md — public HTTP error shape requested; skills/error-handling-design/references/logging-and-redaction.md — sanitized structured logging requested
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: target-reported/procedural read evidence, not filesystem capability isolation.
