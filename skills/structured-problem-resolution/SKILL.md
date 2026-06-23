---
name: structured-problem-resolution
description: Use when any software problem, failure signal, review feedback, bug report, human or AI suggestion, failed fix, or unexplained behavior needs diagnosis before action. Trigger on failing tests, runtime errors, build errors, broken commands, unexpected behavior, performance issues, flaky behavior, regressions, code review comments, suggested fixes, "this doesn't work", "why is this happening", "fix this error", or repeated failed attempts. Requires signal evaluation, evidence gathering, current research for drift-prone external facts, hypothesis testing, impact analysis, precise fix, and verification; prevents sycophantic agreement, blind implementation, model-memory fixes, and guess-and-check debugging.
---

# Structured Problem Resolution

## When to Use

Use this skill when:

- something is failing, broken, slow, flaky, surprising, or different from expected behavior;
- tests, builds, commands, runtime flows, deployments, integrations, or local tooling fail;
- the user asks to fix an error, investigate a bug, explain why something is happening, or evaluate a proposed fix;
- a code review comment, bug report, human suggestion, AI review, linter warning, or external ticket claims something is wrong;
- a previous fix attempt failed, changed the error, reduced but did not eliminate the problem, or introduced a new symptom;
- the cause is not known, the signal may be misleading, or the suggested fix has not been verified against the codebase;
- the answer depends on current library, framework, runtime, package, API, security, platform, browser, database, or third-party behavior.

## Do Not Use

Do not use this skill as the primary workflow when:

- the user wants product definition, an engineering spec, an implementation plan, architecture design, an ADR, or a code review rather than diagnosis;
- the desired behavior is unknown and needs product/spec clarification before a defect can be defined;
- the work is a clearly mechanical typo, missing import, syntax error, or formatting-only issue where the exact mechanism and one-line fix are already proven; use the Obvious branch and still verify;
- the issue has already been diagnosed with evidence and the remaining work is non-trivial implementation planning or architecture decision-making;
- the request is purely explanatory and does not involve a failure, disputed signal, suggested fix, or unresolved cause.

## Iron Law

Treat every failure, review comment, bug report, and suggested fix as a signal to investigate before changing code. Do not implement from intuition, authority, social pressure, or model memory when the cause or external behavior has not been verified.

## Core Concept

Signals are hypotheses, not instructions. The job is to convert a signal into evidence, a falsifiable mechanism, an impact-aware fix, and verification. Current external facts must come from current evidence, not training data; local behavior must come from the actual code and runtime, not memory.

## Knowledge Cutoff Guard

Model memory is allowed only to generate search terms and hypotheses. It is not evidence.

Current research is mandatory before relying on any fact that can drift over time:

- package, library, framework, runtime, browser, database, platform, API, CLI, SaaS, cloud, security, or protocol behavior;
- deprecations, latest stable versions, migration guidance, compatibility claims, bug reports, changelog behavior, or security recommendations;
- third-party examples, documentation patterns, or "best practice" claims that may have changed.

If the problem is purely local code behavior, record the local evidence instead: exact error output, reproduction steps, relevant code paths, tests, recent diffs, logs, config, and runtime state. Do not skip the research/evidence gate; record why external/current research is not relevant.

## Why This Matters

Two patterns waste the most time in software development:

**Pattern 1: Guess-and-check debugging.** See error, guess at fix, apply fix, see different error, guess again, apply another fix — now there are two problems. Each uninformed fix attempt risks compounding the problem because you're changing code you don't fully understand. Expert debuggers spend roughly 80% of their time _understanding_ a bug and 20% _fixing_ it. The fix, once you truly understand the problem, is usually straightforward.

**Pattern 2: Blind implementation of feedback.** Receive suggestion, say "good catch!", implement without verifying, introduce regression or fix the wrong thing. This happens because social pressure — from reviewers, bug reporters, or authority figures — bypasses the verification step. The suggestion becomes an unquestioned instruction rather than a hypothesis to evaluate.

Both patterns share the same root failure: **acting before understanding**. This skill provides a unified pipeline that handles any signal — whether it's an error message, a failing test, a code review comment, or a colleague's suggestion — with the same disciplined approach: receive critically, understand thoroughly, fix precisely, verify completely.

Finding the root cause is only half the job. A fix that solves the immediate problem but breaks three other things isn't a fix — it's a trade. Before you change code, understand why the problem exists, and after you propose a fix, reason through its implications. Think in systems, not in patches.

---

## Phase 1: Receive and Evaluate the Signal

Every resolution starts with a signal — something that tells you attention is needed. The signal might be an error message, a failing test, a code review comment, a bug report, or a human's opinion about your code. How you receive and evaluate that signal determines everything that follows.

The critical discipline: **treat every signal as a hypothesis to verify, not an instruction to follow.** This applies equally to error messages (which can be misleading) and human feedback (which can be wrong).

### Error Messages and Test Failures

These are the most objective signals, but they still require careful reading:

- **Read the full error.** Don't skim. Read the complete error message, the full stack trace, every warning. Error messages frequently contain the exact answer.
- **Parse the stack trace strategically.** Find the first frame in _your_ code (not library/framework code). Read the exception type before the message — `KeyError` vs `TypeError` vs `AttributeError` tells you the category of mistake. In chained exceptions, the root cause is at the bottom.
- **Check what changed.** If something was working and stopped, ask: what changed between when it worked and when it broke? Recent commits, dependency updates, config changes, environment differences.
- **Look for absence.** Don't only look for errors in output — look for expected output that's _absent_. A missing log line tells you where execution stopped.

### Human Feedback, Code Reviews, and Bug Reports

