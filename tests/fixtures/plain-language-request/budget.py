import csv
import sys


def load_expenses(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def total_spent(rows):
    total = 0.0
    for i in range(1, len(rows)):
        total += float(rows[i]["amount"])
    return total


def main():
    if len(sys.argv) != 2:
        print("usage: python3 budget.py expenses.csv")
        sys.exit(1)
    rows = load_expenses(sys.argv[1])
    print(f"You spent {total_spent(rows):.2f} in total.")


if __name__ == "__main__":
    main()
