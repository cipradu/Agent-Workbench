# Decision Readiness Evaluation Report

Date: 2026-08-30
Owner: `coding-project-orchestrator` with harness and phase-owner composition
Packet: `DR-COMPREHENSION`
Case: `DR-001`
Result: PASS after one focused correction and one affected-case serial rerun

## Initial Evidence Identity

- Runtime source identity: `3c0d4c18780dead9466917ea3dff2efc49dc4d874d3b02009173c0affe2133e4`
- Prompt identity: `e1a49cd7c234e36eda8e2ad0b51ed3608aedaebc403237f2e173c924b0d4d585`
- Initial criterion identity: `878c87ef9dfa5c18611ff3196b50cd0d085477a9b52494455c312fdf1f2edbdf`
- Observed RED reused: yes; user-supplied original conversation
- Fresh target runs used: 1 of 1
- Initial result: insufficient boundary evidence after independent review finding `F-001`; one target saw the complete fixture while producing both the phase packet and response

## Corrected Serial Evidence Identity

- Phase source identity: `0925ad9a8fdb4796253d59c79e646e6c5ebe38c95a76a6b7641aaab0edb55195`
- Phase prompt identity: `2a32e19d636e84842a95b00a2a4ab5a388b116384af03d01c91a36850aa5bb85`
- Phase packet identity: `8f8b6250478f789595122ab8e4447ebba95ecbca9b2c2c7b87b4fc53af271cb3`
- Primary source identity: `cb26ed140017e2ef9d8faa4186227ff22b62c9f2e32e0141ac7760a0258a5862`
- Primary prompt-template identity: `dd524c5e3b9215df3441e1ccd7b9c1de5d624819530c7a086b6a3c44df001a94`
- Instantiated primary prompt identity: `8a2374c051c973dfe81be1ca016d46f571da087947228434a11c1a3d8885646c`
- Corrected criterion identity: `4dd204324e96eff770a38b29f23f0501a81372e29f6babb45737178fa32d81dd`
- Focused corrections used: 1 of 1
- Affected-case serial reruns used: 1 of 1; one phase-owner target followed by one separate primary target
- Expansion trigger observed: none
- Stop outcome: accept

## Evaluator Verdict

PASS. The phase-owner target preserved the complete compact decision evidence, including material effect, material cost and risk, and the no-change outcome. The separate primary target received no fixture and used only that packet as case evidence. Its response started with the user's `!command` action and ordinary current behavior, then explained the Pi/extension boundary without requiring source-code knowledge. It stated that neither override is configured and current behavior is unaffected. It limited the blocker to REQ-B05, REQ-B09, their linked acceptance evidence, and the dependent planning branch; all other work remained unaffected.

The primary target rejected duplicate extension-owned settings, recommended one exact amendment that makes the two requirements implementable and records the unsupported override behavior, stated the effect and future limitation, and asked one approval question whose answer changes the spec and planning path. It did not lead with internal identifiers, offer duplicate choices, overstate the blocked scope, paste the internal handoff as the user explanation, or claim the next action was identical regardless of the answer.

## Contamination And Mutation Audit

- The phase-owner target reported exactly the four closed phase files in the supplied order.
- The primary target reported exactly the five closed primary files in the supplied order and reported no fixture access.
- Both targets reported no evaluator, design, report, Git, conversation-history, installed-copy, or external-source access outside their lists and supplied packet.
- Both targets reported no file, Git, subagent, or external mutation.
- Neither target scored itself against the hidden acceptance row.

## Initial Raw Target Output — Insufficient Boundary Evidence

