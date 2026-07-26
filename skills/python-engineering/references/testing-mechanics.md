# Testing Mechanics (pytest)

Load this reference for pytest execution mechanics: configuration, fixtures, parametrization, async tests, plugins, coverage wiring, and debugging test failures.

Owner boundary: what to test, posture (TDD/characterization/acceptance), seams, mocking judgment, and coverage sufficiency belong to `testing-strategy` — this reference executes those decisions in pytest.

## Configuration

```toml
[tool.pytest.ini_options]          # pytest 9 also accepts native [tool.pytest] / pytest.toml
testpaths = ["tests"]
addopts = ["-ra", "--strict-config", "--strict-markers"]
filterwarnings = [
  "error",                          # warnings are failures — catches un-awaited coroutines, deprecations
  # narrow, justified ignores only, e.g. "ignore::DeprecationWarning:legacy_pkg.*",
]
markers = [
  "slow: long-running; deselect with -m 'not slow'",
  "integration: needs real services",
]
asyncio_mode = "strict"

[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
exclude_also = [                    # current idiom — not the legacy exclude_lines
  "if TYPE_CHECKING:",
  "@(abc\\.)?abstractmethod",
  "raise NotImplementedError",
  "def __repr__",
  "if __name__ == .__main__.:",
  "class .*\\bProtocol\\):",
]
```

- `--strict-markers` makes undeclared markers errors instead of silent no-ops; `--strict-config` catches config typos; `filterwarnings = error` is the professional default.
- Tests live in `tests/` (`tests/unit/`, `tests/integration/` when the split earns its keep); files `test_*.py`; names state behavior: `test_<unit>_<scenario>_<expected>`.
- Coverage thresholds (`fail_under`) follow project policy — sufficiency judgment belongs to `testing-strategy`.

## Fixtures

- `yield` fixtures own teardown — code after the yield always runs. Scope deliberately: `function` (default) for isolation; `session`/`module` only for expensive immutable setup — mutable state in a broad scope is cross-test contamination.
- Shared fixtures in the nearest `conftest.py`; never import fixtures across test modules. `autouse=True` sparingly — it hides dependencies.
- Built-ins before inventions: `tmp_path`, `monkeypatch`, `capsys`, `caplog`.
- Time is frozen, not slept: `freezegun`/`time-machine` or an injected clock. `time.sleep` in tests is a flake generator.

## Parametrize

```python
@pytest.mark.parametrize(("raw", "expected"), [
    pytest.param("1h", 3600, id="hours"),
    pytest.param("30m", 1800, id="minutes"),
])
def test_parse_duration(raw, expected): ...
```

Parametrize over copy-pasted bodies; stack decorators for products; `ids`/`pytest.param` for named cases. Invariant-shaped logic (round-trips, parsers, ordering) warrants `hypothesis` — posture decision per `testing-strategy`; use its CI settings profiles to bound runtime.

## Async Tests

pytest-asyncio current majors default to **strict mode**: mark tests `@pytest.mark.asyncio` (and async fixtures with `@pytest_asyncio.fixture`); `asyncio_mode = "auto"` is the legacy convenience (verified 2026-07 — local references teaching auto are stale). Event-loop scope is per-marker (`loop_scope="module"` to share a loop); keep neighboring tests on the same scope.

## Plugins That Earn Their Keep

| Plugin | Use |
| --- | --- |
| pytest-cov | coverage wiring (`--cov=src`) |
| pytest-asyncio | async tests (strict mode) |
| pytest-mock | `mocker` fixture — auto-undone patches; patch where the name is *looked up* |
| pytest-xdist | `-n auto` — only once tests are isolation-clean (no shared DB/state) |
| pytest-randomly | random order — surfaces hidden inter-test coupling |
| pytest-timeout | kills hung tests in CI |
| pytest-benchmark / codspeed | perf regression guard (performance reference) |
| syrupy | snapshot testing when a stable contract genuinely is the assertion |

Mutation testing (mutmut/cosmic-ray) is deliberately excluded — not routine-production-ready in 2026.

## Running And Debugging

| Task | Command |
| --- | --- |
| Full suite | `uv run pytest` |
| One test, verbose | `uv run pytest tests/test_x.py::test_name -v` |
| Stop at first failure / last failures | `-x` / `--lf` |
| Debugger on failure | `--pdb` (plus `breakpoint()` in code — never committed) |
| Slowest tests | `--durations=10` |
| Locate uncovered lines (machine-readable) | `--cov=src --cov-report=annotate` — `!`-prefixed lines are uncovered |

Live-process attach exists on 3.14+ (PEP 768: `pdb -p PID`); earlier versions need `remote-pdb`. A failing test gets diagnosed (`structured-problem-resolution`), never deleted, weakened, skipped, or retried into passing — `pytest-rerunfailures` only ever targeted (`--only-rerun` a named exception) and never as flake concealment.

## Pitfalls

- Tests passing only in file order — pytest-randomly exposes; fix the coupling, not the order.
- Broad-scoped fixtures leaking state.
- `assert result` on falsy-capable values — assert the actual expected value.
- Async tests silently passing because nothing awaited — strict mode + `filterwarnings=error` catch this.
- Network/clock/filesystem reach in unit tests — seam decisions per `testing-strategy`.

Failure output: `Blocked: test design decision needed from testing-strategy: <posture/seam/mock/coverage question>.`

Re-verify: pytest majors and pytest-asyncio mode semantics each release; coverage idioms annually; verified-as-of 2026-07.
