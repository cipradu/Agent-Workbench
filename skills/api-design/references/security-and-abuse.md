# Security And Abuse Controls

Use this reference for API-boundary design checks. It does not replace a full security review, but it prevents common API design mistakes before implementation.

## Boundary Model

For each API operation, identify:

- actor identity and authentication mechanism;
- tenant, account, organization, user, role, scope, or policy context;
- credential surface: bearer token, API key, cookie, session, client certificate, signed webhook secret, or other proof;
- object/resource ownership rules;
- sensitive inputs and outputs;
- trusted and untrusted fields;
- browser exposure: CORS, cookies, CSRF posture, and readable response headers;
- upstream and downstream systems touched;
- side effects and retry behavior;
- body size, field size, upload size, export size, and request timeout limits;
- logs, metrics, traces, and audit events.

## Authentication And Credential Surface

Rules:

- Accept only documented authentication schemes for the surface. Reject invalid, malformed, ambiguous, or mixed schemes before dispatching domain work.
- Prefer one primary scheme per surface. Support alternatives such as `x-api-key` only where the contract or deployment boundary requires them.
- Validate API keys, bearer tokens, cookies, signed webhooks, and client-provided credentials in a centralized boundary path so parsing, expiration, revocation, and redaction are consistent.
- Never log `Authorization`, `Cookie`, `Set-Cookie`, API key headers, bearer tokens, session identifiers, webhook secrets, OAuth codes, one-time codes, or raw credential values.
- When issuing or storing reusable credentials, coordinate with `database-design` for non-plaintext storage, rotation metadata, last-used tracking, expiry, revocation, and display-safe suffixes or fingerprints.
- Authentication proves caller identity or credential possession only; it does not prove object access, tenant access, feature permission, or operation authority.

## Authorization

Rules:

- Authentication is not authorization.
- Route-level or resolver-level role checks are not enough when objects have owners, tenants, teams, scopes, or row-level policy.
- Check both function-level access and object-level access.
- Apply authorization before returning existence-sensitive details unless disclosure is intentional.
- Apply authorization to filters, expansions, nested objects, batch items, and GraphQL fields.
- Do not trust client-submitted user IDs, tenant IDs, role IDs, price IDs, or ownership fields without server-side derivation or verification.
- Prefer service-boundary or policy-module authorization checks over scattered inline route conditionals when the operation is security-sensitive or repeated.

## BOLA/IDOR Checks

For every identifier accepted from the client:

- Can user A access user B's object by changing the ID?
- Can a tenant access another tenant's object through filters or expansions?
- Do batch operations validate each item independently?
- Do nested routes verify both parent and child relationship ownership?
- Do GraphQL nested resolvers re-check object access?
- Do list endpoints filter by authorization before pagination and totals?

## Mass Assignment And Data Exposure

Rules:

- Use explicit request schemas. Do not bind arbitrary JSON directly to persistence models.
- Reject or ignore unknown fields according to a documented policy.
- Maintain separate create, update, patch, and response contracts.
- Do not allow clients to set server-owned fields such as `id`, `tenant_id`, `user_id`, `role`, `status`, `created_at`, `updated_at`, `deleted_at`, `balance`, or authorization scopes unless the operation explicitly owns that transition.
- Use explicit response serializers/mappers to avoid leaking internal fields.

## Resource Consumption

Protect:

- unbounded list endpoints;
- expensive filters/sorts/searches;
- large bodies, deeply nested JSON, oversized fields, and unsupported content types;
- file uploads and exports;
- GraphQL depth, complexity, batching, and alias abuse;
- bulk operations;
- async job creation;
- third-party calls triggered by clients;
- webhooks or callbacks that can be replayed or faked.

Controls include body and field limits, content-type allowlists, upload scanning or type sniffing when applicable, quotas, rate limits, cost budgets, backpressure, async job queues, timeouts, circuit breakers, and clear `429`/`503` behavior.

For `429 Too Many Requests`, define:

- limit scope: user, token, tenant, IP, route, organization, job, or global;
- whether burst, sustained, and expensive-operation limits differ;
- response body shape and stable error code;
- `Retry-After` behavior when the client can use it safely;
- readable rate-limit headers only when they do not help attackers tune abuse;
- logging or security telemetry for suspicious patterns without logging sensitive values.