```text
Target/session identity: /root/decision_readiness_green — fresh read-only behavior target

Packet ID: DR-COMPREHENSION

Source-state identity supplied by dispatcher: 3c0d4c18780dead9466917ea3dff2efc49dc4d874d3b02009173c0affe2133e4

Exact files read, in order:
1. harness-instructions/AGENTS.md
2. agents/opencode/main.md
3. skills/project-rules/SKILL.md
4. skills/coding-project-orchestrator/SKILL.md
5. skills/coding-project-orchestrator/references/ceremony-calibration.md
6. skills/create-spec-readiness-map/SKILL.md
7. skills/create-spec-readiness-map/references/artifact-format.md
8. skills/create-engineering-spec/SKILL.md
9. skills/create-engineering-spec/references/spec-output.md
10. skills/architecture-design/references/decision-framing.md
11. skills/create-implementation-plan/SKILL.md
12. skills/create-implementation-plan/references/plan-output.md

Internal owner handoff:
- Status: Planning blocked only for the branch that implements REQ-B05 and REQ-B09.
- Newly discovered evidence: Pi can apply its configured shell path and shell command prefix to commands that Pi runs itself, but extensions cannot read either configured value. The exported `getShellConfig(customShellPath?)` helper requires the extension to supply the custom path and does not retrieve Pi’s configured value. The extension can use ordinary default shell discovery.
- Source strength: Fixture-supplied current-system and interface evidence; not independently verified because the closed packet forbids reading Pi sources or external documentation.
- Conflict: REQ-B05 and REQ-B09 require behavior that the extension cannot implement through the exposed interface. Keeping those requirements true would require an upstream Pi capability or separate extension-owned settings. Separate settings would duplicate Pi configuration, could drift from it, and are outside the accepted requirement.
- User-visible situation and consequence: Extension `!` commands work with ordinary shell defaults now. The user has not configured either Pi override, so current behavior is unaffected. If the user later configures a custom shell path or command prefix, extension commands cannot match those overrides.
- Why no safe authorized default exists: Changing or superseding normative requirements requires user authority. Planning cannot silently weaken them or invent duplicate settings.
- Exact blocked work: Plan units and acceptance evidence that claim extension commands honor Pi’s configured `shellPath` or `shellCommandPrefix`.
- Unaffected work: All planning and behavior not dependent on those two overrides.
- Recommended resolution: Return the spec to its owner and preserve the stable IDs while amending REQ-B05 to require the ordinary shell resolution available to extensions, and amending REQ-B09 to state that Pi’s configured command prefix is unsupported until Pi exposes it. Explicitly exclude duplicate extension-owned shell settings.
- Exact artifact change approval authorizes: The two requirements and their linked acceptance evidence change from “honor Pi’s configured overrides” to “use Pi’s ordinary default shell behavior available to extensions; do not claim override parity.”
- Material effect: The requirements become implementable and accurately describe current behavior. Users who later configure either Pi override will not receive matching behavior in extension `!` commands.
- Cost and risk: Low implementation cost and no current sandbox behavior change. The lasting limitation is configuration mismatch for users who use those overrides.
- If no change is made: The requirements remain impossible as written, and the dependent planning branch cannot be approved. The alternative is to wait for Pi to expose both values or separately authorize duplicate extension settings.
- Changed next action: On approval, route REQ-B05, REQ-B09, and linked acceptance evidence back to the engineering-spec owner for amendment, then resume planning. Without approval, keep the planning branch blocked.

User-facing response:
When you run an extension `!` command today, it uses the normal shell that the system finds by default. That continues to work in your current setup because you have not configured either of Pi’s shell overrides.

The current requirements promise more than the extension can do. Pi can use a custom shell path and a command prefix for commands that Pi runs itself, but it does not let extensions read either configured value. The helper Pi provides can use a custom path only when the extension already knows that path; it cannot retrieve Pi’s setting. There is also no extension interface for reading the configured command prefix.

This blocks only the two requirements about matching those overrides and the planning work that depends on them. The rest of the plan is unaffected. Adding separate extension settings would create duplicate configuration that could disagree with Pi, so I do not recommend it.

I recommend amending the two requirements to say that extension `!` commands use the normal shell behavior available to extensions and do not promise to honor Pi’s custom shell path or command prefix until Pi exposes those values. This matches current behavior and makes the requirements implementable. The cost is that users who later configure either override will not get the same override in extension commands. If the requirements remain unchanged, that part of the plan cannot be approved.

Do you approve that amendment to the two requirements? If approved, the spec will be revised and planning can resume against the achievable behavior.

Contamination audit: no path outside the closed list was read | The twelve authorized files were read in the supplied order. Some authorized files were reread in line ranges after tool output truncation. No evaluator assets, repository sources, Git state, or external sources were inspected.

Mutation audit: no file, Git, subagent, or external state changed | Only read-only shell commands against the authorized files were used. No files were created or edited, no Git command ran, no subagent was used, and no external action occurred.

Limitations: The Pi API and configuration facts came from fixture DR-001 and were not independently verified because the closed-file packet prohibited reading Pi source code, documentation, or external sources. No canonical spec or plan artifact was inspected or changed, so the exact requirement wording and linked acceptance-evidence IDs remain for the owning workflow to reconcile after user approval.
```

