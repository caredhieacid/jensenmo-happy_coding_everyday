import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from money import add, to_money


class MoneyTests(unittest.TestCase):
    def test_to_money_rounds_half_up(self):
        self.assertEqual(to_money("2.345"), Decimal("2.35"))

    def test_add_sums_amounts(self):
        self.assertEqual(add("1.10", 2, "0.05"), Decimal("3.15"))


if __name__ == "__main__":
    unittest.main()
