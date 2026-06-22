# PRD Output Contract

Use this reference only after `SKILL.md` decides whether PRD gates passed or failed.

## Canonical File Location

Default location when creating a new PRD file:

```text
docs/prds/YYYY-MM-DD_HH-mm_{slug}_prd.md
```

Use local 24-hour time with leading zeroes. Do not use seconds. Do not use colons in filenames. The slug must be lowercase kebab-case using only ASCII letters, numbers, and hyphens, derived from the project, product, feature, or capability name.

If the project already has an explicit PRD convention, use that convention and cite the source. Do not overwrite an existing PRD unless the user explicitly asks to revise that file.

## Output Depth Selection

Use the smallest artifact that preserves the product truth downstream readers need.

| Depth          | Use when                                                                                                                                 | Do not use when                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Compact PRD    | one feature or capability needs durable product truth, with limited stakeholder surface                                                  | project/product scope, high ambiguity, or multiple downstream specs need fuller context |
| Full PRD       | project/product scope, high-risk feature scope, multiple stakeholder groups, launch/business considerations, or broad downstream handoff | the feature can be captured clearly in compact form                                     |
| Blocked packet | missing product truth would force invention                                                                                              | enough product truth exists to write compact or full PRD honestly                       |

Do not pad compact PRDs with empty full-template sections. Do not compress full PRDs when the stakeholder, risk, or downstream handoff surface needs more context.

## Compact PRD Form

Use when gates pass and compact depth is justified.

```markdown
# PRD: concise feature or capability title

PRD file: docs/prds/YYYY-MM-DD*HH-mm*{slug}\_prd.md
Slug: kebab-case-slug
Status: Draft | Proposed | Approved | Superseded
Scope type: Feature | Capability
Depth: Compact
Created: YYYY-MM-DD HH:mm local
Source request: concise summary

## Summary

## Problem

### Who is affected

### Current state or workaround

### Impact

### Evidence

## Goals and success

## Requirements

| ID  | Requirement | Rationale | Product acceptance criteria | Handoff |
| --- | ----------- | --------- | --------------------------- | ------- |

## Key workflows or journeys

## Scope boundaries

### In scope

### Non-goals

### Future or deferred

## Assumptions and constraints

### Facts

### Assumptions to validate

### Constraints

## Open questions

### Blocking

### Deferred

## Engineering-spec handoff

### Product decisions to preserve

### Ready for engineering spec

### Blocked before engineering spec

### Explicitly not decided here
```

## Full PRD Form

Use only when all gates pass.

```markdown
# PRD: concise project/product/feature title

PRD file: docs/prds/YYYY-MM-DD*HH-mm*{slug}\_prd.md
Slug: kebab-case-slug
Status: Draft | Proposed | Approved | Superseded
Scope type: Project | Product | Feature | Capability
Depth: Full
Created: YYYY-MM-DD HH:mm local
Source request: concise summary

## Product Summary

### One-Sentence Definition

### Product / Feature Context

### Why Now

## Problem Statement

### What Is Broken Or Needed

### Who Is Affected

### Impact

### Current Workaround Or Current State

### Evidence

## Target Users And Stakeholders

### Primary User

### Secondary Users

### Buyers / Approvers / Operators

### Context Of Use

## Goals And Success

### Primary Outcome

### Secondary Outcomes

### Success Metrics Or Evidence

| Metric / evidence | Baseline or current signal | Target or success threshold | How measured |
| ----------------- | -------------------------- | --------------------------- | ------------ |

## Target Product Scope

### In Scope

### Non-Goals

### Future Or Deferred Capabilities

### Delivery Sequencing Notes

## Product Requirements

### Must

| ID  | Requirement | Rationale | Product acceptance criteria |
| --- | ----------- | --------- | --------------------------- |

### Should

| ID  | Requirement | Rationale | Product acceptance criteria |
| --- | ----------- | --------- | --------------------------- |

### Could

| ID  | Requirement | Rationale | Product acceptance criteria |
| --- | ----------- | --------- | --------------------------- |

### Won't

| Item | Reason |
| ---- | ------ |

## User Journeys Or Key Workflows

### Primary Workflow

### Important Edge Or Failure Workflows

## Assumptions, Constraints, And Dependencies

### Facts

### Assumptions To Validate

### Constraints

### Dependencies

## Risks

| Risk | Why it matters | Mitigation or validation path |
| ---- | -------------- | ----------------------------- |

## Open Questions

### Blocking

### Deferred

## Engineering-Spec Handoff

### Product Decisions To Preserve

### Requirements Ready For Engineering Spec

### Requirements Blocked Before Engineering Spec

### Constraints / Risks Engineering Must Analyze

### Explicitly Not Decided Here

## Changelog

| Date | Change | Source / reason |
| ---- | ------ | --------------- |
```

## Product Requirement Form

```markdown
PRD-REQ-001 - short requirement name
Priority: Must | Should | Could | Won't
Source: user | research | support | analytics | stakeholder | existing doc | assumption
Statement: product behavior or product constraint
Rationale: why this exists and which goal it supports
Product acceptance criteria: observable product-level evidence
Engineering handoff: ready | blocked | needs discovery
```

Use user stories only when they clarify behavior. Do not require a long story inventory when requirements, workflows, and acceptance criteria carry the product truth more directly.

## Blocked PRD Discovery Packet

Use when any hard gate fails. Do not emit the full PRD template.

```markdown
Status: Draft - blocked
Scope type: Project | Product | Feature | Capability | Unknown
Source request: concise summary

## Known Facts

## Assumptions

## Failed Gates

- Gate:
- Evidence:
- Why this blocks a full PRD:

## Missing Product Truth

## Discovery Needed

## Blocking Question

## Downstream Impact

What cannot safely proceed to create-engineering-spec until this is resolved:
```

## Review Checklist

Before presenting a compact or full PRD, verify:

- Problem is not just a solution restated as a need.
- Primary user or stakeholder is specific.
- Impact and current state are stated.
- Success is measurable or observable.
- Requirements are product behavior, not implementation design.
- Each requirement has rationale and product acceptance criteria.
- Non-goals are explicit.
- Facts, assumptions, constraints, dependencies, and open questions are separated.
- Phases are delivery sequencing only; the target product is still defined.
- Engineering-spec handoff states what is ready, blocked, constrained, and not decided.
- Output depth is justified and no section is padded for ceremony.
- Material inferred scope was confirmed or is clearly marked as an assumption.

## Common Output Failures

| Failure                                          | Correction                                                                                                     |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Full PRD with invented users                     | Use blocked packet and ask for audience evidence.                                                              |
| Requirements list full of implementation details | Move implementation detail to engineering-spec handoff constraints only if product-relevant; otherwise remove. |
| No non-goals                                     | Stop and define likely exclusions before presenting the PRD.                                                   |
| "Improve UX" success metric                      | Replace with observable behavior, outcome metric, qualitative evidence, or blocked metric discovery.           |
| MVP framing                                      | Define full target product and delivery sequencing separately.                                                 |
| Open questions buried in sections                | Move them to blocking or deferred open questions.                                                              |
| Full template used for a bounded feature         | Switch to compact PRD unless stakeholder/risk/downstream handoff needs justify full depth.                     |
| Unconfirmed inferred scope written as fact       | Present a synthesis checkpoint, confirm it, or mark the inference as an assumption/blocker.                    |
| Long user-story dump with weak product truth     | Replace with requirements, workflows, and acceptance criteria tied to problem and success.                     |
