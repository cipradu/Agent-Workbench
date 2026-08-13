# Efficiency and Concurrency

Use this reference for requests about workflow duration, queue delay, runner minutes or cost, caching, matrices, path filters, duplicate work, or concurrency cancellation.

## Measure The Actual Constraint

Collect repository evidence before changing YAML:

- duration and billed runner minutes by workflow, job, event, ref, runner, and matrix cell;
- queue time separately from execution time;
- cache hit, restore, save, and invalidation behavior;
- failure, retry, rerun, flaky, and platform-exclusive failure rates;
- duplicated work across events, jobs, or workflows;
- supported-platform policy and required-check configuration;
- migration, release, security, compliance, and compatibility gate ownership;
- overlap patterns and which runs are safe to supersede.

Distinguish PR wall-clock latency, queue time, total runner minutes/cost, and duplicated computation. Improving one can worsen another.

## Preserve Acceptance Coverage

Never remove a platform, matrix cell, migration check, release packaging check, or required gate because it is expensive without its owner's evidence that the coverage is redundant or no longer required. Path filters must route relevant changes to their required checks; ignoring migration or release paths can suppress the exact validation those paths require.

Candidate mechanisms remain evidence-contingent: cache only stable dependency inputs, split or combine jobs based on measured setup/parallelism cost, use path routing that preserves required gates, and reduce a matrix only after compatibility ownership changes.

## Concurrency Identity

A concurrency key must encode enough workflow, task, ref, pull request, environment, or release identity to prevent unrelated cancellation. A repository-wide group can cause one branch, workflow, migration, or release run to cancel another.

Use `cancel-in-progress` only where policy says a newer run fully supersedes the older one. Release, deployment, migration, or other non-idempotent runs usually require independent completion or a stronger serialized-state design.

## Decision Output

Report the metric being optimized, measured waste, coverage constraints, candidate change, expected effect, rollback signal, and proof needed after an authorized change. With no evidence, give a read-only decision and collect-list; do not change YAML or claim savings.

Failure output: `Blocked: workflow optimization lacks evidence or compatible gate policy: <metric/gate/concurrency identity>.`
