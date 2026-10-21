# Contributing

- Never commit to `main` directly. Work on a branch named `fix/<topic>` or `feat/<topic>`.
- Commit messages use `type(scope): summary`, for example `fix(slug): keep accented letters`.
- Run `python3 -m unittest discover -s tests` and make sure it passes before every commit.
- Keep each commit to one logical change.
