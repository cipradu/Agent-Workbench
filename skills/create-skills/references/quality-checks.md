# Quality Checks

Use this reference before accepting a new or revised skill.

## Skill Quality Checklist

- The skill solves a recurring behavior problem.
- Source signals were classified before becoming instructions.
- Current source evidence was read for existing-skill work: `SKILL.md`, one-level references, related skills, rules, scripts/checks/hooks/CI, agents/subagents, test evidence, and invocation surfaces.
- Exact available skill entries were checked before claiming no existing owner fits.
- A lighter mechanism was considered and rejected with reason.
- Skill type is explicit.
- Top-level structure starts with frontmatter, title, When to Use, Do Not Use, then Iron Law.
- Leading concept is clear and repeated enough to anchor behavior.
- Description is trigger-focused, not a workflow summary.
- Autonomous exposure is justified by a real trigger or cross-skill reach need.
- Main file contains the process every run needs.
- Branch-specific or bulky reference content is in one-level references.
- Reference pointers state when to load the material, not just where it lives.
- Every step has a completion criterion.
- Every hard gate has a failure output.
- Stop conditions are explicit.
- Rationalization table is based on observed or tested failures.
- Red flags are specific to this skill.
- The skill avoids session narrative and user-story prose.
- No-op, stale, or branch-local lines were deleted or moved behind a pointer.
- Behavior-preserving cleanup states which gate, stop condition, safety boundary, or reference pointer was preserved.
- RED/GREEN criteria were stable, or revisions and reruns are recorded.
- The skill is portable unless explicitly scoped otherwise.
- Tests show changed behavior under pressure.

## Hard Gates Versus Diagnostics

Hard gates:

- recurring behavior failure or explicit no-skill stop;
- current owner and inventory check;
- lighter-mechanism decision;
- skill type and structure fit;
- RED baseline or provisional label with fixed criteria;
- GREEN behavior proof against the same criteria;
- mandatory gates with failure outputs;
- portability and one-level reference checks;
- no no-op sediment that weakens signal.

Diagnostics:

- file length;
- number of references;
- number of scenarios;
- prose polish;
- template completeness;
- reviewer preference when not tied to a hard gate.

Diagnostics can guide refactor, but they do not prove the skill changes behavior.

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
| Reference pointer is vague       | Rewrite the pointer around the condition for loading it      |
| Skill carries stale sediment     | Delete stale lines instead of rewording them                 |
| Skill was not tested             | Run RED/GREEN pressure scenarios                             |
| Existing-skill edit rewrites too much | Preserve owner boundary and make targeted behavior changes |
| Feedback is pasted as instructions | Classify source signal, restate behavior failure, then test |
| Tool workflow has vague fallback | State substitution limits, stop condition, and verification  |

## Skill-Validation Packet

For validation, record:

- finding or concern;
- affected gate or reference;
- evidence and source scope;
- consequence if ignored;
- actionability and confidence basis;
- false-positive or rejected rationale;
- readiness state: ready to create, ready to revise, ready to ship, provisional needs baseline RED, blocked missing failure, blocked lighter mechanism wins, blocked missing GREEN proof, or reroute.

This packet supports downstream review or handoff. It does not own independent reviewer dispatch, verdicts, commits, PRs, or release decisions.

## Tool-Workflow Check

- Preflight state and availability are explicit.
- Exact command/action output, sentinel, nonzero, timeout, and ambiguous-result meanings are defined.
- Native owner and substitution policy are defined.
- Allowed writes, forbidden mutations, credentials, privacy, local state, cleanup, and teardown are explicit.
- Manual handoff or stop condition is defined when the workflow cannot preserve its safety promise.
- Verification checks the actual side effect or readback, not only command completion.

## Portability Check

- Directory name matches `name`.
- `SKILL.md` exists at skill root.
- Frontmatter has `name` and `description`.
- References are one level deep.
- No required harness-specific fields or commands in the portable core.
- No placeholders or unresolved template text.
