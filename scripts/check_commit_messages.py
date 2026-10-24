#!/usr/bin/env python3
"""Reject AI attribution lines in commit messages and pull request text.

AI tools often append "Co-authored-by: <tool>" or "Generated with <tool>" lines. GitHub then
lists the tool as a contributor, which this repository does not allow.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from typing import Iterator


AI_NAMES = (
    r"(cursor|cursoragent|claude|anthropic|openai|codex|chatgpt|copilot|devin|gemini|windsurf|"
    r"codeium|aider|cline)"
)
PATTERNS = (
    re.compile(rf"^\s*co-authored-by:.*\b{AI_NAMES}\b", re.IGNORECASE),
    re.compile(r"generated with \[?(claude code|codex|cursor|copilot|chatgpt)\b", re.IGNORECASE),
)


def find_violations(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if any(p.search(line) for p in PATTERNS)]


def commit_messages(rev_range: str) -> Iterator[tuple[str, str]]:
    output = subprocess.run(
        ["git", "log", "--format=%H%x00%B%x01", rev_range],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    for record in output.split("\x01"):
        if record.strip():
            sha, _, body = record.strip().partition("\x00")
            yield sha, body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("range", nargs="?", help="git revision range, such as BASE..HEAD")
    parser.add_argument(
        "--text-env",
        action="append",
        default=[],
        help="environment variable whose text is also checked, such as a PR description",
    )
    args = parser.parse_args()

    found: list[str] = []
    if args.range:
        for sha, body in commit_messages(args.range):
            found.extend(f"commit {sha[:7]}: {line}" for line in find_violations(body))
    for name in args.text_env:
        found.extend(f"{name}: {line}" for line in find_violations(os.environ.get(name, "")))

    if found:
        print("Remove AI attribution lines:")
        for item in found:
            print(f"- {item}")
        return 1
    print("No AI attribution lines found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
