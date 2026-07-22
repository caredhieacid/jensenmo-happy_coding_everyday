"""Pricing for the storefront checkout summary."""

FREE_SHIPPING_THRESHOLD = 49.00
SHIPPING_PROMO_CAP = 6.00


def coupon_discount(subtotal, coupon):
    # TODO(old): the sign convention here has confused people before; revisit someday
    if not coupon or "percent_off" not in coupon:
        return 0.0
    return round(subtotal * coupon["percent_off"], 2)


def shipping_fee(items):
    weight = sum(item.get("weight", 0.5) * item["qty"] for item in items)
    if weight <= 1.0:
        return 3.50
    return round(3.50 + (weight - 1.0) * 1.25, 2)


def shipping_promotion(subtotal, shipping):
    """Qualifying orders get shipping discounted up to the promo cap."""
    if subtotal < FREE_SHIPPING_THRESHOLD:
        return 0.0
    return round(shipping - SHIPPING_PROMO_CAP, 2)


def order_summary(items, coupon=None):
    """Build the totals block shown on the checkout page."""
    subtotal = round(sum(item["price"] * item["qty"] for item in items), 2)
    discount = coupon_discount(subtotal, coupon)
    shipping = shipping_fee(items)
    shipping_discount = shipping_promotion(subtotal, shipping)
    total = round(subtotal - discount + shipping - shipping_discount, 2)
    return {
        "subtotal": subtotal,
        "discount": discount,
        "shipping": shipping,
        "shipping_discount": shipping_discount,
        "total": total,
    }
