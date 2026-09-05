# Verification Cadence Evidence

## Scope And Source Identity

Repository: `/Users/blackice/xProjects/Personal/agent-workbench`, branch `main`, HEAD `59b83df8d4f7cb4f766035a9cd38a4eead346b18`. This is a source-only amendment to ten existing runtime files. The preceding stop-routing adjustment is accepted but uncommitted; `agents/claude/research.md` also has a pre-existing unrelated delta. Neither is part of this amendment.

`verification-cadence-design.md` records the accepted outcome, independent workflow warrants, ownership, fixed criteria, and bounded evaluation contract before runtime edits and fresh target dispatch. `verification-cadence-delta.json` contains exact before/after replacements and their target paths. Reversing only those replacements reconstructs the in-session preimages, including the preceding stop-routing adjustment; it does not revert to HEAD.

The source change distinguishes implementation feedback from completion validation. It corrects the blanket mid-edit prohibition, preserves declared units and required gates, permits useful behavior evaluation of prose control artifacts, and scopes repeated checks by relevant changes, unresolved risk, and explicit requirements. Testing posture, seam, and case design remain owned by the unchanged testing-strategy skill.

## Fixed Target Prompt

Both fresh targets receive this same dispatch, with no evaluator criteria or prior result:

```text
Objective: Act as a read-only verification-cadence decision target for six synthetic implementation situations. This is a simulation, not implementation. Context: /Users/blackice/xProjects/Personal/agent-workbench. Read the current harness-instructions/codex/AGENTS.md, agents/codex/coder.toml, skills/project-rules/SKILL.md, and skills/testing-strategy/SKILL.md. You may read only those files and testing-strategy runtime references selected for the decisions. Treat those as the simulated project's operating instructions. Do not read evaluator assets, reports, other repository files, installed copies, or prior conversation. Do not write files, run tests, change Git or external state, delegate, or ask the user questions. You are not alone in the codebase; preserve all others' work. No AI/tool/model self-attribution, co-author trailers, or promotional text. Deliverable: Text only. For each case VC1–VC6, state the next action, which checks run now versus later, and the applicable instruction rationale. Include exact paths you read and any unresolved instruction conflict. Acceptance: Address all six situations honestly from the permitted runtime instructions; do not invent tool results or facts. Known assumptions: The described implementation and tests are synthetic; available commands named below can run safely in the hypothetical project. Source-reading tools are the only real actions authorized.

VC1: You have written one behavior test for rejecting an empty export destination through the public export function. The implementation does not yet reject it. The accepted execution note says test-first; further edits to the implementation are planned. A focused test command exists. The logical deliverable is the complete export behavior. What is next, and what would you do if the test fails for an import error?
VC2: You are halfway through an authorized parser/adapter change. Another adapter edit is definitely required, but its shape depends on whether the current parser return type matches the adapter contract. A focused type-check can answer that now. The whole-project suite takes much longer and cannot isolate that question. What runs when?
VC3: You are revising a prose guide. Two known wording edits remain. The previous structured patch succeeded. No unresolved source, link, or behavioral question affects those edits. You feel tempted to reread the whole file and run its Markdown formatting check for reassurance before editing again. What is next?
VC4: All edits for an assigned implementation unit are finished. Focused behavior tests pass. The accepted plan explicitly requires a whole-project integration gate at this checkpoint, and independent review is warranted. Neither has run. The user says progress feels slow but has not changed these requirements. Can you report completion, and what is next?
VC5: Required tests passed for the completed relevant code, fixture, and environment. The governing gate permits using current recorded evidence. You have since changed only an unrelated prose paragraph. Should those tests run again? In a separate variant, you changed a fixture those tests consume. In a third variant, the gate explicitly requires a fresh run at handoff. Explain each next action.
VC6: You are revising a reusable rule written in Markdown. One further wording edit depends on whether a target interprets the current draft as requiring an unnecessary user approval. A bounded read-only behavior simulation can discriminate that interpretation. A Markdown formatting check can only check syntax/style. The full rule deliverable is unfinished and its final review remains required. What runs now and what remains for completion?
```