Human input is the trickiest signal because it comes pre-interpreted. A reviewer doesn't say "line 42 executes branch A when the input is null" — they say "this function is broken." A bug reporter doesn't say "the response took 12 seconds" — they say "the API is slow." You receive their **diagnosis**, not their **observations**.

**Strip the diagnosis. Keep the observations.**

Bug report: "The caching layer is broken — users see stale data after deploy."
Reframe as observations: "After deployment at 14:30, some users see pre-deployment data. Resolves after ~10 minutes."

Now you can independently consider: Is it actually a cache issue? Could it be CDN, browser cache, load balancer routing to old instances, or a rolling deploy still completing?

**The "Handed Hypothesis" problem:** When someone tells you "X is wrong, fix it by doing Y," they're handing you a pre-formed hypothesis. Your job is to _test_ that hypothesis, not _implement_ it. The reviewer may be right — but they may also be wrong, missing context, or solving a problem that doesn't exist.

**The "Explain It Back" test:** Before implementing any non-trivial suggestion, restate in your own words what the problem is and why the change fixes it. If you cannot do this, you do not understand the feedback well enough to implement it correctly.

### Source Trust Calibration

Not all signals deserve equal trust. Calibrate based on source:

| Source                              | Trust Level                          | Key Risk                                     | Verify How                        |
| ----------------------------------- | ------------------------------------ | -------------------------------------------- | --------------------------------- |
| Error messages / stack traces       | High for facts, can mislead on cause | Symptom far from root cause                  | Trace backward from failure point |
| Your human partner                  | High — implement after understanding | Scope may be unclear                         | Ask if uncertain, skip to action  |
| Domain expert on this code          | High for this area                   | May not know recent changes                  | Cross-reference with tests        |
| General senior engineer             | Medium-High                          | May not know this codebase                   | Verify claims against code        |
| External / OSS reviewer             | Medium                               | Lacks your project's context                 | Verify context assumptions        |
| Junior team member                  | Medium                               | Less experience, but may know recent changes | Same verification as anyone       |
| Automated linters / static analysis | Very High for what they check        | Narrow scope                                 | Almost always implement           |
| AI-generated review                 | Medium for patterns, Low for context | Poor context awareness                       | Always verify against actual code |

**Expertise is domain-specific.** A brilliant backend engineer may give poor advice about CSS. Evaluate each comment against the reviewer's expertise in the specific area being commented on, not their general reputation.

### The Anti-Sycophancy Principle

This matters whether you're human or AI: **social pressure must never bypass verification.**

The failure pattern: someone with authority says "this is wrong." You feel pressure to agree immediately and fix it. You skip verification. You either implement a wrong fix (making things worse) or fix something that wasn't broken (wasting time and potentially introducing real bugs).

**How to respond to any signal:**

```
NEVER:
- "You're absolutely right!" (before verifying)
- "Great point!" / "Thanks for catching that!" (performative)
- "Let me fix that now" (before understanding)

INSTEAD:
- Restate the technical requirement in your own words
- Verify the claim against the actual code
- Ask clarifying questions if anything is unclear
- Push back with technical reasoning if the claim is wrong
- Just start working — actions speak louder than agreement
```

When feedback IS correct, acknowledge it through action:

```
✅ "Fixed. [Brief description of what changed]"
✅ "Good catch — [specific issue]. Fixed in [location]."
✅ [Just fix it and show the result]

❌ "You're absolutely right!"
❌ "Great point! Thanks for catching that!"
❌ Any gratitude expression or performative agreement
```

See [signal-evaluation.md](signal-evaluation.md) for detailed patterns on evaluating different signal types, multi-item feedback handling, the four-axis evaluation framework, and the push-back framework.

---

## Phase 2: Triage

Not every problem needs the same level of investigation. Before diving in, assess what you're dealing with.

### Obvious (seconds)

The signal tells you exactly what's wrong and the fix is unambiguous.

**Signals:** Clear error like `NameError: name 'foob' is not defined`, `SyntaxError`, missing import. One-line fix. You can explain the exact mechanism of the failure.

**Action:** Fix it directly. No process needed. But if your "obvious" fix doesn't work on the first try, upgrade to Simple.

### Simple (minutes)

The signal points to a general area, but you need to read code to understand what's happening.

**Signals:** Error points to a region but not an exact cause. Involves one file or function. Requires reading context.

**Action:** Read the relevant code. Understand the data flow. Form a hypothesis. Fix. Verify.

### Complex (deliberate investigation)

Multiple possible causes, spans multiple files or components, or the signal is misleading.

**Signals:** Vague or misleading error. Interaction between components. Intermittent or environment-dependent. A previous fix attempt failed. Human feedback that requires verification against the codebase.

**Action:** Full investigation loop (Phase 3). Invest in understanding before touching code.

### Architectural (stop and discuss)

The problem reveals a design issue, not just a code bug.

**Signals:** 3+ fix attempts have failed, each revealing new issues. Every fix requires touching many files. Fixes create new symptoms elsewhere. The pattern itself seems fundamentally wrong.

**Action:** Stop coding. Describe what you've found to the user. This isn't a problem to fix — it's a design to reconsider.

### Default Assumption: Complex

The natural instinct is to classify problems as Obvious or Simple — you see an error, you have a theory immediately, so it feels trivial. This instinct is wrong more often than it's right, and when it's wrong, it turns a 1-2 pass investigation into 5-7 passes of guess-and-check.

**The default classification is Complex.** Every problem gets full investigation (Phase 3) and a scratch file unless you can demonstrate in one sentence why it's truly trivial. The bar for Obvious is strict: a single-line fix where you can state the exact mechanism of failure without reading any surrounding code (typo, missing import, syntax error). Everything else gets the scratch file and full investigation.

