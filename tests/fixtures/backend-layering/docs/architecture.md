# Architecture

Requests flow handler → service → repository. See ADR 0001.

## Endpoints

| Method | Path | Handler | Description |
| --- | --- | --- | --- |
| GET | `/projects/{id}/tasks` | `list_tasks` | Tasks of a project, newest first |