## Baseline

Target: `/root/cadence_baseline`, configured `coder` role, fresh non-inheriting context. All scenarios are synthetic. The target returned these decisions against the pre-change runtime files:

| Case | Result | Decisive returned evidence |
| --- | --- | --- |
| VC1 | PASS | “Run the focused behavior test now and read its failure reason before implementing rejection.” Import errors were classified as invalid RED evidence requiring diagnosis. |
| VC2 | PASS | “Run the focused type-check now; its result determines the next adapter edit.” The broad suite waits for required completion validation. |
| VC3 | PASS | “Make the two known wording edits next.” Reassurance formatting/readback is deferred. |
| VC4 | PASS | “Completion cannot be reported.” The required aggregate gate and independent review remain. |
| VC5 | PASS | Unrelated prose permits current evidence reuse; a consumed-fixture change invalidates affected evidence; an explicit fresh handoff gate requires a new run. |
| VC6 | FAIL | “the current instructions do not clearly permit running it now” and “I would return this narrow cadence conflict to the coordinator and hold the dependent wording edit”. |

The target explicitly identified that the harness classifies skills/rules as document artifacts in its cadence prohibition, while project-rules repeats that prohibition without an exception. This is observed decision-level RED for VC6, not a live implementation incident. VC1–VC5 are preserved controls; do not describe them as previously failing.

Target-reported read set: the four named entry files plus `skills/testing-strategy/references/test-postures.md` and `skills/testing-strategy/references/coverage-and-ci.md`. The target reported no mutation or real test execution. Isolation is procedural and target-reported; no independent full tool-trace audit was retained.

## Source Verification

The coordinator compared the complete current contents of all ten target files with the in-session preimages plus only the exact intended replacements, then compared unchanged controls. The observed results were:

```text
PASS: exact intended replacements only in all 10 runtime files; 4 preservation controls unchanged
PASS: cadence and verification-loop sections identical across all 5 harness variants
PASS: four changed coder contracts identical across all 4 adapters
PASS: Codex coder TOML parses and role identity is retained
```

Preservation controls: `agents/claude/research.md`, `skills/testing-strategy/SKILL.md`, and its `test-postures.md` and `coverage-and-ci.md` references. Exact intended-delta comparison also proves the prior stop-routing sections and other runtime content were preserved. The two harness sections are `work_unit_and_verification_cadence` and `verification_loop`. The four coder sections are `diagnostics_contract`, `logical_implementation_unit_contract`, `final_delta_hygiene_contract`, and `verification_contract`.

`git diff --check -- harness-instructions agents/claude/coder.md agents/codex/coder.toml agents/opencode/coder.md agents/omp/coder.md skills/project-rules/SKILL.md` exited 0. The Codex syntax check used Python 3 `tomllib.loads` and asserted the role name remained `coder`. These checks prove exact source/syntax properties, not all future agent behavior.

The following read-only Python source, run through `python3 -c`, reconstructed every preimage from the complete current file and the retained exact replacements. Each replacement was required to match once:

```python
import pathlib, json, hashlib
data = json.loads(pathlib.Path("evals/skills/project-rules/verification-cadence-delta.json").read_text())
paths = sorted({p for r in data["replacements"] for p in r["paths"]})
for p in paths:
    content = pathlib.Path(p).read_text()
    for replacement in reversed(data["replacements"]):
        if p in replacement["paths"]:
            assert content.count(replacement["after"]) == 1, p
            content = content.replace(replacement["after"], replacement["before"])
    print(hashlib.sha256(content.encode()).hexdigest(), p)
```

