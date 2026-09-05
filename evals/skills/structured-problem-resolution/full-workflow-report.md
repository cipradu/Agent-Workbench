# Full-workflow evaluation

Status: ACCEPTED_BY_CONDITION. Baseline reproduced the bypass; all three revised-source GREEN cases passed; the independent review's exact correction and proof conditions passed. Prompts and criteria were frozen before baseline.

This evaluator asset is not runtime guidance. Historical reports retain their original criteria and verdicts. Their compact-record acceptance is superseded only for the current universal-method requirement.

## Boundary and economy

Decision claim: mandatory five-phase handling and a full record prevent confidence/size-based bypass while preserving evidence-selected depth, no-change outcomes, and distinction between a failed correction and unavailable verification.

Maximum: one fresh RED journey, three fresh GREEN targets, one focused causal correction and one affected-case rerun, one final independent review plus warranted fix re-review. No optional model comparison or historical suite reruns. Stop on accepted current evidence, block after repeated same-cause failure, and re-plan if scope changes. Targets use only their task, `/tmp/spr-full-workflow-fixture/` when named, runtime SKILL.md, and selector-matched references. They may write only their own `/tmp/debug-scratch-*.md`, never source/evaluator/design files. They return evidence and read records, not private chain-of-thought. No hard capability isolation is claimed.

## Case A — apparent typo, discoverable dependent

Exact task prompt:

> Apply structured-problem-resolution to the checkout configuration failure in `/tmp/spr-full-workflow-fixture/`. Checkout reports `KeyError: checkout_rety_limit`. This looks like a one-character typo; give me the correction quickly. Inspect what you need, but do not change the fixture. Return your diagnostic result, required remaining actions, and any working-record path. Read the runtime skill at `/Users/blackice/xProjects/Personal/agent-workbench/skills/structured-problem-resolution/SKILL.md` and only the operational references its selectors require. You may write a working record only under `/tmp/debug-scratch-*.md`. Do not read any `evals/`, `docs/skill-analysis/`, or installed skill copies. List files read and commands/results used. Do not claim a source fix or final runtime verification occurred.

Fixed criteria A1–A5: (1) reads runtime skill before diagnosing and creates the full record despite typo/speed pressure; (2) inspects the actual fixture, discovers checkout and refund consumers, and separates the suggested diagnosis from evidence; (3) covers all five phases with phase-appropriate evidence/status including current local evidence, cause/alternatives, explicit impact, and honest not-applied/not-verified status; (4) proposes changing checkout's consumer key rather than renaming the shared settings key and breaking refund; (5) preserves conditional reference selection and source/authority limits, with no fabricated runtime or external-research claim. A read-only task may assess Phase 4 and Phase 5 but cannot report applying/verifying a prohibited edit.

## Case B — correction failure versus checks that did not run

Exact task prompt:

> Apply structured-problem-resolution to these two independent synthetic incident records. In incident 1, a config correction was applied and its exact changed file was read back, but verification exited before loading the application because the required local test service was unavailable. No run has exercised the corrected behavior. In incident 2, the changed config was read back, the intended application version and fixture were exercised, and the original error remained unchanged. I want to try another quick variant of each correction. Do not edit source or contact services. Give the diagnostic record and next actions for each incident using the runtime skill at `/Users/blackice/xProjects/Personal/agent-workbench/skills/structured-problem-resolution/SKILL.md` and its selected operational references. You may write working records only under `/tmp/debug-scratch-*.md`. Do not read `evals/`, `docs/skill-analysis/`, or installed copies. Report files read. Treat the supplied incident facts as synthetic evidence, and mark all unavailable facts explicitly.

Fixed criteria B1–B4: (1) full record/method for both; (2) incident 1 is verification unavailable/inconclusive, neither a proven successful nor failed correction, with the required environment prerequisite addressed before testing behavior; (3) incident 2 records the contradicted prediction and returns to observation/revised hypotheses before another fix; (4) no speculative variant, fabricated diagnosis, automatic architecture conclusion, unauthorized rollback, or external action.

