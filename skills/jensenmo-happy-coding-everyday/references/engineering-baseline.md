# Engineering baseline

Sensible defaults for a repository that says nothing stricter. Apply only the sections the task touches, to the code the task changes; do not retrofit untouched code or turn a small fix into a standards migration. Repository instructions, project decision records, and narrower standard skills for the same domain take precedence. When they conflict with each other or with this baseline, name the conflict instead of silently choosing.

## Git

- Commit or push only when asked. Follow the project's documented branch and message rules. Without any: on a repository whose default branch receives changes through pull requests, cut a short-lived branch from a freshly fetched base; a solo local project can commit where the user works.
- One logical change per commit, with a message that says what changed and why. Stage only in-scope files: no secrets, caches, build output, or machine-specific paths.
- Prefer recoverable operations (a new commit, revert, stash) over destructive ones (`reset --hard`, `clean`, branch deletion). Never force-push or rewrite a shared branch; on your own branch use a lease-protected force push.
- Update from the base when it has moved and affects your files, not as a ritual. "Merged", "present on a branch", and "deployed" are separate facts; check each before acting on it.
- A pull request states what changed, why, how it was verified, and what was not.

## Secrets and configuration

- Credentials and internal endpoints never go into source, fixtures, logs, commit messages, documents, or chat output. Read them from the environment or a secret store; keep local secret files git-ignored and offer an example file with placeholder names.
- Check configuration by name, presence, and permission; do not print values to confirm them.
- A secret that reached a commit or a shared log is exposed. Recommend rotating it; rewriting history is a separate, authorized step.
- Pin tool and dependency versions in the repository (lockfile or toolchain file) rather than relying on what one machine has installed.

## Security

- Check authorization, not only authentication, on every new or changed entry point: endpoint, handler, job, or tool. Deny by default when ownership or role cannot be established.
- Never pass untrusted input to `eval`, a shell, a query, or a file path without validation or parameterization; encode output for its context (HTML, SQL, shell, URL).
- Do not disable TLS verification, CSRF protection, authentication, or security headers to make something work; fix the configuration instead.
- Give tokens, roles, and containers the least privilege the task needs.

## Data and migrations

- Schema and data changes go through explicit, versioned migrations. Keep old and new code compatible while a rollout is in progress, and know the rollback or forward-fix path before running one against shared data.
- Keep transactions and locks short; never hold one across a network, LLM, or other slow call.
- Use server-side increments or conditional updates for concurrent writes instead of read-modify-write. Release connections on every path, including reads and errors.
- Deleting or overwriting shared data needs a backup or idempotent design, plus authorization for the actual target.
- Bound queries and lists that can grow: paginate or limit them, and avoid one query per item inside a loop.

## Interfaces and errors

- Validate untrusted input once at the boundary; use parameterized queries and commands.
- Keep public API, CLI, file-format, and event contracts backward compatible; make changes additive and announce removals before making them. If a break is necessary, say so and update known consumers.
- Give every external call a timeout. Retry only retryable errors, with a cap and backoff, and only for idempotent operations.
- Handle an error or propagate it; do not log it and rethrow it as well. Messages a person sees say what to do next.
- Cache only with a TTL and an invalidation tied to the write path; do not cache authorization decisions, money, or reservable stock.

## Logging and observability

- Log a stable event name with variables as structured fields, not sentences assembled from strings. Redact secrets and personal data before logs leave the process.
- INFO should be enough to reconstruct what happened; DEBUG holds detail. Control levels through configuration.
- Propagate trace context across process and async boundaries when the service already uses tracing.

## Dependencies

- Prefer the standard library and the existing stack. Add a dependency only when it clearly pays for itself, through the project's package manager and lockfile. Do not upgrade unrelated packages.

## Environment and setup

- Use the project's documented setup and run commands. Install dependencies into the project's own environment (virtualenv, local packages, version manager) with its package manager and lockfile; ask before global or `sudo` installs.
- When setup is missing or broken, report the exact failing command and the fix. Do not change toolchain or package versions, or switch package managers, just to make a check pass.

## Frontend and UI

- Reuse the project's components and design tokens; do not add arbitrary colors and sizes or a second component library.
- Do not hand-edit generated API clients; change the contract and regenerate them.
- Keep type checking meaningful: do not silence errors with `any`, casts, or suppression comments.
- Check UI changes in the running interface, including the loading, empty, and error states the change affects. Widen the check when shared or global styles change.

## LLM and agent features

- Start with the simplest form that works: one model call, then a fixed workflow, and an agent loop only when measurement shows it is needed.
- Every loop has a checkable stop condition, an iteration cap, and a cost or token budget.
- Treat model output as untrusted input: validate its structure and give tools least privilege, timeouts, and limits before acting on it.
- Return short, actionable tool errors to the model. Judge prompt or tool changes on a small set of real cases, grading the output rather than the steps.
- Do not log raw prompts or user content by default.

## Tests, checks, and docs

- Add a focused regression test when the project has a harness; do not introduce a framework for one fix.
- Never make a check pass by weakening it: no deleted or skipped tests, `|| true`, or loosened assertions. Fix or quarantine a flaky test instead of retrying it.
- Keep tests deterministic: control time, randomness, and network.
- A check reports; it does not rewrite files. A newly added gate should be seen failing once before you rely on it.
- Update docs that describe changed behavior in the same change. Do not document a command you have not run unless you mark it as unverified.
