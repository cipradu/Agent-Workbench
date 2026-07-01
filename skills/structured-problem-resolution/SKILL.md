---
name: structured-problem-resolution
description: Use before acting on any troubleshooting or failure signal or proposed diagnosis/fix, including broken or unexpected behavior, failed tests/builds/commands, runtime errors, performance/flaky/regression issues, review/bug-report/human/AI claims, repeated failed attempts, or drift-prone library/API/runtime behavior. Mandatory before diagnosis or fixes; turn signals into current evidence, hypotheses, impact analysis, and verified resolution.
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

### Issue, Review, and Ticket Threads

When the signal references an issue, pull request, code-review thread, bug ticket, chat thread, incident, or prior investigation, read the complete available thread before diagnosing from the title or opening description.

Include the original report, every comment, latest updates, reproduction attempts, environment details, screenshots/logs, prior failed fixes, owner decisions, and scope pivots. Latest comments often invalidate the opening diagnosis. If the thread is unavailable, ask for the missing content or record the gap; do not diagnose from a summary when the source thread exists but has not been read.

### Diagnostic Scope Checkpoint

For vague, multi-item, media-backed, review/ticket, or solution-framed signals, write a compact scope checkpoint before converging on a hypothesis:

- Observed facts: what was directly seen, measured, logged, recorded, or reported.
- Expected behavior: the explicit requirement, contract, acceptance criterion, or user-observed expectation. If expected behavior is undefined, route to product/spec clarification instead of inventing it during diagnosis.
- Handed diagnosis: the reporter's or reviewer's theory, kept as a hypothesis.
- Requested fix: any proposed patch, command, cleanup, retry, refactor, plan, or workaround, kept separate from the problem.
- Agent inference: what you infer, with a basis label, not as fact.
- Out of scope: adjacent complaints, broad product/design asks, and downstream workflow requests that are not needed to diagnose the current signal.
- One missing fact that changes the next diagnostic action, or `none`.

If a human signal is vague, quote the exact weak phrase and ask one observation-seeking question when the answer materially changes the next diagnostic action. If the answer remains unavailable, record the uncertainty and the next evidence artifact needed rather than converting pressure into edits.

See [signal-evaluation.md](references/signal-evaluation.md) for detailed patterns on evaluating different signal types, multi-item feedback handling, the four-axis evaluation framework, and the push-back framework.

---

## Phase 2: Triage

Not every problem needs the same level of investigation. Before diving in, assess what you're dealing with.

Triage is execution routing after this skill has loaded. Obvious cases still use this skill: choose the Obvious branch, make the direct fix, and verify. They do not require the full investigation loop or scratch file unless the first direct fix fails or the mechanism is not actually proven.

### Obvious (seconds)

The signal tells you exactly what's wrong and the fix is unambiguous.

**Signals:** Clear mechanical typo, missing import, syntax error, formatting-only issue, or clear error like `NameError: name 'foob' is not defined`. One-line fix. You can explain the exact mechanism of the failure without reading surrounding code.

**Action:** Fix it directly and verify. No full investigation workflow or scratch file is needed. But if your "obvious" fix doesn't work on the first try, upgrade to Simple.

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

**Verify environment sanity before deep tracing.** Confirm the right branch, version, dependency set, runtime, config, environment variables, database/service/server state, generated artifacts, build output, and test target. Many failures survive multiple clever theories because the wrong code, stale artifact, missing service, or wrong environment is being exercised.

Classify environment findings before treating them as root cause:

- Blocking failure: the required workflow cannot run until fixed, such as the wrong branch, failed build, missing required service, invalid config, or stale generated artifact that directly affects the signal.
- Optional capability gap: a helpful tool, browser driver, simulator, profiler, or integration is missing, but another valid loop or evidence path exists.
- Unrelated observation: a noisy local issue exists but does not affect the current symptom.

Do not treat a missing optional tool as the diagnosis. Route setup repair only when the failing workflow actually depends on that missing tool.

**Build the feedback loop before testing hypotheses.** The loop is the first investigation product, not a side quest. A feedback loop is a fast, deterministic or high-reproduction, agent-runnable pass/fail signal for the user's actual symptom. It can be a test, command, script, trace replay, browser check, benchmark, or structured manual capture, but it must tell you whether the original symptom is present. If no reliable loop exists, the next task is to build or sharpen the loop, not to guess at fixes.

A usable loop is red-capable, specific, fast enough to iterate, deterministic or measured by reproduction rate, and runnable without hidden human interpretation. You should be able to name one command, script, trace, browser check, or structured manual capture that has already been run at least once and can distinguish the original symptom from nearby failures.

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

For surface-specific feedback loops, record what makes the loop reach the real symptom:

- Browser, dogfood, or UI polish: route/scenario, visible state, DOM, console, network, storage, server logs, side effects, screenshots when useful, and the true end state. A screenshot or "looks better" is supporting evidence, not root-cause proof.
- Mobile or device runtime: build/install/launch state, device or simulator context, runtime logs, screenshots, automation limits, human-verification gaps, and cleanup of temporary state.
- Media or recording reports: observed facts with timestamps, transcript/screenshot/event references, confidence in each inference, and raw media kept local by default.
- Production or external evidence: error payloads, request/trace/correlation IDs, release metadata, log snippets, breadcrumbs, exact timestamps, timezone, source window, latest data considered, and known ingestion lag.

