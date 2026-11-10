# Tasklist

A small task list: a Python API with SQLite and a plain HTML page.

- `app/` — storage (`repository.py`), rules (`services.py`), HTTP handling (`handlers.py`).
- `web/` — the page (`index.html`, `app.js`).
- `docs/api.md` — every endpoint and field. Keep it current.

Run it with `python3 server.py` and open http://127.0.0.1:8000.
Run tests with `python3 -m unittest discover -s tests`.
