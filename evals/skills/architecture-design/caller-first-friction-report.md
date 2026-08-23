# Caller-First Interface And Repeated-Friction Report

Status: `PASS`

## Decision Claim

Architecture design must expose caller burden before an interface is accepted and must reopen an accepted design when implementation produces repeated same-shape caller friction. Neither mechanism should trigger universal design ceremony, react to one subjective awkward call, or absorb implementation planning.

## Evaluation Contract

- Source basis: `docs/skill-analysis/cursor-plugins-exhaustive-skill-analysis.md`, Step 3.
- Scenarios: two materially distinct architecture decisions.
- Maximum fresh RED runs: two, one per scenario.
- Maximum focused correction: one combined architecture-owner correction.
- GREEN runs: one unchanged rerun for each failed scenario.
- Reviewers: none.
- Completion reserve: preserve enough context and time to apply the focused correction, run required GREEN targets, and complete the Unit 3 source gate.
- Optional-evidence downshift order: model comparison, extra caller variant, additional target, independent review.
- Expansion trigger: only a new result that changes the causal hypothesis or exposes a distinct owner boundary.
- PASS stop: every fixed criterion passes without evaluator data.
- CORRECT stop: the target blocks on a genuinely missing force that cannot be inferred from the scenario.
- FAIL stop: one or more fixed criteria fail.
- INFRASTRUCTURE stop: the target cannot load the runtime skill or permitted operational reference; the run is invalid evidence.

## Target Context Boundary

Each target receives normal harness and repository instructions, `skills/architecture-design/SKILL.md`, the unchanged scenario prompt, and ordinary read-only repository access. It may load only operational references selected by the runtime skill. It receives no evaluator assets, expected behavior, pass/fail criteria, analysis report, prior target output, or verdict summary. It must not edit files, dispatch another agent, or perform external research.

## Scenario ARCH-CALLER-01 — Caller-First Usage Sketch

Source label: `provisional external-pattern gap`

Prompt:

```text
Apply architecture-design to assess this proposed interface before implementation. Do not edit files.

We are introducing a notification policy module used by an HTTP handler and a scheduled retry worker. The proposed interface is:

`prepare_notification(user_id, template_id, channel, retry_count, request_id, timeout_ms, provider_options) -> ProviderRequest`

The module is meant to own eligibility, template selection, channel fallback, retry policy, and provider-neutral notification intent. The HTTP caller has a request ID and no retry count. The worker has retry state and no request ID. Neither caller should know provider payload shape or timeout policy.

Decide whether the interface is ready to accept. Keep the analysis at the interface/seam level; do not produce an implementation plan.
```

Required behavior:

- Writes a small representative usage sketch for both named callers before accepting or rejecting the interface.
- Uses the sketches to expose caller-supplied mechanism details, irrelevant placeholders, or duplicated choreography.
- Distinguishes the policy contract callers need from provider and execution details they should not know.
- Produces a bounded interface decision, not file structure, implementation units, or broad architecture ceremony.

Target: `/root/arch_caller_red`

Source identity: `3875a27242df8f07b815e2eb952b921a3f186d613cbf2346b408059f93f404a6`

Observed result: The target correctly rejected the leaky interface, separated policy from provider mechanics, and proposed a provider-neutral seam. It did not write representative HTTP and worker usage sketches before deciding, so it did not expose the different placeholder and choreography burdens through the requested caller-first mechanism.

Verdict: `FAIL`

## Scenario ARCH-FRICTION-01 — Repeated Same-Shape Friction

Source label: `provisional external-pattern gap`

Prompt:

```text
Apply architecture-design to this implementation feedback. Do not edit files.

An accepted export interface exposes `start_export(query, format, destination, retry_policy)`. During implementation, both the API caller and the scheduled-job caller had to perform the same three-step workaround: derive a storage key, translate destination errors into the same domain error, and reconstruct retry defaults before calling the interface. A third CLI caller has not been implemented yet. The accepted forces say storage naming, error normalization, and retry policy belong inside the export module. There is no evidence of incompatible caller requirements.

Should implementation continue by adding the workaround to each caller, or should the design decision be reopened? Keep the answer bounded to this signal; do not produce a migration or implementation plan.
```

Required behavior:

- Treats two independent callers with the same workaround shape as evidence against the accepted interface, not as ordinary local implementation inconvenience.
- Reopens the design at the interface/ownership decision and names the violated accepted forces.
- Does not require a third occurrence, wait for the CLI caller, or patch both callers first.
- Does not generalize one awkward call, subjective dislike, or dissimilar friction into a reopen trigger.
- Stops at the architecture correction boundary without implementation sequencing.

Target: `/root/arch_friction_red`

Source identity: `3875a27242df8f07b815e2eb952b921a3f186d613cbf2346b408059f93f404a6`

Observed result: The target treated the same three-step workaround in two independent callers as evidence against the accepted interface, named the violated ownership and locality forces, reopened the public contract, rejected duplication, and stopped before implementation sequencing. It did not wait for the third caller.

Verdict: `PASS`

## Focused Revision Design Brief

Entry mode: existing-skill revision.

Target owner: `architecture-design`.

Recurring behavior failure: Interface analysis can correctly enumerate caller obligations and reject a leaky contract while remaining abstract. Without showing representative calls before acceptance, it can miss placeholder arguments, caller-specific choreography, error handling burden, or mechanism details that become obvious only from the call shape.

Desired behavior: Before accepting an interface or boundary, sketch the smallest representative use from each materially different caller role. Use those sketches as decision evidence for caller burden, hidden complexity, invalid combinations, sequencing, and error handling. The sketches are disposable design probes, not implementation plans or final API syntax.

Mechanism decision: Improve the existing interface-design step and its existing interface-depth reference. Do not create a new skill, template, artifact, reviewer, or mandatory ceremony outside interface/boundary design. The repeated-friction mechanism already passed through current ownership and locality rules, so it remains unchanged.

Skill type: Preserve the current process/discipline skill and its existing reference routing.

Information placement:

- `skills/architecture-design/SKILL.md` makes the caller-first probe a completion condition of Step 3.
- `skills/architecture-design/references/interface-depth-and-seams.md` defines the bounded sketch method and stop condition.
- No other architecture reference or owner changes.

GREEN criteria: The unchanged `ARCH-CALLER-01` case must show separate HTTP and worker caller sketches before the decision, use them to identify irrelevant placeholders and mechanism leakage, preserve provider-neutral policy ownership, and stop without implementation planning.

## Run Ledger

| Scenario | Source identity | Target identity | RED verdict | Correction | GREEN identity |
| --- | --- | --- | --- | --- | --- |
| `ARCH-CALLER-01` | `3875a272...` | `/root/arch_caller_red` | `FAIL` | one focused caller-sketch correction | `/root/arch_caller_green`; `c3cb2d30...`; `b3f389db...`; `PASS` |
| `ARCH-FRICTION-01` | `3875a272...` | `/root/arch_friction_red` | `PASS` | none | not needed |

## Unit Verdict

`PASS`

The unchanged GREEN target produced distinct HTTP-handler and retry-worker usage sketches, used them to expose caller-only placeholders and provider leakage, rejected invalid optional-parameter combinations, preserved provider-neutral policy ownership, and stopped at the interface/seam decision without implementation planning.

Fresh runs: `3/3` maximum used: two RED targets and one GREEN rerun for the only failing case.

Focused corrections: `1/1` maximum used.

Review count: `0`.

Intentionally unchanged mechanism: repeated same-shape implementation friction already triggered the correct ownership/locality reopen behavior in `ARCH-FRICTION-01`; no duplicate instruction was added.
