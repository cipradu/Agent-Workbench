# API Design Runtime Boundary Report

Owner: `api-design`

Checkpoint: CP-002

Fixture ID: CP2-API-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` version 0.4. The target result record was appended after the target run completed.

Runtime skill entry point: `skills/api-design/SKILL.md`

Evaluator suite: `evals/skills/api-design/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one path — trigger basis per selected operational reference, or none applicable>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply api-design to design a backward-compatible REST endpoint for creating payment intents. The accepted project standard already requires REST. Define REST resources and status behavior, public error and validation shape, idempotency and compatibility behavior, an OpenAPI 3.1 contract, and API-boundary abuse controls. Do not edit files.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/api-design/references/rest.md`
- `skills/api-design/references/errors.md`
- `skills/api-design/references/versioning-compatibility.md`
- `skills/api-design/references/openapi.md`
- `skills/api-design/references/security-and-abuse.md`

Expected unselected operational references:

- `skills/api-design/references/api-style.md`
- `skills/api-design/references/graphql.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/api-design/ or none>
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

Target source identity: `/root/cp2_api_target`

Target output:

````text
Conclusion: Add `PaymentIntent` as a new resource in the existing REST version. The proposed contract is backward-compatible because it adds new operations without changing existing ones. It assumes independently deployed authenticated clients, bearer authentication, and a multi-tenant/object-scoped trust boundary; those assumptions must be reconciled with the project’s actual auth and contract authority before implementation.

### Resource and status behavior

- `POST /v1/payment-intents` creates one intent. `Idempotency-Key` is required.
- `GET /v1/payment-intents/{payment_intent_id}` retrieves the durable result and current lifecycle status. This supports recovery after timeouts or connection loss.
- A successful create returns `201 Created`, the direct `PaymentIntent` representation, and `Location`.
- The initial status is `requires_payment_method` when no payment method is supplied, otherwise `requires_confirmation`. Expected later lifecycle outcomes remain resource states, not HTTP errors.
- Known status values are `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `requires_capture`, `succeeded`, and `canceled`. The response schema deliberately leaves the string open; clients must tolerate unknown future values.
- `200` is used for retrieval. `202` is not used: once the resource is durably created, creation returns `201`, even if downstream payment work is still `processing`.
- Semantic validation failure returns `422` and creates no resource. Malformed JSON/header syntax returns `400`; unsupported media type returns `415`.
- Invalid authentication returns `401`; missing operation permission returns `403`; unauthorized referenced objects and cross-tenant retrieval return `404` to avoid existence disclosure.
- Idempotency conflicts return `409`; pressure returns `429`; temporary dependency unavailability before durable creation returns `503`; unexpected failures return sanitized `500`.
- All responses include `X-Request-Id`. Payment responses include `Cache-Control: no-store`.

The request accepts only `amount`, `currency`, `customer_id`, `payment_method_id`, `capture_method`, and `merchant_reference`. It rejects unknown properties. `amount` is an integer in minor currency units; `currency` is an uppercase ISO-4217 code drawn from the server’s supported allowlist. IDs are opaque and must not be parsed by clients. Ownership, tenant, status, timestamps, provider identifiers, and authorization fields are server-owned. Raw card or bank credentials are never accepted.

### Public error and validation shape

Use `application/problem+json` with:

```json
{
  "type": "urn:problem:invalid-payload",
  "title": "Request validation failed",
  "status": 422,
  "code": "INVALID_PAYLOAD",
  "detail": "One or more fields are invalid.",
  "instance": "/v1/payment-intents",
  "request_id": "req_01J...",
  "errors": [
    {
      "path": "/amount",
      "code": "OUT_OF_RANGE",
      "message": "amount must be between 1 and 999999999."
    }
  ]
}
```

`code` and field error codes are stable public identifiers. Field paths use JSON Pointer. Rejected values are not echoed. Authentication, authorization, resource-existence, processor, database, stack, token, and upstream payload details are never exposed. Representative public codes are `INVALID_JSON`, `INVALID_HEADER`, `AUTHENTICATION_REQUIRED`, `FORBIDDEN`, `NOT_FOUND`, `INVALID_PAYLOAD`, `UNSUPPORTED_CURRENCY`, `PAYMENT_METHOD_UNUSABLE`, `IDEMPOTENCY_KEY_REUSED`, `IDEMPOTENCY_IN_PROGRESS`, `RATE_LIMITED`, `SERVICE_UNAVAILABLE`, and `INTERNAL_ERROR`.

### Idempotency and compatibility

- Scope the key to authenticated principal, tenant, method, canonical path, and canonical request hash.
- Accept 16–255 characters matching `[A-Za-z0-9._:-]+`; store and log only a digest where practical.
- Reserve the key only after authentication, syntax, and semantic validation succeed. Pre-execution `400`, `401`, `403`, `415`, `422`, and `429` failures are definite no-ops and are not replay-cached.
- Store the key, request hash, resource ID, and response for at least seven days after execution begins.
- Same key and same request replays the original `201` body and `Location`, with `Idempotency-Replayed: true`.
- Same key with a different request returns `409 IDEMPOTENCY_KEY_REUSED`.
- A concurrent replay while the first request is unresolved returns `409 IDEMPOTENCY_IN_PROGRESS` with `Retry-After`.
- After a connection loss, timeout, or ambiguous `5xx`, clients must resend the identical request with the same key. The server must either replay the committed intent or safely continue the reserved operation; it must not create another intent.
- A newly added endpoint, optional response fields, and new problem codes for new cases are additive. Existing field types, meanings, status mappings, and error meanings cannot change inside `v1`.
- Clients must ignore unknown response properties and unknown `status` values. Request properties remain closed to prevent mass assignment; deployments must update servers before sending new request fields.
- Removal, field renaming, closed-enum changes, or status/error semantic changes require a new API version or a documented deprecation and sunset migration.
- There are no overwrite races in this create/read contract. Future mutable operations must define `ETag`/`If-Match` or explicit transition conflicts rather than silent last-write-wins.

### OpenAPI 3.1 contract

```yaml
openapi: 3.1.0
info:
  title: Payments API
  version: 1.0.0
