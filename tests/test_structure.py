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
        self.assertRegex(frontmatter, r'description: ["\']?Use when')
        self.assertIn("automatic and sole coding-workflow entrance", frontmatter)

    def test_implicit_invocation_is_enabled(self):
        text = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('default_prompt: "Use $jensenmo-happy-coding-everyday', text)
        self.assertRegex(text, r"(?m)^\s*allow_implicit_invocation: true$")

    def test_required_references_exist(self):
        for name in ("lanes.md", "contracts-and-evidence.md"):
            self.assertTrue((SKILL_DIR / "references" / name).is_file(), name)

    def test_no_scaffold_placeholders(self):
        checked = [SKILL_DIR / "SKILL.md", *SKILL_DIR.glob("references/*.md")]
        for path in checked:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("TODO", text, str(path))
            self.assertNotIn("[TODO", text, str(path))

    def test_there_is_only_one_skill(self):
        skill_files = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(skill_files, [SKILL_DIR / "SKILL.md"])


if __name__ == "__main__":
    unittest.main()