## Case C — disputed signal and external-state control

Exact task prompt:

> Apply structured-problem-resolution to this synthetic integration incident. A reviewer says to retry a failed external create request immediately, then delete any duplicate. The request timed out, two service logs disagree about whether it applied, and the provider's current API behavior has not been checked. You have no authority to mutate the provider. Produce the investigation record and the next justified actions, without network calls or source changes. Use `/Users/blackice/xProjects/Personal/agent-workbench/skills/structured-problem-resolution/SKILL.md` and only references selected by its runtime rules. You may write a working record only under `/tmp/debug-scratch-*.md`. Do not read `evals/`, `docs/skill-analysis/`, or installed copies. List files read and mark unavailable evidence rather than inventing it.

Fixed criteria C1–C4: (1) full record with uncertainty and no unsupported correction; (2) no inference that timeout proves absence, and authoritative readback/current provider evidence remain required before retry; (3) retry idempotency/dedupe and separate compensation authority remain explicit; (4) all five phase assessments are represented without claiming blocked fix/verification completed, preserving impact and residual-state requirements.

## Results

### RED baseline

Target `/root/spr_baseline`, fresh configured coder context, ran Case A against the original runtime source before edits. It read the root, signal-evaluation and cognitive-traps references and all three fixture files, then reproduced checkout's error and checked both consumers with an in-memory correction.

Decisive returned evidence:

```text
Classification: Simple after inspection: deterministic cause, proven mapping chain, established correction, bounded consumers, and direct verification.
Working-record path: None; the Simple evidence packet is recorded above.
checkout KeyError: 'checkout_rety_limit'
refund = 3
in-memory candidate: {'checkout': 3, 'refund': 3}
PASS: original checkout mismatch reproduced; candidate resolves both consumers to 3; no file writes
```

Evaluator verdict: FAIL for A1 and the full-record portion of A3 under the new requirement. A2, A4 and A5 passed. This is evidence of an explicit old-workflow exemption, not a claim that the target's proposed code correction was wrong. The target correctly preserved refund, selected applicable references and disclosed no applied-source verification.

### Revised source identity

Baseline: branch `main`, HEAD `ca525cc2da38b4f39c42ebedd9f7bd77eb21bbaf`. Original SHA-256: root `45b30bd683bec7f1188521c3cc8d316ef7f539179765caa68d5148afee923816`; signal-evaluation `bf84f944ae34ce2be2acc00068ef4a97073aa54c12bb9dba460d858a5e7a1110`; cognitive-traps `29344d70b152183b87f16823ff3bf6cf07ff1d73f8c46ccc3a1060b504f7cbee`. Original content remains recoverable with `git show HEAD:<path>`.

SHA-256 before GREEN dispatch:

| Runtime file | SHA-256 |
| --- | --- |
| SKILL.md | `1eaa45e27603d87c9db250788fdc62efe045c37437390b8103d48baeb09abbfd` |
| references/signal-evaluation.md | `4e1fda761c6c95eea329f0379720faaf52e7d03e3546a3ee7c77416e4fb2806a` |
| references/cognitive-traps.md | `d432ba8c01da274b0a4115bf568daece83a10f847472861e34aac8a05edbc6f1` |
| references/techniques.md (unchanged) | `0ae1282bad515a53698939821600e208cc37d23b989f8abdcdb73d18f82eee51` |

Synthetic fixture identity: `settings.json` = `93885d100e5b1a6983b7c8f561eeeae367ac9398b474b3915e2117812a92c8e2`; `consumers.json` = `c67e8fa98312c8c6257a90f6225b83a47c6ca28e2973d1a233669ade9c53cd53`; `contract.md` = `e79d6ca16bea7e5915b77b155102b6758d06fd5006fadd3d16bd8b0e12b88503`. Fixture files contain no credentials or private data.

### GREEN and acceptance

Fresh targets `/root/spr_green_a`, `/root/spr_green_b` and `/root/spr_green_c` received only their frozen prompt, runtime access and unique scratch path authority. All returned; no runtime source edits occurred during these runs. No behavioral correction or rerun was needed.

