# API

| Method | Path | Body | Response |
| --- | --- | --- | --- |
| GET | `/api/tasks` | — | `{"tasks": [{"id", "title", "done"}]}`, newest first |
| POST | `/api/tasks` | `{"title"}` | `201` with the created task; `400` with `{"error"}` when the title is blank |
