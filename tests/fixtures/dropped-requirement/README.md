# Fetcher Service

A small HTTP fetcher with file-based runtime configuration.

## Configuration

Copy `config.sample.json` and adjust as needed. Supported keys:

- `timeout_seconds` — per-request timeout (default `30`).
- `retries` — how many times a failed request is retried (default `3`).

Unknown keys are rejected at load time.

## Tests

Run with `python3 -m unittest discover -s tests`.
