"""Final order pricing for the checkout summary."""


def shipping_fee(items):
    weight = sum(item.get("weight", 0.5) * item["qty"] for item in items)
    if weight <= 1.0:
        return 4.50
    return round(4.50 + (weight - 1.0) * 1.25, 2)


def order_summary(items):
    subtotal = round(sum(item["price"] * item["qty"] for item in items), 2)
    shipping = shipping_fee(items)
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "total": round(subtotal + shipping, 2),
    }
