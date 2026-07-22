#!/usr/bin/env python3
"""Verify a release candidate without executing code from the tagged commit."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile


TAG_RE = re.compile(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
PLUGIN_NAME = "jensenmo-happy-coding-everyday"


def verify(dist: Path, expected_sha: str) -> tuple[str, str]:
    metadata = json.loads((dist / "release-metadata.json").read_text(encoding="utf-8"))
    if metadata.get("schema_version") != 1:
        raise ValueError("unsupported release metadata schema")
    if metadata.get("plugin") != PLUGIN_NAME:
        raise ValueError("release metadata names the wrong plugin")
    if metadata.get("source_sha") != expected_sha:
        raise ValueError("release metadata SHA does not match the triggering workflow")

    source_ref = metadata.get("source_ref", "")
    match = TAG_RE.fullmatch(source_ref)
    if match is None:
        raise ValueError("release source ref must be a strict vMAJOR.MINOR.PATCH tag")
    version = source_ref[1:]
    if metadata.get("version") != version:
        raise ValueError("release metadata version does not match its tag")

    archive = dist / metadata.get("archive", "")
    expected_archive = f"{PLUGIN_NAME}-v{version}.zip"
    if archive.name != expected_archive or not archive.is_file():
        raise ValueError("release archive name or path is invalid")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    if metadata.get("archive_sha256") != digest:
        raise ValueError("release archive digest does not match metadata")

    checksum = dist / f"{archive.name}.sha256"
    if checksum.read_text(encoding="utf-8") != f"{digest}  {archive.name}\n":
        raise ValueError("release checksum file is invalid")

    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        for name in names:
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError("release archive contains an unsafe path")
        manifest_names = [name for name in names if name.endswith("/.codex-plugin/plugin.json")]
        if len(manifest_names) != 1:
            raise ValueError("release archive must contain exactly one plugin manifest")
        manifest = json.loads(bundle.read(manifest_names[0]))
    if manifest.get("name") != PLUGIN_NAME or manifest.get("version") != version:
        raise ValueError("archived plugin manifest does not match release metadata")
    return source_ref, expected_sha


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--expected-sha", required=True)
    args = parser.parse_args()
    try:
        source_ref, source_sha = verify(args.dist, args.expected_sha)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"Release candidate verification failed: {exc}", file=sys.stderr)
        return 1
    print(f"Release candidate verified: {source_ref} at {source_sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