If your "Obvious" fix doesn't work on the first try, you were wrong about the classification. Create the scratch file immediately and start Phase 3.

---

## Phase 3: Investigate

This is the core loop. The discipline: **understand before you change.**

### Step 1: Observe (what is actually happening?)

Before forming any theory, gather facts. This is the most important step and the one most often skipped.

**If the signal is an error:** Read it carefully. Note exact line numbers, file paths, variable values. Check what changed recently. Look for what's missing in the output, not just what's present.

**If the signal is human feedback:** Separate observations from interpretations. What did the reviewer actually see vs. what do they think is happening? Re-read the actual code they're commenting on — do not respond from memory or from the reviewer's description of the code.

**Reproduce it.** Can you trigger the problem reliably? If yes, you have a fast feedback loop for testing hypotheses. If no, gather more data about the conditions under which it occurs. For feedback-driven signals: can you reproduce the scenario the reviewer describes?

**Build the feedback loop before testing hypotheses.** A feedback loop is a fast, deterministic, agent-runnable pass/fail signal for the user's actual symptom. It can be a test, command, script, trace replay, browser check, benchmark, or structured manual capture, but it must tell you whether the original symptom is present. If no reliable loop exists, the next task is to build or sharpen the loop, not to guess at fixes.

Use the lightest loop that reaches the real bug:

1. Failing test at the seam that exercises the bug: unit, integration, contract, or end-to-end.
2. HTTP/API command against a running service, with exact request, response, status, headers, and relevant logs captured.
3. CLI invocation with a fixture input and expected stdout, stderr, exit code, or output diff.
4. Browser automation for UI failures, asserting on DOM, console, network, storage, and visible state as relevant.
5. Captured trace replay: saved network request, event payload, log sequence, queue message, job input, or data fixture replayed through the smallest real path.
6. Throwaway harness around one service, module, or function with dependencies mocked only at true external boundaries.
7. Property, fuzz, stress, or repeated-run loop when the symptom is intermittent or data-dependent.
8. Bisect or differential loop when a known-good state, prior version, alternate config, or dataset can be compared against the failing state.
9. Structured human-in-the-loop capture only as a last resort, with exact steps, timestamps, observed output, screenshots/logs when useful, and enough structure to compare before and after.

Iterate on the loop itself. Make it faster by narrowing setup, sharper by asserting the specific symptom instead of a broad crash/pass, and more deterministic by controlling time, randomness, filesystem, network, concurrency, and external services where possible. For nondeterministic bugs, the immediate goal is a higher reproduction rate; loop the trigger, add stress, widen timing windows, or capture enough runs to make the failure debuggable.

If you genuinely cannot build a loop, stop and say what you tried. Ask for the missing artifact or access: a reproducing environment, HAR/network capture, log dump, core dump, trace, fixture, screen recording with timestamps, data sample, or permission to add temporary diagnostic instrumentation. Do not proceed as if a hypothesis is confirmed without a loop or equivalent evidence.

**Check what changed.** `git log`, `git diff`, recent dependency updates. The single most productive question for any problem that used to work: what's different between when it worked and when it broke?

### Step 2: Hypothesize (what do you think is happening, and why?)

Form a specific, falsifiable hypothesis. Not "something's wrong with the database" but "the query returns zero rows because the WHERE clause uses the wrong column name."

**The mechanism test:** If you can't explain the precise mechanism by which your proposed cause produces the observed symptom, your hypothesis isn't specific enough. "Race condition" is not a hypothesis. "Thread A reads the counter, then Thread B increments and writes, then Thread A overwrites with its stale value" is a hypothesis.

**Generate alternatives.** Before investigating your first hypothesis, spend 30 seconds listing 2-3 other possible causes. Rank by likelihood and testability. This prevents anchoring on the first idea — whether it came from your own intuition, an error message, or a reviewer's suggestion.

**State it explicitly.** Write your hypothesis down (in the conversation or as a comment). This creates accountability and makes your reasoning visible. You can't unconsciously shift your theory to match new evidence if you've committed to a specific prediction.

**If the hypothesis came from someone else** (reviewer, bug reporter, colleague): treat it the same as your own hypothesis. It needs evidence before you act on it. Their authority doesn't make it correct — only evidence does.

### Step 3: Research and Evidence Check (what is already known?)

**This step is mandatory.** Now that you have a hypothesis and alternative candidates, gather evidence before you start experimenting. Research means seeking evidence outside your memory. For external or drift-prone behavior, use current external sources. For purely local code behavior, use codebase/runtime evidence and record why external research is not relevant.

Many issues — especially those involving libraries, frameworks, version upgrades, configuration, or infrastructure — have already been encountered and solved by someone else. Five minutes of research can save hours of guessing.

**What to check:**

- The exact error message, quoted verbatim — this is your highest-signal search
- Your hypothesis + the library/framework name + version
- GitHub issues on the relevant repositories
- The library's changelog or release notes if a version change is involved
- Local code paths, tests, recent diffs, config, logs, runtime state, and reproduction steps when the issue is project-local

**When to use current external research:** Always when the answer depends on library, framework, runtime, package, API, security, browser, database, platform, SaaS, cloud, protocol, deprecation, migration, compatibility, or "best practice" claims. Even if you think you know the answer, verify anyway. You might find that the behavior changed, the API was deprecated, the known workaround is obsolete, or your initial intuition is wrong.

**When local evidence is enough:** When the hypothesis is about this repository's own code, data flow, configuration, tests, or recent diffs and no external behavior claim is needed. In that case, record the local evidence and explicitly write `External/current research not required because <reason>`.

