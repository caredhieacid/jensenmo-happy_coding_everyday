# Accounts portal

- `gateway/proxy.py` — forwards browser requests to the backend.
- `backend/auth.py` — checks the session token on every request.
- `reports/export.py` — CSV export of accounts. Columns, in order: `id`, `email`, `created`.

Run tests with `python3 -m unittest discover -s tests`.
