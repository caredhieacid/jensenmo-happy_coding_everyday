# Architecture

## Decision

HappyCoding Everyday is one automatic dispatcher skill with three internal execution lanes. It replaces competing top-level coding workflows; it does not replace domain standards such as Git safety, backend architecture, observability, or product-specific instructions.

The user provides intent once. The dispatcher owns workflow selection and may call a domain skill or the existing CTO orchestration internally without exposing another required mode to the user.

## Boundaries

The dispatcher owns:

- task contract extraction;
- lane selection and escalation;
- implementation topology;
- verification depth;
- completion evidence.

Repository-local instructions own project conventions. Conditional domain skills own specialized rules. The dispatcher must compose with both and must not override a stricter repository or safety boundary.

## Context strategy

`SKILL.md` contains only the rules needed on every coding turn. Detailed lane and evidence guidance lives under `references/` and is read only when relevant. Everyday work stays in one context. Collaboration delegates bounded read-heavy work and retains a single integration owner. Delivery persists state because the work itself outlives one compact context.

## Escalation philosophy

Everyday is the stable default. Complexity is demonstrated by coupling, independence, blast radius, duration, or acceptance path—not by task prestige or available agent count. Escalation is reversible: a broad investigation can return to Everyday after proving a local cause.

## Unique-entry migration

1. Install or link `skills/jensenmo-happy-coding-everyday` into the Codex skill directory.
2. Keep `policy.allow_implicit_invocation: true`.
3. Disable other implicit skills that own the entire coding lifecycle. Do not delete them if they are still useful as references.
4. Keep CTO orchestration available as a Delivery-only subroutine.
5. Keep Git, backend, observability, browser, and other domain skills conditional.
6. Start a fresh Codex task/session and confirm only this dispatcher appears as the default coding entry.

The exact plugin-disable mechanism is environment-specific. Prefer a supported plugin setting or a reversible move over editing plugin caches.

## Non-goals

- a new agent framework or runtime;
- mandatory multi-agent execution;
- mandatory TDD for files that have no executable behavior or harness;
- a project-management board for routine changes;
- replacing repository-specific engineering rules;
- optimizing agent count as a success metric.
