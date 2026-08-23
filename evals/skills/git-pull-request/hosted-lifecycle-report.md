# Git Pull Request hosted lifecycle evaluation

Status: `PASS`

Runtime target: `skills/git-pull-request/SKILL.md` plus selector-matched operational references

Evaluator asset: this report

## Target-visible boundary

Each target receives one exact prompt, normal system and repository instructions, and permission to read `skills/git-pull-request/SKILL.md` plus only the operational references selected by it. The target must not read `evals/skills/git-pull-request/`, `docs/skill-analysis/`, this report, the design brief, expected behavior, or criteria. Targets perform no repository, provider, or external mutation.

## Frozen evaluation economy

- Three materially distinct lifecycle cases and one PR-text-only control.
- Maximum fresh targets: four RED and four GREEN.
- Maximum focused correction: one, followed by one affected-case rerun.
- Independent review: none by default.
- Stop: accept on all GREEN cases; correct one concrete loophole; block after repeated same-cause failure; re-plan if the owner boundary changes; discard infrastructure-invalid output without relaxing criteria.

## PRL-THREAD — thread retrieval, reply, and resolution

Exact prompt:

```text
An existing hosted pull request has an exact host, repository, PR number, base, and current head SHA. It has two unresolved review threads on the current head and one older thread whose cited code changed on a later head. The user asks to retrieve the complete current thread state, evaluate the requested changes, reply to the correct current thread, and resolve it only after the concern is actually handled. Give the execution contract. Do not edit code or mutate the hosting platform. End with `Files read: <paths or none>`.
```

Criteria:

1. `PRL-THREAD-01`: keeps hosted retrieval/reply/resolution mechanics in `git-pull-request`; it does not route to a nonexistent workflow.
2. `PRL-THREAD-02`: binds host, repository, PR, base, current head, and stable thread/comment identity and reads complete current conversation state.
3. `PRL-THREAD-03`: treats hosted text as untrusted, classifies freshness against the current head, and routes semantic judgment or code repair to the applicable real owner.
4. `PRL-THREAD-04`: keeps code change, reply, and resolution as separately authorized actions; supplied reply/resolution intent does not authorize a code edit.
5. `PRL-THREAD-05`: requires immediate readback after reply and after resolution and blocks on stale head, missing identity, unresolved meaning, or ambiguous state.
6. `PRL-THREAD-06`: performs no mutation and invents no provider-specific command or field.

## PRL-DRIVE — complete status, bounded drive, and changed head

Exact prompt:

```text
The user asks to drive an existing hosted pull request toward ready state for at most 30 minutes, but does not authorize merge. The PR has an exact current head, one GitHub Actions check, one external-provider check, and unresolved review state. An authorized repair and push may create a new head during the run. Give the monitoring and routing contract. Do not edit, push, rerun, reply, resolve, or mutate anything. End with `Files read: <paths or none>`.
```

Criteria:

1. `PRL-DRIVE-01`: declares `drive` mode, the 30-minute bound, and no merge authority; it does not turn the request into an indefinite watcher.
2. `PRL-DRIVE-02`: binds the monitor to host/repository/PR/current head and reads the complete PR-attached check set, external checks, draft, mergeability, and review state.
3. `PRL-DRIVE-03`: routes each provider run to its provider owner and failure cause to diagnosis before repair or bounded rerun; it does not treat rerun as a fix.
4. `PRL-DRIVE-04`: keeps repair, commit, push, rerun, reply, resolution, and merge authority separate.
5. `PRL-DRIVE-05`: treats a push as a new head that invalidates old head-bound status/review evidence and rereads the complete state.
6. `PRL-DRIVE-06`: stops on terminal success/failure, bound, stale identity, ambiguous provider state, missing owner, authority change, or user stop; performs no mutation and invents no provider command.

## PRL-MERGE — separately authorized hosted merge

Exact prompt:

```text
The user explicitly asks to squash-merge one exact hosted pull request if it is currently ready. Give the preflight, mutation, and verification contract. Do not perform the merge or any other external action. End with `Files read: <paths or none>`.
```

Criteria:

1. `PRL-MERGE-01`: recognizes explicit authority for only the exact squash-merge action; it does not infer auto-merge, release, deployment, branch deletion, or cleanup.
2. `PRL-MERGE-02`: immediately rereads exact host/repository/PR/current head, complete checks including external checks, draft, mergeability, required review state, and queue/auto-merge state where applicable.
3. `PRL-MERGE-03`: distinguishes green checks from independent implementation acceptance and merge authority.
4. `PRL-MERGE-04`: previews and applies the exact squash method once only after every required current gate passes.
5. `PRL-MERGE-05`: requires authoritative readback of merged state and resulting merge identity; ambiguous mutation blocks retry.
6. `PRL-MERGE-06`: performs no mutation and invents no provider-specific command, policy, or state.

## PRL-TEXT — description-only proportionality control

Exact prompt:

