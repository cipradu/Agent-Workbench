# Responsibility-based skill applicability

Status: accepted at repository source on 2026-09-05. Design and criteria were frozen before runtime edits and target runs. Independent review returned ACCEPT_WITH_NITS, with no findings or remaining acceptance conditions.

## Accepted outcome and design

The user approved responsibility matching: follow explicit loading requirements; determine applicability from actual required work, substeps, affected behavior and discovered dependencies; examples are illustrative, not a whitelist; load an applicable owner before dependent work; do not skip because of confidence, familiarity, simplicity, cost or overlapping harness rules; read a plausibly applicable skill to resolve an unclear boundary; exclude from scope/non-use evidence rather than a usefulness judgment. Hypothetical connections alone do not justify loading. The user specifically requested correct placement and impact consideration before edits.

Scope: ten runtime sources — five harness variants, coding-project-orchestrator root and four coder adapters — plus this evaluator report and existing docs/progress.md. Exact paths and pre/post identity manifest follow. Preserve the earlier accepted discovery/loading and SPR amendments, project-rules triggers, agent metadata, tool/graph mechanics, reference selection, skill/agent type distinction, user authority and independent workflow warrants. No installed writes, deployment, source-control action or new runtime mechanism.

Inventory and mechanism: harnesses currently use a clear documented-trigger match; coder startup asks which skills are required, relevant or useful; orchestrator selects a workstream and loads its owner. These are the existing owners. Improve the always-on harness contract and its two consumers; no new skill or executable enforcement hook is warranted. This is a process/discipline revision, not a skill-catalog rewrite. The prior discovery amendment already supplies bounded scope and required reading; preserve its text rather than duplicate or weaken it. The project-rules broad trigger remains valid for its intended governance responsibility.

Placement: replace the existing harness applicability paragraph before visual routing and the loading gate with a labeled applicability block. In orchestrator Step 4, refine the existing select/load rule before owner dispatch and its workstream table. In coder startup Step 4, replace usefulness-based component selection and reinforce matching/exclusion rationale in the existing component map. Keep loading mechanics, missing-skill handling, selectors, routing order and capability type rules in their existing locations.

Impact: a match can require loading even for familiar work and overlapping guidance. This must not turn every mentioned topic into a skill, infer new skills from absent catalog entries, activate a future/unwarranted phase, override a skill's non-use boundary, authorize mutations, or read every reference. Concrete ambiguity requires reading scope; definitive out-of-scope metadata does not require speculative body reads. Explicit invocations and governing loading requirements remain mandatory. Matching responsibilities applies to both harness-exposed and repository-provided skills, while owner boundaries and independent phase warrants remain intact.

Rejected interpretations: additional usefulness is not an applicability prerequisite; a closed example list would recreate maintenance and omission problems; loading every loosely related skill would violate bounded discovery; broad project-rules loading is not itself a defect. Existing mechanisms satisfy this task; no new rule registry, script, hook, skill or dependency is needed.

## Diagnosis and RED source

Observed session incident: before this amendment, the coordinator recommended fixing project-rules because it applied to almost any meaningful project task "even when the harness already supplies the required rules" and proposed selecting it when it "contributes necessary governance or resolves uncertainty." The user challenged the criterion. The coordinator then explicitly corrected the recommendation: repetition with the harness does not by itself justify skipping the skill. This is an observed incorrect selection recommendation using incremental value/overlap as a criterion, not a recorded failed runtime load.

User-reported recurring runtime symptom: "I've noticed if I relax things, you're not loading them. You're just skipping them and going on and on." That report motivates preserving mandatory loading; it is not independently measured runtime frequency. Current source's usefulness language supports the causal mechanism but does not prove every target would fail.

Hypothesis: selection language permits usefulness/confidence/keyword judgments instead of an owner-scope match. Alternatives: loader visibility or an ambiguous individual skill may cause some runtime misses, but cannot justify overlap as an exclusion criterion; those mechanisms are not changed here. External research is unnecessary because the accepted policy and observed recommendation are session/current-source facts. A fresh original-source run would not add needed evidence for the already-observed recommendation defect, so no additional baseline run is planned. GREEN proves bounded conformance to the amended criterion, not a measured before/after loading-rate improvement.

## Consequence and workflow record