## Input Validation And Injection

Rules:

- Validate every boundary input by type, range, length, enum, format, and relationship to actor/context.
- Parameterize database queries and use allowlists for dynamic identifiers, sort keys, and field selection.
- Normalize inputs that affect uniqueness, matching, or security decisions.
- Avoid exposing internal parsing errors.
- Treat URLs, file paths, HTML, markdown, SQL fragments, regexes, and template strings as high-risk inputs.

## CORS And Browser Access

Rules:

- CORS is not authorization.
- Use explicit origin allowlists.
- Default to no credentials unless cookie/session behavior explicitly requires credentials and CSRF posture is designed.
- Avoid wildcard origins with credentials; do not reflect arbitrary origins without a trusted allowlist check.
- Allow only required methods and request headers.
- Expose only the headers clients need.
- Review preflight behavior for custom auth, idempotency, rate-limit, request ID, and trace headers.

## Transport, Cookies, And Browser-Security Headers

Rules:

- Production APIs that carry credentials, sessions, personal data, or privileged operations require HTTPS at the exposed boundary.
- Use HSTS where the deployment model supports it and rollback implications are understood.
- Cookies used for authentication or session state should be `HttpOnly`, `Secure`, and have an explicit `SameSite` policy.
- Do not put bearer tokens, session identifiers, API keys, password reset tokens, or one-time codes in URLs where logs, browser history, proxies, or referrers can capture them.
- Cache headers must prevent shared or intermediary caching of user-specific, tenant-specific, or credential-bearing responses unless the cache model is explicitly safe.
- Security headers are boundary controls, not substitutes for authorization or output escaping.

## SSRF And Unsafe External Consumption

If the API accepts URLs, webhook destinations, import sources, image fetches, callback targets, or third-party endpoints:

- allowlist schemes and hosts where possible;
- block internal/private/link-local metadata networks unless explicitly required and guarded;
- resolve DNS safely and consider rebinding;
- limit redirects;
- enforce timeouts and size limits;
- do not forward privileged headers or credentials to client-provided destinations;
- log target host and decision outcome.

## Sensitive Data

Rules:

- Do not put secrets, tokens, session identifiers, or sensitive personal data in URLs if logs, browser history, proxies, or referrers can capture them.
- Do not log raw request/response bodies by default.
- Redact secrets in errors, traces, and audit logs.
- Keep cache headers safe for user-specific data.
- Review response examples and OpenAPI schemas for accidental sensitive fields.
- Keep public error messages generic around credential validity, authorization policy, resource existence, and ownership unless disclosure is intentionally allowed.
- Avoid timing and response-shape differences that make unauthorized resource enumeration easy.

## Credential Rotation And Revocation Contracts

When the API exposes credentials, API keys, webhooks, sessions, tokens, or password-like flows, define:

- creation, display, and one-time reveal behavior;
- rotation and revocation operations;
- expiration and inactive-state behavior;
- last-used or last-seen metadata when useful for operators or users;
- scope, owner, tenant, and environment binding;
- audit events for create, use, failed use, revoke, rotate, and suspicious activity;
- client behavior for old credentials after rotation.

## API Inventory

Keep track of:

- active versions;
- deprecated versions;
- shadow/internal endpoints;
- admin endpoints;
- webhook endpoints;
- GraphQL schemas;
- generated clients;
- public documentation.

Stale or undocumented API surfaces are security and compatibility risks.

## Security Checklist

- Authn and authz are both defined.
- Credential scheme, parsing, redaction, storage handoff, rotation, and revocation behavior are defined when reusable credentials exist.
- Object-level access is tested for identifiers, nested resources, batch items, and GraphQL fields.
- Request schemas prevent mass assignment.
- Response schemas prevent data exposure.
- Expensive operations have limits and backpressure.
- Body limits, content-type limits, upload/export controls, rate-limit behavior, and `Retry-After` semantics are defined where relevant.
- CORS, cookies, transport, browser-security headers, cache headers, and sensitive data handling are safe.
- URL-fetching or callback behavior has SSRF controls.
- Authn/authz/not-found errors follow a deliberate disclosure policy and do not leak secrets or resource existence accidentally.
- API inventory, versioning, and deprecation state are known.
