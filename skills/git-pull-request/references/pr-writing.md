# PR Writing

Use this reference when composing or revising a pull request or merge request title/body.

## Core Principle

The diff is already visible in the review tool. The PR description exists to explain what the diff cannot show: what was impossible before, what is fixed now, why this direction was chosen, what evidence supports it, and what the reviewer should watch.

Bad: "Updates auth.ts, adds tests, and changes config."

Better: "Expired sessions now fail once with a clear 401 instead of repeatedly retrying token refresh until the request times out."

If the first sentence describes file movement, renamed functions, or added modules instead of the value or corrected behavior, rewrite it.

## Title

Use the repository's title convention when one exists. Otherwise prefer a concise, imperative, change-focused title.

Good title qualities:

- names the behavior or outcome;
- uses the narrowest useful scope;
- avoids trailing punctuation;
- stays short enough to scan;
- includes an issue key only when the project uses issue-key-linked PRs.

Common title formats:

```text
fix(auth): reject expired refresh sessions
feat(reports): add scheduled CSV exports
refactor(billing): isolate invoice calculation
docs: document local setup
```

Avoid:

- `WIP`
- `updates`
- `misc fixes`
- `phase 1`
- `ABC-123`
- file-name-only titles
- `!` or breaking-change markers without explicit confirmation

## Body Shape

Use only sections that earn their keep. Small PRs may need only a short paragraph. Medium or risky PRs usually need sections.

Recommended section order:

```markdown
## Summary

<What is now possible/fixed/safer/clearer, and why this exists.>

## Changes

- <Behavioral or design-level change, not a file list.>
- <Another meaningful change, if needed.>

## Validation

- <Command, manual flow, screenshot, log, benchmark, migration check, or reason not run.>

## Review Notes

- <Where to start, risk areas, intentional non-goals, or coupling that prevents splitting.>
```

Do not use every section automatically. Use the smallest body that gives reviewers enough truth.

## Evidence By Change Type

| Change type                 | Expected evidence                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| UI or visual behavior       | Screenshot, before/after image, short demo, or explicit reason visual evidence is unavailable   |
| CLI or generated output     | Before/after output or command transcript                                                       |
| API behavior                | Contract/schema note, request/response example when useful, tests or manual call evidence       |
| Database migration/backfill | Migration test, rollback/recovery note, verification query, lock/backfill risk where relevant   |
| Performance                 | Before/after measurement with environment/context                                               |
| Security/permission/privacy | Negative-path validation, authorization boundary note, redaction/logging note                   |
| Dependency/build/CI         | Command output, compatibility note, lockfile or config impact                                   |
| Refactor                    | Preservation boundary, characterization/testing evidence, explicit no behavior change statement |
| Agent/rule/skill/workflow   | Behavior failure addressed, pressure scenario or review evidence, compatibility risk            |

If evidence is missing, say exactly what was not run and why. Do not write "tests pass" unless the command actually ran.

## Reviewer Guidance

Add reviewer guidance when the diff is large, non-obvious, or risk-bearing.

Useful guidance:

- "Start with `<file/path>`; it owns the new boundary."
- "The risky part is the migration ordering; the application code is compatibility glue."
- "The tests intentionally cover the regression before the refactor assertions."
- "Generated files are included because the project checks them in."
- "Out of scope: follow-up cleanup of `<area>`."

Avoid guidance that only repeats sections or file lists visible in the diff.

## Draft Versus Ready Language

Ready PR body language should not say the change is incomplete unless the user explicitly accepts the review risk.

Draft PR body language may include:

```markdown
## Draft Status

This is draft because <specific incomplete work or missing validation>. Review is useful now for <specific decision or area>.
```

Do not use draft as a way to hide missing context. Draft means "not merge-ready", not "no explanation needed."

## Templates

If the repository has a PR template:

- keep required sections;
- delete optional sections only when the project allows it;
- mark irrelevant required sections as `Not applicable: <reason>`;
- do not leave placeholder text;
- do not fill checkboxes dishonestly.

If no template exists, use the body shape above.

## Forbidden Content

Never include:

- assistant/tool attribution footers;
- assistant/model co-author text;
- promotional badges or self-attribution;
- fake test evidence;
- unexplained issue-closing keywords;
- hard-wrapped prose purely for a column limit;
- links or references that were not actually verified.

End on the last substantive line.