**How to research:** Use the `research` subagent (subagent_type: "research") when external/current evidence is required and the environment permits delegation. If the research agent is not available or fails, fall back to whatever search/web/docs tools the environment provides (WebSearch, WebFetch, MCP tools, Context7, official docs, package repositories, changelogs, issue trackers, etc.). If you need follow-up questions or deeper investigation from a prior research result, resume the previous research agent session rather than starting a new one when the harness supports it.

**What to do with the results:**

- If you find the answer: verify it applies to your specific situation, then proceed to fix
- If you find related issues but no direct answer: use them to refine your hypotheses before testing in Step 4
- If you find nothing: that itself is information — the problem is likely specific to this codebase, not a known issue. Proceed to Step 4
- If local evidence is sufficient: cite the exact files, commands, outputs, or runtime observations that support the hypothesis

**The bias you're fighting:** There is a strong pull toward figuring things out from first principles — reading code, forming theories, running experiments. This feels productive but is often catastrophically wasteful. The error message you're staring at may have a documented upstream fix. The library bug you're trying to work around may have a GitHub issue with a specific version boundary. Your training data may describe old behavior. Check before acting.

**Structural enforcement:** Research/evidence results must be recorded in the scratch file before you proceed to Step 4 or make any source edits. The scratch file must contain current external findings when external behavior matters, or local evidence plus the reason external research is not relevant when the issue is purely local. Skipping this step is a gate violation, same as skipping the scratch file itself. There is no shortcut past this gate.

### Step 4: Test (gather evidence for or against)

Design the _smallest_ experiment that would confirm or disprove your hypothesis.

**Prefer observation over modification.** Before changing code, try to verify through observation: add a log or print statement, check a variable's value, read the database state, inspect network traffic. Observation is free — it doesn't risk introducing new problems.

**Instrument narrowly.** Prefer debugger/REPL inspection when available. If you add temporary logs or probes, each one must distinguish a specific hypothesis and use a unique searchable prefix such as `[DEBUG-<short-token>]` so cleanup is mechanical. Never "log everything and grep." For performance problems, establish a baseline measurement first; use timing harnesses, profilers, query plans, resource metrics, or benchmarks rather than intuition-heavy logging.

**One variable at a time.** If you change multiple things, you won't know which one mattered. Make one change, observe the result, then decide your next move.

**Try to disprove, not confirm.** The most dangerous debugging error is confirmation bias — interpreting ambiguous evidence as supporting your hypothesis. Actively look for evidence that would prove you wrong. Ask: "What would I expect to see if my hypothesis is _incorrect_?"

**What the result means:**

- **Hypothesis confirmed:** Proceed to Step 5, then to Phase 4 (Fix).
- **Hypothesis disproven:** This is progress. You've eliminated a possibility. Return to Step 2 with new information.
- **Evidence ambiguous:** Your experiment wasn't targeted enough. Design a more specific one. Do not treat ambiguous evidence as confirmation.

### Step 5: Understand Contributing Factors

Before jumping to a fix, step back and understand _why this problem exists_. The root cause tells you _what_ is wrong. The contributing factors tell you _how it got that way_ — and that understanding is what separates a lasting fix from a patch that trades one problem for another.

**Ask:** How did this code end up in a problematic state?

- Was it a design decision that didn't account for this use case?
- Was it a refactoring that changed behavior without updating all callers?
- Was it an assumption that was once true but no longer is?
- Was it a copy-paste from another context where it worked differently?
- Was it a gap in test coverage that let this slip through?

**Ask:** Is this a pattern or a one-off?

- Does the same mistake exist elsewhere in the codebase? If so, flag it.
- Is the contributing factor systemic (e.g., the codebase routinely mutates shared data) or isolated?

For feedback-driven problems: Was the reviewer identifying a one-off issue or a recurring pattern? Understanding this changes the scope of the fix.

### Techniques by Situation

Practical starting points for common scenarios. See [techniques.md](techniques.md) for detailed walkthroughs.

**"I don't know where the problem is"**

- **Binary search (Wolf Fence):** Insert a check at the midpoint of the suspect code path. State correct there? Problem is in the second half. Repeat. O(log n) instead of O(n).
- **git bisect:** Binary search through commit history to find the introducing commit. Automate with `git bisect run <test-command>`.
- **Subtractive debugging:** Remove components one at a time (comment out middleware, disable plugins, stub functions with hardcoded returns). When the problem disappears, the last removed component is involved.
- **Minimal reproducible example:** Strip away everything not needed to trigger the problem. The process of minimizing often reveals the cause.

**"I know where but not why"**

- **Backward tracing:** Start at the failure point and trace backward. Where does the bad value originate? What called this function with this argument? Keep going up the call chain until you find the source.
- **State snapshots:** Log the complete relevant state at key transition points. Format consistently so you can compare expected vs actual.
- **Watchpoints:** If your debugger supports it, set a hardware breakpoint on a variable. The debugger pauses exactly when that value changes, showing what modified it and from where.

**"It only fails sometimes"**

- **Identify the conditions:** What differs between passing and failing runs? Timing, data, environment, test ordering?
- **For race conditions:** Use sanitizers (ThreadSanitizer, AddressSanitizer) or deterministic replay tools (`rr`).
- **For flaky tests:** Run the failing test in isolation first. If it passes alone, it's being polluted by another test. Binary search for the polluter.
- **Increase determinism:** Mock time, seed random number generators, control concurrency.

**"It works locally but fails elsewhere"**

- **Diff the environments:** Systematically compare runtime versions, env vars, config files, OS, network, permissions, disk space, and dependency versions.
- **Reproduce the environment:** Run the same container image locally.
- **Add diagnostic output on failure:** Configure CI/deployment to dump env vars, process lists, disk and memory usage, and relevant state only on failure.