When logs, metrics, screenshots, traces, HAR files, transcripts, config snippets, generated reports, or data samples become evidence, record provenance and safety: source/tool, query or filter shape, source window, timestamp/timezone, redaction status, whether raw data is local-only, and which source is canonical when CI, local reproduction, monitoring, user reports, and database state disagree. Ask for tool/source and query shape, not credentials or secret-bearing connection details.

If you are resuming an investigation, prior scratch files, old issue titles, review comments, failed-fix notes, solution docs, session summaries, logs, and prior learnings are evidence leads, not current truth. Reconcile them against current code, branch/diff, dependency versions, runtime state, generated artifacts, test target, latest thread updates, and the current symptom. Classify the old context as `current/no action`, `stale but correctable`, `contradicted by latest evidence`, `superseded by new symptom`, `missing feedback loop`, `missing environment sanity`, `ambiguous source authority`, or `requires restart from observation`.

**Check what changed.** `git log`, `git diff`, recent dependency updates. The single most productive question for any problem that used to work: what's different between when it worked and when it broke?

**Trace the bad-state transition.** Identify the last point where the relevant state is valid and the first point where it becomes invalid. Observe actual runtime values, database rows, request payloads, config values, files, logs, or traces rather than inferring from how the code reads. Root cause lives where the bad state originates, not where it finally crashes.

### Step 2: Hypothesize (what do you think is happening, and why?)

Form a specific, falsifiable hypothesis. Not "something's wrong with the database" but "the query returns zero rows because the WHERE clause uses the wrong column name."

**Audit assumptions before choosing a theory.** List the concrete beliefs your hypothesis depends on: which code is running, which input shape exists, which dependency behavior applies, which state is present, which caller path executes, which reviewer claim is factual. Mark each one verified or assumed. Unverified assumptions become investigation targets, not hidden premises.

**The mechanism test:** If you can't explain the precise mechanism by which your proposed cause produces the observed symptom, your hypothesis isn't specific enough. "Race condition" is not a hypothesis. "Thread A reads the counter, then Thread B increments and writes, then Thread A overwrites with its stale value" is a hypothesis.

**The causal-chain gate:** A hypothesis must explain the full path from trigger to symptom with no hand-waved links. For each uncertain link, state a prediction that should be visible somewhere else in the system. If the prediction fails but the proposed code change appears to help, you probably found a symptom patch rather than the root cause.

**Generate alternatives.** Before investigating your first hypothesis, spend 30 seconds listing 2-3 other possible causes. Rank by likelihood and testability. This prevents anchoring on the first idea — whether it came from your own intuition, an error message, or a reviewer's suggestion.

For Complex investigations, include the handed hypothesis plus at least two independent alternatives unless you can explain why the search space is genuinely narrower. Cover different plausible axes when relevant: runtime path, data shape, environment/config, recent change, concurrency/time, external dependency, user/input boundary, and stale artifact or source window. Each candidate needs the observation it explains and the evidence that would disprove it.

**State it explicitly.** Write your hypothesis down (in the conversation or as a comment). This creates accountability and makes your reasoning visible. You can't unconsciously shift your theory to match new evidence if you've committed to a specific prediction.

Label the basis for every material claim: `observed`, `reproduced`, `local-code`, `external-current`, `prior-learning`, `reasoned`, or `unsupported`. Reasoned claims can guide the next probe; they are not proof. Absence claims such as no reproducer, no callers, no similar bug, no external research needed, no regression risk, or no residual risk require evidence for the search space checked.

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
- Prior learning or solution records, if the repository has them, for similar exact errors, symptoms, root causes, components, failed attempts, and prevention notes. Treat them as hypothesis sources that may be stale, not as proof.

**When to use current external research:** Always when the answer depends on library, framework, runtime, package, API, security, browser, database, platform, SaaS, cloud, protocol, deprecation, migration, compatibility, or "best practice" claims. Even if you think you know the answer, verify anyway. You might find that the behavior changed, the API was deprecated, the known workaround is obsolete, or your initial intuition is wrong.

**When local evidence is enough:** When the hypothesis is about this repository's own code, data flow, configuration, tests, or recent diffs and no external behavior claim is needed. In that case, record the local evidence and explicitly write `External/current research not required because <reason>`.

**How to research:** Use the `research` subagent (subagent_type: "research") when external/current evidence is required and the environment permits delegation. If the research agent is not available or fails, fall back to whatever search/web/docs tools the environment provides (WebSearch, WebFetch, MCP tools, Context7, official docs, package repositories, changelogs, issue trackers, etc.). If you need follow-up questions or deeper investigation from a prior research result, resume the previous research agent session rather than starting a new one when the harness supports it.

**What to do with the results:**

- If you find the answer: verify it applies to your specific situation, then proceed to fix
- If you find related issues but no direct answer: use them to refine your hypotheses before testing in Step 4
- If you find nothing: that itself is information — the problem is likely specific to this codebase, not a known issue. Proceed to Step 4
- If local evidence is sufficient: cite the exact files, commands, outputs, or runtime observations that support the hypothesis

