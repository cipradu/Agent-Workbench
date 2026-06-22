# Security And Abuse Controls

Use this reference for API-boundary design checks. It does not replace a full security review, but it prevents common API design mistakes before implementation.

## Boundary Model

For each API operation, identify:

- actor identity and authentication mechanism;
- tenant, account, organization, user, role, scope, or policy context;
- object/resource ownership rules;
- sensitive inputs and outputs;
- trusted and untrusted fields;
- upstream and downstream systems touched;
- side effects and retry behavior;
- logs, metrics, traces, and audit events.

## Authorization

Rules:

- Authentication is not authorization.
- Route-level or resolver-level role checks are not enough when objects have owners, tenants, teams, scopes, or row-level policy.
- Check both function-level access and object-level access.
- Apply authorization before returning existence-sensitive details unless disclosure is intentional.
- Apply authorization to filters, expansions, nested objects, batch items, and GraphQL fields.
- Do not trust client-submitted user IDs, tenant IDs, role IDs, price IDs, or ownership fields without server-side derivation or verification.

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
- file uploads and exports;
- GraphQL depth, complexity, batching, and alias abuse;
- bulk operations;
- async job creation;
- third-party calls triggered by clients;
- webhooks or callbacks that can be replayed or faked.

Controls include limits, quotas, rate limits, cost budgets, backpressure, async job queues, timeouts, circuit breakers, and clear `429`/`503` behavior.

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
- Avoid wildcard origins with credentials.
- Expose only the headers clients need.
- Review preflight behavior for custom auth, idempotency, rate-limit, request ID, and trace headers.

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
- Object-level access is tested for identifiers, nested resources, batch items, and GraphQL fields.
- Request schemas prevent mass assignment.
- Response schemas prevent data exposure.
- Expensive operations have limits and backpressure.
- CORS, cache headers, and sensitive data handling are safe.
- URL-fetching or callback behavior has SSRF controls.
- API inventory, versioning, and deprecation state are known.
