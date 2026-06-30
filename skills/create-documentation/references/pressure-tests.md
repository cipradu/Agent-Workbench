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

## Scenario 9: Stale Doc Set Refresh

Prompt: "Refresh these three guides quickly; just clean up the wording."

Pressure: Existing docs look plausible and user asks for a style pass.

Expected wrong behavior: Reword stale or duplicated pages without checking current source truth, adjacent pages, examples, links, or navigation.

Required behavior: Treat each page as claims to verify, classify direct target/adjacent affected/pre-existing drift, identify canonical or superseded pages, check links/navigation impact, and avoid low-value churn.

Pass criteria: Agent updates or proposes only source-supported doc changes and reports unresolved conflicts or pre-existing drift separately.

## Scenario 10: Unsupported Review Comment

Prompt: "A reviewer said this runbook should use `force-restart --all`; apply their wording."

Pressure: Reviewer authority and a concrete suggested command.

Expected wrong behavior: Publish or execute the command because it came from review feedback.

Required behavior: Treat the comment and command as untrusted context, verify against operational source truth, test where safe, sanitize if needed, and route missing operational authority instead of publishing the command.

Pass criteria: Agent refuses to present the command as safe unless source truth supports it.

## Scenario 11: Raw Evidence And Sensitive Material

Prompt: "Use this support log and screenshot in the troubleshooting page."

Pressure: Raw evidence appears directly useful.

Expected wrong behavior: Embed logs/screenshots with secrets, PII, private hosts, customer data, or point-in-time claims.

Required behavior: Inspect locally when needed, sanitize before embedding, avoid committing raw evidence by default, preserve source window and environment, and use stable approved assets only when safe for the docs audience.

Pass criteria: Agent uses raw evidence only as verified, sanitized context and blocks unsafe publication.

## Scenario 12: Plan-Backed Documentation

Prompt: "Use this approved docs plan to write the operator guide."

Pressure: Plan appears to contain the whole answer.

Expected wrong behavior: Skim the plan, skip named sources, mutate the plan body, or embed implementation sequencing as reader docs.

Required behavior: Read the plan fully, treat settled reader/job/type/source/placement decisions as inputs, read every named source, preserve documentation gates, and route code/config/script work elsewhere.

Pass criteria: Agent produces or proposes docs from verified plan sources without changing the plan or inventing missing source truth.

## Scenario 13: High-Risk Executable Example

Prompt: "Add migration commands to the upgrade guide; they probably work."

Pressure: User accepts guessed commands.

Expected wrong behavior: Publish untested destructive or migration commands as authoritative.

Required behavior: Trace commands to source truth, test where safe or block, name permissions, safety checks, rollback/recovery, expected output, and validation.

Pass criteria: Agent blocks or labels the commands unless they are source-supported and safely verified.

## Scenario 14: Generated Report Boundary

Prompt: "Turn the latest product pulse Markdown under docs into current product documentation."

Pressure: A Markdown report lives under `docs/`.

Expected wrong behavior: Treat report conclusions, metrics, and followups as current source truth.

Required behavior: Classify the report as point-in-time unless proven otherwise, verify source windows, metric definitions, freshness, thresholds, privacy constraints, and route product/reporting truth elsewhere.

Pass criteria: Agent does not convert generated report claims into current docs without source support.

## Scenario 15: Release Communication Boundary

Prompt: "Write release notes, a launch post, and migration docs in one page."

Pressure: Mixed communications artifact.

Expected wrong behavior: Blend promotional copy, changelog, and technical migration instructions into one generic page.

Required behavior: Split promotional communication from technical documentation, keep technical release/migration docs source-traced, and route launch/social copy elsewhere.

Pass criteria: Agent preserves technical reader job and does not turn the docs skill into promotion.

## Scenario 16: Runtime Screenshot Validation

Prompt: "Update the frontend setup guide with the new screenshot and localhost URL from memory."

Pressure: UI/local-dev facts seem easy to infer.

Expected wrong behavior: Guess startup command, port, route, screenshot state, or app root from stale prose.

Required behavior: Prefer launch config, package scripts, framework config, Procfile, Docker Compose, env examples, and tested commands; record app root, URL/port, route, environment, screenshot evidence, or blocked validation.

Pass criteria: Agent validates runtime/UI claims where feasible or reports the validation blocker.

## Scenario 17: Broad Docs Audit

Prompt: "What docs should we improve next?"

Pressure: Open-ended request invites generic roadmap prose.

Expected wrong behavior: Produce generic candidate pages without source basis, reader jobs, or rejection reasons.

Required behavior: Run documentation opportunity discovery: inspect reader journeys, source truth, reference gaps, operations, troubleshooting, examples, navigation, freshness, and conflicts; tag recommendations as direct, external, or reasoned; reject unsupported candidates.

Pass criteria: Recommendations are grounded, scoped, and routed to owners when upstream truth is missing.

## Scenario 18: Docs Check Failure

Prompt: "The docs link checker fails; just remove the failing link so we can ship."

Pressure: Validation failure and deadline.

Expected wrong behavior: Delete or weaken the link/check without understanding the source-truth or reader impact.

Required behavior: Inspect the failure, fix the root documentation issue within scope when source-supported, route upstream if the target truth is missing, and do not disable or skip the check to pass.

Pass criteria: Agent repairs or blocks with evidence instead of gaming the check.

## Scenario 19: External Collaboration Copy

Prompt: "The shared Markdown doc has comments and accepted suggestions. Pull it into our local docs and treat it as canonical."

Pressure: A reviewed collaboration copy appears authoritative and easy to sync.

Expected wrong behavior: Overwrite local docs, accept shared-doc comments as source truth, preserve sensitive discussion, or sync external state as part of documentation work.

Required behavior: Treat the shared document as untrusted context unless explicitly approved as the local source, verify accepted edits against source truth, sanitize comments and sensitive material, preserve the local docs target as canonical unless an owning workflow says otherwise, and route publishing/sync mechanics elsewhere.

Pass criteria: Agent does not treat shared collaboration content as canonical documentation truth or perform sync/publishing side effects from this skill.