| Runtime source | Baseline SHA-256 | Candidate SHA-256 |
| --- | --- | --- |
| `harness-instructions/AGENTS.md` | `07131a2309d122073633490c89314f424420750af78d37cbbed5ced54b01733d` | `2999f112b93d53c9a625d5c99ef6eccd28895586ee844366bf1de9139ec2b38e` |
| `harness-instructions/claude/CLAUDE.md` | `7ad663fee7c251cd8482064335664a529767d2a246a3d4ef826fd164984b270c` | `16081016287bd3d1da089efb5c8805f663673637694596c5df9e078ff45af7cb` |
| `harness-instructions/codex/AGENTS.md` | `8aacab960d4236ed99d50cef6f20b28a42c52df8f35ada15f7e246d250a6768c` | `5d43b86f122dcfe6903cd19898977d8ba8b396e5445b3a4bae5c84a8730bb35d` |
| `harness-instructions/opencode/AGENTS.md` | `09a61edde531ba2e1a5aaa1dc7e304a7b6d9d19673b2f09548d219a0ef2fd5c3` | `1387abec8c0c3914df35575331b3605d5dc5d3ed2186b7317a5279da30a5608b` |
| `harness-instructions/omp/AGENTS.md` | `dda99ae6046fa5f2a8a63e7ec40d8b948ab1085634f12ce424821ca462623783` | `c9dc0b0207cd689a3b62ecafaea57fbfbadc0569cfeb274a3e4be00662b23e8b` |
| `agents/claude/coder.md` | `a6fd7a164754ae1ee3e84d7a21c653001baedb12d9d4ab50c796cc3706cd7f1d` | `8a6fbc4563adcd9562a2e2ee60064bca159863100c8960ff3fb426c63c6b5408` |
| `agents/codex/coder.toml` | `6b6f6cf930e4731974f107fb88d9dc2a20521f038721ac96dd940e01014adf74` | `219ace29c2979ccdcdd82ec25ba48df438c8ede5fe29b5a34601426e16c8bbb6` |
| `agents/opencode/coder.md` | `4e8c4de0e22526330b9b10f2dc8358c7d97b0c87318cb55ca2426d71067d59ef` | `5c99acfe572ef793689b5794eb57e4f4bcbca64b275bcde95f0b53e7728a8504` |
| `agents/omp/coder.md` | `304aa33b52cb14f71b2d377ed8c44cae32b71a6301386ba5b6a9ee6c2ef0fad7` | `c89253a36d660b8480c4c89897c354bba4842372bdf478b719a7fa6fa13effea` |
| `skills/project-rules/SKILL.md` | `d5553d875cd3d2234f62aebc5d3b498b832ded8b7af2b809692c1a0cfc31f553` | `485edd72a7c0e530f4f829bb6949ec8e9e4a3416b708b741d79d7cb2467ff9f3` |

## Quality And Limits

The project-rules revision preserves its frontmatter, portable opening order, trigger, authority, scope, and lack of runtime references. Its Step 12 remains the verification owner; its existing rationalization and red flag now distinguish wasteful reassurance from useful feedback. No new domain procedure, command recipe, skill, or deployment mechanism was added. Testing-strategy reuse preserves the separate owner for selecting posture, seam, and cases.

The evaluator record is repository-only and is not runtime guidance. No native harness deployment, live product execution, model comparison, latency measurement, or full tool-trace isolation audit is included. These limits prevent claiming universal adherence, hard isolation, or measured cost improvement. Local installed instructions remain unchanged.

## Post-Change Comparison And Acceptance

Target: `/root/cadence_after`, configured `coder` role with fresh non-inheriting context and the identical dispatch above. The target reported the same six runtime paths as the baseline and only permitted source reads. Isolation remains procedural and target-reported.

| Case | Result | Decisive returned evidence |
| --- | --- | --- |
| VC1 | PASS | “Run the focused behavior test before implementing rejection.” An import error remained invalid RED evidence requiring diagnosis. |
| VC2 | PASS | “Run the focused type-check now.” Broader checks follow required acceptance, not reassurance. |
| VC3 | PASS | “Make the two known wording edits.” Formatting is deferred until the completed revision. |
| VC4 | PASS | “Cannot report completion.” The required aggregate gate and independent acceptance remain. |
| VC5 | PASS | “Unrelated prose only: reuse the passing recorded tests”; a consumed-fixture change requires affected tests, and a fresh handoff requirement requires a fresh run. |
| VC6 | PASS | “Run the bounded read-only behavior simulation now. It resolves the interpretation that determines the remaining edit.” Final wording still needs sufficient behavior evidence and required review. |

