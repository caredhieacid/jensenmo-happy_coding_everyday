# Engineering baseline

Sensible defaults for a repository that says nothing stricter. Apply only the sections the task touches, to the code the task changes; do not retrofit untouched code or turn a small fix into a standards migration. Repository instructions, project decision records, and narrower standard skills for the same domain take precedence. When they conflict with each other or with this baseline, name the conflict instead of silently choosing.

## Git

- Commit or push only when asked. Follow the project's documented branch and message rules. Without any: on a repository whose default branch receives changes through pull requests, cut a short-lived branch from a freshly fetched base; a solo local project can commit where the user works.
- One logical change per commit, with a message that says what changed and why. Stage only in-scope files: no secrets, caches, build output, or machine-specific paths.
- Prefer recoverable operations (a new commit, revert, stash) over destructive ones (`reset --hard`, `clean`, branch deletion). Never force-push or rewrite a shared branch; on your own branch use a lease-protected force push.
- Update from the base when it has moved and affects your files, not as a ritual. "Merged", "present on a branch", and "deployed" are separate facts; check each before acting on it.
- A pull request states what changed, why, how it was verified, and what was not.

## Repository structure and governance

- Before adding backend or shared code, read the repository's architecture notes, decision records, and module docs for the area. Place code in the layer and module they assign (for example handler, service, repository), follow the nearest existing example of the same kind, and extend existing components instead of creating parallel ones.
- Keep documented inventories current in the same change: endpoint lists, module responsibilities, configuration keys, and runbooks that the change affects.
- A new architectural decision (a datastore, service, protocol, cross-module dependency, or a deviation from a recorded decision) gets a short decision record where the repository keeps them, or a question to the user if it keeps none. Supersede old records instead of rewriting them. Routine changes need no record.
- When docs and code disagree, report the conflict instead of silently choosing one.
- Run the repository's documented gate (format, lint, types, tests) before a commit; do not weaken or skip it.

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

- Make new UI look like the product, not a template: reuse its components, tokens, spacing, type scale, layout, and navigation, and match the density and alignment of neighboring screens. Do not add arbitrary colors, fonts, radii, shadows, or a second component library.
- Unless the project already uses them or the user asks, avoid the marks of generated UI: decorative gradients, glows, or glass effects; emoji or icons used as decoration; a hero, banner, or illustration nobody requested; a card around every block; oversized radii and stacked shadows; pill badges and "New" or "Pro" labels; placeholder statistics, testimonials, or logos; centered marketing layouts; and motion that does not communicate state.
- Write interface copy in the words the product already uses: short, specific, and calm, with no hype, exclamation marks, filler, jargon, or invented terms. Give each thing one name, in the interface's language, everywhere it appears: navigation, page title, labels, buttons, and messages.
- Add headings, subheadings, and helper text only where neighboring screens have them; a short form usually needs none. Keep notes for developers off the page: caveats about unfinished parts, disclaimers, and "please note" text belong in your report, not the UI. Use real labels and data shapes; when real content is missing, use neutral placeholders and mention them in the report.
- Build only the screens, controls, and states the task needs; ask before adding settings, sections, or variants (such as a dark theme) that nobody requested. Handle the loading, empty, and error states the change actually introduces, without decorative empty-state art.
- Keep controls accessible: labels tied to inputs, visible keyboard focus, and native elements before custom widgets.
- Do not hand-edit generated API clients; change the contract and regenerate them. Keep type checking meaningful: do not silence errors with `any`, casts, or suppression comments.
- Check UI changes in the running interface when a browser is available, including affected states. Widen the check when shared or global styles change.

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
- Update docs that describe changed behavior in the same change, and add no other docs. Do not document a command you have not run unless you mark it as unverified.
