from datetime import date

DATE_FORMAT = "%Y-%m-%d"


def format_date(value):
    return value.strftime(DATE_FORMAT)


def render_invoice(number, customer, issued, due, lines):
    total = sum(amount for _, amount in lines)
    rows = [f"  {item:<24}{amount:>10.2f}" for item, amount in lines]
    return "\n".join(
        [
            f"Invoice {number}",
            f"Customer: {customer}",
            f"Issued:   {format_date(issued)}",
            f"Due:      {format_date(due)}",
            "",
            *rows,
            f"  {'Total':<24}{total:>10.2f}",
        ]
    )


if __name__ == "__main__":
    print(render_invoice("INV-1042", "Northwind GmbH", date(2026, 10, 1), date(2026, 10, 31),
                         [("Consulting", 1200.0), ("Travel", 180.5)]))
