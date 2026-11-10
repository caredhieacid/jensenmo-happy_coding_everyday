import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.app import handle
from reports.export import export_accounts


class PortalTests(unittest.TestCase):
    def test_internal_call_with_token_is_accepted(self):
        self.assertEqual(handle({"Authorization": "Bearer tok-ana"}, via_gateway=False), (200, "ana"))

    def test_unknown_token_is_rejected(self):
        self.assertEqual(handle({"Authorization": "Bearer nope"}, via_gateway=False)[0], 401)

    def test_export_has_one_line_per_account(self):
        text = export_accounts([{"id": 1, "email": "a@example.com", "created": "2026-01-02"}])
        self.assertEqual(len(text.strip().splitlines()), 2)


if __name__ == "__main__":
    unittest.main()