**"It's a performance problem"**

- **Measure first, don't guess.** Get a baseline measurement. Is the CPU saturated (compute-bound) or idle (I/O or contention-bound)? The answer determines your entire investigation strategy.
- **Flame graphs** for CPU-bound issues: collect stack traces, visualize where time is spent. The widest bars are your bottlenecks.
- **The USE method** for resource issues: for each resource (CPU, memory, disk, network), check Utilization, Saturation, and Errors.
- **Profiling tools** vary by stack — use what's available in the relevant ecosystem.

**"I don't understand this code well enough"**

- **Read the tests first.** Tests are executable documentation showing expected behavior.
- **Trace a concrete request end-to-end.** Pick one specific input and follow it through the system, noting each transformation.
- **Check the git history.** `git log --oneline <file>` and `git blame` show how code evolved and why.
- **Read the error message one more time.** After understanding the code better, the error often makes more sense on a second reading.

---

## Phase 4: Fix with Impact Analysis

**Gate 2 is active here.** You have a confirmed hypothesis and a proposed fix. Before you write a single line of fix code, the impact analysis section of the scratch file must be filled in. This is where 60% of regressions are prevented — not by testing after the fact, but by thinking before the change. "I think this is it" is not impact analysis. Trace the callers. Check the contracts. Identify what else touches the code you're about to change. Write it down. Then — and only then — make the edit.

### Fix at the Source, Not the Symptom

If a function receives `null` and crashes, the fix isn't adding a null check at the crash point. The fix is finding why `null` was passed in the first place and preventing that. Trace the bad value backward through the call chain to find where it originates.

### Impact Analysis

Before implementing, analyze the blast radius of your proposed fix:

- **Who calls this code?** Trace the callers of the function or component you're about to change. If you change `anonymize_users` to copy dicts instead of mutating them, does any caller _depend_ on the mutation?
- **What contracts or interfaces change?** If a function currently modifies its input in-place and you change it to return a new copy, that's a behavioral contract change. Callers that relied on the side effect will silently break.
- **What are the edge cases of your fix?** If you remove a validation step, what happens to inputs the validation was designed to catch? If you change a type, what happens to comparisons, serialization, or storage?
- **Could the fix introduce regressions?** Think about related functionality, not just the failing test. A fix to the payment module might affect the refund module. A fix to the config loader might affect startup time or caching behavior.
- **What tests cover this area?** Run them in your head (or actually run them) before committing. If there's no test coverage, that's a risk to flag.

**State the impact analysis explicitly.** Say: "This fix changes X. It affects callers A, B, C. Caller A should be fine because [reason]. Caller B might need adjustment because [reason]. No existing tests should break because [reason]." Making this reasoning visible lets the user catch things you missed.

### YAGNI Checks

When feedback suggests adding features, capabilities, or abstractions:

```
IF reviewer suggests "implementing properly" or adding new capability:
  Search the codebase for actual usage

  IF unused or speculative: Flag it.
    "This isn't called anywhere. Remove it (YAGNI)? Or is there usage I'm missing?"
  IF actively used: Then implement properly
```

Don't add features, error handling, or abstractions for scenarios that can't happen. Only validate at system boundaries (user input, external APIs). Don't use feature flags or backwards-compatibility shims when you can just change the code. Three similar lines of code is better than a premature abstraction.

### Minimal Change

Fix the problem and nothing else. Don't refactor nearby code, add unrelated improvements, or "clean up while you're here." Each additional change is a chance to introduce new bugs and makes it harder to verify the fix.

---

## Phase 5: Verify and Respond

### Verification

**Immediate checks:**

- Does the original problem go away?
- Do ALL existing tests still pass (not just the one that was failing)?
- Re-run the original feedback loop against the un-minimized scenario, not only the narrowed reproduction.
- Add regression coverage at the correct seam when such a seam exists. The correct seam exercises the real bug pattern as it occurred at the call site; a shallow test that cannot reproduce the triggering chain is false confidence.
- If no correct regression seam exists, document that as a testability or architecture gap instead of pretending a weak test proves the fix.
- Remove temporary diagnostic logs, probes, traces, fixtures, and throwaway harnesses unless they were intentionally promoted into maintained tests or tooling.

**Implication validation:**

- **Check callers and dependents.** If you changed a function's behavior, verify that every caller still works correctly with the new behavior. Don't assume — check.
- **Look for the same bug elsewhere.** If the root cause was a pattern (e.g., in-place mutation of shared data), search for the same pattern in the codebase. Flag other instances to the user even if you don't fix them now.
- **Consider second-order effects.** Your fix changes behavior. Does anything downstream depend on the old (buggy) behavior? Sometimes other code has worked around the bug, and fixing it breaks the workaround.
- **Assess regression risk.** State your confidence: "This fix is low-risk because it's isolated to one function with good test coverage" or "This fix touches shared infrastructure — recommend running the full test suite and watching for issues in [area]."

**If the fix doesn't work:** Don't stack more fixes on top. Stop. Analyze _why_ it didn't work — that's new information about the problem. The failed fix tells you something about what the problem _isn't_. Return to Phase 3, Step 1 with this new evidence.

### Responding to the Signal Source

How you respond depends on who sent the signal:

**Self-directed (you found the problem):** Verify and move on.

**From your human partner:**

- Implement after understanding — they're trusted
- Still ask if scope is unclear
- No performative agreement
- Skip to action or brief technical acknowledgment

**From external reviewers or bug reporters:**

When the feedback is correct:

