import csv
import io


def export_accounts(accounts):
    """CSV text for the accounts list."""
    buffer = io.StringIO()
    columns = sorted(accounts[0].keys()) if accounts else []
    writer = csv.DictWriter(buffer, fieldnames=columns)
    writer.writeheader()
    writer.writerows(accounts)
    return buffer.getvalue()
