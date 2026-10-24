import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_commit_messages", ROOT / "scripts" / "check_commit_messages.py"
)
check_commit_messages = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_commit_messages)


class CommitMessageTests(unittest.TestCase):
    def test_ai_attribution_lines_are_found(self):
        for line in (
            "Co-authored-by: Cursor <cursoragent@cursor.com>",
            "Co-Authored-By: Claude Opus <noreply@anthropic.com>",
            "co-authored-by: Copilot <copilot@github.com>",
            "Generated with [Claude Code](https://claude.com/claude-code)",
        ):
            with self.subTest(line=line):
                message = f"fix: keep digits in slugs\n\n{line}\n"
                self.assertEqual(check_commit_messages.find_violations(message), [line])

    def test_human_co_authors_and_plain_messages_pass(self):
        message = (
            "feat: add open task count endpoint\n\n"
            "Counts open tasks per project.\n"
            "Co-authored-by: Ana Lee <ana@example.com>\n"
        )
        self.assertEqual(check_commit_messages.find_violations(message), [])


if __name__ == "__main__":
    unittest.main()
