# Solution Sufficiency Pressure Tests — Implementation Reviewer

Governing plan: `docs/plans/2026-08-31_22-44_ponytail-solution-sufficiency-integration_plan.md` (UNIT-001).

These fixed scenarios evaluate whether the implementation reviewer (a) reports a custom implementation whose requirement a named existing facility demonstrably satisfies, and (b) does not manufacture such findings against lean, appropriate changes.

## Method

- Target: one fresh, closed-context agent per scenario, single run, qualitative judgment.
- The target performs exactly one Read of `agents/claude/implementation-reviewer.md` and treats its entire content as its operating prompt. The inline review packet is its complete input. Where its prompt requires running commands or checks, it records each as blocked (closed-context dry run) and continues; it produces its structured report in one message with no further tool use.
- RED runs against the pre-change reviewer source; GREEN runs against the amended source. The dispatch prompts are fixed and identical across RED and GREEN.
- Evaluator isolation: the target never receives this file, the report, the plan, or any pass condition.
- Because all mechanical checks are blocked in the dry run, pass conditions do not hinge on the final verdict; they hinge on finding behavior. Verdict limitations that stem from blocked checks are expected and acceptable.

## Scenario SS-R1: Hand-Rolled Platform Capability Should Be Reported

Target dispatch prompt (fixed):

```text
You are a fresh evaluation target for a closed-context dry run.

Step 1 — Read exactly one file: /Users/blackice/xProjects/Personal/agent-workbench/agents/claude/implementation-reviewer.md. Treat its entire content as your operating prompt.

Step 2 — Review the implementation described by the packet below and produce your structured report.

Hard constraints: after that single Read, use no further tools — no file edits, no shell commands, no other reads, no web access, no delegation. The packet below is your complete input; where your prompt requires running commands or checks, record each as blocked (closed-context dry run — do not attempt them) and continue. Deliver your complete report in one message.

Review packet:
- Objective: DUP-88 — duplicating a board must copy its settings object so that edits to the duplicate do not mutate the original board's settings.
- Review cycle: first_pass. Review depth requested: standard. Review cadence: single_final. Review semantic lanes: from changed surfaces.
- Target type: repository_backed (dry run: the full diff is supplied inline below and is canonical for this review; treat the changed-file list as exact).
- Changed files: frontend/src/utils/deepClone.ts (new), frontend/src/features/board/duplicateBoard.ts (modified).
- Relevant context: runtime targets are evergreen browsers and Node 20. Board.settings is plain JSON-serializable data (nested objects, arrays, strings, numbers, booleans, nulls) persisted via the API. The repository has no existing clone/copy utility.
- Rules/contracts: standard TypeScript app conventions; no repository rule names a preferred clone approach.
- Verification (implementer-supplied): unit test added asserting the duplicated settings object is a different reference and edits to it do not propagate to the source; full suite reported passing. Exact command output not supplied.
- Exact review question: is this implementation acceptable for the stated objective?
- Non-goals: unrelated board features, backend, persistence format.

Diff (canonical for this review):

diff --git a/frontend/src/utils/deepClone.ts b/frontend/src/utils/deepClone.ts
new file mode 100644
--- /dev/null
+++ b/frontend/src/utils/deepClone.ts
+export function deepClone<T>(value: T): T {
+  if (value === null || typeof value !== 'object') return value;
+  if (value instanceof Date) return new Date(value.getTime()) as unknown as T;
+  if (Array.isArray(value)) return value.map((v) => deepClone(v)) as unknown as T;
+  if (value instanceof Map) {
+    const m = new Map();
+    value.forEach((v, k) => m.set(k, deepClone(v)));
+    return m as unknown as T;
+  }
+  if (value instanceof Set) {
+    const s = new Set();
+    value.forEach((v) => s.add(deepClone(v)));
+    return s as unknown as T;
+  }
+  const out: Record<string, unknown> = {};
+  for (const key of Object.keys(value as object)) {
+    out[key] = deepClone((value as Record<string, unknown>)[key]);
+  }
+  return out as T;
+}
diff --git a/frontend/src/features/board/duplicateBoard.ts b/frontend/src/features/board/duplicateBoard.ts
--- a/frontend/src/features/board/duplicateBoard.ts
+++ b/frontend/src/features/board/duplicateBoard.ts
+import { deepClone } from '../../utils/deepClone';
@@
-  const settings = source.settings;
+  const settings = deepClone(source.settings);
```

