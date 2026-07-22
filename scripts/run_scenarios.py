#!/usr/bin/env python3
"""Run behavior scenarios against a fresh Codex context for human grading.

Each run copies a disposable fixture repository, executes ``codex exec`` inside
it with only the scenario prompt, and writes distilled evidence plus a grading
checklist under ``.scenario-runs/``. The runner never marks a scenario as
passed: per docs/evaluation-methodology.md a pass requires a reviewer to check
the recorded evidence against every invariant.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCENARIO_DIR = ROOT / "tests" / "scenarios"
FIXTURE_DIR = ROOT / "tests" / "fixtures"
RUN_DIR = ROOT / ".scenario-runs"


def load_scenarios(only: list[str]) -> list[dict]:
    scenarios = []
    for path in sorted(SCENARIO_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if only and data["id"] not in only:
            continue
        scenarios.append(data)
    missing = set(only) - {s["id"] for s in scenarios}
    if missing:
        raise SystemExit(f"unknown scenario ids: {', '.join(sorted(missing))}")
    return scenarios


def prepare_workspace(scenario_id: str, run_dir: Path) -> Path | None:
    fixture = FIXTURE_DIR / scenario_id
    if not fixture.is_dir():
        return None
    workspace = run_dir / "workspace"
    shutil.copytree(fixture, workspace)
    subprocess.run(
        ["git", "init", "--quiet", "--initial-branch=main"], cwd=workspace, check=True
    )
    subprocess.run(["git", "add", "-A"], cwd=workspace, check=True)
    subprocess.run(
        ["git", "-c", "user.email=eval@example.invalid", "-c", "user.name=eval",
         "commit", "--quiet", "-m", "fixture baseline"],
        cwd=workspace,
        check=True,
    )
    return workspace


def write_checklist(scenario: dict, run_dir: Path) -> None:
    lines = [
        f"# Grading checklist: {scenario['id']}",
        "",
        f"Pressure: {scenario['pressure']}",
        f"Acceptable lanes: {', '.join(scenario['expected_lanes'])}",
        "",
        "Score each item pass / fail / not observable, with primary evidence.",
        "",
        "## Invariants",
        "",
    ]
    lines += [f"- [ ] {item}" for item in scenario["expected_invariants"]]
    lines += ["", "## Forbidden (any occurrence is a blocking failure)", ""]
    lines += [f"- [ ] {item}" for item in scenario["forbidden_behaviors"]]
    lines += [
        "",
        "## Record",
        "",
        "- date / model / skill commit:",
        "- selected lane:",
        "- user questions or interruptions:",
        "- files or external state changed (see workspace diff):",
        "- verification commands and results:",
        "- verdict and remaining uncertainty:",
        "",
    ]
    (run_dir / "checklist.md").write_text("\n".join(lines), encoding="utf-8")


def run_scenario(scenario: dict, codex_bin: str, dry_run: bool) -> Path:
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RUN_DIR / f"{stamp}-{scenario['id']}"
    run_dir.mkdir(parents=True)
    (run_dir / "prompt.txt").write_text(scenario["prompt"] + "\n", encoding="utf-8")
    write_checklist(scenario, run_dir)

    workspace = prepare_workspace(scenario["id"], run_dir)
    if workspace is None:
        (run_dir / "SKIPPED.txt").write_text(
            f"No fixture at tests/fixtures/{scenario['id']}/ — add one before running.\n",
            encoding="utf-8",
        )
        print(f"[skip] {scenario['id']}: no fixture repository")
        return run_dir

    command = [
        codex_bin,
        "exec",
        "--sandbox",
        "workspace-write",
        "--output-last-message",
        str(run_dir / "last-message.md"),
        scenario["prompt"],
    ]
    (run_dir / "command.txt").write_text(" ".join(command) + "\n", encoding="utf-8")
    if dry_run:
        print(f"[dry-run] {scenario['id']}: {' '.join(command)}")
        return run_dir

    with (run_dir / "session.log").open("w", encoding="utf-8") as log:
        result = subprocess.run(command, cwd=workspace, stdout=log, stderr=log)
    diff = subprocess.run(
        ["git", "diff"], cwd=workspace, capture_output=True, text=True
    )
    (run_dir / "workspace.diff").write_text(diff.stdout, encoding="utf-8")
    status = "done" if result.returncode == 0 else f"exit {result.returncode}"
    print(f"[{status}] {scenario['id']}: grade {run_dir.relative_to(ROOT)}/checklist.md")
    return run_dir


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ids", nargs="*", help="scenario ids to run (default: all)")
    parser.add_argument("--codex-bin", default="codex", help="codex executable")
    parser.add_argument(
        "--dry-run", action="store_true", help="prepare evidence folders without invoking codex"
    )
    args = parser.parse_args()

    if not args.dry_run and shutil.which(args.codex_bin) is None:
        raise SystemExit(f"codex executable not found: {args.codex_bin}")

    for scenario in load_scenarios(args.ids):
        run_scenario(scenario, args.codex_bin, args.dry_run)
    print("Runs are evaluation inputs; a scenario passes only after human grading.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
