# Message Conventions

Use this reference when a commit message convention, type, body, or footer decision is not obvious from repository instructions and recent history.

## Detection Order

1. Repository instructions: `AGENTS.md`, `CLAUDE.md`, contribution docs, commit template, release tooling notes, or explicit user direction.
2. Recent history: `git log --oneline -10`, expanding to more commits only if the first sample is noisy.
3. Conventional Commits fallback: use only when no stronger local convention exists.

Do not invent a new style because it looks cleaner than the repository history. Do not copy a bad message pattern when documented rules contradict it.

## Conventional Commits Fallback

Format:

```text
<type>(<scope>): <description>

<body>

<footer>
```

Common types:

| Type       | Use when                                                                              |
| ---------- | ------------------------------------------------------------------------------------- |
| `feat`     | Adds a user, operator, developer, or integration capability that did not exist before |
| `fix`      | Corrects broken, missing, unsafe, or unintended behavior                              |
| `refactor` | Changes internal structure without intended behavior change                           |
| `perf`     | Improves performance or resource usage                                                |
| `test`     | Adds or changes tests or test infrastructure                                          |
| `docs`     | Changes documentation only                                                            |
| `style`    | Formatting-only changes with no behavior or tooling change                            |
| `chore`    | Maintenance, repository housekeeping, or non-runtime support work                     |
| `build`    | Build system, packaging, dependency graph, or artifact generation changes             |
| `ci`       | CI/CD workflow or automation changes                                                  |
| `revert`   | Reverts an earlier commit                                                             |

When `fix` and `feat` both seem plausible, prefer `fix` if the change remedies behavior users or maintainers reasonably expected to work. Reserve `feat` for a genuinely new capability.

Scope is optional. Use the narrowest stable project area when it adds clarity. Omit scope when no single scope is honest.

## Body Decision

Add a body when any of these are true:

- the commit touches more than three files;
- the commit changes public API, data model, schema, migration, authentication, permissions, security, privacy, billing, operations, agent rules, skills, templates, or workflow/control artifacts;
- the commit includes tests or verification whose significance is not obvious;
- the commit intentionally excludes files that might look related;
- the commit is a refactor whose preservation boundary matters;
- the commit message needs to record why this approach was chosen.

The body should answer the useful subset of:

- What was broken, missing, risky, or hard to maintain before?
- What is true after this commit?
- Why is this the chosen boundary or approach?
- How was it verified?
- What scope was intentionally excluded?

Do not hard-wrap body prose at a fixed column width unless the repository explicitly requires it. Use blank lines, bullets, or paragraphs where they carry meaning.

## Footer Decision

Use footers only for semantic metadata that the repository expects or the user requested.

Allowed when explicitly justified:

- `BREAKING CHANGE: <description>` for confirmed breaking changes.
- `Refs <id>` or equivalent non-closing references when the repo uses them.
- Real human co-author trailers only when the user dictates the exact human identity.
- `Signed-off-by` only when the repository requires Developer Certificate of Origin signoff.

Avoid by default:

- `Closes`, `Fixes`, or other issue-closing footers unless the user or repo policy wants the commit to close the issue on merge.
- Assistant/tool attribution lines.
- AI co-author trailers.
- Promotional badges, links, or signatures.

## Anti-Patterns

| Bad                          | Better                                                          |
| ---------------------------- | --------------------------------------------------------------- |
| `updates`                    | `fix(auth): reject expired refresh tokens`                      |
| `misc changes`               | Split into logical commits or name the single coherent behavior |
| `wip`                        | Finish, verify, and commit a reviewable unit                    |
| `update files`               | Explain the behavior or maintenance outcome                     |
| `feat!: change API`          | Use breaking markers only after explicit confirmation           |
| `fix bug`                    | Name the failing behavior and the corrected outcome             |
| Assistant attribution footer | End on the last substantive line                                |
