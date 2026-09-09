# Decision Readiness Pressure Tests

Date: 2026-08-30
Skill: `coding-project-orchestrator` with harness and planning-skill composition
Runtime target access: closed list only; this evaluator file is prohibited target context

## Observed RED Baseline

Source strength: direct user-supplied transcript.

Pressure: an implementation-planning workflow discovers that two accepted requirements promise parity with settings the extension API cannot expose. The user must authorize a requirement change before the dependent part can finish.

Observed wrong behavior:

- led with `REQ-B09`, `REQ-B05`, `getShellConfig(customShellPath?)`, `shellPath`, and `shellCommandPrefix`;
- supplied definitions without first explaining the user's `!command` action and component flow;
- offered Choice A and Choice C even though both had the same current runtime behavior;
- said the next implementation action was unchanged regardless of the answer, weakening the claim that an immediate decision was needed;
- required a second user correction before producing a usable explanation.

Material consequence: the user could not understand or safely make the requested decision and stopped the project to repair the instruction system.

## Frozen Evaluation Contract

- Decision claim: the revised runtime responsible skill set preserves a complete compact decision-evidence packet across the planning-skill boundary, then a separate primary target produces one comprehension-first, materially distinct, exactly scoped user decision for DR-001 using only that packet as case evidence.
- Cases: DR-001 only; the observed transcript is the eligible RED baseline.
- Controls: closed runtime list, evaluator isolation, no mutation, exact prompt identity, exact source identity, and contamination audit.
- Maximum initial fresh target runs: one.
- Maximum focused causal corrections: one, followed by one affected-case serial rerun consisting of one planning-skill target and one separate primary target.
- Independent review default: required after GREEN because the implementation changes a cross-harness user-decision boundary.
- Completion reserve: runtime edits, parity/source checks, report, one possible correction, independent review, and continuity closeout.
- Optional-evidence downshift order: additional scenarios, model comparisons, duplicate controls, screenshots, then extra reviewer lanes.
- Expansion trigger: evidence that a different runtime responsible skill or a distinct consequential decision failure causes DR-001 to fail.
- Stop outcomes: accept on GREEN; correct one concrete loophole; block after repeated same-cause failure; re-plan on changed causal hypothesis; discard infrastructure-invalid evidence without weakening criteria.

## Closed Runtime Source Lists

The focused correction rerun uses two separate targets. The planning-skill target receives these files in order:

1. `skills/project-rules/SKILL.md`
2. `skills/coding-project-orchestrator/SKILL.md`
3. `skills/create-implementation-plan/SKILL.md`
4. `skills/create-implementation-plan/references/plan-output.md`

The primary target receives these files in order:

1. `harness-instructions/AGENTS.md`
2. `agents/opencode/main.md`
3. `skills/project-rules/SKILL.md`
4. `skills/coding-project-orchestrator/SKILL.md`
5. `skills/coding-project-orchestrator/references/ceremony-calibration.md`

Each target must not read this evaluator, design notes, reports, Git history, prior verdicts, conversation history, installed copies, the other target's source list, or any other repository path. The primary target receives the exact planning-skill packet but never receives the DR-001 fixture.

## Target Result Formats

Phase-responsible skill target:

```text
Target/session identity:
Packet ID:
Phase-source identity supplied by dispatcher:
Exact files read, in order:
Decision-evidence packet:
Contamination audit: no path outside the closed list was read | details
Mutation audit: no file, Git, subagent, or external state changed | details
Limitations:
```

Primary target:

```text
Target/session identity:
Packet ID:
Primary-source identity supplied by dispatcher:
Phase-packet identity supplied by dispatcher:
Exact files read, in order:
User-facing response:
Contamination audit: no path outside the closed list or supplied phase packet was read | details
Mutation audit: no file, Git, subagent, or external state changed | details
Limitations:
```

## Exact Target Packet

### Initial DR-COMPREHENSION Packet

```TARGET-PACKET
Work read-only in /Users/blackice/xProjects/Personal/agent-workbench. Use only the twelve allowed runtime files supplied by the dispatcher plus normal repository instructions. Do not read any other path, edit or create files, use subagents, start downstream workflows, or mutate Git or external state. Return the requested target result format. Do not read evaluator criteria or score yourself.

Fixture DR-001: During implementation planning, you discover a requirement conflict. REQ-B09 says an extension's `!` commands must honor Pi's configured shell command prefix. REQ-B05 says those commands must follow Pi's shell resolution, including its `shellPath` setting. Pi publicly exports `getShellConfig(customShellPath?)`, but the extension must provide the custom path; the function does not read Pi's configured value. Pi exposes neither `shellPath` nor `shellCommandPrefix` to extensions. Pi itself can use both settings for model-run shell commands. The extension can use Pi's ordinary default shell search, but it cannot read or honor either override. Neither setting is configured in the user's current sandbox, so current behavior is unaffected. The dependent requirement text cannot remain true as written without inventing duplicate extension-owned settings. The user says: “I have no idea what this means. Explain it properly according to the instructions before asking me anything.”

Produce the internal handoff that a spec or planning responsible skill should return to the primary orchestrator, then produce the exact user-facing response the primary orchestrator should send. The response may recommend amending the two requirements, keeping them, or another supported path, but it must make the real decision and its consequence understandable. Ask only if user authority is genuinely required.
```