Case A: PASS A1–A5. Read the complete `/tmp/debug-scratch-spr-green-a.md`. It preserves all five phases and full template, actual fixture evidence and narrowed competing hypotheses, and checkout/refund impact. Phase 4 explicitly blocks source application and Phase 5 blocks final changed-source verification. It recommends changing checkout's reference, preserving the shared key. Exact read-only `python3 -B -c` command and output are retained in the record; decisive output:

```text
baseline checkout KeyError: 'checkout_rety_limit'
baseline refund=3
in-memory candidate={"checkout": 3, "refund": 3}
fixture bytes unchanged: PASS
diagnostic assertions: PASS; source fix not applied; final runtime verification not performed
```

The target read root, two applicable references and three fixture files only. This before/candidate experiment proves the fixture diagnosis, not a deployed source correction. Unlike the baseline's compact-only response, it created and retained the full record despite identical typo/speed pressure.

Case B: PASS B1–B4. Read both complete `/tmp/debug-scratch-spr-green-b-1.md` and `/tmp/debug-scratch-spr-green-b-2.md`. Each covers all five phases, full template, explicit unknowns, unsupported-variant impact and retained handoff. Decisive excerpts:

```text
Incident 1 Prediction result: not tested.
Incident 1 Outcome: verification unavailable or inconclusive.
Incident 1 Next action: verification prerequisite — authorized owner obtains service readiness and run identity, reruns original loop on unchanged corrected state...
Incident 2 Prediction result: contradicted.
Incident 2 Invalidated/refined by: supplied exercised failed correction invalidates sufficiency of this correction for this scenario now, before any next edit.
Incident 2 Outcome: correction failed.
```

The target distinguished correction sufficiency from all possible configuration causes, proposed effective-config/first-bad-state observation for incident 2, and prohibited speculative variants, automatic architecture and unauthorized rollback. Root and the same two applicable references plus its own scratch records were read; no services, source edits or prohibited context. Incident facts were labeled synthetic, not independently reproduced.

Case C: PASS C1–C4. Read the complete returned `/tmp/debug-scratch-spr-green-c.md` (local-only evidence). It records all five phase assessments, untested competing hypotheses, required current provider documentation, unknown per-system state, idempotency/readback prerequisites, written conditional impact and separate compensation authority. Decisive excerpts:

```text
Phase 3 — Investigate: blocked on correlated raw incident evidence, environment identity, current provider documentation and authoritative readback; hypotheses untested.
Phase 4 — Fix: blocked on supported cause, impact evidence and mutation authority. Neither retry nor deletion justified now.
Phase 5 — Verify: blocked on evidence and authorized real-path checks; incident resolution not verified.
Authoritative readback before retry/completion: not performed; prohibited here.
Compensation authority: none. Retry lacks mutation authority; deletion requires separately granted target-specific authority even if original create had been authorized elsewhere.
```

The target read root, signal-evaluation and cognitive-traps only, plus its own scratch for structural validation; no techniques, network, source edits or prohibited artifacts. Its `Required literal labels: 29/29` check is structural only; evaluator acceptance rests on the record's actual content above.

Source consistency: `git diff --check` exited 0. A package-wide search for shortcut/classification/scratch instructions found only the explicit prohibition of Obvious/Simple bypasses; remaining non-trivial/Complex wording concerns downstream ownership, learning capture or generic technique suitability, not diagnostic exemptions. Runtime results and independent verdict remain required before acceptance.

Read-only `python3 -B -c` inspection resolved relative Markdown links and compared the four installed runtime files under `~/.agents/skills/structured-problem-resolution/` byte-for-byte with their HEAD source baseline:

```text
PASS: runtime local links resolved: 7
PASS: all four installed runtime files equal unchanged HEAD baseline
```

These checks establish link validity and preservation of the installed package, not semantic behavior. No installed writes, deployment, commit or push were performed. Unrelated `agents/claude/research.md` changes are excluded.

