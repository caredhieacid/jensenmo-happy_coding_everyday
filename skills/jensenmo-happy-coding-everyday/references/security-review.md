# Security review

Use this when the user asks for a security review or audit, and before finishing your own change when it alters how sign-in, sessions, permission checks, secrets, or payments work, or lets request input choose a file, command, or URL. An ordinary field, endpoint, or validation rule does not need it; the security section of the engineering baseline covers those.

A requested review is read-only: report what you find and offer to fix it. For your own change, fix what you find inside the task's scope and report the rest; do not add hardening the task did not ask for.

## How to review

1. List the entry points: every place outside input arrives (routes, handlers, jobs, command-line arguments, uploads, webhooks, model output) and what each one can reach (records, files, commands, other services).
2. Follow the input from each entry point to where it is used. A finding needs that path: who can send what, and what happens as a result.
3. Check each path against the table below.
4. Where it is safe and cheap, confirm a finding with a local call or test on throwaway data. Never probe production or systems that are not the user's.
5. Clear code that only looks risky. A fast hash used for a cache key, a command run with fixed arguments, or a parameterized query is not a finding.

## What to check

| Area | Look for |
| --- | --- |
| Access | Each entry point checks who the caller is and whether the record belongs to them; an ID from the request is never enough on its own; admin and internal paths; access denied when ownership is unknown |
| Injection | Queries, commands, templates, file paths, or regular expressions built from input; `eval`; loading untrusted serialized data; paths that can escape their folder; server-side requests to user-supplied URLs |
| Output | User data written into HTML, attributes, scripts, or URLs without encoding; redirects to user-supplied addresses; error messages that reveal internals |
| Secrets and personal data | Keys in source or client bundles; passwords, tokens, or personal data in logs, URLs, or responses that return more fields than needed |
| Sign-in and sessions | Slow, salted password hashing; random tokens that expire; constant-time comparison; cookie flags; CSRF protection for cookie sessions; wildcard CORS with credentials; limits on sign-in and reset attempts |
| Files | Upload type and size limits; files stored outside the served folder; names chosen by the server |
| Configuration and dependencies | Debug mode, default credentials, disabled TLS verification; packages with known flaws or no maintenance; install scripts fetched without a pinned version |
| LLM features | Instructions hidden in retrieved content; tools with more permission than the task needs; model output used in queries or commands without validation |

## Report

- Findings first, most severe first. For each: severity (critical, high, medium, or low, by what an attacker gains and how easily), file and line, how it could be abused in one or two concrete sentences, and the smallest fix. Say when abuse needs a signed-in user.
- Then, briefly, what you checked and found sound, and what you could not check, such as deployment settings or dependency advisories without network access.
- Leave out advice that is not tied to a line of this code, and do not raise a severity to look thorough.
