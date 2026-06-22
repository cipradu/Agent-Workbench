# Quality Checks

Use this reference before accepting a new or revised skill.

## Skill Quality Checklist

- The skill solves a recurring behavior problem.
- A lighter mechanism was considered and rejected with reason.
- Skill type is explicit.
- Top-level structure starts with frontmatter, title, When to Use, Do Not Use, then Iron Law.
- Leading concept is clear and repeated enough to anchor behavior.
- Description is trigger-focused, not a workflow summary.
- Main file contains the process every run needs.
- Branch-specific or bulky reference content is in one-level references.
- Every step has a completion criterion.
- Every hard gate has a failure output.
- Stop conditions are explicit.
- Rationalization table is based on observed or tested failures.
- Red flags are specific to this skill.
- The skill avoids session narrative and user-story prose.
- The skill is portable unless explicitly scoped otherwise.
- Tests show changed behavior under pressure.

## Information Hierarchy

| Content                  | Location                                    |
| ------------------------ | ------------------------------------------- |
| Always-needed process    | `SKILL.md`                                  |
| Branch-specific workflow | one-level reference                         |
| Long lookup/reference    | one-level reference                         |
| Deterministic operation  | script/check, referenced by skill           |
| Project-only policy      | repository instructions, not portable skill |

## No-Op Test

For each sentence, ask: would an agent behave differently because this sentence exists?

If not, delete it or move it to a reference only when it supports a specific branch.

## Common Failure Corrections

| Failure                          | Correction                                                   |
| -------------------------------- | ------------------------------------------------------------ |
| Skill is a context dump          | Convert to steps, gates, references, and completion criteria |
| Skill is only an output template | Add reasoning method and stop conditions                     |
| Gates are optional               | Make failure output mandatory or remove the gate             |
| Skill is too broad               | Split by invocation or branch                                |
| Skill is too fragmented          | Inline material required by every branch                     |
| Description summarizes process   | Rewrite as trigger conditions                                |
| Skill was not tested             | Run RED/GREEN pressure scenarios                             |

## Portability Check

- Directory name matches `name`.
- `SKILL.md` exists at skill root.
- Frontmatter has `name` and `description`.
- References are one level deep.
- No required harness-specific fields or commands.
- No placeholders or unresolved template text.