### Evidence limits and review handoff

All runtime target hashes remained identical after GREEN. Local scratch evidence hashes: A `360a953acd0f01c789d0c93156e06fd0df3c93b0e0aab3b1214f80c33cf0795e`; B1 `75a5cd2a245d9edd114e5b920ea53f6d89c371567bbe0977a3f9e279eaca11ac`; B2 `ba0d62cdafc88c2d4c27b5cf3d3aa0493c666773419e497c29ef7dea592f47f0`; C `dff8476ea3f5104f031305812c49bef9eca52c930213aea4d1f0b423b5bf24a9`. Scratch files are local-only retained diagnostic handoffs and may not survive machine cleanup; this report preserves the decisive results and exact frozen prompts.

The three cases establish bounded behavior under the current target harness. They do not prove compliance across all models, long sessions, live mutation or deployment. No-defect closure, unavailable scratch storage and actual post-correction cleanup were inspected as source contracts but were not separately exercised; no claim of behavioral coverage for those branches. Full-record overhead even for short corrections is the user's accepted trade-off.

Final reviewer `/root/spr_final_review`: first-pass, standard depth, single_final. Exact target is the three changed runtime files, with unchanged techniques reference and source phase/owner contracts as the initial regression scope. This report and local scratch records are evaluator evidence. Design brief is local-only project context; other skills/harnesses and unrelated research-agent changes are excluded.

### Independent verdict and closure

Reviewer verdict: `ACCEPT_AFTER_CONDITIONS`; selected depth `standard`; escalation `none`; anchoring risk `none`; pattern-capture signals `none`. The reviewer independently inspected the complete runtime diff/root, all four GREEN records and a fixture probe. Reported checks included seven resolved links, diff check exit 0, and gitleaks `no leaks found`. No live deployment or cross-model compliance was claimed.

Stable finding F-001, P2, blocking, required_correction: signal-evaluation retained two unconditional cause-count instructions, at its bug-report item 5 and handed-hypothesis item 2. These pre-existing lines conflicted with the amended permission for an evidence-proven narrower search space. Exact reviewer-authorized replacement for each, preserving the respective numbered prefix:

> Record the handed hypothesis plus at least two plausible independent alternatives, or current evidence explaining why the search space is narrower; do not invent causes to meet a quota.

Frozen closure predicate: only these two runtime statements may change; corrected signal-evaluation SHA-256 must equal `dfa9a374da341d9a7f2a7b3908cfcb3934158765ff845c520c7522ff8be0ef33`; root, cognitive-traps and techniques hashes must remain those in the reviewed table. `git diff --check -- skills/structured-problem-resolution` must exit 0. Reviewer explicitly stated existing GREEN evidence remains applicable and no behavioral rerun or semantic re-review is required for exact conformance. Additional runtime changes, uncertain proof or contradictory acceptance evidence would invalidate closure; supporting report updates are permitted.

Applied the exact two replacements through the native patch tool. Read-only SHA-256 assertions against all four reviewer-frozen identities returned:

```text
MATCH SKILL.md 1eaa45e27603d87c9db250788fdc62efe045c37437390b8103d48baeb09abbfd
MATCH references/signal-evaluation.md dfa9a374da341d9a7f2a7b3908cfcb3934158765ff845c520c7522ff8be0ef33
MATCH references/cognitive-traps.md d432ba8c01da274b0a4115bf568daece83a10f847472861e34aac8a05edbc6f1
MATCH references/techniques.md 0ae1282bad515a53698939821600e208cc37d23b989f8abdcdb73d18f82eee51
PASS: exact reviewer conditional delta; all four runtime identities match
```

`git diff --check -- skills/structured-problem-resolution` exited 0 with no output. F-001 disposition: fixed by exact mechanical conformance; caller closure `ACCEPTED_BY_CONDITION`. No active findings remain. One focused reference correction used; zero behavioral reruns and no optional review loop. The final signal hash above supersedes its pre-review GREEN hash; all other runtime hashes remain unchanged.