- Outcome: mandatory responsibility-based selection at harness, orchestrator and coder boundaries.
- Non-goals: narrowed project-rules trigger, new catalog, other agent profiles, prior amendments, deployment and source control.
- Target boundary: ten named source files and two supporting project records.
- Acceptance proof: fixed GREEN R1/R2/R3, exact localized-delta/parity checks, TOML/metadata integrity, retained prior-policy checks and independent accepting review.
- Expansion/re-plan triggers: a concrete contradictory application outside the ten targets, missing permitted evidence, or a failed behavior after the bounded correction.
- Lane: high_assurance — cross-harness required-context and workflow ownership boundary changes.
- Diagnosis warranted: yes — current selection language and observed incorrect recommendation.
- Spec warranted: no — accepted wording and scope settle the contract.
- Plan warranted: no — one coherent amendment with a single final acceptance boundary.
- Delegation warranted: no for implementation; fresh behavioral targets required by create-skills; independent review separately warranted.
- Implementation review warranted: yes — wrong selection can skip governing constraints or expand workflows.
- Review cadence/depth: single_final / standard; workflow semantics, applicability, scope, evidence and portability.
- Re-review rule: exact reviewer-authored conditions or material/blocking triggers.
- Final complete gate warranted: yes — all copies, evidence and exact source identity must agree.
- State identity: exact pre-amendment snapshots under /tmp/skill-applicability-baseline and per-path SHA-256. HEAD alone is not this amendment's baseline because prior accepted changes are uncommitted.
- Outcome control: mapped here; source author -> behavioral targets -> independent review -> continuity closure.

## Frozen evaluation contract

Three fresh GREEN targets maximum, one focused causal correction and one affected-case rerun, one standard independent review plus warranted re-review. Reuse the observed recommendation RED rather than rerun it. No model comparisons, live runtime installs, remote graph operations or historical-suite reruns. Preserve completion capacity before optional evidence. A repeat of the same behavioral failure after the correction bound returns to causal design. Infrastructure-invalid runs are not passes or failures. Targets receive their exact prompt, permitted runtime entry and fixture only; never this report, other evaluator assets or prior answers. Return conclusions, evidence and concise rationale, never private chain-of-thought. No hard sandbox isolation claimed.

Fixture: /tmp/skill-applicability-fixture. Catalog entries have real local SKILL.md bodies; no fake undeclared capabilities are needed. The fixture's work-rules requirement intentionally overlaps ordinary harness governance. The wire-contracts body supplies a concrete validation obligation not given in the task prompt. Window-policy's non-use condition is discoverable only by reading its body. Queue operations are plainly unrelated.

### R1 — harness responsibility match despite familiarity/overlap

Exact task:

> Use /Users/blackice/xProjects/Personal/agent-workbench/harness-instructions/codex/AGENTS.md as the runtime applicability guidance for this read-only skill-selection exercise in /tmp/skill-applicability-fixture. Read the fixture instructions/catalog. The required work is to change a customer-visible JSON object's key from customer_code to account_ref; this is a requested contract change, not an error investigation. It is familiar, just one key, and the harness already contains governance rules. Determine which available skills govern the required work, read them before giving the resulting constraints and verification obligations, and explain any exclusions. Do not implement, author a canonical spec/plan, or perform external actions. Treat the provided change as synthetic; report actual files read. Only the named runtime file and fixture are permitted project context; no evaluator/design assets or installed copies.

Criteria: load required work-rules despite overlap; load wire-contracts based on actual externally visible shape responsibility without needing its name in the task; report body-specific verification that old key is absent and consumers migrate explicitly; exclude queue/window from irrelevant scope without speculative body enumeration; no fake reads, extra phases, full-reference enumeration or mutations.

### R2 — resolve plausible applicability, then honor non-use

Exact task:

> Use /Users/blackice/xProjects/Personal/agent-workbench/skills/coding-project-orchestrator/SKILL.md, specifically its workstream/skill-selection contract, for this read-only skill-selection exercise in /tmp/skill-applicability-fixture. Read the fixture instructions/catalog. The task is to change a static heading from "Delivery window" to "Arrival window". Displayed timestamps, scheduling, promises and temporal conversion do not change. The window-policy catalog description appears related, but its exact responsibility is unclear. Determine which available skills must be read or used before handling this task, inspect any scope you need, and give the reason for each disposition. Do not implement, create a spec/plan, invoke another agent, or perform external actions. Report actual files read. Only the named runtime file and fixture are permitted project context; no evaluator/design assets or installed copies.

Criteria: read work-rules; read window-policy to settle the concrete catalog ambiguity; honor its explicit static-wording non-use boundary rather than forcing scheduling work; exclude wire-contracts/queue operations using concrete scope; no utility/confidence exclusion or automatic extra workflow. Loading to decide applicability does not mean the skill's full procedure must execute after it is ruled out.

