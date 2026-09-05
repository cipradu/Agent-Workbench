# Verification Cadence Alignment

## Scope And Decisions

Outcome: Align verification timing and breadth so checks can guide unfinished implementation, required acceptance remains complete, and unchanged evidence is not repeatedly collected without a reason.
Non-goals: Deployment, installed-copy edits, commits, pushes, new test infrastructure, changed permissions, changed review warrants, changed plan sequencing, and the remaining Astra refinement topics.
Target boundary: Existing cadence and verification sections in all five `harness-instructions/` variants, all four `agents/*/coder` adapters, and `skills/project-rules/SKILL.md`; evaluator evidence here and project continuity. Preserve the earlier stop-routing changes and unrelated `agents/claude/research.md` delta.
Acceptance proof: Fixed before/after decision cases; section parity; Codex TOML parsing; bounded delta from current uncommitted source; preservation of mandatory acceptance, review, and scope controls; independent review of the completed source state.
Expansion or re-plan triggers: A newly discovered verification owner contradicts the policy; new mandatory gates or authority become necessary; plan order or review warrants change; repeated behavior failure after one focused correction.
Lane: high_assurance
Escalation triggers present: Shared policy changes when verification may run and how acceptance scope is selected across harnesses; a mistake could suppress required proof across projects.
Named uncertainties: How targets resolve the current cadence contradiction; whether the distinction preserves acceptance while avoiding unnecessary repetition.
Diagnosis warranted: yes — inspect the source conflict and test its consequence without assuming an observed incident.
Spec warranted: no — the user-approved outcome plus this bounded contract leaves no separate engineering decision unresolved.
Plan warranted: no — one coherent correction without rollout, multiple executors, or dependency-sensitive implementation units.
Delegation warranted: yes for fresh behavior targets and independent acceptance; implementation stays with the coordinator.
Implementation review warranted: yes — independent judgment must check that feedback timing and proportional breadth preserve acceptance.
Review cadence: single_final — one complete runtime delta.
Review depth: standard — focused policy semantics and evidence consistency.
Review semantic lanes: verification timing, scope, evidence freshness, preserved acceptance and authority.
Re-review rule: contingent_acceptance
Final complete gate warranted: yes — source identity, controls, behavior results, and review must agree.
State/evidence identity: Exact in-session preimages and SHA-256 per source; HEAD alone omits the preceding uncommitted adjustment.
Outcome control: mapped — implementation produces the candidate for behavioral comparison and review; accepting review plus exact proof produces closure and continuity.

## Source, Diagnosis, And Ownership

Source classification: reasoned provisional behavior signal supported by a directly observed instruction contradiction. No live failure or reduced cost is claimed before testing.

The harness `work_unit_and_verification_cadence` prohibits checks while another edit is planned, then allows executable checks within a unit. Its `verification_loop` says to skip checks whenever more work is known. `project-rules` Step 12 repeats the prohibition. Coder diagnostics and repository-wide checks operate at logical boundaries, but hygiene ordering can be read as preceding every check. `testing-strategy` Step 2 and `references/test-postures.md` already require feedback between test and implementation; its coverage reference already selects affected and broader gates by risk.

The source defect is competing instructions for the same decision. Delayed feedback and unnecessary broad checks are inferred consequences; the baseline tests that inference. Correct the existing distinction, not the test framework or loader. Exact searches over `harness-instructions/`, `agents/`, and `skills/` found the conflicting clauses in the named owners. No new script, hook, skill, or enforcement mechanism is justified. Mechanical checks prove parity and syntax; simulations and review assess interpretation.

`project-rules` remains a portable discipline/process skill with unchanged trigger, opening structure, authority, and scope. Target its existing completion-verification section and matching rationalization/red flag. Always-on policy stays in the harness; execution application stays in coder; test posture, seam, case selection, and commands stay with `testing-strategy`. Reuse the testing skill without duplicating its procedure or adding references. Existing skill inventory and lighter-mechanism check favor correcting the deployed instruction owners, not creating another capability.

Leading concept: implementation feedback and completion evidence have different timing. Feedback resolves a named uncertainty or checks a test-first expectation. Completion evidence proves the declared outcome at its required checkpoint. A feedback check does not finish a plan unit or bypass acceptance. Knowing that work remains does not make feedback useless. Reuse depends on relevant source, test setup, environment, and the governing gate.

Preserve the declared logical unit; no checks merely to confirm a successful edit; prose formatting at the end of a revision; early source or semantic investigation when it changes the next edit; all applicable mandatory tests and review checkpoints; diagnosis of failures; truthful skipped/blocked evidence; and existing scope and mutation limits. Select behavior evidence for prose control artifacts without treating formatting as semantic proof.

## Frozen Evaluation Contract

Decision claim: Targets choose check timing and breadth from the next decision and required acceptance, including while edits remain, without broad gates by habit or stale/partial completion claims.

All six cases are synthetic, reasoned provisional scenarios from current source. Prompts and criteria stay fixed across baseline and post-change runs:

- VC1 test-first feedback: run the new behavior test before implementation and investigate an unexpected failure cause.
- VC2 unfinished work with an unresolved integration choice: run the focused diagnostic before the dependent edit; no whole-project gate merely for feedback.
- VC3 prose polish: defer formatting/readback for reassurance until the planned revision is complete; formatting cannot prove content.
- VC4 required acceptance: preserve a mandatory aggregate check and warranted review despite focused tests passing.
- VC5 evidence reuse: reuse unchanged sufficient evidence when permitted; rerun affected evidence after fixture changes; retain an explicit fresh-run requirement.
- VC6 prose policy behavior: allow scoped behavior evaluation to inform the next rule edit; do not claim final acceptance of an unfinished artifact.

Target-visible boundary: Fresh non-inheriting target receives the same scenario prompt and may read only current Codex harness/coder sources, project-rules, testing-strategy, and that skill's selected runtime references. No evaluator criteria, prior results, or expected answers. Source reads are allowed; no file writes, test execution, external actions, or native-app changes. Return decisions as text. Isolation is procedural and target-reported unless independent observation establishes more.

Maximum fresh runs: 3 — baseline, post-change, and at most one affected-case rerun. Maximum focused causal corrections: 1. Reviewer default: one configured implementation-reviewer for shared acceptance-policy consequences. Completion reserve: full source correction, decisive checks, report, review reconciliation, and continuity take priority over optional evidence. Downshift order: omit model comparisons, duplicate controls, native harness trials, convenience artifacts. Expand only for a distinct consequential failure or changed hypothesis. Stop on passing evidence and acceptance; correct only an observed loophole; return to causal design after repeated failure; discard infrastructure-invalid evidence without relaxing criteria.

Baseline eligibility: pending. If decisions already pass, record that honestly and reassess whether source clarification alone justifies the skill delta. Do not invent a failed incident or claim measured behavioral improvement.

## Verification And Recovery

Use native structured patches for exact sections. Current preimages are retained in-session; never restore whole files from HEAD or discard prior work. Recovery reverses only this task's hunks.

At the complete runtime boundary, check shared-section parity, Codex TOML, unchanged testing owners and unrelated edits, exact delta, and hashes. Formatting is a diagnostic, not behavior proof. Metadata, opening order, invocation, and references remain unchanged; quality review checks that each changed clause serves a tested decision and preserves the existing owner. The report retains prompts, returned evidence, identities, limits, and review disposition. Continuity records current acceptance and next action; it grants no deployment authority.
