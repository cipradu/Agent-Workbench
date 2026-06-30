# Cognitive Traps in Problem Resolution

When problem resolution goes wrong, it's usually not because of lacking technical skill. It's because thinking goes wrong in predictable, well-documented ways. These traps affect both debugging (finding bugs) and feedback processing (evaluating suggestions). Understanding them makes them easier to recognize and avoid.

## Table of Contents

1. [Traps in Investigation](#traps-in-investigation)
2. [Traps in Receiving Feedback](#traps-in-receiving-feedback)
3. [The Thrashing Pattern](#the-thrashing-pattern)
4. [The Meta-Trap](#the-meta-trap)

---

## Traps in Investigation

### Confirmation Bias

**What it is:** Interpreting ambiguous evidence as supporting your existing hypothesis. Seeking evidence that confirms rather than evidence that could disprove.

**How it manifests in debugging:**

- You believe it's a database issue, so you focus on database logs and ignore the application logs that show the real problem
- You run a test that produces unclear results and interpret them as "probably confirming" your theory
- You find one piece of evidence that matches and stop looking, ignoring three pieces that don't match

**How it manifests when receiving feedback:**

- A reviewer says "this has a race condition" and you look for thread interleaving scenarios, finding one that "looks like it could maybe happen" — confirming the reviewer's theory without testing whether it actually can happen in practice
- You accept feedback that aligns with your own doubts about the code, while dismissing feedback that challenges your design decisions

**How it feels:** "See, the connection pool _is_ running low — that must be it." (But you haven't checked whether the pool was also low during the times it worked.)

**Countermeasures:**

- Before each experiment, write down what you'd expect to see if your hypothesis is _wrong_
- Look for that disconfirming evidence first
- When evidence is ambiguous, treat it as uninformative, not supportive
- Ask: "What's the strongest argument against my current theory?"

### Anchoring

**What it is:** The first piece of information you encounter disproportionately shapes your entire investigation, even when it's misleading.

**How it manifests:**

- The error says "timeout" so you investigate network issues, but the timeout is caused by an infinite loop
- A colleague says "I think it's the cache" and you spend two hours on cache logic
- The most recent commit touched file X, so you assume the bug is in file X, even though the commit was unrelated
- The user's bug report says "the button doesn't work" so you debug the button click handler, when the actual issue is the API response
- A reviewer frames their feedback as "the validation is wrong" and you spend an hour on validation logic, when the actual issue is data transformation upstream

**How it feels:** You keep coming back to your starting point even when the evidence leads elsewhere.

**Countermeasures:**

- After your initial read of the error or feedback, deliberately pause and generate 3+ alternative hypotheses
- Rank them by likelihood _independently_ before investigating any
- Be especially skeptical of the first theory that comes to mind — it's the most likely to be an anchor rather than a conclusion
- When someone hands you a diagnosis, generate your own hypothesis before evaluating theirs

### Sunk Cost Fallacy

**What it is:** Continuing a line of investigation because of the time already invested, not because it's still promising.

**How it manifests:**

- "I've spent 3 hours investigating the auth layer, so the bug MUST be in the auth layer"
- Refusing to restart with a different approach because it would mean "wasting" previous work
- Adding increasingly elaborate logging to a component that probably isn't the problem, because you've already added a lot of logging there
- Continuing to implement a reviewer's suggestion even after discovering it doesn't apply to your situation, because you've already started

**How it feels:** The thought of starting over feels physically painful. You tell yourself "just a little more investigation in this direction."

**Countermeasures:**

- Time-box your investigations: 15-30 minutes without progress means step back and reassess
- Reframing: time spent investigating the wrong thing isn't wasted — you've learned where the problem _isn't_
- Ask yourself: "If I were starting fresh right now, would I choose this same line of investigation?" If no, switch.

### Tunnel Vision (Premature Narrowing)

**What it is:** Zooming into a specific area of code too quickly, before understanding the broader picture.

**How it manifests:**

- You see an error in function X, so you stare at function X for an hour, when the actual bug is in the data that function X receives
- You debug the rendering logic when the problem is in the data transformation upstream
- You focus on one log line and miss the broader pattern across many log lines

**How it feels:** You're deep in the code, reading every line carefully, but making no progress.

**Countermeasures:**

- Read the full error output (all of it) before narrowing
- Trace the complete data flow before focusing on any single point
- Every 20 minutes, zoom out: "Am I sure the problem is in this area? What evidence do I have?"

### Availability Bias

**What it is:** Diagnosing based on bugs you've encountered recently or frequently, rather than based on the evidence.

**How it manifests:**

- You just spent last week fixing a race condition, so this week's bug "must be a race condition too"
- You've seen many null pointer bugs, so every crash looks like a null pointer
- The team has been having database issues, so you blame the database first

**How it feels:** Strong intuition that "I've seen this before." That intuition may be wrong.

**Countermeasures:**

- Enumerate possible causes systematically rather than going with gut feel
- Ask: "What evidence do I have that this is the same type of bug I saw before?" If the answer is "it feels similar," that's not evidence.

### The Einstellung Effect

**What it is:** Prior experience with similar problems blocks you from seeing a different (often simpler) solution. Expert debuggers can be MORE susceptible to this than novices.

**How it manifests:**

- You know exactly how to debug authentication issues, so you apply your auth debugging playbook. But this isn't actually an auth issue — it just looks like one.
- Your known debugging approach isn't working, but you keep applying it with small variations instead of trying a fundamentally different approach.
- You recognize a pattern and immediately apply the corresponding fix, but the pattern was superficial — the underlying cause is different.

**How it feels:** "I know how to debug this." Followed by... it doesn't work. Followed by confusion, because your trusted approach should have worked.

**Countermeasures:**

- When your usual approach isn't working after 2-3 attempts, explicitly consider that this might be a different kind of problem than you think
- Ask: "What if I'm wrong about what _type_ of problem this is?"

### The "Looks Right" Trap

**What it is:** Code that reads correctly to a human but executes incorrectly. Your brain autocorrects the mistake when reading.

**How it manifests:**

- Off-by-one errors (`<` vs `<=`, `i` vs `i+1`)
- Wrong comparison operators (`>` vs `>=`, `==` vs `===`)
- Subtle ordering issues (initialize after use, close before write completes)
- Variable shadowing (using a local with the same name as an outer variable)
- Copy-paste errors where one instance wasn't updated

**How it feels:** "I've read this function five times and it looks correct." It isn't.

**Countermeasures:**

- Don't trust your reading of the code. Observe actual runtime values.
- Add logging that prints the actual values at each step
- Use a debugger to step through the actual execution
- Explain the code line by line to someone (or a rubber duck). The act of articulating forces sequential reasoning that catches what scanning misses.

### Environmental Blindness ("Works on My Machine")

**What it is:** Assuming your local environment is representative, even when the bug report says otherwise.

**How it manifests:**

- "I can't reproduce it, so it's probably user error"
- Testing in your development environment and concluding the bug is fixed, without testing in the environment where it actually fails
- Ignoring environment differences: different OS, different runtime version, different config, different data

**Countermeasures:**

- Believe the bug reporter first. "It works for me" means the environments differ, not that the bug doesn't exist.
- Reproduce in the actual failing environment (or as close as you can get)
- Systematically diff environments when something works in one place but not another

### Stale Scratch Anchoring

**What it is:** Treating an old scratch file, prior issue title, previous failed fix, old log excerpt, or session summary as current truth.

**How it manifests:**

- Yesterday's scratch says "cache bug", so today's investigation starts in cache even though the latest log points to auth.
- A prior solution doc describes the same error string, so you apply its fix without checking current versions, branch, config, or runtime state.
- A review comment was written against old code, but you resolve it as if the line still means the same thing.

**Countermeasures:**

- Reconcile old notes against current code, branch/worktree, dependencies, runtime, latest thread update, and current symptom.
- Label stale context as current, stale but correctable, contradicted, superseded, or requiring restart from observation.
- Treat prior learnings as leads that generate hypotheses, not as root-cause proof.

### Metric Gaming

**What it is:** Accepting a scalar improvement as success while the original behavior, correctness, safety, or user-visible outcome remains unproven.

**How it manifests:**

- One benchmark run is faster, but variance is larger than the improvement.
- A quality score improves because the fixture or rubric was weakened.
- Cache hit rate rises while stale reads increase.
- A flaky test passes once after a timing tweak and is declared fixed.

**Countermeasures:**

- Define baseline, target, guardrails, variance policy, and immutable measurement assets before changing code.
- Re-run enough to understand noise, or label the result inconclusive.
- Verify the original symptom and hard correctness gates, not just the proxy metric.

### False-Success Command Output

**What it is:** Trusting stdout, a URL, a success code, or a "completed" message without reading back the target state.

**How it manifests:**

- A command exits 0 but wrote an empty remote artifact.
- An API call times out after the remote side already created the object, then a retry creates a duplicate.
- A 202 response is treated as success even though the eventual job failed.

**Countermeasures:**

- Capture stdout, stderr, exit code/status, target state, and fallback path.
- Read back authoritative state before retrying or claiming completion when mutation status is ambiguous.
- Separate stale/precondition failures, invalid payloads, false success, and ambiguous post-write failures.

### Optional-Tool False Blocker

**What it is:** Treating a missing helpful tool as proof the investigation is blocked or as the cause of the symptom.

**How it manifests:**

- Browser automation is unavailable, so a UI bug is declared untestable even though logs, screenshots, or manual capture could narrow it.
- A profiler is missing, so a performance issue is guessed at instead of using a coarser baseline.
- A simulator is unavailable, so device evidence is ignored rather than recorded as an automation limitation.

**Countermeasures:**

- Classify environment findings as blocking failure, optional capability gap, or unrelated observation.
- Use the lightest valid loop that reaches the symptom.
- Ask for setup help only when no valid evidence path remains.

### Visual-Satisfaction False Proof

**What it is:** Treating a screenshot, hot reload, visual polish, or user satisfaction as root-cause proof.

**How it manifests:**

- The UI "looks better" after a CSS tweak, but the original click path still fails under a different state.
- A screenshot shows the expected page but not whether the side effect, network call, storage update, or accessibility behavior succeeded.
- A dogfood note says the flow feels fixed, but the failing runtime logs were never rechecked.

**Countermeasures:**

- Capture the original observable symptom and re-run the same path after the fix.
- Pair visual evidence with DOM, console, network, storage, server logs, or true end-state checks as relevant.
- Record manual or automation limits as residual risk.

### Prior-Learning Overtrust

**What it is:** Applying a remembered or documented old fix because the current problem resembles a past problem.

**How it manifests:**

- "We fixed this by bumping the timeout last time" becomes the first edit, even though the current trace shows a data-shape error.
- A solution doc's old dependency behavior is copied after the dependency changed.
- A known workaround is applied without checking whether the upstream bug was fixed.

**Countermeasures:**

- Search prior learnings for leads, failed attempts, and stale warnings, then verify applicability with current evidence.
- Record conflicts between prior learning and current source/runtime evidence.
- Use current official docs or current local runtime behavior for drift-prone facts.

---

## Traps in Receiving Feedback

These traps are specific to processing human input — code reviews, suggestions, bug reports, and directions from authority figures. They often interact with the investigation traps above, compounding the risk.

### Sycophancy (Agreement Bias)

**What it is:** Agreeing with feedback because of social pressure rather than technical evaluation. For AI systems, this is amplified by RLHF training that rewards agreeable responses. For humans, it stems from conflict avoidance and desire for social harmony.

**How it manifests:**

- Saying "You're absolutely right!" before verifying the claim
- Implementing a suggestion you don't understand because the reviewer seems confident
- Changing working code because someone authoritative said it's wrong, without checking
- Abandoning a correct approach when a user says "Are you sure?"
- The "phantom bug" — agreeing there's a bug and "fixing" code that was actually working correctly

**How it feels:** An urge to agree quickly and move on. The thought of pushing back feels uncomfortable or risky.

**Countermeasures:**

- Establish a personal rule: for any non-trivial suggestion, you must articulate _in your own words_ why the change is an improvement. If you cannot, you haven't evaluated it — you're complying.
- Re-read the actual code before responding to feedback about it
- If you feel pressure to agree quickly, that pressure is the signal to slow down and verify
- Check: "Would I make this change if nobody suggested it?"

### Authority Bias

**What it is:** Weighting feedback based on who said it rather than what they said. Accepting suggestions from senior engineers without verification while dismissing valid feedback from junior engineers.

**How it manifests:**

- A senior developer says "use pattern X" and you implement it without evaluating whether X applies here
- A junior developer identifies a real bug and you dismiss it because "they're probably wrong"
- An external security auditor flags an issue and you implement their exact suggestion without checking if it fits your architecture

**How it feels:** "They're more experienced, so they're probably right." Maybe. But experience doesn't equal correctness on every specific point.

**Countermeasures:**

- Evaluate the comment, not the commenter
- Ask: "If this exact comment came from a new hire, would I still implement it?"
- Conversely: "If this came from the CTO, would I still push back if I thought it was wrong?"
- Remember: expertise is domain-specific. A brilliant backend engineer may give poor CSS advice.

### Frame Adoption

**What it is:** Adopting the reviewer's framing of a problem without independently evaluating whether the framing is correct. Once a reviewer frames a problem ("this function is too complex," "this should use pattern X"), it becomes very difficult to see the code independently.

**How it manifests:**

- Reviewer says "this function is too complex" → you start refactoring complexity, but the actual issue is that the function has a bug
- Bug report says "the caching layer is broken" → you investigate caching, but the actual issue is a database migration
- Colleague says "we need better error handling here" → you add try/catch blocks, but the actual issue is that the function shouldn't be called in that context at all

**How it feels:** The reviewer's lens becomes your lens. You can't see the code independently anymore.

**Countermeasures:**

- Before reading the reviewer's suggested _solution_, understand only the _problem_ they're identifying
- Then independently consider what the right solution is
- Compare your independent solution with the reviewer's suggestion
- If they diverge, that's a conversation worth having, not a signal to defer

### Deference Under Pressure

**What it is:** Skipping verification to seem responsive, especially during time pressure, review fatigue, or when multiple rounds of review have already occurred.

**How it manifests:**

- After multiple review rounds, accepting every suggestion just to get the PR merged
- Implementing changes during an incident because someone with authority suggested them, without evaluating whether they'll actually help
- Agreeing to "just fix it" because the reviewer is impatient
- Late-round review changes receiving the least scrutiny despite being most likely to introduce bugs

**How it feels:** "I just want this done. Fine, I'll change it." The cost of discussion feels higher than the cost of a wrong change. (It almost never is.)

**Countermeasures:**

- Recognize that late-round changes and time-pressured changes are the HIGHEST risk, not the lowest
- "I want to get this right rather than fast. Let me verify this will work."
- If you catch yourself implementing without understanding, stop. The 5 minutes spent verifying is always cheaper than the debugging session that follows a wrong change.

### The Shotgun Fix (from feedback)

**What it is:** A reviewer identifies a problem in one place, and you "fix" it everywhere — including places where it wasn't a problem — introducing bugs in previously working code.

**How it manifests:**

- Reviewer says "use `===` instead of `==` here" → you change every `==` in the file, including intentional type coercions
- Reviewer says "add null checks" → you add null checks everywhere, including paths where null is impossible
- Reviewer flags missing error handling in one function → you add try/catch to every function, obscuring real errors

**Countermeasures:**

- Understand the _principle_ behind the feedback, not just the literal instruction
- Apply the principle only where it's actually relevant
- For each additional instance you're considering changing, verify it's actually a problem

### Review Fatigue Capitulation

**What it is:** After multiple review rounds, the author starts accepting every suggestion just to get the PR merged, regardless of whether the suggestions are improvements.

**How it manifests:**

- "Sure, I'll change it" without thinking about whether the change is correct
- Making increasingly less-considered changes in later review rounds
- Treating the review as an obstacle course to get through rather than a quality process
- Late-round changes receiving the least scrutiny from both author and reviewer

**Why it's dangerous:** Late-round changes are the most likely to introduce bugs because they receive the least scrutiny. Both author and reviewer are fatigued, cognitive reserves are depleted, and the motivation shifts from "get it right" to "get it done."

**Countermeasures:**

- Recognize the pattern when it starts ("I just want this merged")
- Take a break before addressing late-round feedback
- Apply the same verification discipline to the last round as to the first
- If you genuinely disagree with late-round feedback, say so rather than capitulating

### Review-Fatigue Auto-Apply

**What it is:** Treating review feedback as a queue to clear instead of a set of evidence claims to verify.

**How it manifests:**

- Applying every AI or reviewer suggestion because a prior batch had valid findings.
- Letting "safe" cleanup remove validation, redaction, accessibility behavior, logging, or compatibility checks.
- Marking feedback resolved because code changed, without verifying the original evidence disappeared.

**Countermeasures:**

- Keep stable IDs and dispositions for each item.
- Verify factual claims, scope, and current relevance before each edit.
- Use `fixed differently`, `not addressing with evidence`, `declined harmful`, or `needs human decision` when the literal suggestion is not the right fix.

---

## The Thrashing Pattern

Thrashing deserves special attention because it's the end state of many of the traps above. It can be triggered by both debugging frustration AND by receiving conflicting or overwhelming feedback.

**What it looks like:**

- Rapid changes with decreasing thoughtfulness
- Making a change, seeing it fail, reverting, trying another, reverting that
- Losing track of what's been changed and what the original state was
- Frustration or time pressure driving faster-but-dumber changes
- Implementing reviewer suggestions without verification, getting more comments, implementing those too
- Sometimes accidentally re-trying something that was already disproven

**How you get there:**

1. You run out of hypotheses (availability/anchoring used them up) OR you're drowning in feedback
2. Time pressure makes investigation feel too slow (sunk cost makes restarting feel wasteful)
3. You've lost your mental model of the system's state (tunnel vision kept you from maintaining the big picture)
4. Each quick fix adds complexity, making the next one harder (compounding errors)

**How to break out:**

1. **Stop changing code.** Literally stop. Take a breath.
2. **Revert to a known state.** Undo all your debugging changes. Get back to the original problem, not the problem-plus-your-changes.
3. **Write down what you know.** Use the scratchpad template from SKILL.md. What have you observed? What have you tried? What worked, what didn't?
4. **Get fresh eyes.** Explain the problem to the user, a colleague, or rubber duck. The act of explaining often reveals the gap in your understanding.
5. **If you're an AI agent:** Tell the user you're stuck. Describe what you've found and tried. Ask for their input. This is not failure — this is efficient use of a resource (the human's domain knowledge) that you don't have.

---

## The Meta-Trap

The biggest trap of all is thinking you're immune to these traps. Everyone falls into them — experts and novices, humans and AI alike. The difference is not avoiding them entirely (impossible) but recognizing them quickly and course-correcting.

The scratchpad, the time-boxing, the explicit hypothesis-stating, and the verification-before-implementation rule are all structural countermeasures. They work not by making you smarter, but by making your reasoning process visible so that errors in thinking become errors in text — and errors in text are much easier to spot.

For feedback-specific traps, the structural countermeasure is even simpler: **verify every claim against the actual code before acting on it.** This single discipline prevents sycophancy, authority bias, frame adoption, and blind implementation simultaneously.
