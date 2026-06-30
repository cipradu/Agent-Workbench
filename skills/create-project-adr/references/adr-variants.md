# ADR Variants

Use the project convention first. Use a variant only when it is already the project standard or when no convention exists and the variant fits the decision's complexity.

## Nygard-Style ADR

Best default for most project decisions.

Core sections:

- Status
- Context
- Decision
- Consequences
- Alternatives Considered
- Related Decisions

Use when the decision needs enough context for future maintainers but does not require a full options matrix.

## Y-Statement

Best for very small decisions or executive summaries when the project accepts lightweight ADRs.

Format:

```text
In the context of [situation/requirement],
facing [concern/constraint],
we decided for [option]
and against [alternatives],
to achieve [benefit],
accepting that [trade-off].
```

Use only when the decision is simple enough that the single statement still captures context, alternatives, and consequences honestly.

Do not use a Y-statement when the ADR is derived from a review finding, implementation-plan KTD, incident, optimization run, optional-provider decision, reporting/data-source decision, or stale/superseded ADR conflict unless the one sentence can preserve the source authority, alternatives, and accepted costs without hiding evidence. Use Nygard-style or MADR instead when the source chain matters.

## MADR

Best for decisions requiring explicit options analysis.

Skeleton:

```markdown
# [Title]

## Status

[status]

## Context and Problem Statement

[problem description]

## Decision Drivers

- [driver 1]
- [driver 2]

## Considered Options

- [Option 1]
- [Option 2]
- [Option 3]

## Decision Outcome

Chosen option: "[Option N]", because [justification].

### Consequences

- Good, because [positive]
- Bad, because [negative]

## Pros and Cons of Options

### [Option 1]

- Good, because [argument]
- Bad, because [argument]
```

Use MADR when the value is in comparing drivers and options in detail. Do not use it merely to make a simple decision look more formal.

MADR is often the safer variant for option-heavy or evidence-heavy decisions, such as architecture alternatives, provider/tool selection, metric or evaluation-harness choices, data-source authority, credential-boundary decisions, workflow-control surfaces, or superseding an accepted ADR after new evidence. The matrix must still end in one active decision and honest consequences.

## Selection Rule

| Format       | Best for                  | Avoid when                                       |
| ------------ | ------------------------- | ------------------------------------------------ |
| Nygard-style | Most decisions            | Project uses a different existing convention     |
| Y-statement  | Lightweight capture       | Trade-offs or evidence need sections             |
| MADR         | Detailed options analysis | The options matrix adds ceremony without clarity |

The format can vary. The behavior cannot: preserve context, state one decision clearly, document consequences honestly, document meaningful alternatives, and preserve accepted history.

## Variant Safety Rules

- Variant choice must not bypass decision readiness, the ADR bar, project convention, existing coverage, source authority, alternatives, consequences, or immutability.
- Keep source-derived evidence visible enough for future maintainers to trace why the decision was accepted or proposed.
- Use project status vocabulary even when the variant is compact.
- Preserve supersession links and related decisions regardless of format.
- Do not use compact formats to hide unresolved decisions, all-positive consequences, stale authority conflicts, or multiple independently reversible decisions.
