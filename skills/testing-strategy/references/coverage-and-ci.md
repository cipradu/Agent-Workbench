# Coverage And CI

Coverage and CI are feedback systems. They do not replace test design.

## Coverage Rules

- Follow local thresholds when they exist.
- Do not invent a universal percentage threshold for all projects.
- Use coverage to find untested risk, especially branches, error paths, permission paths, and critical policy logic.
- Treat high line coverage with weak assertions as low confidence.
- Treat low coverage on high-risk behavior as material even when global coverage passes.
- Exclude generated, type-only, framework boilerplate, or intentionally untestable code only through project-approved rules.
- When reviewing a coverage claim, inspect the tests or changed test diff for critical behavior and assertion quality. A coverage report alone is not enough to accept the claim.

## Better Coverage Questions

Ask:

- Which requirements or risks have no test?
- Which branches decide permissions, money/data integrity, migrations, retries, idempotency, or error handling?
- Which code is changed often but weakly tested?
- Which tests would fail if the main behavior regressed?
- Which tests only execute code without meaningful assertions?

## CI Gate Design

Fast feedback should be reliable and scoped. Acceptance feedback should be complete enough for the risk.

Common layers:

- format/lint/type/static checks for mechanical issues;
- focused unit tests for changed behavior;
- integration/contract tests for affected boundaries;
- E2E/browser/simulator tests for critical user journeys;
- migration/backfill verification for persistence changes;
- security or dependency checks where relevant;
- release smoke tests for deployed behavior.

## Changed-Scope Testing

When testing a change:

- run the narrow test that proves the changed behavior;
- run affected package/module tests;
- run boundary tests for changed APIs, database behavior, UI routes, commands, or generated artifacts;
- run broader suite gates when shared infrastructure, public contracts, migrations, or cross-cutting behavior changed.

## Reporting Evidence

Report exact commands and outcomes, not summaries alone.

When a check is skipped, state:

- what was skipped;
- why it was skipped;
- what risk remains;
- what alternate evidence was used.
