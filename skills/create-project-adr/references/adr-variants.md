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

## Selection Rule

| Format       | Best for                  | Avoid when                                       |
| ------------ | ------------------------- | ------------------------------------------------ |
| Nygard-style | Most decisions            | Project uses a different existing convention     |
| Y-statement  | Lightweight capture       | Trade-offs or evidence need sections             |
| MADR         | Detailed options analysis | The options matrix adds ceremony without clarity |

The format can vary. The behavior cannot: preserve context, state one decision clearly, document consequences honestly, document meaningful alternatives, and preserve accepted history.
