#!/usr/bin/env python3
"""Build a deterministic plugin archive and SHA-256 checksum."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import stat
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "jensenmo-happy-coding-everyday"
INCLUDED_FILES = ("LICENSE", "README.md", "README.zh-CN.md", "CHANGELOG.md")
INCLUDED_DIRS = (".codex-plugin", "skills")
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def plugin_version() -> str:
    manifest = json.loads(
        (ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    return manifest["version"]


def release_files() -> list[Path]:
    paths = [ROOT / name for name in INCLUDED_FILES]
    for directory in INCLUDED_DIRS:
        paths.extend(path for path in (ROOT / directory).rglob("*") if path.is_file())
    return sorted(paths, key=lambda path: path.relative_to(ROOT).as_posix())


def build_archive(output_dir: Path, version: str) -> tuple[Path, Path]:
    expected = plugin_version()
    if version != expected:
        raise ValueError(f"release version {version} does not match plugin version {expected}")

    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{PLUGIN_NAME}-v{version}.zip"
    prefix = f"{PLUGIN_NAME}-{version}"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in release_files():
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{relative}", FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            bundle.writestr(info, path.read_bytes())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = output_dir / f"{archive.name}.sha256"
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    return archive, checksum


def write_metadata(
    output_dir: Path,
    version: str,
    source_ref: str,
    source_sha: str,
    archive: Path,
) -> Path:
    metadata = output_dir / "release-metadata.json"
    payload = {
        "schema_version": 1,
        "plugin": PLUGIN_NAME,
        "version": version,
        "source_ref": source_ref,
        "source_sha": source_sha,
        "archive": archive.name,
        "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
    }
    metadata.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--version", default=plugin_version())
    parser.add_argument("--source-ref")
    parser.add_argument("--source-sha")
    args = parser.parse_args()
    archive, checksum = build_archive(args.output_dir, args.version)
    print(archive)
    print(checksum)
    if bool(args.source_ref) != bool(args.source_sha):
        parser.error("--source-ref and --source-sha must be provided together")
    if args.source_ref and args.source_sha:
        print(
            write_metadata(
                args.output_dir,
                args.version,
                args.source_ref,
                args.source_sha,
                archive,
            )
        )


if __name__ == "__main__":
    main()