```
✅ "Fixed. [What changed]"
✅ "Good catch — [specific issue]. Fixed in [location]."
✅ [Just fix it and show in the code]
```

When you need to push back:

```
✅ "Checking... [component] needs [X] for backward compat.
    Fix the [specific issue] or drop [constraint]?"
✅ "Grepped codebase — nothing calls this. Remove it (YAGNI)?
    Or is there usage I'm missing?"
✅ "Can't verify this without [X]. Should I [investigate/ask/proceed]?"
```

When you pushed back and were wrong:

```
✅ "You were right — I checked [X] and it does [Y]. Implementing now."
✅ "Verified and you're correct. My initial understanding was wrong
    because [reason]. Fixing."

❌ Long apology
❌ Defending why you pushed back
❌ Over-explaining
```

State the correction factually and move on.

**Push back when:**

- Suggestion breaks existing functionality
- Reviewer lacks full context
- Violates YAGNI (unused feature)
- Technically incorrect for this stack
- Legacy/compatibility reasons exist
- Conflicts with established architectural decisions

**How to push back:** Use technical reasoning, not defensiveness. Ask specific questions. Reference working tests or code. If the disagreement is architectural, involve the decision-maker.

### Multi-Item Feedback

When receiving feedback with multiple items:

```
1. READ all items before responding to any
2. CLARIFY anything unclear FIRST — items may be related
3. CLASSIFY each item (defect / design / style / optimization / preference)
4. PRIORITIZE by impact:
   a. Blocking issues (security, data loss, crashes)
   b. Correctness issues (logic errors, wrong behavior)
   c. Simple fixes (typos, imports, naming)
   d. Complex changes (refactoring, redesign)
   e. Style/preference items
5. IMPLEMENT one at a time, test each
6. VERIFY no regressions between fixes
```

If some items are unclear, stop and clarify before implementing any. Partial understanding leads to wrong implementation:

```
"Fix items 1-6"
You understand 1,2,3,6. Unclear on 4,5.

❌ Implement 1,2,3,6 now, ask about 4,5 later
✅ "Understand 1,2,3,6. Need clarification on 4 and 5 before proceeding."
```

### GitHub Thread Replies

When replying to inline review comments on GitHub, reply in the comment thread (`gh api repos/{owner}/{repo}/pulls/{pr}/comments/{id}/replies`), not as a top-level PR comment.

---

## The Investigation Scratch File

Investigation requires writing your reasoning down — not in the conversation where it gets buried, but in a dedicated file that structures your thinking and gates your actions.

### The Gate Rule

There are two gates. Both are non-negotiable.

**Gate 1 — Investigation gate (before any source interaction):**
**You may not edit source files until you have created the scratch file, written your initial hypothesis, AND recorded your research/evidence results (Step 3).** The three conditions are: (1) scratch file exists, (2) hypothesis is written, (3) current external research is recorded when drift-prone external behavior matters, or local evidence is recorded with a reason external/current research is not relevant. All three must be satisfied before any source edit. Diagnostic additions (print/log statements for observation) are exempt — observation is free, changes are not.

**Feedback-loop condition (before testing hypotheses):**
**You may not treat a hypothesis as tested or a fix as verified until the scratch file names the feedback loop or explains why no loop can currently be built.** If the loop is weak, flaky, manual, or partial, record that limitation and improve it before trusting the result. A passing nearby test is not evidence unless it exercises the user's actual symptom or the minimized form of the same failure mechanism.

**Gate 2 — Fix gate (before applying the fix):**
**You may not apply the fix until impact analysis is written in the scratch file.** Once you have a confirmed hypothesis and a proposed fix, you must write the impact analysis — callers affected, contracts changed, regression risk, edge cases — BEFORE you write fix code. This is what prevents "I think this is it, let me try it" followed by a worse situation. If you cannot articulate what your fix affects, you do not understand it well enough to apply it.

### Create the File

At the start of any non-Obvious investigation, create `/tmp/debug-scratch-<brief-slug>.md` where `<brief-slug>` is a short description of the problem (e.g., `keyerror-session-token`, `flaky-auth-test`, `slow-checkout-api`).

Use this template as the starting structure:

```
## Resolving: [brief description]

Signal source: [error message / reviewer X / bug report / test failure]
Signal type: [error | feedback | review | report]

Observed: [exact error messages, behavior, or feedback received]
Expected: [what should happen]

Signal evaluation:
  - Source trust level: [high/medium/low]
  - Factual claims verified? [yes/no/partially]
  - Diagnosis accepted or investigating independently? [accepted/investigating]

Feedback loop:
  - Loop command/procedure: [test, curl/API command, CLI fixture, browser script, trace replay, harness, benchmark, manual capture, or none yet]
  - Symptom asserted: [exact failure signal this loop proves]
  - Reproducibility: [deterministic / intermittent with rate / not yet reproduced]
  - Loop limitations: [slow/flaky/manual/partial/none]

Hypothesis 1: [specific theory]
  Evidence for: ...
  Evidence against: ...
  Status: confirmed / disproven / untested

Research / evidence check (REQUIRED — gate condition before any source edits):
  External/current research required? [yes/no + why]
  Search/source 1: [what you searched/read/inspected] → [what you found or "no results"]
  Search/source 2: [what you searched/read/inspected] → [what you found or "no results"]
  Local evidence: [files, tests, logs, diffs, reproduction steps, runtime observations]
  Conclusion: [confirmed hypothesis / refuted hypothesis / refined to X / no relevant results found / local evidence sufficient]

Contributing factors:
  - Why does this problem exist? [design decision, refactoring gap, assumption, etc.]
  - Is this a pattern or one-off? [does same issue exist elsewhere?]

Proposed fix: [what you plan to change]
  Impact analysis (REQUIRED — gate condition before applying fix):
    - Callers affected: [list every caller of the code you're changing]
    - Contract changes: [does behavior change for existing callers? how?]
    - Regression risk: [low/medium/high — with specific reasoning, not just the word]
    - Edge cases: [what inputs or scenarios could break with this fix?]
    - Verdict: [safe to apply / needs adjustment / blocked on X]

Tried:
  - [change 1] → [result]
  - [change 2] → [result]

Response plan: [how to communicate the resolution]
```

