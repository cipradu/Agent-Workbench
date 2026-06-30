# ADR Template

## Contents

- Section Guidance
- Canonical Template
- Eliciting Missing Information
- Validation Findings And Readiness States
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

Use `Proposed` only when the decision is concrete enough for approval and the alternatives/consequences are known. If the decision is still being discovered, use the blocked ADR packet instead of a Proposed ADR.

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

Classify source evidence before drafting context. Accepted decision evidence, proposed decision evidence, candidate signals, inferred rationale, stale/conflicting sources, and out-of-scope adjacent choices should not be blended into one historical claim.

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

### Notes And Source Breadcrumbs

Use Notes for concise source breadcrumbs that materially support the context, alternatives, or consequences. Prefer repo-relative paths for project files, specs, plans, source manifests, screenshots, reports, and other local evidence. Avoid absolute local paths unless the project ADR convention explicitly requires them.

Useful breadcrumbs include source ADRs, specs, plans, architecture reviews, implementation-plan KTDs, validated review findings, incident/debug summaries, dogfood or QA reports, experiment summaries, source manifests, and code paths. Omit process exhaust such as phase logs, command transcripts, tool plumbing, commit/PR status, or implementation progress unless it is concise decision evidence.

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

[Optional links to discussions, specs, plans, research, code, docs, review evidence, KTDs, incident reports, experiment summaries, or source manifests. Use repo-relative paths for local project evidence.]
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

Ask one targeted question at a time. Challenge weak answers directly and tie the challenge to the failed ADR gate:

| Weak input | Gate at risk | Better response |
| ---------- | ------------ | --------------- |
| "We chose it because it is better." | alternatives/consequences | Ask what measurable force, constraint, or quality attribute makes it better, and what cost is accepted. |
| "The plan already says to do it." | decision readiness | Ask whether the plan's KTD is accepted as a durable project decision or only a local execution choice. |
| "The reviewer asked for it." | source authority | Ask whether the finding was validated and whether the project accepts the resulting decision. |
| "The bug proved it." | context evidence | Ask for the confirmed causal chain and why a local fix is insufficient. |
| "The metric improved." | consequence honesty | Ask for the baseline, hard gates, immutable evidence, and unacceptable ways to satisfy the metric. |
| "The current code does this." | authority/freshness | Ask whether code reflects an accepted decision, drift from an accepted ADR, or an unrecorded supersession. |

Do not accept a weak ADR after arbitrary rounds. If the decisive information remains missing, emit the blocked ADR packet.

## Validation Findings And Readiness States

Use structured findings when validating a draft ADR or evaluating an ADR candidate.

| Field | Meaning |
| ----- | ------- |
| ADR gate | decision readiness, ADR bar, project convention, context, one decision, alternatives, consequences, immutability, variant fit, source authority, freshness |
| Severity | blocking or advisory |
| Type | error or omission |
| Evidence | exact text, source artifact, related ADR, rule, code path, or missing required section |
| Affected section | ADR section or source decision field affected |
| Consequence | why future maintainers would be misled or blocked |
| Suggested correction | one concrete correction, owner route, or blocked next action |
| Readiness state | ready to write, ready for approval as Proposed, rejected below ADR bar, blocked for missing evidence, supersession required |

Suppress false positives:

- style-only preferences that do not affect future-maintainer understanding;
- requests for implementation steps, test plans, or rollout choreography;
- demands to create ADRs for routine fixes, local refactors, or already-covered decisions;
- product/spec questions already settled upstream;
- stale review comments, unvalidated findings, or pre-existing debt that has not become an accepted/proposed decision.

## Review Checklist

Before calling an ADR ready, verify:

- The ADR records one decision.
- The title is specific and searchable.
- Status and date are present.
- `Proposed` means ready for approval, not still being discovered.
- Context is factual, not advocacy.
- Source evidence is classified and source breadcrumbs are portable.
- The decision is active and actionable.
- Alternatives are concrete and rejection reasons tie back to context.
- Consequences include positives and negatives.
- Related or superseded ADRs are linked.
- Numbering and path follow project convention.
- Existing coverage and freshness conflicts were checked.
- Accepted ADR history is not rewritten.

## Blocked ADR Packet

Use this when the ADR cannot be created safely.

```markdown
# ADR Blocked: [short title]

Status: Blocked
Requested ADR path: [path or unknown]
Blocking gate: [decision readiness | ADR bar | project convention | existing coverage | source authority | context | one decision | alternatives | consequences | immutability | freshness]
Readiness state: [blocked for missing evidence | rejected below ADR bar | supersession required | owner decision needed]

## Missing Evidence

## What Was Checked

## Source Authority Or Freshness Conflict

## Why ADR Creation Cannot Continue Safely

## Smallest Next Action
```
