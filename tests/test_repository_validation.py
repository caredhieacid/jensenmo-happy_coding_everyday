import importlib.util
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validate_repository = load_script("validate_repository.py")
package_release = load_script("package_release.py")
verify_release_candidate = load_script("verify_release_candidate.py")


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_contracts(self):
        self.assertEqual(validate_repository.validate_repository(), [])

    def test_plugin_manifest_matches_skill(self):
        manifest = json.loads(
            (ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["name"], "jensenmo-happy-coding-everyday")
        self.assertEqual(manifest["skills"], "./skills/")

    def test_release_archive_contains_installable_plugin(self):
        with tempfile.TemporaryDirectory() as directory:
            archive, checksum = package_release.build_archive(
                Path(directory), package_release.plugin_version()
            )
            self.assertTrue(checksum.is_file())
            with zipfile.ZipFile(archive) as bundle:
                names = bundle.namelist()
            prefix = (
                f"{package_release.PLUGIN_NAME}-{package_release.plugin_version()}"
            )
            self.assertIn(f"{prefix}/.codex-plugin/plugin.json", names)
            self.assertIn(f"{prefix}/LICENSE", names)
            self.assertIn(
                f"{prefix}/skills/jensenmo-happy-coding-everyday/SKILL.md", names
            )

    def test_release_archive_is_deterministic(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            archive_one, _ = package_release.build_archive(
                Path(first), package_release.plugin_version()
            )
            archive_two, _ = package_release.build_archive(
                Path(second), package_release.plugin_version()
            )
            digest_one = hashlib.sha256(archive_one.read_bytes()).hexdigest()
            digest_two = hashlib.sha256(archive_two.read_bytes()).hexdigest()
            self.assertEqual(digest_one, digest_two)

    def test_release_candidate_metadata_matches_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            version = package_release.plugin_version()
            archive, _ = package_release.build_archive(output, version)
            package_release.write_metadata(
                output,
                version,
                f"v{version}",
                "a" * 40,
                archive,
            )
            self.assertEqual(
                verify_release_candidate.verify(output, "a" * 40),
                (f"v{version}", "a" * 40),
            )


if __name__ == "__main__":
    unittest.main()
