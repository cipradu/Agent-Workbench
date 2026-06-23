# API Design Pressure Tests

Use these scenarios to test whether the skill changes agent behavior under pressure.

## RED Scenarios

### Route-First Pressure

Prompt: "Just add `POST /createUser` quickly."

Pressure: speed and familiar REST anti-pattern.

Expected wrong behavior: accept the verb route and implement before defining resource, contract, validation, auth, errors, and docs.

Required correct behavior: stop route-first implementation, model the resource/operation, prefer `POST /users` if REST fits, and define contract details before implementation.

Pass/fail criteria: passes only if the agent refuses to treat the route name as enough design.

### Model Leakage Pressure

Prompt: "Return the database user row directly. It already has everything the frontend needs."

Pressure: convenience and false confidence.

Expected wrong behavior: expose ORM/database shape and internal fields.

Required correct behavior: require an explicit response contract, sensitive-field review, and internal-to-external mapping.

Pass/fail criteria: passes only if the agent blocks accidental model leakage.

### Unbounded List Pressure

Prompt: "Add a users list endpoint. No pagination for now."

Pressure: short-term speed.

Expected wrong behavior: create an unbounded collection API and promise to add pagination later.

Required correct behavior: require pagination or prove the result set is permanently bounded; define defaults, maximums, and ordering.

Pass/fail criteria: passes only if unbounded list behavior is rejected.

### Unsafe Retry Pressure

Prompt: "Create a payment/order/message POST endpoint. The client can retry if it times out."

Pressure: hidden side effects and client retry assumptions.

Expected wrong behavior: implement unsafe `POST` without duplicate protection.

Required correct behavior: require idempotency key, natural idempotency, or explicit non-retryable semantics.

Pass/fail criteria: passes only if duplicate side effects are addressed before implementation.

### Breaking Change Pressure

Prompt: "Rename this response field and remove the old one. No need for a new version."

Pressure: same-team assumption and local cleanup desire.

Expected wrong behavior: make a client-visible breaking change with no compatibility plan.

Required correct behavior: classify the change, identify consumers, and require versioning/deprecation/migration or prove no independent clients exist.

Pass/fail criteria: passes only if compatibility is analyzed before changing the contract.

### Error Semantics Pressure

Prompt: "Return `200` with `{ success: false }` because the frontend expects JSON."

Pressure: frontend convenience.

Expected wrong behavior: violate HTTP semantics and monitoring/caching expectations.

Required correct behavior: use correct failure status plus a consistent JSON error body.

Pass/fail criteria: passes only if the agent rejects `200` failures for REST.

### GraphQL Complexity Pressure

Prompt: "GraphQL is flexible. Add the schema and resolvers; we can optimize later."

Pressure: attractive flexibility and deferred operations risk.

Expected wrong behavior: add GraphQL without depth, complexity, batching, N+1, authorization, or introspection policy.

Required correct behavior: require GraphQL operational controls as part of the contract design.

Pass/fail criteria: passes only if GraphQL controls are considered mandatory.

### Envelope Universality Pressure

Prompt: "Always use our old success/fail envelope for every API."

Pressure: copying a previous project convention.

Expected wrong behavior: force one previous project's envelope into every protocol and project.

Required correct behavior: treat envelopes as a project decision, use the local source of truth when present, and choose response shape from consumer/protocol needs.

Pass/fail criteria: passes only if the agent preserves the useful envelope idea without making it universal law.

## GREEN Criteria

The skill passes if a fresh agent:

- invokes the skill for API contract work;
- establishes consumers, contract authority, compatibility surface, and trust boundary before implementation;
- chooses or validates API style instead of defaulting to REST;
- blocks unbounded collections, unsafe retries, inconsistent errors, model leakage, and breaking changes without migration;
- loads only the relevant protocol reference;
- produces an output that a client and server implementer can follow without guessing.
