# Notes service

A small notes API. Each user sees and edits only their own notes.

- `app/auth.py` — accounts, password hashing, session tokens.
- `app/handlers.py` — request handlers.
- `app/db.py` — SQLite schema and connection.

Run tests with `python3 -m unittest discover -s tests`.