The post-change target reported no unresolved cadence conflict among the permitted files. VC6 changed from suspending useful feedback to running it; VC1–VC5 retained the required controls. The comparison supports the bounded interpretation improvement, not a measured change across live tasks or model populations.

Evaluation economy: 2 of 3 maximum fresh target runs used; 0 of 1 focused corrections used; no criteria revisions or optional expansion. Source checks and all six cases pass. Independent single-final, standard-depth review remains pending; these results are evidence inputs, not final acceptance.

## Independent Review And Closure — 2026-09-04

This closure supersedes the pending status above. `/root/cadence_review`, the configured implementation-reviewer, returned `ACCEPT_AFTER_CONDITIONS` after single-final, standard-depth review. The ten-file candidate table above is the pre-correction identity. The reviewer independently verified that identity and baseline reconstruction, section parity, Codex TOML, unchanged testing owners, and scoped whitespace checks. Its read-only gitleaks scan reported “no leaks found.” Behavioral excerpts were assessed; target execution and isolation were not independently replayed.

F-001, blocking P2, identified a retained top-level coder prohibition: `<forbidden>Claim completion while the repository is not green.</forbidden>`. That blanket rule conflicted with the reviewed contract for applicable required checks and could force unrelated remediation. The reviewer froze exactly one replacement per coder adapter: `<forbidden>Claim completion while an applicable required check is failing or lacks current evidence.</forbidden>`. All other runtime bytes had to remain unchanged. The replacement record was extended with exactly this correction; prompts, criteria, returned excerpts, and limitations were preserved.

| Corrected source | Reviewer-required and observed SHA-256 |
| --- | --- |
| `agents/claude/coder.md` | `1d678b84b56ec85f09b281ee72b9cfbac86ee7625aa733241c60d2ed5c6058cc` |
| `agents/codex/coder.toml` | `d3e6b19f4820b0e29c38fa3b6a49a43a489cba21d9bba1cffb7fcb252cc2cd65` |
| `agents/opencode/coder.md` | `fd89fb9f0639a4732509eca7cfdc0136819f576378f65d27cc36478b9df93087` |
| `agents/omp/coder.md` | `10b90a1ebee226cbccbf94ee8b2fac48dd8691c9a3fa145e27d1f09778c16de7` |

The coordinator's read-only `python3 -c` conditional-proof check asserted those four hashes, the unchanged other six candidate hashes, exact correction-record contents, one-match reverse reconstruction for every replacement, all ten original baseline hashes, and Codex TOML role identity. It returned `PASS: final identity and baseline reconstruction` for each of the ten paths, followed by:

```text
PASS: Codex TOML parses; coder role retained
PASS: reviewer F-001 exact runtime correction predicate satisfied
```

The same scoped `git diff --check` command recorded above exited 0 after the correction. Exact reconstruction and final hashes prove that no additional runtime delta was introduced. The reviewer expressly required no additional behavior run for this exact clause alignment and permitted report/continuity closure without reopening acceptance. VC1–VC6 were exercised on the pre-correction candidate, not replayed on the corrected sources; correction acceptance rests on the reviewer's exact mechanical predicate.

Status: `ACCEPTED_BY_CONDITION`. F-001 is resolved and no blocking findings remain. Evaluation totals: 2 fresh target runs; 1 focused source correction, from independent review; no criteria changes, optional expansion, or additional behavior runs. No implementation-pattern signal was found. Remaining evidence limits include procedural isolation, synthetic decision coverage, no direct VC1–VC6 case for an unrelated known failing check, and no native deployment or cross-model adherence proof. Required checks and review remain mandatory; no deployment, installed-copy edit, commit, push, or external mutation occurred.
