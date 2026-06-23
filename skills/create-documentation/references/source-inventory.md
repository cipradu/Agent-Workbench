# Source Inventory

Use this reference before creating or materially revising technical documentation.

## Source Precedence

Prefer sources in this order unless the project defines a stricter authority:

1. Current code, tests, schemas, generated contracts, migration files, configs, scripts, CI, and runtime manifests.
2. Accepted ADRs, approved PRDs, approved engineering specs, implementation plans, runbooks, and operational policies.
3. Existing docs that are known to be current.
4. User-provided context and explicit decisions.
5. Current official external documentation for libraries, frameworks, protocols, standards, vendors, or platforms.
6. Inferred assumptions, only when labeled and non-normative.

If sources conflict, document the conflict as a finding and do not choose silently.

## General Repository Inventory

Check the relevant subset:

- root docs: `README`, `docs/`, `CONTRIBUTING`, `CHANGELOG`, `SECURITY`, `LICENSE`;
- project instructions: `AGENTS.md`, `CLAUDE.md`, harness instruction files, local rules;
- decisions and planning: ADRs, PRDs, specs, plans, design docs, architecture docs, issue/PR context;
- manifests: `package.json`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Cargo.toml`, `.csproj`, `pom.xml`, `build.gradle`;
- entry points and public surfaces: routes, controllers, commands, exports, SDKs, modules, packages;
- generated contracts: OpenAPI, GraphQL schemas, protobuf, AsyncAPI, JSON Schema, database schema, migration files;
- examples and tests: sample apps, snippets, fixtures, test commands, E2E flows;
- operations: Dockerfiles, compose files, Helm/Kubernetes, Terraform, deployment config, monitoring/runbook files;
- docs tooling: static-site config, nav/sidebar config, markdownlint, Vale, cspell, link checkers, docs build scripts.

## Documentation Update Triggers

Docs likely need updates when a change adds or modifies:

- public features or user-visible workflows;
- API endpoints, schemas, SDKs, generated clients, events, webhooks, or error formats;
- CLI commands, flags, environment variables, config files, setup steps, dependencies, or supported platforms;
- architecture boundaries, component responsibilities, data flow, persistence, deployment, security, or operations;
- auth, permissions, roles, rate limits, quotas, retry behavior, idempotency, or compatibility policy;
- breaking changes, deprecations, migrations, renamed concepts, or removed behavior;
- troubleshooting paths, known issues, support procedures, runbooks, or escalation paths.

## External Research Triggers

Verify current external facts when documentation asserts:

- library/framework APIs, versions, deprecations, or recommended patterns;
- protocol or standard behavior;
- cloud/vendor product behavior, pricing-sensitive limitations, quotas, regions, or security controls;
- generated documentation formats such as OpenAPI, GraphQL, AsyncAPI, Javadoc, XML docs, Sphinx, pdoc, rustdoc, godoc, or TSDoc;
- regulatory, legal, compliance, accessibility, or security standards.

Record source URL, date accessed when useful, version, and caveat.

## Sensitive Content Check

Do not include:

- secrets, tokens, keys, passwords, credentials, private certificates, session values;
- private hostnames, internal network topology, customer identifiers, account IDs, production data, PHI/PII, or billing-sensitive records unless explicitly approved for that docs audience;
- exploit steps, operational bypasses, or internal incident details beyond the audience's need;
- screenshots or logs containing sensitive data;
- unsupported security claims.

## Evidence Notes

For each substantive claim, know which source supports it:

| Claim type                   | Good source                                                       |
| ---------------------------- | ----------------------------------------------------------------- |
| "Run this command"           | manifest script, Makefile, existing docs, tested command          |
| "This endpoint returns..."   | route/controller, OpenAPI schema, contract test, generated client |
| "This option defaults to..." | config schema, code default, documented config file               |
| "The architecture uses..."   | code structure, deployment config, ADR, architecture doc          |
| "This is deprecated"         | code annotation, changelog, ADR, official external docs           |
| "This is safe to operate"    | runbook, tests, monitoring, rollback procedure, operational owner |

## Blockers

Block or produce a discovery packet when:

- source truth is missing for material claims;
- docs and code conflict and no authority resolves it;
- examples cannot be validated and would be unsafe to present as working;
- the user asks for docs that would expose sensitive details;
- the doc depends on unresolved product/engineering/architecture decisions.