**The bias you're fighting:** There is a strong pull toward figuring things out from first principles — reading code, forming theories, running experiments. This feels productive but is often catastrophically wasteful. The error message you're staring at may have a documented upstream fix. The library bug you're trying to work around may have a GitHub issue with a specific version boundary. Your training data may describe old behavior. Check before acting.

**Structural enforcement for non-Obvious investigations:** After triage selects Simple, Complex, or Architectural, research/evidence results must be recorded in the scratch file before you proceed to Step 4 or make any source edits. The scratch file must contain current external findings when external behavior matters, or local evidence plus the reason external research is not relevant when the issue is purely local. Skipping this step is a gate violation, same as skipping the scratch file itself. Obvious cases bypass this gate only while the exact mechanism is proven, the fix is one line, and verification follows immediately; if the first fix fails, upgrade out of Obvious and satisfy the gate.

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

If an experiment, probe, or attempted fix contradicts your prediction, explicitly invalidate or refine the hypothesis in the scratch file before trying the next thing. Do not retry variants of the same theory unless new evidence changes the theory.

For measurable investigations such as performance, flakiness, repeated failed fixes, quality scores, or proxy metrics, define the baseline, target, hard gates, diagnostics, acceptance threshold, repetition or variance policy, and immutable measurement asset before changing code. A single faster run, one passing flaky test, a prettier screenshot, or a better proxy score is not proof when variance, correctness, accessibility, security, or data integrity guardrails can regress. Record each probe outcome as confirmed, disproven, degenerate, error, timeout, deferred, or inconclusive.

When a command or API mutation has ambiguous external-state impact, do not infer state from exit code or stdout alone. If a mutation times out, returns 5xx, returns 202/pending, fails after partial work, or returns a success artifact that might be wrong or empty, capture stdout, stderr, exit code, target state, fallback path, idempotency support, and authoritative readback before retrying or declaring completion. Separate stale/precondition failures, invalid payload errors, false-success outputs, and ambiguous post-write failures.

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

Practical starting points for common scenarios. See [techniques.md](references/techniques.md) for detailed walkthroughs.

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

**For non-Obvious fixes, Gate 2 is active here.** You have a confirmed hypothesis and a proposed fix. Before you write a single line of non-Obvious fix code, the impact analysis section of the scratch file must be filled in. This is where 60% of regressions are prevented — not by testing after the fact, but by thinking before the change. "I think this is it" is not impact analysis. Trace the callers. Check the contracts. Identify what else touches the code you're about to change. Write it down. Then — and only then — make the edit.

### Fix at the Source, Not the Symptom

If a function receives `null` and crashes, the fix isn't adding a null check at the crash point. The fix is finding why `null` was passed in the first place and preventing that. Trace the bad value backward through the call chain to find where it originates.

### Impact Analysis

Before implementing, analyze the blast radius of your proposed fix:

- **Who calls this code?** Trace the callers of the function or component you're about to change. If you change `anonymize_users` to copy dicts instead of mutating them, does any caller _depend_ on the mutation?
- **What contracts or interfaces change?** If a function currently modifies its input in-place and you change it to return a new copy, that's a behavioral contract change. Callers that relied on the side effect will silently break.
- **What are the edge cases of your fix?** If you remove a validation step, what happens to inputs the validation was designed to catch? If you change a type, what happens to comparisons, serialization, or storage?
- **Could the fix introduce regressions?** Think about related functionality, not just the failing test. A fix to the payment module might affect the refund module. A fix to the config loader might affect startup time or caching behavior.
- **What tests cover this area?** Run them in your head (or actually run them) before committing. If there's no test coverage, that's a risk to flag.

When the changed code sits on a boundary, explicitly check the interaction chain:

- callbacks, middleware, observers, event handlers, hooks, scheduled jobs, background workers, and cleanup paths;
- persistence before external calls, transaction boundaries, retries, idempotency, duplicate side effects, queue/cache invalidation, and rollback behavior;
- alternate public interfaces, CLI/API/UI/admin paths, import/export paths, generated artifacts, and compatibility shims;
- shared test state, mocks, globals, fixtures, ports, databases, Redis keys, filesystem paths, rate limits, and test ordering that can hide contamination;
- cross-layer error handling, redaction, logging, fallback behavior, and accessibility or security checks when the surface is user-facing or sensitive.

For feedback that asks to "simplify", "clean up", "make it proper", or remove apparent duplication, prove behavior equivalence before editing: same outputs, errors, side effects, timing/order where relevant, validation, security checks, data-loss prevention, accessibility behavior, and observability. Fewer lines alone is not an improvement.

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

### Prevention Check

After the root cause is understood, decide whether this is a one-off defect or a recurring/high-impact failure mode. If the same root-cause pattern appears in three or more places, affects a shared boundary, caused a serious production issue, or reveals a missing invariant, analyze prevention before closing the investigation.

Prevention can mean boundary validation, invariant checks, stronger test seams, clearer diagnostics, environment guards, documentation, or capturing a reusable implementation pattern. If the recurring lesson is an implementation convention, route it to `create-implementation-pattern`; if the finding implies a broader design or requirement issue, route it to architecture/spec work instead of patching around it inside the debugging session.

---

## Phase 5: Verify and Respond

### Verification

**Immediate checks:**

