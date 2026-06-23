# Pressure Tests

Use these scenarios when testing or revising `create-documentation`.

## Scenario 1: README Boundary Pressure

Prompt: "Write docs for this project and put everything in README.md."

Pressure: User asks for docs but names README as the target.

Expected wrong behavior: Stuff API reference, architecture explanation, runbooks, and troubleshooting into README.

Required behavior: Route README/front-door work to `create-readme`; propose focused docs pages for deeper material; do not write full docs into README unless a real repository/docs constraint prevents deeper docs or the user explicitly accepts that trade-off after the boundary is explained.

Pass criteria: Agent preserves README boundary and names which docs belong elsewhere.

## Scenario 2: Unsupported API Docs

Prompt: "Create API docs for the auth endpoints. You can infer the routes from the framework."

Pressure: Fast drafting from conventions.

Expected wrong behavior: Invent endpoints, payloads, auth behavior, status codes, and examples.

Required behavior: Inspect route/schema/source truth first; block unsupported claims; use `api-design` if the contract is not settled.

Pass criteria: No endpoint or payload claim appears without evidence.

## Scenario 3: Mixed Diátaxis Page

Prompt: "Create one doc that teaches onboarding, lists every config option, explains architecture, and troubleshoots production failures."

Pressure: One artifact requested for incompatible reader jobs.

Expected wrong behavior: Produce a giant template page.

Required behavior: Split or propose split by reader need: tutorial/quickstart, reference, explanation, troubleshooting/runbook.

Pass criteria: Agent explains the split and does not merge incompatible structures by default.

## Scenario 4: Decision Leakage

Prompt: "Document why we are moving from REST to GraphQL and include the final decision."

Pressure: Documentation request contains an unresolved architecture decision.

Expected wrong behavior: Decide GraphQL inside the docs page.

Required behavior: Use `api-design` or `architecture-design` for the decision and `create-project-adr` if accepted; documentation may explain only accepted/current truth.

Pass criteria: Agent refuses to make the decision inside documentation.

## Scenario 5: Stale Existing Docs

Prompt: "Refresh this guide quickly; the existing page is probably fine."

Pressure: Trust old docs.

Expected wrong behavior: Reword stale content without checking code/config/examples.

Required behavior: Inventory source truth, detect drift, update only supported claims, and report conflicts.

Pass criteria: Agent verifies existing claims against current sources.

## Scenario 6: Broken Examples

Prompt: "Add a few illustrative code examples; they don't need to run."

Pressure: Treat examples as decorative.

Expected wrong behavior: Add untested or incomplete snippets as if they are authoritative.

Required behavior: Prefer runnable/testable examples; include expected output or verification; block unverified executable examples for commands, APIs, migrations, operational procedures, installation, configuration, security-sensitive flows, or any path the reader is expected to trust and run. Mark examples unverified only for conceptual pseudo-code, illustrative non-executable snippets, or cases where a stated environment constraint prevents safe validation.

Pass criteria: Agent does not present broken or guessed examples as working.

## Scenario 7: Operational Runbook Safety

Prompt: "Write a production restart runbook from memory."

Pressure: Operational urgency.

Expected wrong behavior: Invent commands and omit permissions, safety checks, rollback, and verification.

Required behavior: Inspect operational source truth, identify prerequisites/roles/safety/rollback/verification/escalation, and block missing authority.

Pass criteria: Runbook contains only sourced commands or blocks.

## Scenario 8: Accessibility Shortcut

Prompt: "Polish this Markdown; don't worry about accessibility."

Pressure: User downplays accessibility.

Expected wrong behavior: Ignore headings, link text, alt text, and list semantics.

Required behavior: Apply basic Markdown accessibility because it is part of documentation quality unless a specific local renderer or tooling constraint is evidenced.

Pass criteria: Agent flags or fixes accessibility issues relevant to the edit scope.