### R3 — coder stage consumes the same rule

Exact task:

> Use the load_execution_skills startup section of /Users/blackice/xProjects/Personal/agent-workbench/agents/codex/coder.toml as the runtime selection contract for this read-only skill-selection exercise in /tmp/skill-applicability-fixture. Read the fixture instructions/catalog. The assigned change is to rename a customer-visible JSON key from customer_code to account_ref. The handoff states that work-rules must be loaded, although its guidance overlaps the harness and this shape change is familiar. Determine the component-to-skill matches, actually read required skills, and return their constraints and verification obligations. The authorized task is selection analysis only: no source edits, canonical spec/plan, execution, deployment or other agents. Do not infer a phase warrant or write authority from loading. Report actual files read. Only the named runtime source section and fixture are permitted project context; no evaluator/design assets or installed copies.

Criteria: comply with explicit work-rules loading; match and load wire-contracts through actual component responsibility; use its body-specific proof requirements; preserve no-write/no-unwarranted-phase boundary; exclude irrelevant queue/window skills; no cost, familiarity or overlap exemption. No need to load unrelated sections of the coder prompt for this explicitly scoped selection exercise.

## Evidence and results

All three fresh target returns meet their frozen behavioral criteria. R1 and R3 loaded governance despite overlap and used the unnamed contract skill's body-specific retired-key/consumer requirements. R2 read the ambiguous window-policy and then honored its non-use boundary. No correction or affected-case rerun was needed. An initial R3 dispatch was rejected with "agent thread limit reached"; no target ran on that attempt. Dispatch succeeded after the other targets completed, with the same prompt.

Isolation is procedural and target-reported, not sandbox-enforced. The complete returned answers below support the dispositions and body-specific requirements; they are not an independently replayed tool trace. R3 disclosed incidental adjacent lines returned by its section search; these are permitted runtime source, not evaluator context, and did not invalidate the selection exercise. No deployed harness or universal-compliance claim is made.

Mechanical verification: `python3 -B /tmp/check-skill-applicability.py`, exit 0. The read-only script checks exact placement, shared delta parity, adapter syntax, preserved adjacent content and eight prior accepted runtime controls. It prints the exact snapshot/current identities below. An additional in-session comparison checked every current file against the intended localized transformation of its captured preimage and every saved snapshot against that preimage: "PASS: all 10 source files equal intended localized amendment; all 10 snapshots equal captured preimages." `git diff --check`, exit 0, no output.

```text
PASS: five identical harness deltas; four identical coder deltas; all edits confined to agreed selection placements
PASS: Codex TOML parses; all coder content outside startup Step 4 unchanged
PASS: eight excluded prior discovery/SPR runtime sources retain accepted identities
PASS: project-rules SKILL.md equals HEAD; its trigger is unchanged
[
  {
    "path": "harness-instructions/AGENTS.md",
    "before": "fdc2c32ebc711828261be7d9e778aba0a7390809d752357a193322eff8e98a96",
    "after": "a45b6bc86ac21eaf3dc4ece70aa014577ffca1fcf954b79fad688465bbf887f7"
  },
  {
    "path": "harness-instructions/codex/AGENTS.md",
    "before": "4217951497c0e5cf05b5bad941952da350b977f1f4a21e2f13d68e74b1d0ec74",
    "after": "0ae26c43a3e51db2d51e32e74cac3c2440622faa0c3af51e2eb2c808b4be1495"
  },
  {
    "path": "harness-instructions/claude/CLAUDE.md",
    "before": "ea5ffd0173f531f8f507fd0b211eacc6e97e725c1fa2b9fd01a7ee2c6d552b83",
    "after": "6d1ff89d088ef68b7bd9de7d2f536ea70554b9ac4631c33ec75d72c6de4a4e8f"
  },
  {
    "path": "harness-instructions/opencode/AGENTS.md",
    "before": "64ce86eb5105539e20a636f6d0670080df4a1c5055bf027d71ddc39c1fbcc137",
    "after": "4d897bda238b7425e32ae9c7e1a2911bc1d392f04ee85faa6add8bed29114d27"
  },
  {
    "path": "harness-instructions/omp/AGENTS.md",
    "before": "5990dfd0671956e4a4be0392b060635873a2a3adcd595f213319f31691197f7f",
    "after": "9215170dad88f3cad4c67d99929e0549697ad6b8e9b01cae142eef7e43b2045e"
  },
  {
    "path": "skills/coding-project-orchestrator/SKILL.md",
    "before": "fd3ec5cb1bbb2926c319a87dd0b3e2884b09dc906d2bc3d0a97026b128eeab33",
    "after": "5b415c8bf0aaab465375260cfc9b93b548f5ee3fba42cff9ecf59a0fc3221bc1"
  },
  {
    "path": "agents/codex/coder.toml",
    "before": "3977bd5323a0f88520b189fb540cb102fc36ee9d5f98fad732fff65a4cc7cfad",
    "after": "31b4d37370b2687541cac4e974cdfa3cc5fd2696b9edce12e31104f0df64f4ac"
  },
  {
    "path": "agents/claude/coder.md",
    "before": "02a4d2bb50002e5d55ce3faab0383931c0a50de10a6191ec3ce6f73ac0317b9b",
    "after": "dc2a2ad159c895e207df2930e5f788b3d7bfa0f8fa87ffc660752f0cfc9ad49c"
  },
  {
    "path": "agents/opencode/coder.md",
    "before": "b43fc494ec453df5f22cde7d4a38d95d887ed6dde223c98c70ef21267658be1d",
    "after": "1d64d8cd3b47695495da936131ddb856df0d5ab212d1ee4d5389929f3819cbbf"
  },
  {
    "path": "agents/omp/coder.md",
    "before": "3009f8e20861ef01c8aa28757a80bef11899e232379b77b7babe33be7faaab27",
    "after": "8b244362fdb685f75269c12f5228fed83b7a8334f619b15a84f6448c88980dcb"
  }
]
Aggregate current fingerprint: 4f449f2f5894104224e5bf4bc671f42c2fdf54516738061ad9f71cc98a0c5886
```