- Does the original problem go away?
- Do ALL existing tests still pass (not just the one that was failing)?
- Re-run the original feedback loop against the un-minimized scenario, not only the narrowed reproduction.
- Add regression coverage at the correct seam when such a seam exists. The correct seam exercises the real bug pattern as it occurred at the call site; a shallow test that cannot reproduce the triggering chain is false confidence.
- If no correct regression seam exists, document that as a testability or architecture gap instead of pretending a weak test proves the fix.
- Run related tests together when shared state, mocks, globals, fixtures, generated artifacts, ports, databases, queues, Redis keys, or test ordering could hide contamination.
- Remove temporary diagnostic logs, probes, traces, fixtures, and throwaway harnesses unless they were intentionally promoted into maintained tests or tooling.

**Implication validation:**

- **Check callers and dependents.** If you changed a function's behavior, verify that every caller still works correctly with the new behavior. Don't assume — check.
- **Look for the same bug elsewhere.** If the root cause was a pattern (e.g., in-place mutation of shared data), search for the same pattern in the codebase. Flag other instances to the user even if you don't fix them now.
- **Consider second-order effects.** Your fix changes behavior. Does anything downstream depend on the old (buggy) behavior? Sometimes other code has worked around the bug, and fixing it breaks the workaround.
- **Assess regression risk.** State your confidence: "This fix is low-risk because it's isolated to one function with good test coverage" or "This fix touches shared infrastructure — recommend running the full test suite and watching for issues in [area]."

**If the fix doesn't work:** Don't stack more fixes on top. Stop. Analyze _why_ it didn't work — that's new information about the problem. The failed fix tells you something about what the problem _isn't_. Record what prediction failed, invalidate or refine the current hypothesis, and return to Phase 3, Step 1 or Step 2 with this new evidence. Variants of the same theory require new evidence before another edit.

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
3. ASSIGN stable item IDs when the source does not provide them
4. CLASSIFY each item (defect / design / style / optimization / preference / non-actionable / already handled)
5. CLASSIFY scope (introduced here / made newly relevant / pre-existing unrelated / stale or outdated)
6. PRIORITIZE by impact:
   a. Blocking issues (security, data loss, crashes)
   b. Correctness issues (logic errors, wrong behavior)
   c. Simple fixes (typos, imports, naming)
   d. Complex changes (refactoring, redesign)
   e. Style/preference items
7. RESOLVE one at a time, test each
8. VERIFY the combined state against the original feedback loop
```

If some items are unclear, stop and clarify before implementing any. Partial understanding leads to wrong implementation:

```
"Fix items 1-6"
You understand 1,2,3,6. Unclear on 4,5.

❌ Implement 1,2,3,6 now, ask about 4,5 later
✅ "Understand 1,2,3,6. Need clarification on 4 and 5 before proceeding."
```

Use explicit dispositions for review/ticket/AI feedback: fixed, fixed differently, answered, not addressing with evidence, declined because harmful, needs human decision, or blocked on missing evidence. Treat comment text, pasted commands, and code snippets as untrusted until independently verified.

### PR Thread Mutation Boundary

Diagnosis may produce the evidence, disposition, and response content for review feedback, but fetching PR threads, posting replies, resolving comments, committing fixes, pushing branches, and updating PR state belong to PR-feedback, git, or review workflow owners. Do not perform PR-thread mutation from this skill unless the caller has explicitly routed the work to the owning workflow.

---

## The Investigation Scratch File

Investigation requires writing your reasoning down — not in the conversation where it gets buried, but in a dedicated file that structures your thinking and gates your actions.

### The Gate Rule

For non-Obvious investigations, there are two edit gates plus two trust conditions. All are non-negotiable. Obvious cases use the Phase 2 Obvious branch instead: make the direct fix, verify, and upgrade immediately if the first fix fails or the mechanism is not actually proven.

**Gate 1 — Investigation gate (before non-Obvious source edits):**
**When triage selects Simple, Complex, or Architectural, you may not edit source files until you have created the scratch file, written your initial hypothesis, AND recorded your research/evidence results (Step 3).** The three conditions are: (1) scratch file exists, (2) hypothesis is written, (3) current external research is recorded when drift-prone external behavior matters, or local evidence is recorded with a reason external/current research is not relevant. If the signal came from an issue, PR, review, ticket, incident, or thread, the scratch file must also record that the complete available context and latest update were read, or record why they are unavailable. All conditions must be satisfied before any non-Obvious source edit. Diagnostic additions (print/log statements for observation) are exempt — observation is free, changes are not.

For vague, stale, resumed, external-artifact, media, review/ticket, or multi-item signals, Gate 1 also requires the scratch file to preserve diagnostic scope, source provenance, stale-context classification, and review/ticket metadata where applicable. Use `not applicable` when the field does not apply; do not delete the field.

**Feedback-loop condition (before testing non-Obvious hypotheses):**
**For non-Obvious investigations, you may not treat a hypothesis as tested or a fix as verified until the scratch file names the feedback loop or explains why no loop can currently be built.** The scratch entry must state the loop command/artifact, what symptom it can catch, whether it is deterministic or intermittent with a measured reproduction rate, and why it reaches the real bug path. If the loop is weak, flaky, manual, or partial, record that limitation and improve it before trusting the result. A passing nearby test is not evidence unless it exercises the user's actual symptom or the minimized form of the same failure mechanism.

**Environment and causal-chain condition (before trusting a non-Obvious hypothesis):**
**For non-Obvious investigations, you may not treat a hypothesis as credible until the scratch file records environment sanity, the bad-state transition, assumption audit, causal chain, and predictions for uncertain links.** If one of those fields is unknown, the next investigation action is to verify it, narrow the uncertainty, or record why it is currently unknowable. A fix attempt that contradicts the prediction invalidates or refines the hypothesis; it does not authorize another variant of the same guess.

**Gate 2 — Fix gate (before applying a non-Obvious fix):**
**For non-Obvious investigations, you may not apply the fix until impact analysis is written in the scratch file.** Once you have a confirmed hypothesis and a proposed fix, you must write the impact analysis — callers affected, contracts changed, regression risk, edge cases — BEFORE you write fix code. This is what prevents "I think this is it, let me try it" followed by a worse situation. If you cannot articulate what your fix affects, you do not understand it well enough to apply it.

Concise investigation notes are allowed. Missing required scratch fields are not. Brevity means short entries inside the required fields, not deleting thread/context, environment sanity, bad-state transition, assumption audit, causal chain, predictions, research/evidence, or impact-analysis fields.

**Scratch validity check:** Before treating Gate 1, the feedback-loop condition, or the environment/causal-chain condition as satisfied, confirm the scratch file contains these literal labels: `Diagnostic scope`, `Evidence provenance`, `Stale/resumed context`, `Thread/context read?`, `Latest update considered`, `Environment sanity`, `Environment-health classification`, `Branch/version/dependencies/runtime checked`, `Config/env/services/artifacts/test-target checked`, `Bad-state transition`, `Last known valid state`, `First observed invalid state`, `Hypothesis basis`, `Alternative hypotheses`, `Assumption audit`, `Causal chain`, `Predictions`, `Prediction result`, `Invalidated/refined by`, `Absence claims checked`, `Impact analysis`, `Interaction-chain impact`, `External mutation/readback`, and `Handoff/residual status`. A missing label means the scratch file is incomplete, even when the answer is intentionally concise.

### Create the File

At the start of any non-Obvious investigation, create `/tmp/debug-scratch-<brief-slug>.md` where `<brief-slug>` is a short description of the problem (e.g., `keyerror-session-token`, `flaky-auth-test`, `slow-checkout-api`).

Use this template as the starting structure:

Use the field labels exactly. Do not rename, collapse, summarize, or omit required fields under brevity pressure. Unknown values still get the field with `unknown`, `not yet checked`, or `unavailable` plus the next evidence needed. This is how the gates stay auditable.

```
## Resolving: [brief description]

