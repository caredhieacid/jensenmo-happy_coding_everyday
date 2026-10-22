import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from invoice import render_invoice


class InvoiceTests(unittest.TestCase):
    def test_dates_are_rendered(self):
        text = render_invoice("INV-1", "Acme", date(2026, 1, 2), date(2026, 2, 3), [("Work", 10.0)])
        self.assertIn("Issued:   2026-01-02", text)
        self.assertIn("Due:      2026-02-03", text)


if __name__ == "__main__":
    unittest.main()
