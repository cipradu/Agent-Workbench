# Error Shapes And Delivery

Use this reference when deciding how failures are represented and delivered across a boundary.

## Shape Selection

Choose the shape from caller needs, protocol, and project convention.

| Shape                            | Use When                                                                                               | Watch For                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Exception                        | Framework/language expects thrown failures, failure is exceptional, or control exits the current stack | Do not throw for ordinary validation branches when explicit results are clearer             |
| Typed result/outcome             | Expected failures are normal branches and callers must handle success/failure explicitly               | Do not hide protocol status or force every low-level helper into noisy envelopes            |
| Protocol response                | HTTP/RPC/GraphQL/event/CLI boundary needs serialized public contract                                   | Keep protocol semantics and body semantics aligned                                          |
| Field/domain error list          | Caller can correct specific input or business rule violation                                           | Avoid leaking forbidden fields or unauthorized resource details                             |
| Aggregate error/result           | Multiple independent validation, preflight, or item-level failures should be reported together         | Preserve item/field identity and keep top-level success/failure unambiguous                 |
| Partial-success result           | Batch, bulk, sync, import, or multi-item operation can succeed partially                               | Define per-item identity, ordering, idempotency, rollback, and retry behavior               |
| Job status or dead-letter record | Async job, queue, scheduler, workflow, or import needs durable failure state                           | Include retry count, terminal status, safe reason, private cause pointer, and recovery path |
| UI state                         | User-facing workflow needs displayable recovery guidance                                               | Do not bind UI wording to raw backend exception text                                        |
| CLI exit code plus stderr/stdout | Script or command-line tool is consumed by humans and automation                                       | Keep machine-readable output separate from human diagnostics when needed                    |
| Sentinel/result state            | Local tools, agents, reports, or pipelines need non-exceptional residual states                        | Distinguish skipped, no data, no sink, deferred, partial, blocked, and failed outcomes      |

## Common Public Shape Fields

Use local convention first. A generic public shape often includes:

- stable machine-readable code;
- safe human-readable message;
- category/type if useful;
- field/domain details for corrective failures;
- retry/remediation hint when true and safe;
- request/correlation/support ID;
- documentation link only when stable and maintained.

Do not require a universal envelope across all projects or protocols. A direct data response with structured errors can be correct. An envelope can be correct. Problem Details-style responses can be correct. GraphQL payload errors can be correct. The design must fit the boundary and existing contract.

## Result Or Envelope Rules

When using result/outcome/envelope shapes:

- make success and failure variants structurally distinguishable;
- do not require callers to infer failure from a nullable data field;
- do not include both success data and failure details unless partial success is explicitly designed;
- avoid wrapping protocol no-content responses where the protocol already has a clear meaning;
- keep payload serializable across the target boundary;
- include the same correlation/request/support ID location consistently.

Failure output: `Rejected: result shape makes success/failure ambiguous: <specific shape>.`

## Field And Domain Errors

Field errors are for caller-correctable input. Domain errors are for valid input that violates state or policy.

Field error example structure, adapted to local convention:

```text
field/path:
code:
message:
constraint:
safe rejected value:
```

Domain error example structure, adapted to local convention:

```text
code:
message:
reason:
affected domain object:
remediation:
```

Do not expose field details that let unauthorized callers enumerate resources, infer hidden fields, or learn authorization rules.

## Partial Success

Bulk and async workflows need explicit failure semantics:

- all-or-nothing, best-effort, or per-item commit behavior;
- per-item identity used to correlate results;
- ordering guarantees;
- retry behavior for failed items;
- duplicate detection or idempotency;
- rollback or compensation behavior;
- terminal and retryable status values;
- dead-letter and manual recovery path.

Failure output: `Blocked: partial failure semantics are missing for multi-item operation: <operation>.`

## Generated Reports And Artifacts

Generated artifacts and reports can look complete while hiding missing or failed sources. Their shape must make changed semantics visible.

Define:

- source identity and source coverage;
- `no data` versus `not configured` versus `instrumentation pending`;
- source skipped by scope, cost, permission, or mode;
- source attempted and failed;
- partial output and which sections/items are affected;
- blocked output when a required credential, decision, safety condition, or sink is missing;
- private diagnostic pointer for failed or skipped sources when support needs investigation;
- public omission and redaction rules for sensitive raw inputs, provider payloads, transcripts, screenshots, prompts, and internal commentary.

Do not let a polished artifact imply success when required data is absent, stale, unparseable, skipped, or failed.

Failure output: `Rejected: generated artifact hides missing, skipped, failed, or partial source state: <specific source>.`

## Aggregate Errors

Aggregate errors are useful when multiple independent failures can be discovered without unsafe side effects and the receiver benefits from fixing them together.

Rules:

- aggregate validation, preflight, import, and per-item failures only when checks are independent;
- include field/path or item identity for each failure;
- keep per-error codes stable and safe;
- preserve a top-level failure or partial-success status so callers cannot mistake aggregate errors for full success;
- stop instead of aggregating when the first failure invalidates later work, continuing would trigger unsafe side effects, or later errors would leak authorization-sensitive information.

Failure output: `Rejected: aggregate error shape is ambiguous or unsafe: <specific issue>.`

## CLI And Automation Output

For commands and automation:

- exit status must match success/failure;
- stderr should carry human-readable diagnostics;
- stdout should stay machine-readable when automation consumes it;
- sensitive values must be redacted from both streams;
- error output should include enough context to find logs or rerun safely;
- usage errors, validation errors, operational failures, and internal bugs should be distinguishable.
- non-interactive mode must not block on prompts; return a structured blocked state or actionable failure instead;
- manual mode may include next-action guidance, but automation still needs deterministic status, code, or sentinel output;
- a missing sink, skipped destination, deferred write, or partial publish is not full success unless the contract explicitly defines it that way;
- stdout/stderr separation is a contract when downstream tools parse stdout.

## Runtime Evidence Boundaries

Browser checks, UI smoke tests, screenshots, simulator logs, transcripts, and dogfood reports can verify that a user-facing branch is observable. They do not prove:

- raw exceptions are not leaked elsewhere;
- private diagnostics preserve cause;
- logs are redacted;
- retries are idempotent and bounded;
- cleanup or rollback happened;
- correlation IDs connect public output to private diagnostics;
- fallback or partial success is truthful in every caller mode.

Pair runtime evidence with contract, mapper, log/redaction, recovery, and negative-path evidence for the claims being made.

## Shape Checklist

- Shape follows local convention or documents why a new shape is needed.
- Success and failure are unambiguous.
- Public fields are stable and safe.
- Field/domain details are corrective where useful.
- Aggregate errors preserve independent item/field identity.
- Partial success has explicit retry and recovery behavior.
- CLI/job/event/API/UI delivery matches the caller's handling needs.
- Generated artifacts make missing, skipped, partial, blocked, failed, and no-sink states explicit.
- Human and automation modes have compatible but distinct diagnostics and machine-readable outcomes.