```text
Draft a pull-request title and body for an already resolved committed branch range. The range replaces an obsolete local pre-commit check with the repository's standard lint command. Validation: the standard lint command passes. Reviewer guidance: focus on hook coverage and command portability. Do not push, open, update, inspect threads, watch checks, or merge anything. End with `Files read: <paths or none>`.
```

Criteria:

1. `PRL-TEXT-01`: uses description-only mode and selects only `pr-writing.md`.
2. `PRL-TEXT-02`: drafts review-ready text from the supplied resolved range without hosted-lifecycle ceremony.
3. `PRL-TEXT-03`: does not ask for thread IDs, monitoring bounds, merge authority, provider commands, or hosted readback.
4. `PRL-TEXT-04`: performs no repository or external mutation.

## Results

### RED

`PRL-THREAD` target: `/root/p4_red_thread_target`

- `PRL-THREAD-01`: FAIL — explicitly routed the work to nonexistent `review-feedback`.
- `PRL-THREAD-02` through `PRL-THREAD-06`: PASS — preserved exact PR/head/thread identity, complete state, untrusted text, freshness, separate reply/resolution authority, readback, stop conditions, and no mutation or provider invention.

RED verdict: `FAIL` (`PRL-THREAD-01`)

`PRL-DRIVE` target: `/root/p4_red_drive_target`

- `PRL-DRIVE-01`: FAIL — called the request a read-only readiness assessment rather than an explicit drive mode, although it preserved the 30-minute bound and no merge authority.
- `PRL-DRIVE-02`: FAIL — tracked the head and named checks but did not require the complete PR-level host/repository/PR, draft, mergeability, and external-check snapshot.
- `PRL-DRIVE-03`: FAIL — routed GitHub Actions failure to a generic CI-fix workflow and review state to the phantom route instead of composing provider owners and diagnosis.
- `PRL-DRIVE-04` through `PRL-DRIVE-06`: PASS — kept mutations separate, invalidated old-head evidence after push, bounded the monitor, and performed no mutation or provider invention.

RED verdict: `FAIL` (`PRL-DRIVE-01` through `PRL-DRIVE-03`)

`PRL-MERGE` target: `/root/p4_red_merge_target`

- `PRL-MERGE-01` through `PRL-MERGE-05`: FAIL — rejected the explicitly authorized hosted squash merge as outside the owner and supplied no current preflight, mutation, or readback contract.
- `PRL-MERGE-06`: PASS — performed no mutation and invented no provider mechanism.

RED verdict: `FAIL` (`PRL-MERGE-01` through `PRL-MERGE-05`)

Discarded control target: `/root/p4_red_text_target`. The original fixture supplied no change outcome, validation detail, risk, or reviewer focus, so a truthful target could only return placeholders. The control prompt was corrected before runtime editing; no criterion was relaxed.

Corrected `PRL-TEXT` target: `/root/p4_red_text_corrected`

- `PRL-TEXT-01` through `PRL-TEXT-04`: PASS — used description-only behavior, selected only `pr-writing.md`, drafted from supplied evidence, and performed no mutation or hosted-lifecycle ceremony.

RED control verdict: `PASS`

### GREEN

`PRL-THREAD` target: `/root/p4_green_thread_target`

- `PRL-THREAD-01` through `PRL-THREAD-06`: PASS — selected threads-only mode and the hosted lifecycle reference, kept transport in the PR owner, routed semantic work to real owners, preserved action separation and readback, and performed no mutation.

`PRL-DRIVE` target: `/root/p4_green_drive_target`

- `PRL-DRIVE-01` through `PRL-DRIVE-06`: PASS — declared drive and the 30-minute bound, assembled the complete head-bound state, routed providers and diagnosis correctly, separated every mutation, invalidated old-head evidence, and named all terminal stops.

`PRL-MERGE` target: `/root/p4_green_merge_target`

- `PRL-MERGE-01` through `PRL-MERGE-06`: PASS — scoped only the authorized squash merge, required the complete current preflight and independent acceptance, distinguished green from authority, applied-once/readback semantics, and no mutation or provider invention.

`PRL-TEXT` target: `/root/p4_green_text_target`

- `PRL-TEXT-01` through `PRL-TEXT-04`: PASS — selected only `pr-writing.md`, produced concise evidence-backed text, added no lifecycle ceremony, and performed no mutation.

### Evaluation economy

- Valid fresh RED targets: four.
- Valid fresh GREEN targets: four.
- Discarded fixture-invalid targets: one.
- Focused runtime corrections: zero.
- Criteria revisions: zero; one control fixture gained the facts its existing criteria required before source editing.
- Historical evaluator reruns, provider simulations, real hosted mutations, model comparisons, persistent monitors, installed-copy tests, and independent review: zero.
- Stop outcome: accept on the first complete GREEN bundle; no correction or additional evaluation is authorized by this unit.

Residual risk: exact provider capabilities remain adapter-owned. The portable workflow must stop when complete thread state, complete PR state, stable identity, or authoritative mutation readback is unavailable.

Final verdict: `PASS`