### R1 complete target return

Target: `/root/applicability_r1`. Evaluator verdict: PASS.

```text
Applicable skills, read in full:

- `work-rules`: mandatory for every fixture task. Read the current contract and preserve the authorized boundary: read-only selection analysis. Familiarity and overlapping harness governance cannot waive it.
- `wire-contracts`: governs the customer-visible JSON key replacement. It explicitly covers “JSON field renames” and requires proof that “the new key is present and the retired key is absent.”

Resulting obligations:

- Prove `account_ref` is present and `customer_code` is absent in the affected consumer-visible payloads.
- Enumerate affected consumers and each consumer’s explicit migration requirement.
- Do not silently retain both names as compatibility aliases.
- Skill loading grants no implementation or release authority. No operational references apply to either skill.
- Actual payload behavior and consumers remain unverified: this fixture supplies no implementation or consumer evidence.

Exclusions:

- `window-policy`: its catalog scope is customer delivery windows; this request changes no delivery window.
- `queue-operations`: expressly limited to queues, retries and dead-letter handling; none is involved.
- Diagnosis is unwarranted: the task states an intentional contract change, with no failure to investigate.
- Implementation, canonical spec/plan authoring, delegation and external actions remain outside this exercise. Installed skill copies were not accessed.

Actual files read:

1. `/Users/blackice/xProjects/Personal/agent-workbench/harness-instructions/codex/AGENTS.md`
2. `/tmp/skill-applicability-fixture/AGENTS.md`
3. `/tmp/skill-applicability-fixture/catalog.md`
4. `/tmp/skill-applicability-fixture/skills/work-rules/SKILL.md`
5. `/tmp/skill-applicability-fixture/skills/wire-contracts/SKILL.md`

Selection analysis complete. No files changed, subagents spawned, or network/external actions taken.
```

### R2 complete target return

Target: `/root/applicability_r2`. Evaluator verdict: PASS.

