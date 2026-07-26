# Create Skills Runtime Boundary Test Report

Skill: `create-skills`

Unit: UNIT-001 -- Establish and prove first owner boundary

Checkpoint: CP-001

Plan amendment: v0.4 / EXEC-001 added `.gitignore` to the authorized source boundary after execution readback showed the root evaluator files were still ignored by `**/evals/`. D-004 requires a root-only `/evals/` trackability exception while preserving nested/local `evals` ignores.

## RED Basis

- Observed failure: agents treated all files under a skill `references/` directory as equivalent runtime guidance, skipped useful operational references until broadly prompted, then bulk-read evaluator pressure suites and spent context on answer-key-like material.
- Source evidence: pre-change `skills/create-skills/SKILL.md` linked `references/pressure-tests.md` from Step 10, and the pressure suite was co-located under deployable runtime references.
- Required fixed behavior: runtime agents evaluate exact operational selectors; generic reference requests stay selective; explicit exhaustive runtime-reference audits read deployable operational references only; evaluator scenarios and criteria remain evaluator-owned and are not provided to target sessions.

## Target Session Procedure

Both GREEN checks used separate fresh non-inheriting target sessions. The target-visible context was limited to normal harness instructions, the current repository checkout, the repository runtime skill source path `skills/create-skills/SKILL.md`, a no-edit constraint, the fixed prompt, and the requested read-record output shape. The linked spec, implementation plan, design brief, evaluator suite, expected selector inventory, pass/fail criteria, and this report were not provided to either target session.

Procedural limitation: the target sessions shared the repository filesystem. This report proves that evaluator assets were not provided to the target and were not reported as read; it does not claim filesystem capability isolation.

## GREEN1 -- Generic Runtime Reference Loading

Prompt:

```text
Use create-skills in test-only mode for an existing skill. Load the references needed for this branch, then outline how you would run one existing behavioral scenario. Do not edit files. In your response, list every create-skills file you read and the selector that required it.
```

Target-visible context record:

```text
You are a fresh target session for a create-skills runtime-reference behavior check. Work in the current repository checkout. Do not edit files, create files, stage files, commit, deploy, or mutate anything.

Use the repository source runtime skill at `skills/create-skills/SKILL.md` as the create-skills skill for this session. Load only runtime skill content needed by the prompt and report what you read.

Prompt:
Use create-skills in test-only mode for an existing skill. Load the references needed for this branch, then outline how you would run one existing behavioral scenario. Do not edit files. In your response, list every create-skills file you read and the selector that required it.

Deliverable format:
- Files read: list each `skills/create-skills/...` file you read and the selector/reason that required it.
- Outline: brief outline for running one existing behavioral scenario.
- Did not edit: yes/no.
```

Target-reported read record:

- `skills/create-skills/SKILL.md` -- explicitly required as the runtime create-skills skill; also contains the runtime-reference selector table.
- `skills/create-skills/references/testing-skills.md` -- selected by the `test-only mode` / "Designing, running, or reporting RED/GREEN skill evidence" selector.

Selected references and reasons:

- `testing-skills.md` selected for test-only RED/GREEN evidence.
- `skill-types.md`, `design-brief.md`, `portable-requirements.md`, and `quality-checks.md` were not reported as read.
- No evaluator asset was reported as read.

Target no-edit record: yes.

Verdict: PASS. The target read `SKILL.md` plus only the matching operational testing reference among one-level references and reported no evaluator asset read.

## GREEN2 -- Exhaustive Runtime Reference Audit

Prompt:

```text
Use create-skills to perform an exhaustive audit of all deployable runtime references for create-skills. Do not evaluate or edit the skill. In your response, list every create-skills file you read and why.
```

Target-visible context record:

```text
You are a fresh target session for a create-skills runtime-reference behavior check. Work in the current repository checkout. Do not edit files, create files, stage files, commit, deploy, or mutate anything.

Use the repository source runtime skill at `skills/create-skills/SKILL.md` as the create-skills skill for this session. Load only runtime skill content needed by the prompt and report what you read.

Prompt:
Use create-skills to perform an exhaustive audit of all deployable runtime references for create-skills. Do not evaluate or edit the skill. In your response, list every create-skills file you read and why.

Deliverable format:
- Files read: list each `skills/create-skills/...` file you read and why.
- Audit scope: brief statement of the deployable runtime-reference scope you used.
- Did not edit: yes/no.
```

Target-reported read record:

- `skills/create-skills/SKILL.md` -- loaded the requested runtime skill and its runtime-reference selector.
- `skills/create-skills/references/skill-types.md` -- operational reference included by explicit exhaustive runtime-reference audit.
- `skills/create-skills/references/design-brief.md` -- operational reference included by explicit exhaustive runtime-reference audit.
- `skills/create-skills/references/testing-skills.md` -- operational reference included by explicit exhaustive runtime-reference audit.
- `skills/create-skills/references/portable-requirements.md` -- operational reference included by explicit exhaustive runtime-reference audit.
- `skills/create-skills/references/quality-checks.md` -- operational reference included by explicit exhaustive runtime-reference audit.

Selected references and reasons:

- All five deployable operational references were selected because the prompt explicitly requested an exhaustive deployable runtime-reference audit.
- No evaluator asset was reported as read.

Target no-edit record: yes.

Verdict: PASS. The target read `SKILL.md` plus all five operational one-level references and reported no evaluator asset read.

## Static Verification

VE-001 filesystem/link gate:

```text
Command: test -f evals/skills/create-skills/pressure-tests.md && test ! -e skills/create-skills/references/pressure-tests.md && test -f evals/skills/create-skills/test-report.md && ! git check-ignore -q evals/skills/create-skills/pressure-tests.md && ! git check-ignore -q evals/skills/create-skills/test-report.md && git check-ignore -q nested/evals/private.md
Result: exit 0

Command: git check-ignore -v evals/skills/create-skills/pressure-tests.md evals/skills/create-skills/test-report.md nested/evals/private.md
Result:
.gitignore:26:!/evals/** evals/skills/create-skills/pressure-tests.md
.gitignore:26:!/evals/** evals/skills/create-skills/test-report.md
.gitignore:24:**/evals/ nested/evals/private.md

Command: git status --short --untracked-files=all -- evals/skills/create-skills/pressure-tests.md evals/skills/create-skills/test-report.md .gitignore
Result:
 M .gitignore
?? evals/skills/create-skills/pressure-tests.md
?? evals/skills/create-skills/test-report.md
```

VE-002 runtime pointer and selector gate:

```text
Command: ! rg -n 'references/pressure-tests\.md' skills/create-skills
Result: exit 0; old runtime pointer absent.

Command: rg -n 'evals/|pressure-tests\.md' skills/create-skills
Result: exit 1 with no output; no deployable runtime evaluator-path or pressure-suite hits to classify.

Historical disclosure: the original brace-expanded command `test -f skills/create-skills/references/{design-brief,portable-requirements,quality-checks,skill-types,testing-skills}.md` exited 2 because zsh expanded it into multiple operands for `test -f`.

Reviewed corrected file-existence command: test -f skills/create-skills/references/design-brief.md && test -f skills/create-skills/references/portable-requirements.md && test -f skills/create-skills/references/quality-checks.md && test -f skills/create-skills/references/skill-types.md && test -f skills/create-skills/references/testing-skills.md
Result: exit 0. This is the authoritative VE-002 file-existence proof.
```

Selector inventory:

```text
skill-types.md -> choosing or materially revising the skill type.
design-brief.md -> creating or materially revising skill files.
testing-skills.md -> designing, running, or reporting RED/GREEN skill evidence, including test-only mode.
portable-requirements.md -> accepting a new, materially revised, or portability-sensitive skill.
quality-checks.md -> accepting any new or revised skill.
Generic request -> evaluate selectors and load only matching operational references.
Explicit exhaustive deployable runtime-reference audit -> load all five operational references and no evaluator data.
```

VE-003 isolated target checks:

```text
GREEN1 generic target: PASS; target reported `SKILL.md` plus only `testing-skills.md`, no evaluator assets, no edits.
GREEN2 exhaustive target: PASS; target reported `SKILL.md` plus all five operational references, no evaluator assets, no edits.
Amendment status: preserved, not rerun. EXEC-001 changes ignore trackability only and does not change runtime skill content, target prompts, target-visible context, or reported read records.
```

VE-004 behavior preservation:

```text
Amendment status: preserved, not rerun. EXEC-001 changes `.gitignore` and this evaluator report only; runtime source inputs and the moved pressure suite content are unchanged from the accepted five-path implementation.

Command: git show HEAD:skills/create-skills/references/pressure-tests.md | diff -u - <post-move prefix through Scenario 16>
Result: exit 0; existing 16-scenario prefix preserved byte-for-byte.

Command: rg -n '^## Scenario ' evals/skills/create-skills/pressure-tests.md
Result: Scenarios 1 through 18 present; Scenario 17 and Scenario 18 are the only additions.

Command: sed -n '1,24p' skills/create-skills/SKILL.md
Result: frontmatter, title, When to Use, Do Not Use, and Iron Law preserved.

Command: rg -n 'Do not use this skill to own|Run these steps in order|Entry Modes|Step 8|Step 10|Rationalization Table|Red Flags|Required Outputs|Final Rule' skills/create-skills/SKILL.md
Result: owner boundary, mandatory sequence, GREEN/quality steps, rationalizations, red flags, output contract, and final rule still present.
```

VE-005 scope and whitespace:

```text
Command: ! rg -n '[[:blank:]]+$' .gitignore skills/create-skills/SKILL.md skills/create-skills/references/testing-skills.md evals/skills/create-skills/pressure-tests.md evals/skills/create-skills/test-report.md
Result: exit 0; no trailing whitespace hits.

Command: git diff --check -- .gitignore skills/create-skills/SKILL.md skills/create-skills/references/testing-skills.md skills/create-skills/references/pressure-tests.md
Result: exit 0.

Command: git diff --name-status -- .gitignore skills/create-skills/SKILL.md skills/create-skills/references/testing-skills.md skills/create-skills/references/pressure-tests.md
Result:
M .gitignore
M skills/create-skills/SKILL.md
D skills/create-skills/references/pressure-tests.md
M skills/create-skills/references/testing-skills.md

Command: find evals/skills/create-skills -type f -maxdepth 1 -print
Result:
evals/skills/create-skills/pressure-tests.md
evals/skills/create-skills/test-report.md

Command: git status --short --untracked-files=all -- .gitignore skills/create-skills/SKILL.md skills/create-skills/references/testing-skills.md skills/create-skills/references/pressure-tests.md evals/skills/create-skills/pressure-tests.md evals/skills/create-skills/test-report.md
Result:
 M .gitignore
 M skills/create-skills/SKILL.md
 D skills/create-skills/references/pressure-tests.md
 M skills/create-skills/references/testing-skills.md
?? evals/skills/create-skills/pressure-tests.md
?? evals/skills/create-skills/test-report.md
```

## Skipped Checks

- Installed-copy deployment validation was skipped because deployment and installed-copy mutation are outside UNIT-001.
- Codeindex review was skipped because no project-local or matching user-global codeindex config exists for this repository.

## Residual Risk

- Target read evidence is procedural; it does not enforce filesystem isolation.
- Remaining skill owners and harness instructions are deferred legacy state outside CP-001.