## Corrected Raw Phase-Owner Output

```text
Target/session identity: DR-001 fresh read-only phase-owner target; exact phase-prompt identity `2a32e19d636e84842a95b00a2a4ab5a388b116384af03d01c91a36850aa5bb85`
Packet ID: DR-PHASE
Phase-source identity supplied by dispatcher: `0925ad9a8fdb4796253d59c79e646e6c5ebe38c95a76a6b7641aaab0edb55195`
Exact files read, in order:
1. `skills/project-rules/SKILL.md`
2. `skills/coding-project-orchestrator/SKILL.md`
3. `skills/create-implementation-plan/SKILL.md`
4. `skills/create-implementation-plan/references/plan-output.md`

Decision-evidence packet:
- User-visible situation and consequence: The extension’s `!` commands are required to behave like Pi’s shell commands, including two user-configurable overrides. Pi does not expose either override to extensions, so the extension cannot meet those promises when a user configures them.
- Concrete evidence: REQ-B09 requires Pi’s configured shell-command prefix. REQ-B05 requires Pi’s shell resolution, including `shellPath`. Pi exports `getShellConfig(customShellPath?)`, but the extension must already know and supply the custom path; the function does not retrieve Pi’s configured value. Pi exposes neither `shellPath` nor `shellCommandPrefix` to extensions. Pi itself can apply both settings to model-run shell commands. The extension can use Pi’s ordinary default shell search only.
- Current impact: Neither override is configured in the current sandbox, so existing behavior there is unaffected. The incompatibility appears when either override is configured.
- Why no safe authorized default exists: Planning cannot alter accepted requirement truth or invent new extension-owned configuration. Silently weakening REQ-B05/REQ-B09 would change the promised behavior; adding duplicate settings would create new product behavior and maintenance obligations.
- Exact blocker: Implementation planning for the portions of REQ-B05 and REQ-B09 that promise parity with Pi’s private `shellPath` and `shellCommandPrefix` overrides. Other planning work and current default-shell behavior remain unaffected.
- User authority required: Yes. The user must authorize a requirement change or authorize a new extension-owned settings surface.
- Recommended resolution: Revise REQ-B05 and REQ-B09 so extension `!` commands follow Pi’s ordinary default shell search while explicitly excluding Pi overrides that extensions cannot access. Do not add duplicate extension settings.
- Exact artifact/behavior changed by approval: The normative requirement text and its dependent acceptance evidence for `!` command shell selection and prefix handling.
- Material effect: The documented and tested behavior becomes implementable and honest. Default behavior remains unchanged; users who configure Pi’s private overrides will not receive automatic parity in extension `!` commands.
- Material cost and risk: The product promise becomes narrower. Users may observe different behavior between Pi model-run shell commands and extension `!` commands when Pi overrides are configured.
- Materially distinct alternative: Add extension-owned equivalents for shell path and command prefix. This could provide configurable parity but duplicates Pi settings, requires separate configuration and precedence semantics, can drift from Pi, and expands product scope, tests, documentation, and maintenance.
- No-change outcome: The requirement remains impossible to satisfy as written, so the affected planning branch must remain blocked; a valid plan must not disguise the conflict as an implementation task.
- Changed next action: Return to the requirement-owning workflow for an authorized revision. Resume affected implementation planning only after the decision is recorded in current accepted engineering truth.
- Evidence limits: Pi API and sandbox-state facts are dispatcher-supplied fixture evidence. Closed-list constraints prevented checking Pi source, public documentation, the canonical requirements artifact, its approval state, dependent acceptance items, or repository implementation surfaces.

Contamination audit: no path outside the closed list was read. The third file was reread in bounded chunks after the initial command output was truncated; no additional file was accessed.
Mutation audit: no file, Git, subagent, or external state changed. No network or installed-copy access occurred.
Limitations: This packet does not identify the canonical requirement file or every dependent plan unit because those paths were outside the allowed runtime set. It does not independently verify the fixture’s Pi API claims or write the user-facing decision explanation.
```

