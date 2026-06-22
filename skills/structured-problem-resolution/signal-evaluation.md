# Signal Evaluation Guide

Detailed patterns for critically evaluating different types of input signals before acting on them. This reference supplements the Signal Reception phase in SKILL.md.

## Table of Contents

1. [Reading Error Messages](#reading-error-messages)
2. [Evaluating Human Feedback](#evaluating-human-feedback)
3. [Processing Code Review Comments](#processing-code-review-comments)
4. [Handling Bug Reports](#handling-bug-reports)
5. [The Handed Hypothesis Problem](#the-handed-hypothesis-problem)
6. [Multi-Item Feedback Processing](#multi-item-feedback-processing)
7. [The Push-Back Framework](#the-push-back-framework)
8. [Anti-Sycophancy Patterns](#anti-sycophancy-patterns)

---

## Reading Error Messages

Error messages vary enormously in helpfulness. Understanding the signal quality helps calibrate your response.

### High-Quality Signals (trust the message)

These tell you exactly what's wrong:

- `NameError: name 'foob' is not defined` — typo, fix directly
- `TypeError: expected str, got int` — type mismatch, trace the value
- `ModuleNotFoundError: No module named 'requests'` — missing dependency
- `SyntaxError: unexpected indent` — formatting issue at the indicated line

### Medium-Quality Signals (trust the location, investigate the cause)

These point to the right area but the stated cause may be misleading:

- `ConnectionTimeout` — could be network, server down, DNS, firewall, or the server is just slow
- `NullPointerException` — the null is the symptom; the cause is wherever the null originated
- `Permission denied` — could be file permissions, user context, SELinux, container config, or wrong path

### Low-Quality Signals (don't trust the message)

These are actively misleading:

- `Internal Server Error (500)` — tells you almost nothing about the actual cause
- `Segmentation fault` — the crash location is usually not the bug location
- `CORS error` — often a symptom of a server-side error that returns an error response without CORS headers
- Any error that says "X is wrong" when X is actually fine and the problem is in Y

### Error Message Checklist

For any error message:

1. Read the **exception type** before the message text — it tells you the category of mistake
2. Find the **first frame in your code** in the stack trace — that's where the bug manifests
3. In chained exceptions, the **root cause is at the bottom**, not the top
4. Note exact **line numbers, file paths, and variable values** mentioned
5. Check if the error mentions **what it expected vs. what it got** — this often contains the answer directly
6. Look for **"caused by"** or **"due to"** clauses — these point closer to the root cause
7. Read the **full output** — don't stop at the first error if there are warnings or additional context below

---

## Evaluating Human Feedback

### The Four-Axis Evaluation

For each piece of human feedback, evaluate independently on four axes:

**Axis 1: Technical Correctness**

- Is the reviewer's claim about code behavior factually correct?
- Does the suggested alternative actually compile/run/pass tests?
- Is the reviewer reasoning from the actual code, or from a mental model of what they think the code does?

**Axis 2: Contextual Appropriateness**

- Does this apply to THIS codebase, its conventions, and constraints?
- Does the reviewer have visibility into requirements that shaped the current design?
- Would this suggestion be correct in general but wrong here?

**Axis 3: Net Impact**

- Even if technically correct, is the change worth the risk/churn?
- Does fixing this introduce complexity elsewhere?
- What's the defect probability if we do nothing vs. the regression probability if we change it?

**Axis 4: Verifiability**

- Can this claim be tested or verified before implementation?
- Is there a way to confirm the reviewer's assertion against the actual codebase?
- Can you write a test that demonstrates the problem they're describing?

**Key insight:** These axes are independent. Feedback can be technically correct but contextually inappropriate. It can be contextually appropriate but have negative net impact. Evaluating on all four prevents the common mistake of treating "correct" as synonymous with "should implement."

### The Verification Sequence

Before implementing ANY non-trivial suggestion:

```
1. Re-read the actual code being discussed (not from memory)
2. Verify the reviewer's factual claims against what the code actually does
3. Check: Does the code actually behave as the reviewer says?
4. Check: Is the scenario they describe actually possible given the control flow?
5. Check: Would their suggestion break existing functionality?
6. Check: Would their suggestion work on all platforms/versions?
7. Check: Does their suggestion conflict with prior architectural decisions?

IF any check fails:
  Push back with specific technical reasoning

IF can't easily verify:
  Say so: "Can't verify without [X]. Should I [investigate/ask/proceed]?"

IF conflicts with your partner's decisions:
  Stop and discuss with your partner first
```

---

## Processing Code Review Comments

### Classify Each Comment

Before acting, categorize each piece of feedback:

| Category             | Description                                                | Action                                           |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| **Defect**           | The code has a bug or will fail under specified conditions | Fix with tests, high priority                    |
| **Design**           | Structural or architectural concern                        | Discuss if you disagree, implement if you agree  |
| **Style/Convention** | Naming, formatting, patterns differing from norms          | Follow team norms; establish one if none exists  |
| **Optimization**     | Performance or efficiency improvement                      | Only if measurable or cost of change is very low |
| **Informational**    | Reviewer sharing context, not requesting a change          | Acknowledge, no action needed                    |
| **Preference**       | Reviewer would do it differently, but current isn't wrong  | Acknowledge, explain rationale, move on          |

The classification matters because different categories require different levels of verification and different response patterns. A defect needs immediate attention. A preference needs acknowledgment but not necessarily action.

### Source-Specific Handling

**From your human partner:**

- Trusted — implement after understanding
- Still ask if scope is unclear
- No performative agreement needed
- Skip to action or brief technical acknowledgment

**From external reviewers:**

```
BEFORE implementing:
  1. Technically correct for THIS codebase?
  2. Breaks existing functionality?
  3. Reason for current implementation?
  4. Works on all platforms/versions?
  5. Does reviewer understand full context?

IF suggestion seems wrong:
  Push back with technical reasoning

IF can't easily verify:
  State limitation, ask for direction

IF conflicts with your partner's prior decisions:
  Stop and discuss with your partner first
```

**From automated tools (linters, static analysis):**

- Very high trust for what they check
- Almost always implement
- But: false positives exist — if the warning seems wrong, investigate before suppressing
- If suppressing, leave a comment explaining why

**From AI-generated reviews:**

- Medium trust for pattern detection
- Low trust for contextual understanding
- Always verify against the actual code path
- AI reviewers often flag things that are intentional design decisions
- Particularly prone to suggesting "best practices" that don't apply to your specific situation

---

## Handling Bug Reports

### Separating Symptoms from Diagnosis

Bug reports contain a mixture of:

- **Observations** (facts): "I clicked submit and saw a blank page"
- **Interpretations** (opinions): "The form submission is broken"
- **Diagnoses** (theories): "I think the API is down"

Observations are usually reliable (though "I definitely didn't change anything" is almost always false). Interpretations and diagnoses can anchor your investigation in the wrong direction.

**Technique: Extract raw observations, discard the diagnosis, form your own hypothesis.**

| Bug Report                                      | Observations to Extract                               | Reporter's Diagnosis (evaluate separately)     |
| ----------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------- |
| "The cache is broken — stale data after deploy" | Data reflects pre-deploy state, resolves after ~10min | Cache issue? Or CDN/LB/rolling deploy?         |
| "The button doesn't work"                       | Click produces no visible response                    | Button handler? API? Network? JS error?        |
| "The API is slow"                               | Response took 12s for user X at 3pm                   | API code? Database? Network? CDN?              |
| "Authentication is broken"                      | User gets redirected to login after authenticating    | Session? Cookie? Token expiry? Redirect logic? |

### Avoiding Anchoring on First Framing

1. **Look at evidence before the diagnosis.** If possible, check logs and metrics before reading the reporter's theory.
2. **Ask "what did you actually see?"** Push past interpretations to raw observations. "The API is slow" becomes "The /checkout endpoint took 12 seconds to respond at 3:00 PM for user ID 12345."
3. **Generate your own hypothesis independently.** Based solely on the observations, what would YOU think? Only then compare with the reporter's diagnosis.
4. **Consider the reporter's vantage point.** They may only see one part of the system. Their diagnosis is reasonable given their perspective but may miss the bigger picture.
5. **List at least 3 different causes that could produce the same symptom.** Force yourself beyond the obvious. Blank page could be: JS error, API failure, CORS issue, DNS issue, deployment still in progress, feature flag misconfigured.

### The Reproducer as Ground Truth

The single best way to get past misleading reports is to **reproduce the issue yourself.** A reliable reproducer is:

- **Independent of the reporter's interpretation** — you observe the actual behavior
- **Controllable** — you can vary conditions to test hypotheses
- **The ultimate acceptance test** — the problem is fixed when the reproducer passes

When you can't reproduce: that itself is information. Either the environment differs (check config, data, permissions, browser, OS), the issue is intermittent (need more precise conditions), or the report is inaccurate.

---

## The Handed Hypothesis Problem

When someone gives you their diagnosis ("the bug is in X," "fix it by doing Y"), they're handing you a pre-formed hypothesis. This is dangerous because:

1. **Authority bias** makes you weight it higher than your own analysis
2. **Social pressure** makes you want to validate it quickly
3. **Anchoring** makes it hard to consider alternatives
4. **Skipping verification** feels efficient but is actually risky

### How to Handle a Handed Hypothesis

```
1. Receive it as one hypothesis among several — not as truth
2. Generate 2-3 alternative explanations independently
3. Test the handed hypothesis with the same rigor as your own
4. If it's correct — implement it (but verify the fix)
5. If it's wrong — push back with evidence, not opinion
```

**The key mental model:** The person handing you the hypothesis has a _partial view_ of the system. They may be right — they often are. But "often right" is not "always right," and the cost of implementing a wrong hypothesis (introducing bugs, wasting time) outweighs the cost of spending 5 minutes verifying.

### Real Examples

**Reviewer hands you a wrong hypothesis:**

```
Reviewer: "Remove this legacy code path — it's dead code."
❌ "Good catch, removing it."
✅ "Checking... build target is 10.15+, this API needs 13+. The legacy
    path is needed for backward compat. The bundle ID is wrong though —
    fix that, or drop pre-13 support?"
```

**Reviewer hands you a correct hypothesis:**

```
Reviewer: "This function mutates the input dict. That'll cause issues
          for callers who don't expect mutation."
✅ [Verify: check if callers depend on mutation or not]
✅ "Verified — callers don't depend on mutation. Changed to return a
    copy. Tests pass."
```

**Bug reporter hands you a misleading diagnosis:**

```
Reporter: "The caching layer is broken."
✅ [Check: is it actually the cache?]
✅ "Investigated — it's not cache. The CDN edge server in EU was serving
    a stale version. Purged CDN cache, confirmed resolution."
```

---

## Multi-Item Feedback Processing

### The Correct Order

```
1. READ all items before responding to any
   - Items may be related — understanding the full set prevents redundant work

2. CLARIFY anything unclear FIRST
   - Don't implement partial understanding
   - "Understand items 1,2,3,6. Need clarification on 4 and 5."

3. CLASSIFY each item
   - Defect / Design / Style / Optimization / Informational / Preference

4. PRIORITIZE by impact:
   a. Blocking issues (security, data loss, crashes)
   b. Correctness issues (logic errors, wrong behavior)
   c. Simple fixes (typos, imports, naming)
   d. Complex changes (refactoring, redesign)
   e. Style/preference items

5. IMPLEMENT one at a time, test each
   - Don't batch changes — verify each fix individually

6. VERIFY no regressions between fixes
```

### When Items Conflict

If two feedback items contradict each other, or if implementing one makes another unnecessary:

- Note the conflict explicitly
- Ask for clarification before proceeding
- Don't try to reconcile contradictions on your own

### Review Fatigue

After multiple review rounds, the temptation to accept everything just to get the PR merged grows stronger. This is exactly when you need MORE scrutiny, not less — late-round changes receive the least review but are the most likely to introduce bugs because both author and reviewer are fatigued.

---

## The Push-Back Framework

### When to Push Back

Push back when:

- Suggestion breaks existing functionality — demonstrate with a test or trace
- Reviewer lacks full context — provide the missing context
- Violates YAGNI — adds unused capability
- Technically incorrect for this stack/platform
- Legacy/compatibility reasons exist that aren't visible to the reviewer
- Conflicts with established architectural decisions
- Implementation would introduce more complexity than the problem it solves

### How to Push Back

**Use technical reasoning, never defensiveness:**

```
✅ "Checking... build target is 10.15+, this API needs 13+. Need legacy
    for backward compat. Fix the bundle ID or drop pre-13 support?"

✅ "Grepped codebase — nothing calls this endpoint. Remove it (YAGNI)?
    Or is there usage I'm missing?"

✅ "The current approach handles [edge case X] which the suggested
    change wouldn't cover. Want me to modify the suggestion to handle
    that, or is X not a concern?"

✅ "I considered that approach, but it doesn't work here because
    [specific reason with evidence]."
```

**Never push back with:**

- "I disagree" (without reasoning)
- "That won't work" (without explaining why)
- Defensiveness about your original code
- Appeals to authority or convention without technical substance

### Gracefully Correcting Your Pushback

If you pushed back and were wrong:

```
✅ "You were right — I checked [X] and it does [Y]. Implementing now."
✅ "Verified and you're correct. My initial understanding was wrong
    because [reason]. Fixing."

❌ Long apology
❌ Defending why you pushed back
❌ Over-explaining
```

State the correction factually and move on.

---

## Anti-Sycophancy Patterns

### Why Sycophancy Happens

For AI systems: RLHF training creates a bias toward agreement because human raters tend to prefer agreeable responses. The model learns that agreement gets positive feedback, even when disagreement would be more helpful.

For humans: social pressure, conflict avoidance, authority bias, and the desire to be perceived as cooperative all push toward agreement over accuracy.

Both failure modes produce the same result: implementing changes without verification, leading to bugs, wasted time, and degraded code quality.

### The Sycophancy Failure Pattern

```
1. Receive feedback → "You're right!" (before verifying)
2. Skip verification → start implementing immediately
3. Implement literally → miss the underlying principle
4. Don't check implications → break adjacent code
5. Respond performatively → "Great catch, fixed!"
6. Move on → problem not actually solved, or new problem introduced
```

### The Correct Pattern

```
1. Receive feedback → read and understand
2. Verify against code → does the code actually do what they claim?
3. Evaluate on four axes → correct? appropriate? worth it? verifiable?
4. If correct: fix it, state what changed
5. If incorrect: push back with evidence
6. If unclear: ask for clarification
7. Verify the fix → tests pass, no regressions
```

### Red Flags You're Being Sycophantic

- You're about to write "You're absolutely right" — stop, verify first
- You're implementing a change you don't understand — stop, ask
- You feel social pressure to agree quickly — that pressure is the signal to slow down
- You're changing working code because someone said it's wrong — verify the claim
- You're adding code to satisfy a reviewer's preference rather than fixing an actual problem — evaluate net impact
- You caught yourself about to write "Thanks for catching that" — replace with a statement of what you fixed and why

### Five Common Sycophancy Anti-Patterns

**1. Phantom Bug Acknowledgment:** Human says "this has a bug." You agree and "fix" code that was actually working correctly, potentially introducing a real bug.

**2. Immediate Capitulation:** "You're right, I apologize. Let me fix that." — without verifying whether the critique is actually correct.

**3. Frame Adoption:** Human says "this approach is wrong, use pattern X instead." You adopt pattern X without evaluating whether it's actually better or even applicable.

**4. Cascading Agreement:** Once you agree with one point, you become more likely to agree with all subsequent points, even unrelated ones.

**5. Loss of Context:** You may have had good reasons for your original implementation but abandon them under social pressure without articulating them. The human loses information they need to make a good decision.

### The Bottom Line

External feedback = hypotheses to evaluate, not instructions to follow.
Error messages = clues to investigate, not diagnoses to trust.

Verify. Question. Then implement.

Technical rigor always. Performance never.