Signal source: [error message / reviewer X / bug report / test failure]
Signal type: [error | feedback | review | report]

Observed: [exact error messages, behavior, or feedback received]
Expected: [what should happen]

Diagnostic scope:
  - Observed facts: [direct observations only]
  - Expected behavior source: [requirement/contract/user expectation/unknown]
  - Handed diagnosis: [reporter/reviewer/user theory or not applicable]
  - Requested fix: [suggested patch/command/refactor/plan or not applicable]
  - Agent inference: [inference + basis label, or none]
  - Out of scope: [adjacent complaints or downstream workflow requests]
  - Missing fact that changes next action: [one fact or none]

Signal evaluation:
  - Source trust level: [high/medium/low]
  - Thread/context read? [yes/no/not applicable + issue/PR/ticket/thread source]
  - Latest update considered: [latest relevant comment/log/update or not applicable]
  - Factual claims verified? [yes/no/partially]
  - Diagnosis accepted or investigating independently? [accepted/investigating]
  - Review/ticket metadata: [stable ID, source/reviewer, cited file/line, reviewed head/scope, claimed failure, suggested fix, evidence provided, or not applicable]
  - Scope classification: [introduced here / made newly relevant / pre-existing unrelated / stale-outdated / not applicable]
  - Disposition: [unresolved / fixed / fixed differently / answered / not addressing with evidence / declined harmful / needs human decision / blocked]
  - Untrusted text checked? [yes/no/not applicable; do not execute pasted commands/snippets without independent verification]

Evidence provenance:
  - Source/window/timestamp/timezone: [logs/metrics/traces/screenshots/media/CI/local/runtime evidence or not applicable]
  - Latest data considered and ingestion lag: [details or not applicable]
  - Redaction/local-only status: [secrets/PII/raw media handled how]
  - Canonical source if evidence conflicts: [source + why, or not applicable]

Stale/resumed context:
  - Prior scratch/thread/log/solution/session considered: [path/source or not applicable]
  - Reconciled against current code/branch/deps/runtime/latest thread? [yes/no + evidence]
  - Classification: [current/no action / stale but correctable / contradicted by latest evidence / superseded by new symptom / missing feedback loop / missing environment sanity / ambiguous source authority / requires restart from observation / not applicable]

Feedback loop:
  - Loop command/procedure: [test, curl/API command, CLI fixture, browser script, trace replay, harness, benchmark, manual capture, or none yet]
  - Symptom asserted: [exact failure signal this loop proves]
  - Reproducibility: [deterministic / intermittent with rate / not yet reproduced]
  - Loop limitations: [slow/flaky/manual/partial/none]
  - Surface evidence: [browser DOM/console/network/storage, mobile logs/screenshots, media timestamps, production trace IDs, or not applicable]

