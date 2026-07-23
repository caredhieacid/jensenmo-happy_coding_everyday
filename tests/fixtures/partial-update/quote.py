"""Running cart estimate for the cart preview page."""


def estimate_shipping(cart_items):
    weight = sum(item.get("weight", 0.5) * item["qty"] for item in cart_items)
    if weight <= 1.0:
        return 4.50
    return round(4.50 + (weight - 1.0) * 1.25, 2)


def cart_preview(cart_items):
    subtotal = round(sum(item["price"] * item["qty"] for item in cart_items), 2)
    shipping = estimate_shipping(cart_items)
    return {
        "subtotal": subtotal,
        "estimated_shipping": shipping,
        "estimated_total": round(subtotal + shipping, 2),
    }
