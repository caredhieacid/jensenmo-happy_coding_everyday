import unittest

from pricing import order_summary, shipping_fee


class PricingTests(unittest.TestCase):
    def test_light_order_flat_shipping(self):
        items = [{"price": 12.00, "qty": 1, "weight": 0.4}]
        summary = order_summary(items)
        self.assertEqual(summary["shipping"], 4.50)
        self.assertEqual(summary["total"], 16.50)

    def test_heavy_order_shipping_scales_with_weight(self):
        items = [{"price": 5.00, "qty": 4, "weight": 1.0}]
        self.assertEqual(shipping_fee(items), 8.25)


if __name__ == "__main__":
    unittest.main()