Environment sanity:
  - Environment-health classification: [blocking failure / optional capability gap / unrelated observation / healthy]
  - Branch/version/dependencies/runtime checked: [yes/no + evidence]
  - Config/env/services/artifacts/test-target checked: [yes/no + evidence]

Bad-state transition:
  - Last known valid state: [where/value/evidence]
  - First observed invalid state: [where/value/evidence]

Hypothesis 1: [specific theory]
  Hypothesis basis: [observed / reproduced / local-code / external-current / prior-learning / reasoned / unsupported]
  Alternative hypotheses: [handed hypothesis + 2 independent alternatives for Complex cases, or why not applicable]
  Assumption audit: [verified assumptions vs unverified assumptions]
  Causal chain: [trigger -> state transition -> symptom]
  Predictions: [what else should be observable if this is true]
  Evidence for: ...
  Evidence against: ...
  Prediction result: [matched/contradicted/not tested]
  Invalidated/refined by: [failed experiment/fix/result, if applicable]
  Absence claims checked: [no repro/no callers/no similar bug/no external research/no residual risk claims + search space checked]
  Status: confirmed / disproven / untested

Research / evidence check (REQUIRED — gate condition before non-Obvious source edits):
  External/current research required? [yes/no + why]
  Search/source 1: [what you searched/read/inspected] → [what you found or "no results"]
  Search/source 2: [what you searched/read/inspected] → [what you found or "no results"]
  Prior learning checked? [yes/no/not applicable + conflict/staleness if any]
  Local evidence: [files, tests, logs, diffs, reproduction steps, runtime observations]
  Conclusion: [confirmed hypothesis / refuted hypothesis / refined to X / no relevant results found / local evidence sufficient]

Measurement overlay:
  - Applies? [yes/no: performance/flaky/repeated-fix/quality metric/proxy metric]
  - Baseline/target/guardrails: [measurement + acceptance threshold]
  - Variance/repetition policy: [runs/rate/noise threshold or not applicable]
  - Immutable measurement asset: [benchmark/fixture/trace/rubric or not applicable]
  - Probe outcome: [confirmed/disproven/degenerate/error/timeout/deferred/inconclusive/not applicable]

External mutation/readback:
  - Applies? [yes/no]
  - Command/API result: [stdout/stderr/exit code/status/URL/pending state]
  - Target state and idempotency support: [details or not applicable]
  - Authoritative readback before retry/completion: [evidence or not applicable]
  - Classification: [stale/precondition failure / invalid payload / false success / ambiguous post-write / confirmed applied / not applicable]

Contributing factors:
  - Why does this problem exist? [design decision, refactoring gap, assumption, etc.]
  - Is this a pattern or one-off? [does same issue exist elsewhere?]
  - Prevention needed? [no / yes: boundary validation, invariant, test seam, diagnostic, documentation, implementation pattern, architecture/spec follow-up]

