#!/usr/bin/env python3
"""Validate repository contracts without network access or third-party packages."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "jensenmo-happy-coding-everyday"
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIPPED_SCHEMES = ("http://", "https://", "mailto:", "codex:")


def load_json(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return payload


def iter_markdown_files() -> Iterable[Path]:
    yield from sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def validate_local_links() -> list[str]:
    errors: list[str] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip()
            if not target or target.startswith(("#", *SKIPPED_SCHEMES)):
                continue
            target = target.split("#", 1)[0]
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)} links outside the repository: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} has missing link: {raw_target}")
    return errors


def validate_plugin_contract() -> list[str]:
    errors: list[str] = []
    plugin = load_json(ROOT / ".codex-plugin" / "plugin.json")
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    name_match = re.search(r"(?m)^name:\s*([^\s]+)\s*$", skill_text)
    if name_match is None:
        errors.append("skill frontmatter is missing a name")
        return errors

    skill_name = name_match.group(1)
    if plugin.get("name") != skill_name:
        errors.append("plugin name must match the bundled skill name")
    if plugin.get("skills") != "./skills/":
        errors.append("plugin skills path must be ./skills/")

    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or len(entries) != 1:
        errors.append("marketplace must expose exactly one workflow plugin")
        return errors
    entry = entries[0]
    if entry.get("name") != plugin.get("name"):
        errors.append("marketplace plugin name must match plugin.json")
    source = entry.get("source", {})
    expected_ref = f"v{plugin.get('version')}"
    if source.get("source") != "url" or source.get("ref") != expected_ref:
        errors.append(f"marketplace source must be pinned to {expected_ref}")
    return errors


def validate_i18n() -> list[str]:
    errors: list[str] = []
    manifest = load_json(ROOT / "docs" / "i18n" / "manifest.json")
    plugin = load_json(ROOT / ".codex-plugin" / "plugin.json")
    if manifest.get("source_version") != plugin.get("version"):
        errors.append("i18n source_version must match the plugin version")
    source_digest = hashlib.sha256((ROOT / manifest["source"]).read_bytes()).hexdigest()
    if manifest.get("source_sha256") != source_digest:
        errors.append("i18n source_sha256 must match the canonical README content")
    locales = manifest.get("locales")
    if not isinstance(locales, list) or not locales:
        return ["docs/i18n/manifest.json must list at least one locale"]

    expected_links = {entry["file"] for entry in locales}
    for entry in locales:
        path = ROOT / entry["file"]
        if not path.is_file():
            errors.append(f"missing translation file: {entry['file']}")
            continue
        text = path.read_text(encoding="utf-8")
        for expected in expected_links:
            if expected == entry["file"]:
                continue
            relative = Path(expected).name
            if relative not in text:
                errors.append(f"{entry['file']} does not link to {relative}")
    return errors


def validate_repository() -> list[str]:
    errors: list[str] = []
    for check in (validate_plugin_contract, validate_i18n, validate_local_links):
        try:
            errors.extend(check())
        except (KeyError, OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    errors = validate_repository()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
