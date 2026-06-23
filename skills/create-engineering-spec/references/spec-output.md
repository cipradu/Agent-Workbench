# Spec Output Contract

Use this reference only after the top-level skill decides whether gates passed or failed.

## Canonical File Location

Save engineering specs under:

```text
docs/specs/YYYY-MM-DD_HH-mm_{slug}_spec.md
```

Use local 24-hour time with leading zeroes. Do not use seconds. Do not use colons in filenames. The slug must be lowercase kebab-case using only ASCII letters, numbers, and hyphens, derived from the spec title or primary capability, and normally no longer than 60 characters.

If the target filename already exists, do not overwrite it. Add a numeric suffix to the slug segment before `_spec.md`, for example:

```text
docs/specs/2026-06-18_14-07_user-management-02_spec.md
```

The implementation plan must reuse the exact spec slug segment when creating its corresponding plan file.

## Full Spec Form

Use only when all gates pass.

```markdown
# Spec: concise title

Spec file: docs/specs/YYYY-MM-DD_HH-mm_{slug}_spec.md
Slug: kebab-case-slug
Status: Draft | Proposed | Approved | Superseded
Mode: Greenfield | Brownfield
Created: YYYY-MM-DD HH:mm local
Source request: concise summary

## Decomposition Summary

### Goal

### Actors

### Desired Impacts

### Deliverable Class

### Events / Processes

### Rules / Invariants

### Data Concepts

### Constraints / NFRs

## Research Summary

### Domain Research

### Authority / Existing-System Discovery

### Library / Protocol / Vendor Research

### Compliance / Risk Research

### Constraint Validation

## Fit Analysis

### Greenfield Foundation or Brownfield Fit

### Source / Authority Map

### Planning-Relevant Impact Surfaces

## Scope Shaping

### Problem Baseline

### Appetite / Decision Budget

### Rabbit Holes

### Scope Trade-offs

### Scope Additions / Displacement

### Lifecycle Ownership Cost

## Scope

## Non-Scope

## Domain Model

### Terms

### Actors and Systems

### Sources of Truth

### Invariants

### State Transitions or Flows

## Requirements

## Acceptance Criteria

## Risk Register

## Facts, Assumptions, Decisions, and Open Questions

### Facts

### Assumptions

### Decisions

### Blocking Questions

### Deferred Questions

## Reviewer Guidance

### Must Flag

### Must Not Flag

## Approval Checklist
```

## Requirement Form

```markdown
REQ-001 — short requirement name
Source: user | rule | ADR | existing spec | code/test | external source | assumption
Statement: observable behavior, contract, invariant, or constraint
Acceptance evidence: AE-001 or explicit evidence
Risk addressed: risk ID or `none` with reason
Planning impact surfaces: contracts/data flows/modules/tests/docs/runtime/ops areas to analyze later
```

## Acceptance Example Form

```markdown
AE-001 — short example name
Context/input:
Action/event:
Expected result:
Requirements covered: REQ-001, REQ-002
```

## Risk Register Form

```markdown
RISK-001 — short risk name
Dimension: security/attack | reliability/failure | compliance/regulatory | operational
Description:
Severity:
Likelihood:
Mitigation or acceptance:
Owner/authority:
Verification evidence:
```

## Authority Map Form

```markdown
AUTH-001 — concept or rule name
Authority type: data | business rule | process | interface/API | schema | operational policy | compliance/regulatory | other
Owner/role:
Location/source:
Applies to:
Conflict/tiebreaker:
```

## Blocked Packet Form

Use when any hard gate fails. Do not emit the full spec template.

```markdown
Status: Draft — blocked
Mode: Greenfield | Brownfield

## Decomposition State

## Facts

## Assumptions

## Failed Gates

- Gate:
- Evidence:
- Why this blocks a full spec:

## Missing Source-of-Truth / Evidence

## Required Research or Discovery

## Blocking Question
```