paths:
  /v1/payment-intents:
    post:
      operationId: createPaymentIntent
      tags: [PaymentIntents]
      summary: Create a payment intent
      description: >
        Creates a durable payment intent. The operation requires an
        Idempotency-Key. Replaying an identical request with the same key
        returns the original result.
      security:
        - bearerAuth: []
      parameters:
        - $ref: "#/components/parameters/IdempotencyKey"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreatePaymentIntentRequest"
            example:
              amount: 2500
              currency: USD
              customer_id: cus_01JABC
              payment_method_id: pm_01JABC
              capture_method: automatic
              merchant_reference: order-1042
      responses:
        "201":
          description: Payment intent created or idempotently replayed
          headers:
            Location:
              description: Canonical URI of the payment intent
              required: true
              schema:
                type: string
                format: uri-reference
            X-Request-Id:
              $ref: "#/components/headers/RequestId"
            Idempotency-Replayed:
              description: Present and true when this is a replay
              schema:
                type: boolean
            Cache-Control:
              $ref: "#/components/headers/NoStore"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PaymentIntent"
              example:
                id: pi_01JABC
                object: payment_intent
                amount: 2500
                currency: USD
                customer_id: cus_01JABC
                payment_method_id: pm_01JABC
                capture_method: automatic
                merchant_reference: order-1042
                status: requires_confirmation
                created_at: "2026-07-25T15:00:00Z"
                updated_at: "2026-07-25T15:00:00Z"
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthenticated"
        "403":
          $ref: "#/components/responses/Forbidden"
        "404":
          $ref: "#/components/responses/NotFound"
        "409":
          $ref: "#/components/responses/Conflict"
        "415":
          $ref: "#/components/responses/UnsupportedMediaType"
        "422":
          $ref: "#/components/responses/ValidationFailed"
        "429":
          $ref: "#/components/responses/RateLimited"
        "500":
          $ref: "#/components/responses/InternalError"
        "503":
          $ref: "#/components/responses/Unavailable"

  /v1/payment-intents/{payment_intent_id}:
    get:
      operationId: getPaymentIntent
      tags: [PaymentIntents]
      summary: Retrieve a payment intent
      security:
        - bearerAuth: []
      parameters:
        - name: payment_intent_id
          in: path
          required: true
          description: Opaque payment-intent identifier
          schema:
            type: string
            minLength: 1
            maxLength: 128
      responses:
        "200":
          description: Current payment-intent representation
          headers:
            X-Request-Id:
              $ref: "#/components/headers/RequestId"
            Cache-Control:
              $ref: "#/components/headers/NoStore"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PaymentIntent"
        "401":
          $ref: "#/components/responses/Unauthenticated"
        "404":
          $ref: "#/components/responses/NotFound"
        "429":
          $ref: "#/components/responses/RateLimited"
        "500":
          $ref: "#/components/responses/InternalError"
        "503":
          $ref: "#/components/responses/Unavailable"

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

  parameters:
    IdempotencyKey:
      name: Idempotency-Key
      in: header
      required: true
      description: >
        Unique key for safely replaying this creation request. Reuse with
        different request content is rejected.
      schema:
        type: string
        minLength: 16
        maxLength: 255
        pattern: "^[A-Za-z0-9._:-]+$"

  headers:
    RequestId:
      description: Opaque request identifier for support correlation
      required: true
      schema:
        type: string
    NoStore:
      description: Prevents storage of payment data by clients and intermediaries
      required: true
      schema:
        type: string
        const: no-store
    RetryAfter:
      description: Seconds before the client should retry
      schema:
        type: integer
        minimum: 1

  schemas:
    CreatePaymentIntentRequest:
      type: object
      additionalProperties: false
      required: [amount, currency]
      properties:
        amount:
          type: integer
          minimum: 1
          maximum: 999999999
          description: Amount in the currency's minor unit
        currency:
          type: string
          pattern: "^[A-Z]{3}$"
          description: Supported ISO-4217 currency code
        customer_id:
          type: string
          minLength: 1
          maxLength: 128
          description: Opaque customer ID authorized in the caller's scope
        payment_method_id:
          type: string
          minLength: 1
          maxLength: 128
          description: Opaque pre-tokenized payment-method ID
        capture_method:
          type: string
          enum: [automatic, manual]
          default: automatic
        merchant_reference:
          type: string
          minLength: 1
          maxLength: 64

    PaymentIntent:
      type: object
      additionalProperties: false
      required:
        - id
        - object
        - amount
        - currency
        - capture_method
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          description: Opaque identifier; clients must not parse its structure
        object:
          type: string
          const: payment_intent
        amount:
          type: integer
          minimum: 1
        currency:
          type: string
          pattern: "^[A-Z]{3}$"
        customer_id:
          type: [string, "null"]
        payment_method_id:
          type: [string, "null"]
        capture_method:
          type: string
          enum: [automatic, manual]
        merchant_reference:
          type: [string, "null"]
        status:
          type: string
          description: >
            Known values are requires_payment_method, requires_confirmation,
            requires_action, processing, requires_capture, succeeded, and
            canceled. Clients must tolerate unknown future values.
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time

    FieldError:
      type: object
      additionalProperties: false
      required: [path, code, message]
      properties:
        path:
          type: string
          description: JSON Pointer to the invalid request field
        code:
          type: string
        message:
          type: string

    Problem:
      type: object
      additionalProperties: false
      required: [type, title, status, code, detail, request_id]
      properties:
        type:
          type: string
          format: uri-reference
        title:
          type: string
        status:
          type: integer
          minimum: 400
          maximum: 599
        code:
          type: string
        detail:
          type: string
        instance:
          type: string
          format: uri-reference
        request_id:
          type: string
        errors:
          type: array
          items:
            $ref: "#/components/schemas/FieldError"

  responses:
    BadRequest:
      description: Malformed JSON or invalid required header
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    Unauthenticated:
      description: Missing or invalid authentication
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
        WWW-Authenticate:
          schema:
            type: string
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    Forbidden:
      description: Authenticated caller lacks operation permission
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    NotFound:
      description: Resource is absent or intentionally concealed
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    Conflict:
      description: Idempotency key conflict or operation still in progress
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
        Retry-After:
          $ref: "#/components/headers/RetryAfter"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    UnsupportedMediaType:
      description: Request body is not application/json
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    ValidationFailed:
      description: Syntactically valid request violates field or domain constraints
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    RateLimited:
      description: Request rate or quota exceeded
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
        Retry-After:
          $ref: "#/components/headers/RetryAfter"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    InternalError:
      description: Unexpected internal failure
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
    Unavailable:
      description: Temporary service or dependency unavailability
      headers:
        X-Request-Id:
          $ref: "#/components/headers/RequestId"
        Retry-After:
          $ref: "#/components/headers/RetryAfter"
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Problem"
```

### API-boundary abuse controls

- Enforce the existing authentication scheme centrally and require a `payment_intents:create`-equivalent permission. Derive principal and tenant from trusted server context.
- Authorize `customer_id` and `payment_method_id` at object level before use. Cross-tenant or unauthorized IDs receive the same `404` shape and materially similar timing as absent IDs.
- Accept only `application/json`; cap the body at 16 KiB; enforce all documented type, length, pattern, amount, currency, and relationship constraints; reject unknown properties.
- Never accept raw PAN, CVV, bank credentials, owner, tenant, status, balance, or provider-routing fields. Use explicit request and response mappers rather than persistence/provider objects.
- Apply token-bucket limits by principal plus tenant, separate limits for unauthenticated/IP failures, and tighter cost limits for provider-triggering operations. Idempotent replays may use a lower-cost replay bucket but remain bounded.
- Return stable `429 RATE_LIMITED` and a usable `Retry-After`; do not expose internal capacity, provider quotas, or limit calculations.
- Reserve idempotency before expensive/provider work. Use provider timeouts, circuit breakers, bounded concurrency, and backpressure. If a durable intent exists, preserve it as `processing` rather than reporting a no-op.
- Require HTTPS. Use explicit browser-origin allowlists, no credentialed wildcard CORS, and expose only `Location`, `X-Request-Id`, `Retry-After`, `Idempotency-Replayed`, and `Cache-Control` when browser clients require them. With bearer auth, do not enable cookies or credentialed CORS by default.
- Redact authorization credentials, payment-method IDs, idempotency keys, request bodies, and provider payloads from logs and traces. Audit creation, replay, key mismatch, authorization failure, rate limit, and state transition using hashed or opaque identifiers.
- Return `Cache-Control: no-store`; do not place secrets or client credentials in URLs, errors, examples, or response fields.
- Verify with contract validation, backward-compatibility diffing, success/error schema tests, cross-tenant BOLA tests, unknown-field/mass-assignment tests, idempotency replay/mismatch/concurrency tests, body-limit tests, rate-limit tests, and commit-ambiguity recovery tests.

References read: skills/api-design/references/errors.md, skills/api-design/references/versioning-compatibility.md, skills/api-design/references/rest.md, skills/api-design/references/openapi.md, skills/api-design/references/security-and-abuse.md
Evaluator assets read: none
Selector basis: skills/api-design/references/errors.md — public response, validation, status, correlation, and error shape requested; skills/api-design/references/versioning-compatibility.md — backward compatibility and idempotency requested; skills/api-design/references/rest.md — accepted REST resource, method, status, header, rate-limit, caching, and idempotency behavior requested; skills/api-design/references/openapi.md — OpenAPI 3.1 contract requested; skills/api-design/references/security-and-abuse.md — API-boundary abuse controls requested
````

Reported audit lines:

```text
References read: skills/api-design/references/errors.md, skills/api-design/references/versioning-compatibility.md, skills/api-design/references/rest.md, skills/api-design/references/openapi.md, skills/api-design/references/security-and-abuse.md
Evaluator assets read: none
Selector basis: skills/api-design/references/errors.md — public response, validation, status, correlation, and error shape requested; skills/api-design/references/versioning-compatibility.md — backward compatibility and idempotency requested; skills/api-design/references/rest.md — accepted REST resource, method, status, header, rate-limit, caching, and idempotency behavior requested; skills/api-design/references/openapi.md — OpenAPI 3.1 contract requested; skills/api-design/references/security-and-abuse.md — API-boundary abuse controls requested
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: target-reported/procedural read evidence, not filesystem capability isolation.
