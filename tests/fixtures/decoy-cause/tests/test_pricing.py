import unittest

from pricing import order_summary, shipping_fee


class PricingTests(unittest.TestCase):
    def test_small_order_pays_full_shipping(self):
        items = [{"price": 12.00, "qty": 1, "weight": 0.4}]
        summary = order_summary(items)
        self.assertEqual(summary["subtotal"], 12.00)
        self.assertEqual(summary["shipping"], 3.50)
        self.assertEqual(summary["shipping_discount"], 0.0)
        self.assertEqual(summary["total"], 15.50)

    def test_percent_coupon_reduces_total(self):
        items = [{"price": 20.00, "qty": 2, "weight": 0.5}]
        summary = order_summary(items, coupon={"percent_off": 0.10})
        self.assertEqual(summary["discount"], 4.00)
        self.assertEqual(summary["total"], 39.50)

    def test_heavy_order_shipping_scales_with_weight(self):
        items = [{"price": 5.00, "qty": 4, "weight": 1.0}]
        self.assertEqual(shipping_fee(items), 7.25)


if __name__ == "__main__":
    unittest.main()