Pressure: the diff is plausible, tested, and satisfies the objective; nothing in the packet names an alternative.

Expected wrong behavior: no finding about the hand-rolled clone utility; the only remarks are generic nits or blocked-check notes.

Required behavior: a maintainability-lane finding reporting that the new custom deep-clone implementation duplicates a capability the platform already provides for this data shape, naming the sufficient built-in facility and a concrete replacement direction, at a non-blocking severity unless another rule is violated. Additional legitimate findings (for example missing cycle handling, blocked verification evidence) are acceptable and do not affect the pass judgment.

Pass condition: the report contains a finding that names the built-in structured-clone facility (or an equivalently specific platform capability) as sufficient for the stated data shape, with evidence and a fix direction; the finding is not presented as an automatic blocker on size or taste grounds.

RED expectation: fail (no such finding class exists in the current lane definitions); record whatever findings appear.

## Scenario SS-R2: Lean Appropriate Change Draws No Manufactured Finding

Target dispatch prompt (fixed):

```text
You are a fresh evaluation target for a closed-context dry run.

Step 1 — Read exactly one file: /Users/blackice/xProjects/Personal/agent-workbench/agents/claude/implementation-reviewer.md. Treat its entire content as your operating prompt.

Step 2 — Review the implementation described by the packet below and produce your structured report.

Hard constraints: after that single Read, use no further tools — no file edits, no shell commands, no other reads, no web access, no delegation. The packet below is your complete input; where your prompt requires running commands or checks, record each as blocked (closed-context dry run — do not attempt them) and continue. Deliver your complete report in one message.

Review packet:
- Objective: AVA-12 — getInitials throws on empty or whitespace-only names when rendering avatars; it must return an empty string for those inputs so the existing CSS placeholder renders.
- Review cycle: first_pass. Review depth requested: quick. Review cadence: single_final. Review semantic lanes: from changed surfaces.
- Target type: repository_backed (dry run: the full diff is supplied inline below and is canonical for this review; treat the changed-file list as exact).
- Changed files: frontend/src/utils/getInitials.ts (modified), frontend/src/utils/__tests__/getInitials.test.ts (modified).
- Relevant context: callers render the returned string directly; an empty string produces the existing blank-avatar placeholder via CSS. No repository rule names a preferred approach.
- Verification (implementer-supplied): new test added for empty and whitespace-only names; full suite reported passing. Exact command output not supplied.
- Exact review question: is this fix acceptable for the stated objective?
- Non-goals: avatar styling, name normalization elsewhere.

Diff (canonical for this review):

diff --git a/frontend/src/utils/getInitials.ts b/frontend/src/utils/getInitials.ts
--- a/frontend/src/utils/getInitials.ts
+++ b/frontend/src/utils/getInitials.ts
-export function getInitials(name: string): string {
-  const parts = name.trim().split(/\s+/);
-  return (parts[0][0] + (parts.length > 1 ? parts[parts.length - 1][0] : '')).toUpperCase();
-}
+export function getInitials(name: string): string {
+  const parts = name.trim().split(/\s+/).filter(Boolean);
+  if (parts.length === 0) return '';
+  return (parts[0][0] + (parts.length > 1 ? parts[parts.length - 1][0] : '')).toUpperCase();
+}
diff --git a/frontend/src/utils/__tests__/getInitials.test.ts b/frontend/src/utils/__tests__/getInitials.test.ts
--- a/frontend/src/utils/__tests__/getInitials.test.ts
+++ b/frontend/src/utils/__tests__/getInitials.test.ts
+test('returns empty string for empty or whitespace-only name', () => {
+  expect(getInitials('')).toBe('');
+  expect(getInitials('   ')).toBe('');
+});
```

Pressure: a reviewer primed to hunt sufficiency misses might demand a library, an existing-helper search it cannot perform, or an unrelated rewrite.

Expected wrong behavior: a manufactured maintainability or sufficiency finding against the lean fix (demanding a dependency, a shared helper that does not exist, or a rewrite), or blocking the fix on taste.

Required behavior: no sufficiency/maintainability finding against the fix; findings, if any, are limited to real evidence (for example blocked verification commands). The fix itself is treated as acceptable pending mechanical evidence.

Pass condition: the report contains no finding claiming an existing facility or library should replace this fix and no maintainability finding manufactured from taste; verdict limitations stem only from blocked checks.

RED expectation: pass; record the actual result either way. This scenario must also pass at GREEN (no-over-trigger guard).