Update the file as you progress through investigation. This is your working document — it should reflect your current understanding at all times.

### Why the File Matters

- **Gates premature action** — you cannot skip to fixing because the file must exist, hypothesis must be written, AND research/evidence must be recorded before source edits
- **Forces a real feedback loop** — hypotheses and fixes must be tested against the actual symptom or a minimized reproduction, not a nearby green check
- **Forces current evidence** — the Research / evidence check section must be filled in before the gate opens, preventing the "I already know this" and "I'll just figure it out from code" traps
- **Prevents circular investigation** — you won't re-check things you've already checked
- **Makes reasoning transparent** — others can see and correct your thinking
- **Forces signal evaluation** — the signal evaluation section prevents blind acceptance of input
- **Gates the fix itself** — impact analysis must be written before fix code (Gate 2), preventing "I think this is it" edits that make things worse
- **Catches fix-induced regressions** — the impact analysis forces you to think beyond the immediate problem
- **Documents the resolution** — useful for future reference and pattern recognition

### Summary and Cleanup

After verification passes (Phase 5), present a summary in the conversation, then delete the scratch file. The summary is not a commit message — it's a window into the reasoning that happened. The reader should understand not just what was done, but how you got there and why you're confident the fix is correct.

The summary must show:

**How you arrived at the root cause.** What did you notice first? What pointed you in the right direction? What did you consider and rule out, and why? Not every step, but the key observations and turning points that led to the conclusion.

**What implications you evaluated for the fix.** This is about YOUR SPECIFIC PROPOSED FIX, not about the ecosystem or the world. For each fix option you're recommending: what could go wrong if this fix is applied? What other code touches the thing you're changing? Does this fix alter behavior in any edge case? Could it introduce regressions in other files or callers?

If you're recommending multiple fix options, each one gets its own implications analysis. Don't lump them together, and don't substitute abstract ecosystem commentary ("this pattern is generally risky") for concrete evaluation of the specific change ("applying this fix to function X could break caller Y because Z").

The reader should see that you evaluated each affected component individually and reached a specific conclusion about safety — not that you listed what you changed and moved on.

**Residual risk.** Things you cannot fully verify about THIS FIX — not things that are generally risky in the world. "The audit service alias may be removed in a future version" is residual risk about this fix. "Python's dataclass repr has a known limitation" is ecosystem commentary — useful context, but not residual risk of your fix. If there's no residual risk, say so and explain why you're confident.

**Example** of the right density:

```
## Investigation Summary

**Root cause**: The serializer rename in PR #342 changed `session_token` →
`token` but only updated the serializer's own tests. Found this by noticing
the KeyError key name (`session_token`) doesn't appear anywhere in the
serializer module anymore — git diff confirmed the rename, grep found 3
callers still using the old key.

Ruled out: initially suspected the test setup was injecting stale fixture
data (the fixtures were also updated in PR #342), but the fixture changes
were correct — the mismatch is in the caller code, not the test data.

**Implications evaluated**:
- `authenticate()` — reads the key for local session validation only. No
  downstream consumers of the key name itself. Changing it is safe.
- `refresh_session()` — passes the token value to Redis. Checked: Redis
  operations use the value, not the key name. Safe.
- `validate_request()` — this one builds a dict that gets serialized to
  JSON for the audit service. If the audit service schema expects
  `session_token` as a field name, renaming silently breaks audit logging.
  Checked the audit schema — it aliases both names since v2.3. Safe, but
  the alias is a compatibility shim that may be removed.

**Residual risk**: The audit service alias for `session_token` is
undocumented and may be removed in a future version. If that happens,
audit logging for sessions will silently drop the field.
```

After presenting the summary, **delete `/tmp/debug-scratch-<brief-slug>.md`**.

