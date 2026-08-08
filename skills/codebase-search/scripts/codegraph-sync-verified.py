#!/usr/bin/env python3

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys


SYNC_PROGRAM = r"""
import { pathToFileURL } from "node:url";

const modulePath = process.argv[1];
const projectRoot = process.argv[2];
let graph;

try {
  const namespace = await import(pathToFileURL(modulePath).href);
  const CodeGraph = namespace.CodeGraph ?? namespace.default?.default ?? namespace.default;
  if (typeof CodeGraph?.open !== "function") {
    throw new Error("resolved module does not expose CodeGraph.open");
  }

  graph = await CodeGraph.open(projectRoot);
  const result = await graph.sync();
  if (result.filesChecked === 0 && result.durationMs === 0) {
    console.error(
      "CodeGraph freshness not proven: sync did not acquire the index lock " +
      "(filesChecked=0, durationMs=0)."
    );
    process.exitCode = 3;
  } else {
    console.log(JSON.stringify({ freshnessVerified: true, sync: result }));
  }
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`CodeGraph verified sync failed: ${message}`);
  process.exitCode = 1;
} finally {
  try {
    graph?.destroy();
  } catch {
    // The sync result already determines the command outcome.
  }
}
"""


def _find_codegraph_executable() -> Path:
    executable = shutil.which("codegraph")
    if executable is None:
        raise RuntimeError("codegraph executable was not found on PATH")
    return Path(executable).resolve()


def _module_candidates(executable: Path) -> list[Path]:
    candidates: list[Path] = []
    current = executable.parent

    for _ in range(7):
        candidates.extend(
            [
                current / "lib" / "dist" / "index.js",
                current / "dist" / "index.js",
                current / "index.js",
            ]
        )
        if current.parent == current:
            break
        current = current.parent

    npm = shutil.which("npm")
    if npm is not None:
        try:
            completed = subprocess.run(
                [npm, "root", "-g"],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
            if completed.returncode == 0 and completed.stdout.strip():
                candidates.append(
                    Path(completed.stdout.strip())
                    / "@colbymchenry"
                    / "codegraph"
                    / "dist"
                    / "index.js"
                )
        except subprocess.TimeoutExpired:
            pass

    return candidates


def _find_codegraph_module(executable: Path) -> Path:
    for candidate in _module_candidates(executable):
        if candidate.is_file():
            return candidate.resolve()
    raise RuntimeError(
        "could not resolve the installed @colbymchenry/codegraph library "
        f"from executable {executable}"
    )


def _find_node_runtime(executable: Path) -> Path:
    current = executable.parent
    for _ in range(7):
        candidate = current / ("node.exe" if os.name == "nt" else "node")
        if candidate.is_file():
            return candidate.resolve()
        if current.parent == current:
            break
        current = current.parent

    node = shutil.which("node")
    if node is None:
        raise RuntimeError("Node.js runtime was not found")
    return Path(node).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a CodeGraph filesystem sync and reject its lock-failure sentinel."
    )
    parser.add_argument(
        "--project-root",
        required=True,
        help="Repository root containing the initialized CodeGraph project.",
    )
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    if not project_root.is_dir():
        print(
            f"CodeGraph verified sync failed: project root is not a directory: {project_root}",
            file=sys.stderr,
        )
        return 1

    try:
        executable = _find_codegraph_executable()
        module = _find_codegraph_module(executable)
        node = _find_node_runtime(executable)
    except RuntimeError as error:
        print(f"CodeGraph verified sync failed: {error}", file=sys.stderr)
        return 1

    child_environment = os.environ.copy()
    child_environment["CODEGRAPH_TELEMETRY"] = "0"

    completed = subprocess.run(
        [
            str(node),
            "--liftoff-only",
            "--disable-warning=ExperimentalWarning",
            "--input-type=module",
            "-e",
            SYNC_PROGRAM,
            str(module),
            str(project_root),
        ],
        check=False,
        env=child_environment,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
