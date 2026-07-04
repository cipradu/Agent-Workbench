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

## Stable ID Lifecycle

Use stable IDs from the first draft that may be reviewed or handed off.

- Preserve `REQ`, `AE`, `RISK`, and `AUTH` IDs across reordering and wording changes.
- When splitting an item, keep the original ID on the part that preserves the original meaning and create new IDs for new obligations.
- When merging items, record which IDs were merged and why.
- When removing or superseding an item, record its status instead of silently deleting it when downstream artifacts may reference it.
- Preserve stable upstream IDs from PRDs, audits, prior specs, ADRs, plans, or reviews by mapping them to the spec IDs.

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

### Source Scope And Confidence

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

### Product-Domain Inputs To Preserve Or Refine

### Engineering Domain Terms

### Current Vs Target Concepts

### Actors and Systems

### Sources of Truth

### Rules, Invariants, And Permissions

### State Transitions or Flows

### Scenario Probes

### Conflicts And Resolutions

## Requirements

## Acceptance Criteria

## Risk Register

## Facts, Assumptions, Decisions, and Open Questions

### Facts

### Assumptions

### Decisions

### Blocking Questions

### Deferred Questions

## Review Finding Disposition

## Planning Handoff

## Reviewer Guidance

### Must Flag

### Must Not Flag

## Approval Checklist
```

## Requirement Form

```markdown
REQ-001 — short requirement name
Source: user | rule | ADR | existing spec | code/test | external source | assumption
Source scope: target authority | adjacent impact | pre-existing contradiction | historical context | untrusted signal | inferred hint | unsupported
Source confidence: authority-backed | current-system | current-external | verified evidence | weak context | unsupported
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
Modality: automated | manual/human | external-system | blocked | diagnostic-only | hard gate
Proof source:
Blocked/skipped proof:
Degenerate pass to reject:
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
Source scope:
Source confidence:
Applies to:
Conflict/tiebreaker:
```

## Review Finding Disposition Form

```markdown
REV-001 — short finding name
Finding type: decomposition gap | source/authority gap | research-currency gap | domain-model conflict | brownfield-fit gap | stale-source conflict | risk/impact gap | acceptance-evidence gap | implementation leakage | scope drift | unresolved blocker
Affected section or ID:
Evidence:
Confidence anchor:
Consequence:
Blocks readiness: yes | no
Disposition: revised | revised-differently | answered-no-change | invalid-with-evidence | declined-with-harm | deferred-non-blocking | blocked-needs-decision
Resolution evidence:
```

## Planning Handoff Form

```markdown
Spec path:
Slug:
Status:
Mode:
Review state:
Requirement IDs:
Acceptance evidence IDs:
Risk IDs:
Authority IDs:
Non-scope and no-gos:
Open blockers:
Deferred planning-safe questions:
Planning-relevant impact surfaces:
ADR candidates:
External handoff note:
```

The external handoff note may summarize what later commit, PR, publishing, review, or implementation workflows need to preserve. It must not include implementation units, file choreography, git commands, PR mutation, CI watch, tracker filing, or publishing mechanics.

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

## Stale Or Conflicting Source State

## Required Research or Discovery

## Blocking Question

## Durable Residuals
```

## Output Checklist Addendum

Before presenting a full spec, confirm that any reference artifact, source-code example, prototype, screenshot, external implementation, or comparable system used as evidence states what property transfers, what does not transfer, and what target-context difference matters. If that cannot be stated, the reference may remain background context but must not support a normative requirement.