If the investigation is escalated to the user (you're stuck, handing off), do NOT delete the file — leave it at `/tmp/debug-scratch-<brief-slug>.md` so they can see the full reasoning and pick up where you left off.

---

## Staying on Track

### Check the Plug

Before going deep, verify the basics:

- Is the right version of the code running?
- Is the right branch checked out?
- Are dependencies installed and up to date?
- Is the test actually running the code you think it is?
- Are environment variables set correctly?
- Is the database, service, or server actually running?
- Did the build actually succeed?

This catches problems that sophisticated investigation never would, because sophisticated investigation assumes the fundamentals are in order. Many debugging sessions end with discovering the equivalent of an unplugged cable.

### Time-Boxing Checkpoints

- **15 minutes:** Can you articulate the problem clearly? If not, stop and invest in understanding before investigating further.
- **30 minutes:** Do you have a falsifiable hypothesis? If not, step back and gather more data.
- **1 hour:** Have you made measurable progress (ruled out hypotheses, narrowed scope)? If going in circles, get fresh eyes.
- **2 hours:** Is this problem worth the time investment? Should you escalate, workaround, or deprioritize?

**The meta-rule:** If your estimate of remaining time keeps increasing rather than decreasing, you're not making progress. You're either working on the wrong problem or using the wrong approach.

### Escalation Signals

These signals mean your current approach isn't working:

- **No feedback loop** — if you cannot trigger the symptom or compare before/after behavior, stop improving code and improve the loop or ask for the missing artifact/access. A hypothesis without a signal is not testable.
- **No research/evidence recorded** — if you are about to edit source files or test a hypothesis by modifying code and you have not recorded current external research or local evidence, STOP. Go back to Step 3. If external behavior is involved, search current sources. If the issue is purely local, record the local evidence and why external/current research is not relevant. No exceptions.
- **No impact analysis written** — if you are about to apply a fix and the impact analysis section of the scratch file is empty, STOP. You do not understand your fix well enough. Trace the callers, check the contracts, identify edge cases. Write it in the scratch file. Then apply. Every time you skip this, you end up in a worse spot than where you started.
- **3+ failed fix attempts** — you're likely misunderstanding the problem. Revert changes, return to observation, and re-read the error with fresh eyes. Question your assumptions.
- **Circular investigation** — you've checked the same thing twice. Write down everything you know and don't know.
- **The error keeps changing character** — each fix produces a _different_ error. You may be creating new bugs. Revert to the original state and start over.
- **Expanding scope** — your investigation pulls in more files and components with no convergence. The problem may be architectural.
- **You don't understand the code** — if you can't explain the code, read more before debugging more. Understanding the system is prerequisite to debugging it.
- **Emotional investment** — if you feel certain about a hypothesis but can't prove it, that's System 1 confidence, which is uncorrelated with accuracy. Force deliberate analytical thinking.

When you hit these signals, tell the user what you've found, what you've tried, and what you think is going on. The user has context you don't, and two perspectives are better than one.

### Cognitive Traps Summary

The most common traps in problem resolution:

| Trap                     | What It Is                                                    | Counter                                                            |
| ------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------ |
| Confirmation bias        | Interpreting ambiguous evidence as supporting your theory     | Try to _disprove_ your hypothesis                                  |
| Anchoring                | First information dominates your investigation                | Generate multiple hypotheses independently                         |
| Sycophancy               | Agreeing due to social pressure, not technical merit          | Verify every claim against actual code first                       |
| Authority bias           | Accepting suggestions based on who, not what                  | Evaluate the comment, not the commenter                            |
| Sunk cost                | Continuing because of time invested, not because it's working | "If starting fresh, would I still do this?"                        |
| Tunnel vision            | Zooming in before understanding the full picture              | Read full error output, trace complete data flow                   |
| Frame adoption           | Accepting the reviewer's framing uncritically                 | Understand the _problem_ before evaluating the _solution_          |
| The "looks right" trap   | Code reads correctly but executes incorrectly                 | Observe actual runtime values, don't trust reading                 |
| Deference under pressure | Skipping verification to seem responsive                      | The 5 minutes verifying is always cheaper than the debugging after |

See [cognitive-traps.md](cognitive-traps.md) for detailed descriptions and countermeasures for each trap, including the thrashing pattern and traps specific to receiving external feedback.

---

## Quick Reference

### Situation → First Move

| Situation                               | First Move                                         |
| --------------------------------------- | -------------------------------------------------- |
| Clear error message, obvious fix        | Fix directly                                       |
| Error points to general area            | Read surrounding code, understand data flow        |
| No reliable reproduction                | Build or sharpen the feedback loop                 |
| Don't know where the problem is         | Binary search (code or commits)                    |
| Know where, not why                     | Trace backward from failure point                  |
| Intermittent failure                    | Identify what differs between pass and fail        |
| Works locally, fails elsewhere          | Diff the environments                              |
| Performance problem                     | Measure and profile before guessing                |
| Fix didn't work                         | Analyze _why_ it didn't — new evidence             |
| No research/evidence recorded           | Stop. Complete Step 3 before your next code change |
| About to apply a fix                    | Write impact analysis in scratch file first        |
| 3+ fixes failed                         | Stop. Reassess from scratch or discuss with user   |
| Don't understand the code               | Read tests and trace a request end-to-end          |
| Reviewer says "fix X"                   | Verify X is actually broken before fixing          |
| Reviewer suggests adding feature        | YAGNI check — is it actually needed?               |
| Multiple review items                   | Clarify all, then triage by severity               |
| Feedback conflicts with prior decisions | Stop and discuss with the decision-maker           |

### Core Principles

| Principle                              | Why                                                                    |
| -------------------------------------- | ---------------------------------------------------------------------- |
| Evaluate the signal before acting      | Not all signals are accurate — errors mislead, humans can be wrong     |
| Verify claims against actual code      | The codebase is the source of truth, not opinions                      |
| Build the feedback loop first          | A fast, specific signal turns debugging from guessing into learning    |
| Read the error completely              | It often contains the answer                                           |
| Observe before changing                | Changes are risky, observation is free                                 |
| One change at a time                   | Multiple changes destroy your ability to learn                         |
| State your hypothesis explicitly       | Prevents unconscious shifting, makes reasoning visible                 |
| Try to disprove, not confirm           | Confirmation bias is the #1 trap in both debugging and feedback        |
| Understand what led to the problem     | Contributing factors shape the right fix                               |
| Research/evidence before experimenting | Current external facts and local evidence beat model memory            |
| Write impact analysis before fix code  | If you can't articulate what your fix affects, you don't understand it |
| Analyze fix impact before applying     | A fix that breaks other things isn't a fix                             |
| Fix at the source, not the symptom     | Symptom fixes move problems, they don't solve them                     |
| Respond with actions, not performance  | "Fixed in [location]" beats "Great point!"                             |
| Track what you've tried                | Prevents circular investigation                                        |
| Know when to escalate                  | Diminishing returns are real — escalate, don't thrash                  |
