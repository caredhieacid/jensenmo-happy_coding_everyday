from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def to_money(value):
    """Convert a number or numeric string to a two-place Decimal."""
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)


def add(*amounts):
    return sum((to_money(amount) for amount in amounts), Decimal("0.00"))