Proposed fix: [what you plan to change]
  Impact analysis (REQUIRED — gate condition before applying fix):
    - Callers affected: [list every caller of the code you're changing]
    - Contract changes: [does behavior change for existing callers? how?]
    - Regression risk: [low/medium/high — with specific reasoning, not just the word]
    - Edge cases: [what inputs or scenarios could break with this fix?]
    - Interaction-chain impact: [callbacks/middleware/events/jobs/persistence/external calls/retries/cleanup/alternate interfaces/shared test state]
    - Simplification equivalence: [same behavior/side effects/order/safety checks, or not applicable]
    - Verdict: [safe to apply / needs adjustment / blocked on X]

Tried:
  - [change 1] → [result]
  - [change 2] → [result]

Response plan: [how to communicate the resolution]
Handoff/residual status: [none / planning/spec/architecture/implementation/commit/learning/residual owner + evidence packet path, unresolved assumptions, durable sink if current workflow has one]
```

Update the file as you progress through investigation. This is your working document — it should reflect your current understanding at all times.

### Why the File Matters

- **Gates premature action** — for non-Obvious work, you cannot skip to fixing because the file must exist, hypothesis must be written, AND research/evidence must be recorded before source edits
- **Forces complete signal intake** — issue, PR, review, ticket, and incident signals must include the full available thread and latest update, not just a title or summary
- **Forces a real feedback loop** — hypotheses and fixes must be tested against the actual symptom or a minimized reproduction, not a nearby green check
- **Forces environment sanity and causal proof** — the scratch file must show the right code/environment is being exercised and that the hypothesis explains the bad-state transition
- **Forces current evidence** — the Research / evidence check section must be filled in before the gate opens, preventing the "I already know this" and "I'll just figure it out from code" traps
- **Forces evidence labels and freshness checks** — observed facts, current external facts, local-code evidence, prior learning, reasoned claims, and unsupported claims cannot collapse into one confidence bucket
- **Forces external-state readback** — ambiguous command/API results must be read back from the authoritative target before retry or completion
- **Prevents circular investigation** — you won't re-check things you've already checked
- **Makes reasoning transparent** — others can see and correct your thinking
- **Forces signal evaluation** — the signal evaluation section prevents blind acceptance of input
- **Gates the fix itself** — impact analysis must be written before fix code (Gate 2), preventing "I think this is it" edits that make things worse
- **Catches fix-induced regressions** — the impact analysis forces you to think beyond the immediate problem
- **Documents the resolution** — useful for future reference and pattern recognition

### Diagnosis Handoff Packet

When the investigation does not end as a narrow verified fix, hand off the diagnosis without importing downstream mechanics. Use this packet for engineering spec, architecture, implementation planning, commit preparation, learning capture, residual-risk tracking, or user escalation:

- observed symptom and original signal source;
- original feedback loop or equivalent evidence path, including limitations;
- confirmed root cause or current best hypothesis with basis label;
- causal chain, bad-state transition, predictions, and prediction results;
- ruled-out hypotheses, failed fixes, and evidence that invalidated them;
- source truth used: current files, runtime evidence, external/current sources, prior learnings, logs, traces, screenshots, media, or generated reports;
- affected boundaries and impact analysis, including interaction-chain surfaces;
- proposed fix class or next workflow, not a full plan unless a planning owner is invoked;
- verification already run, verification still needed, and known gaps;
- scratch cleanup or retained scratch path;
- residual risk, unresolved assumptions, durable sink if one already exists in the current workflow, and recommended next owner.

Unverified hypotheses must not become plan decisions, commit rationale, review dispositions, or durable learning. Preserve them as assumptions or open evidence gaps.

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

When the diagnosis is verified and non-trivial, recurring, high-impact, or teaches a reusable diagnostic lesson, recommend a separate learning-capture or documentation workflow after the scratch summary. Do not create or update solution docs, trackers, PR bodies, commits, or project-continuity files from this skill unless the caller has explicitly routed that work to the owning workflow.

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

- **Thread not read** — if the signal came from an issue, PR, review, ticket, incident, or prior investigation and you have not read the complete available thread plus latest updates, stop diagnosing and read it or record why it is unavailable.
- **Stale context unreconciled** — if a scratch file, prior solution, old review comment, log excerpt, session summary, or issue title is driving the diagnosis without current reconciliation, stop and classify it against current code, runtime, and latest thread evidence.
- **Environment sanity skipped** — if branch/version/dependencies/runtime/config/services/artifacts/test target are unverified, stop deep tracing and check the basics first.
- **Optional tool treated as blocker** — if a missing optional tool is being treated as the root cause or as a reason to stop while another evidence path exists, reclassify it as an optional capability gap and continue with the valid loop.
- **No feedback loop** — if you cannot trigger the symptom or compare before/after behavior, stop improving code and improve the loop or ask for the missing artifact/access. A hypothesis without a signal is not testable.
- **Evidence provenance missing** — if logs, metrics, traces, screenshots, recordings, generated reports, or external artifacts lack source, time window, freshness, or redaction status, record those facts before treating them as evidence.
- **No research/evidence recorded** — in non-Obvious investigations, if you are about to edit source files or test a hypothesis by modifying code and you have not recorded current external research or local evidence, STOP. Go back to Step 3. If external behavior is involved, search current sources. If the issue is purely local, record the local evidence and why external/current research is not relevant. Obvious one-line fixes are the only exception; verify immediately and upgrade if the first fix fails.
- **No impact analysis written** — in non-Obvious investigations, if you are about to apply a fix and the impact analysis section of the scratch file is empty, STOP. You do not understand your fix well enough. Trace the callers, check the contracts, identify edge cases. Write it in the scratch file. Then apply. Obvious one-line fixes are the only exception; verify immediately and upgrade if the first fix fails.
- **External mutation ambiguous** — if a command/API may have partially written state, read back the authoritative target before retrying or claiming completion.
- **Metric or screenshot treated as proof** — if success rests on one faster run, one passing flaky run, a screenshot, hot reload, or user satisfaction without causal-chain evidence and guardrails, keep investigating.
- **Causal-chain gap** — if the hypothesis cannot explain trigger to symptom with observable intermediate states, do not fix yet. Turn the unknown link into a prediction and test it.
- **Failed fix not invalidated** — if an attempted fix failed or contradicted a prediction and the current hypothesis is still being treated as true, stop. Record what was disproven and return to observation or hypothesis formation.
- **2-3 hypotheses exhausted with no convergence** — summarize the evidence, ruled-out theories, remaining unknowns, and next highest-value observation. Get fresh eyes or escalate with the scratch file instead of continuing privately.
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
| Stale scratch anchoring  | Treating old notes or prior fixes as current truth            | Reconcile against current code, runtime, and latest thread         |
| Metric gaming            | Treating scalar improvement as root-cause proof               | Keep guardrails, variance policy, and original symptom evidence    |
| False-success output     | Trusting command output without target-state readback         | Read back authoritative state when mutation status is ambiguous    |
| Optional-tool blocker    | Treating missing helpful tooling as a root cause              | Classify required vs optional capability before blocking           |
| Visual false proof       | Treating screenshots or polish as causal proof                | Pair visual evidence with path, state, and side-effect checks      |
| Frame adoption           | Accepting the reviewer's framing uncritically                 | Understand the _problem_ before evaluating the _solution_          |
| Prior-learning overtrust | Applying old fixes without current evidence                   | Treat prior learnings as leads, not proof                          |
| The "looks right" trap   | Code reads correctly but executes incorrectly                 | Observe actual runtime values, don't trust reading                 |
| Deference under pressure | Skipping verification to seem responsive                      | The 5 minutes verifying is always cheaper than the debugging after |
| Review auto-apply        | Clearing feedback as a queue instead of verifying claims      | Keep stable IDs, dispositions, and evidence per item               |

See [cognitive-traps.md](references/cognitive-traps.md) for detailed descriptions and countermeasures for each trap, including the thrashing pattern and traps specific to receiving external feedback.

---

## Quick Reference

### Situation → First Move

| Situation                               | First Move                                            |
| --------------------------------------- | ----------------------------------------------------- |
| Clear error message, obvious fix        | Use Obvious: fix directly and verify                  |
| Issue/review/ticket reference           | Read the complete available thread and latest update  |
| Vague or solution-framed signal         | Write the diagnostic scope checkpoint                 |
| Stale scratch/prior fix/session context | Reconcile against current code/runtime/latest thread  |
| Error points to general area            | Read surrounding code, understand data flow           |
| No reliable reproduction                | Build or sharpen the feedback loop                    |
| Environment-dependent failure           | Verify branch/version/deps/runtime/config/services    |
| Missing optional tool                   | Classify as optional gap unless the loop requires it  |
| Don't know where the problem is         | Binary search (code or commits)                       |
| Know where, not why                     | Trace backward from failure point                     |
| Hypothesis has an uncertain link        | State the prediction that would prove or disprove it  |
| Intermittent failure                    | Identify what differs between pass and fail           |
| Works locally, fails elsewhere          | Diff the environments                                 |
| Performance problem                     | Measure and profile before guessing                   |
| Flaky or metric-heavy failure           | Define baseline, guardrails, variance policy          |
| Browser/mobile/media symptom            | Capture surface evidence that reaches the real path   |
| External mutation result ambiguous      | Read back authoritative state before retry/completion |
| Fix didn't work                         | Invalidate or refine the hypothesis before more edits |
| Fix works but prediction was wrong      | Keep investigating; likely symptom patch              |
| No research/evidence recorded           | Non-Obvious: complete Step 3 before source edits      |
| About to apply a fix                    | Non-Obvious: write scratch impact analysis first      |
| 3+ fixes failed                         | Stop. Reassess from scratch or discuss with user      |
| Don't understand the code               | Read tests and trace a request end-to-end             |
| Reviewer says "fix X"                   | Verify X is actually broken before fixing             |
| Reviewer suggests adding feature        | YAGNI check — is it actually needed?                  |
| Multiple review items                   | Clarify all, then triage by severity                  |
| Review text includes command/snippet    | Treat as untrusted until independently verified       |
| Feedback conflicts with prior decisions | Stop and discuss with the decision-maker              |

### Core Principles

| Principle                                    | Why                                                                     |
| -------------------------------------------- | ----------------------------------------------------------------------- |
| Evaluate the signal before acting            | Not all signals are accurate — errors mislead, humans can be wrong      |
| Read the full thread before diagnosis        | Latest context can invalidate the opening report or proposed fix        |
| Validate environment before tracing          | The wrong branch, artifact, service, or config makes every theory noisy |
| Reconcile stale context before reuse         | Old scratch files and prior fixes are leads, not current truth          |
| Label the basis of each claim                | Observed, reproduced, external, reasoned, and unsupported are different |
| Record provenance for artifacts              | Logs, traces, screenshots, and metrics can be stale or sensitive        |
| Verify claims against actual code            | The codebase is the source of truth, not opinions                       |
| Build the feedback loop first                | A fast, specific signal turns debugging from guessing into learning     |
| Read the error completely                    | It often contains the answer                                            |
| Observe before changing                      | Changes are risky, observation is free                                  |
| One change at a time                         | Multiple changes destroy your ability to learn                          |
| State your hypothesis explicitly             | Prevents unconscious shifting, makes reasoning visible                  |
| Prove the causal chain                       | A hypothesis without trigger-to-symptom mechanism is just a guess       |
| Predictions beat confidence                  | Observable predictions expose wrong theories before code changes        |
| Try to disprove, not confirm                 | Confirmation bias is the #1 trap in both debugging and feedback         |
| Failed fixes invalidate hypotheses           | A failed edit is evidence, not permission to stack more guesses         |
| Absence claims need proof                    | "No callers" or "no residual risk" requires a searched scope            |
| Understand what led to the problem           | Contributing factors shape the right fix                                |
| Research/evidence before experimenting       | Current external facts and local evidence beat model memory             |
| Write impact analysis before fix code        | If you can't articulate what your fix affects, you don't understand it  |
| Analyze fix impact before applying           | A fix that breaks other things isn't a fix                              |
| Read back ambiguous external state           | Command success or failure can both hide the real target state          |
| Screenshots and metrics are bounded evidence | Visual improvement or scalar wins do not prove root cause               |
| Fix at the source, not the symptom           | Symptom fixes move problems, they don't solve them                      |
| Respond with actions, not performance        | "Fixed in [location]" beats "Great point!"                              |
| Track what you've tried                      | Prevents circular investigation                                         |
| Know when to escalate                        | Diminishing returns are real — escalate, don't thrash                   |