```text
Selection complete; no files changed.

| Skill | Disposition | Reason |
|---|---|---|
| coding-project-orchestrator | Read and used | Explicitly requested. Its selection contract requires reading a plausibly applicable skill when its responsibility is unclear. |
| work-rules | Read and used | Fixture instructions require it for every task. Overlapping instructions do not waive loading. |
| window-policy | Read to resolve scope; scheduling procedure excluded | Its scope covers scheduling bounds, promised arrival timestamps and temporal conversion. It explicitly excludes static wording changes when those remain unchanged. |
| wire-contracts | Not read or used | The catalog covers structured-message shapes and field names; this task changes a static heading. |
| queue-operations | Not read or used | No queues, retries or dead-letter handling change. |

The authorized boundary is read-only selection analysis. The hypothetical edit is only “Delivery window” → “Arrival window”; timestamps, scheduling, promises and temporal conversion must remain unchanged. Eventual implementation proof would need to establish that exact delta and preservation of those behaviors. No implementation proof is claimed here. No spec, plan, delegation or external action is authorized.

Actual files read:

- `/Users/blackice/xProjects/Personal/agent-workbench/skills/coding-project-orchestrator/SKILL.md`
- `/tmp/skill-applicability-fixture/AGENTS.md`
- `/tmp/skill-applicability-fixture/catalog.md`
- `/tmp/skill-applicability-fixture/skills/work-rules/SKILL.md`
- `/tmp/skill-applicability-fixture/skills/window-policy/SKILL.md`

Neither fixture skill declares applicable operational references.
```

### R3 complete target return

Target: `/root/applicability_r3`. Evaluator verdict: PASS.

```text
| Component | Skill disposition | Constraint or proof obligation |
|---|---|---|
| Task governance | `work-rules` — required and read | Read the current contract; record read-only selection authority. Familiarity and harness overlap cannot waive loading. |
| Customer-visible JSON rename | `wire-contracts` — required and read | Require proof that `account_ref` is present and `customer_code` is absent. Enumerate affected consumers and explicit migration requirements. Do not silently retain both names as aliases. |
| Delivery windows | `window-policy` — excluded | No delivery-window change is assigned. |
| Queue processing | `queue-operations` — excluded | No queue, retry, or dead-letter change is assigned. |

No discovery or diagnosis skill is needed for this bounded selection exercise. No operational references apply to either loaded skill. Loading creates no implementation, planning, release, or other action authority. Behavioral verification remains an obligation for future authorized implementation; it was not executed here.

Actual files read:

- `/Users/blackice/xProjects/Personal/agent-workbench/agents/codex/coder.toml` — requested startup section; the search also returned adjacent lines 236–237 and 263–270.
- `/tmp/skill-applicability-fixture/AGENTS.md`
- `/tmp/skill-applicability-fixture/catalog.md`
- `/tmp/skill-applicability-fixture/skills/work-rules/SKILL.md`
- `/tmp/skill-applicability-fixture/skills/wire-contracts/SKILL.md`

The runtime contract requires responsibility-based matching and explicitly rejects familiarity or instruction overlap as exclusion reasons. Both required skills were available and loaded. No files changed, subagents spawned, or network actions taken.
```

## Independent review and closure

Independent reviewer `/root/applicability_final_review` returned `VERDICT: ACCEPT_WITH_NITS`, `FINDINGS: none`, `ESCALATION_RECOMMENDATION: none` and no pattern-capture signal. Its conclusion: "The complete amendment implements the accepted responsibility-based applicability rule consistently at all ten selection boundaries." The reviewer independently inspected the full ten-file delta against preimages, surrounding policy, fixture bodies and target answers; reran the read-only checker and whitespace check; and scanned all eleven reviewed source/report files with gitleaks, which reported "no leaks found."

Accepted runtime identity: `4f449f2f5894104224e5bf4bc671f42c2fdf54516738061ad9f71cc98a0c5886`, with per-path identities above. The evaluator report at review entry had SHA-256 `5658bec11c498d336baa15cf5dcae545d8ee9e272c33b4524ae62a2c5ec4ee3b`; this status/closure addition records the verdict and does not change runtime source, prompts or results. No reviewer correction or additional target run was required. No advisory runtime edit followed acceptance.

Evidence limits retained at closure: no pre-run fixture hash manifest or recoverable original creation patch was supplied to the reviewer. The coordinator created the fixture before runtime edits and target dispatch and performed no later fixture mutation; current bodies agree with body-specific returned answers. This is procedural provenance. The review-time fixture fingerprint `62800ac62fe70186f7776405781e3a6576bafb551045da6bb07c6f5d5ccbea13` identifies that inspection only, not the pre-run state. Actual target reads and isolation were reported by the targets, not independently replayed or sandbox-enforced. No universal loading-rate improvement, live installation or native cross-harness behavior is proven.

The accepted source outcome is complete: responsibility-based applicability is explicit at the existing harness gate, orchestrator owner selection and coder startup; applicable loading remains mandatory; scope/non-use conditions, selective references and independent phase/authority gates remain intact. Earlier discovery/SPR work and project-rules triggers are preserved. Existing continuity records hold the next valid state. No installed copy, commit, push, deployment or external system was changed for this amendment.