## Corrected Raw Primary Output

```text
Target/session identity: DR-001 primary-orchestrator rerun — `/root/decision_readiness_primary_rerun`; exact instantiated primary-prompt identity `8a2374c051c973dfe81be1ca016d46f571da087947228434a11c1a3d8885646c`

Packet ID: DR-PRIMARY

Primary-source identity supplied by dispatcher: `cb26ed140017e2ef9d8faa4186227ff22b62c9f2e32e0141ac7760a0258a5862`

Phase-packet identity supplied by dispatcher: `8f8b6250478f789595122ab8e4447ebba95ecbca9b2c2c7b87b4fc53af271cb3`

Exact files read, in order:

1. `harness-instructions/AGENTS.md`
2. `agents/opencode/main.md`
3. `skills/project-rules/SKILL.md`
4. `skills/coding-project-orchestrator/SKILL.md`
5. `skills/coding-project-orchestrator/references/ceremony-calibration.md`

User-facing response:

The extension’s `!` commands use Pi’s ordinary default shell behavior now, and the current sandbox is unaffected because neither override is configured. However, when a user configures Pi’s custom shell path or shell-command prefix, the extension cannot read those values. It therefore cannot make its `!` commands match Pi as currently promised.

This cannot be resolved safely during planning. Silently narrowing the promise would change accepted requirements, while adding extension-owned settings would create new product behavior, configuration precedence, tests, documentation, and maintenance. Only the parts of REQ-B05 and REQ-B09 that promise parity with Pi’s private overrides are blocked; other planning and default-shell behavior can continue.

I recommend revising REQ-B05 and REQ-B09, plus their dependent acceptance evidence, so extension `!` commands follow Pi’s ordinary default shell search and explicitly exclude Pi overrides that extensions cannot access. This makes the documented and tested behavior implementable without adding duplicate settings. The cost is a narrower promise: users who configure Pi’s private overrides may see different behavior between Pi’s model-run shell commands and extension `!` commands. If no requirement change is approved, the affected planning branch must remain blocked. The materially different alternative is to add extension-owned shell-path and command-prefix settings, but that expands scope and can drift from Pi.

Do you approve the recommended revision to REQ-B05 and REQ-B09? If approved, the requirement-owning workflow can record the narrower behavior and affected planning can resume; otherwise, that planning branch remains blocked unless you separately authorize the extension-owned settings alternative.

Contamination audit: no path outside the closed list or supplied phase packet was read | The five permitted files were first requested together in the required order; because the combined output was truncated, the same five files were reread individually and in the same order, with the first file split into sequential line ranges. No additional repository path, evaluator asset, fixture, prior verdict, report, or installed copy was accessed.

Mutation audit: no file, Git, subagent, or external state changed | Only read-only file-display commands were used. No files were created or edited, no Git command ran, no subagent was started, and no network or external-system action occurred.

Limitations: Pi API behavior, sandbox state, requirement wording, and the blocker are based only on the dispatcher-supplied phase packet. Pi source, public documentation, the canonical requirements artifact, its approval state, dependent acceptance items, and repository implementation surfaces were not inspected, so their independent verification and exact downstream edit scope remain unavailable.
```

## Residual Risk

The corrected DR-001 journey proves the intended behavior for the observed failure pattern across one fresh phase-owner-to-primary handoff. It does not prove every future decision explanation, installed-copy consumption, already-running harness reload behavior, or the interrupted project's Pi facts beyond the supplied fixture. The targets' access and mutation audits are procedural self-reports rather than hard sandbox transcripts.
