from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "jensenmo-happy-coding-everyday"


class SkillStructureTests(unittest.TestCase):
    def test_skill_frontmatter_and_name(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        frontmatter = match.group(1)
        self.assertIn("name: jensenmo-happy-coding-everyday", frontmatter)
        description = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
        self.assertIsNotNone(description, "Skill discovery needs a description")
        text = description.group(1).strip("\"\' ")
        self.assertLessEqual(len(text), 1024)
        # Implicit invocation depends on the description naming the coding activities it covers.
        self.assertRegex(text, r"^Use (for|when)\b")
        for trigger in ("editing", "reviewing", "debugging", "committing"):
            self.assertIn(trigger, text)

    def test_implicit_invocation_is_enabled(self):
        text = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('default_prompt: "Use $jensenmo-happy-coding-everyday', text)
        self.assertRegex(text, r"(?m)^\s*allow_implicit_invocation: true$")

    def test_required_references_exist(self):
        for name in ("lanes.md", "contracts-and-evidence.md", "engineering-baseline.md"):
            self.assertTrue((SKILL_DIR / "references" / name).is_file(), name)

    def test_no_scaffold_placeholders(self):
        checked = [SKILL_DIR / "SKILL.md", *SKILL_DIR.glob("references/*.md")]
        for path in checked:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("TODO", text, str(path))
            self.assertNotIn("[TODO", text, str(path))

    def test_skill_stays_compact(self):
        # SKILL.md loads on every coding turn; conditional depth belongs in references/.
        lines = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLessEqual(len(lines), 60)

    def test_every_reference_is_linked_from_skill(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        for path in (SKILL_DIR / "references").glob("*.md"):
            with self.subTest(path=path.name):
                self.assertIn(f"(references/{path.name})", text)

    def test_runtime_skill_has_no_private_markers(self):
        # The skill ships publicly; machine paths and addresses must not leak into it.
        patterns = (
            r"/Users/[^/\s]+",
            r"/home/[^/\s]+",
            r"[A-Za-z]:\\Users\\",
            r"[\w.+-]+@[\w-]+\.[\w.-]+",
        )
        for path in SKILL_DIR.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for pattern in patterns:
                with self.subTest(path=str(path.relative_to(SKILL_DIR)), pattern=pattern):
                    self.assertIsNone(re.search(pattern, text))

    def test_there_is_only_one_skill(self):
        skill_files = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(skill_files, [SKILL_DIR / "SKILL.md"])


if __name__ == "__main__":
    unittest.main()
