# ADR Template

## Contents

- Section Guidance
- Canonical Template
- Eliciting Missing Information
- Review Checklist
- Blocked ADR Packet

## Section Guidance

### Title

Use a short, searchable title that names the decision.

Format:

```markdown
# ADR-NNNN: [Short descriptive title]
```

Examples:

- `ADR-0001: Use PostgreSQL for primary database`
- `ADR-0012: Adopt event-driven architecture for order processing`
- `ADR-0023: Implement rate limiting at API gateway`

Number sequentially according to project convention. Never reuse numbers.

### Status

Use the project status vocabulary when one exists. Common statuses:

| Status     | Meaning                                    |
| ---------- | ------------------------------------------ |
| Proposed   | Under consideration; not yet in effect     |
| Accepted   | Agreed and in effect                       |
| Rejected   | Considered but not adopted                 |
| Deprecated | No longer recommended or no longer applies |
| Superseded | Replaced by another ADR                    |

Superseded format:

```markdown
**Status:** Superseded by ADR-0045
```

The superseding ADR should also reference what it supersedes.

### Context

Describe the situation that led to the decision. Context should be factual and value-neutral.

Include:

- problem or question;
- relevant constraints;
- forces in tension;
- functional requirements driving the decision;
- quality attributes or operational constraints;
- candidate alternatives.

Bad context:

```markdown
We need a better database because the current one is terrible.
```

Better context:

```markdown
The current SQLite database does not support concurrent writes. With traffic at 500 req/s and projected to reach 2000 req/s by Q3, write contention is causing 5% of requests to fail. The system needs concurrent writes while preserving ACID guarantees for invoice records. Options considered: PostgreSQL, MySQL, and CockroachDB.
```

### Decision

State the decision in active voice.

Good:

- "We will use PostgreSQL as the primary database."
- "We adopt event-driven processing for order fulfillment."
- "The API will enforce rate limits at the gateway."

Avoid:

- "PostgreSQL was chosen."
- "A database should be selected."
- "Consider using PostgreSQL."

### Consequences

Document positive, negative, and neutral consequences.

If the negative section is empty, the ADR is probably not ready. Every decision accepts costs.

### Alternatives Considered

For each meaningful alternative:

- name the alternative;
- describe what it actually was;
- state why it was rejected;
- tie rejection reasons to forces named in Context.

Do not write "rejected because it did not fit" unless the fit problem is concrete.

## Canonical Template

Adapt this to the project's existing convention. Do not force frontmatter when the project does not use it.

```markdown
---
tags: [] # optional topical tags, if the project uses frontmatter
supersedes: "" # ADR-NNNN this one replaces, if any
superseded_by: "" # ADR-NNNN that replaces this one, if any
---

# ADR-NNNN: [Short Descriptive Title]

**Status:** Proposed | Accepted | Rejected | Deprecated | Superseded by ADR-XXXX
**Date:** YYYY-MM-DD
**Author(s):** [names or project convention]

## Context

[Describe the situation that led to this decision.

- What problem or question are we addressing?
- What constraints apply?
- What forces are in tension?
- What alternatives are being weighed?
- What evidence supports this context?

Be factual and value-neutral.]

## Decision

[State one decision clearly in active voice.

"We will..."
"We adopt..."
"The system will..."

Be specific enough that someone can implement or respect the decision.]

## Consequences

### Positive

- [Benefit from this decision]

### Negative

- [Trade-off, limitation, cost, or risk accepted]

### Neutral

- [Side effect that is neither clearly good nor bad]

## Alternatives Considered

[One subsection per meaningful alternative. Omit only if there were genuinely no alternatives, and say that in Context.]

### [Alternative Name]

**Description:** [What this alternative actually is.]

**Rejection reason:** [Why it was rejected, tied to forces in Context.]

## Related Decisions

- ADR-XXXX: [How it relates]

## Notes

[Optional links to discussions, specs, plans, research, code, docs, or review evidence.]
```

## Eliciting Missing Information

When the decision is unclear, ask:

- "What specifically is being decided?"
- "Which options have been considered?"
- "What is the recommended option and why?"

When context is unclear, ask:

- "What problem is this solving?"
- "What constraints or forces are driving this decision?"
- "Why is the decision being made now?"

When alternatives are unclear, ask:

- "What would we do if this option were rejected?"
- "Which alternatives were seriously considered?"
- "Why were they rejected in this project context?"

When consequences are unclear, ask:

- "What becomes easier because of this decision?"
- "What becomes harder?"
- "What risk, cost, coupling, operational burden, or migration path are we accepting?"

If the user cannot articulate alternatives or trade-offs, block ADR creation and route to architecture/spec/research until the decision is ready.

## Review Checklist

Before calling an ADR ready, verify:

- The ADR records one decision.
- The title is specific and searchable.
- Status and date are present.
- Context is factual, not advocacy.
- The decision is active and actionable.
- Alternatives are concrete and rejection reasons tie back to context.
- Consequences include positives and negatives.
- Related or superseded ADRs are linked.
- Numbering and path follow project convention.
- Accepted ADR history is not rewritten.

## Blocked ADR Packet

Use this when the ADR cannot be created safely.

```markdown
# ADR Blocked: [short title]

Status: Blocked
Requested ADR path: [path or unknown]
Blocking gate: [decision readiness | ADR bar | project convention | context | alternatives | consequences | immutability]

## Missing Evidence

## What Was Checked

## Why ADR Creation Cannot Continue Safely

## Smallest Next Action
```