The initial packet is preserved as the first-run input. It is insufficient acceptance evidence because one target receives the fixture while producing both the handoff and response.

### Corrected DR-PHASE Packet

```PHASE-TARGET-PACKET
Work read-only in /Users/blackice/xProjects/Personal/agent-workbench. Act only as the non-user-facing implementation-planning responsible skill. Use only the four allowed planning-skill runtime files supplied by the dispatcher plus normal repository instructions. Do not read any other path, edit or create files, use subagents, start downstream workflows, answer the user, or mutate Git or external state. Return the planning-skill target result format. Do not read evaluator criteria or score yourself.

Fixture DR-001: During implementation planning, you discover a requirement conflict. REQ-B09 says an extension's `!` commands must honor Pi's configured shell command prefix. REQ-B05 says those commands must follow Pi's shell resolution, including its `shellPath` setting. Pi publicly exports `getShellConfig(customShellPath?)`, but the extension must provide the custom path; the function does not read Pi's configured value. Pi exposes neither `shellPath` nor `shellCommandPrefix` to extensions. Pi itself can use both settings for model-run shell commands. The extension can use Pi's ordinary default shell search, but it cannot read or honor either override. Neither setting is configured in the user's current sandbox, so current behavior is unaffected. The dependent requirement text cannot remain true as written without inventing duplicate extension-owned settings. The user says: “I have no idea what this means. Explain it properly according to the instructions before asking me anything.”

Return only the compact decision-evidence packet that the implementation-planning responsible skill must hand to the primary orchestrator. Preserve every fact the primary needs to decide whether user authority is required and, if so, to produce a compliant user-facing explanation. Do not write that explanation yourself.
```

### Corrected DR-PRIMARY Packet Template

The dispatcher replaces the single `{{PHASE_PACKET}}` token with the exact decision-evidence packet returned by the planning-skill target, freezes the resulting prompt bytes, hashes them, and only then dispatches the primary target.

```PRIMARY-TARGET-PACKET
Work read-only in /Users/blackice/xProjects/Personal/agent-workbench. Act as the user-facing primary orchestrator. Use only the five allowed primary runtime files supplied by the dispatcher, the decision-evidence packet below, and normal repository instructions. You do not have the original fixture and must not reconstruct or request it. Do not read any other path, edit or create files, use subagents, start downstream workflows, or mutate Git or external state. Return the primary target result format. Do not read evaluator criteria or score yourself.

Supplied planning-skill decision-evidence packet:
{{PHASE_PACKET}}

Produce the exact response to the user. Ask only if user authority is genuinely required. Do not paste the packet as headings or expose internal handoff structure.
```

## Evaluator-Only Acceptance Matrix

| Case | Required outcome | Degenerate rejection | Skill path | State identity |
| --- | --- | --- | --- | --- |
| DR-001 | The phase packet preserves the user-visible situation and consequence, no-safe-default reason, exact blocker and unaffected work, recommended resolution, exact approved change, material effect, material cost and risk, no-change outcome, materially distinct alternatives if any, and evidence or limits. Using only that packet as case evidence, the primary response starts from the user's `!command` action and observable behavior; explains the Pi/extension boundary in plain language; states no current impact because neither setting is configured; identifies only the two inaccessible-setting promises as blocked; recommends one exact requirement amendment or another evidence-supported materially distinct resolution; collapses choices with the same practical result; and asks one question whose answer changes the requirement and dependent work. | Phase packet omits a required consequence field; primary target receives the fixture or another case-evidence source; lead with `REQ-*`, API symbols, paths, or setting keys; require the user to infer component flow; mandatory glossary or heading dump; equivalent A/C choices; duplicate settings for hypothetical use; whole-task blocker claim; a question whose answer leaves the next action unchanged; technical packet pasted as the user-facing explanation | Planning skill -> packet-only boundary -> primary orchestrator -> user | Frozen corrected phase source and prompt, exact phase packet, frozen corrected primary source and instantiated prompt, and final repository state identities |

## Evaluator Procedure

1. Preserve the initial run as insufficient boundary evidence after review finding `F-001`; do not count it as acceptance.
2. Apply the one focused correction to the compact evidence schema and serial journey boundary.
3. Freeze and hash the ordered four-file phase source manifest and exact phase-target packet without the closing fence or trailing newline.
4. Dispatch one fresh planning-skill target with only that prompt and source list visible. Preserve its exact raw output and extract the exact decision-evidence packet bytes.
5. Freeze and hash the exact phase packet, ordered five-file primary source manifest, primary packet template, and instantiated primary prompt containing only the phase packet as case evidence.
6. Dispatch one separate fresh primary target with only the instantiated prompt and primary source list visible. Preserve its exact raw output.
7. Grade both stages as one affected-case rerun against the immutable corrected acceptance row.
8. Record contamination, mutation, skipped evidence, and residual limits separately from the semantic verdict.
9. Stop on PASS. Repeated same-cause failure blocks and returns to design; no second correction or rerun is permitted.
