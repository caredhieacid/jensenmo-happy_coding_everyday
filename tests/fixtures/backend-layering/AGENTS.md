# Agent instructions

- Layers: `app/handlers.py` parses requests and shapes responses; `app/services.py` owns business rules; `app/repository.py` owns all SQL. Handlers never touch SQL, and repositories never apply business rules.
- Every endpoint is listed in `docs/architecture.md`. Keep that list current in the same change.
- Architectural decisions (new datastore, service, protocol, or cross-layer dependency) need a record in `docs/adr/`. Routine endpoints do not.
- Gate before every commit: `python3 -m unittest discover -s tests`.
