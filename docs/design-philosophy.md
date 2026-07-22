# Design Philosophy

## The problem is duplicate ownership

Planning, test-driven development, code review, multi-agent orchestration, Git safety, and release
engineering are all useful. The failure mode appears when several automatic workflows each believe
they own the complete coding lifecycle. The user then pays for duplicated questions, plans, review
loops, context, and handoffs.

HappyCoding makes one dispatcher responsible for task shape and lets conditional domain standards
remain responsible for their own expertise.

## One entrance, three amounts of rigor

The three lanes are not status levels and they do not measure task prestige.

- **Everyday** is the stable default for one bounded outcome.
- **Collaboration** protects the main context when work can be partitioned independently.
- **Delivery** carries state and gates when failure, coordination, or acceptance becomes durable.

The lane follows the cheapest evidence that proves what the task really is. Multiple files do not
prove independent work. A pull request does not prove release risk. A high-profile feature does not
prove that more agents will help.

## The four-field contract

Every task can be compressed into:

- **Goal** — the observable outcome;
- **Scope** — the code, systems, environments, or artifacts in play;
- **Acceptance** — the behavior and evidence required for completion;
- **Exclusions** — explicit boundaries and likely scope traps.

For a small task this contract remains internal and conversational. Persisting a document is useful
only when work must survive multiple sessions, owners, or release gates.

## Evidence is layered

Static inspection, a focused regression, an affected-module build, an integration path, and a real
environment probe answer different questions. HappyCoding starts with the lowest proof that can
establish the requested behavior and climbs with blast radius.

This prevents two opposite errors:

- declaring victory because a broad command exited zero even though it never exercised the behavior;
- running an expensive full suite for a one-string change when a direct focused check proves it.

Freshness matters. Evidence from before the final edit, from a worker summary, or from a different
environment cannot silently become completion proof.

## Collaboration protects context, not agent count

Parallel work is valuable when outputs are independent and integration is clear. Reading can often
be partitioned safely. Shared schemas, migrations, contracts, and files need one controlled write
line. The main agent remains accountable for decisions and inspects critical primary evidence.

The success metric is reduced uncertainty and coordination cost—not the number of active agents.

## Read-only work is real work

An architecture audit, incident diagnosis, review, explanation, or status report may be the full
requested outcome. Treating every investigation as implied authorization to patch creates surprise
and destroys the evidence boundary the user asked for.

HappyCoding therefore separates understanding from mutation. It acts after the user requests a
change, not merely because a change is imaginable.

## Reversibility defines agency

Local edits and focused checks are usually reversible. Deletion, force push, production migration,
deployment, permission changes, secret writes, and external messages can create durable impact.
The workflow resolves the exact target and obtains current authorization at that boundary.

Autonomy reduces user coordination; it does not broaden scope or create production authority.

## What we learned from other projects

The project studies current public repositories as design evidence:

- [OpenAI Plugins](https://github.com/openai/plugins) demonstrates the current Codex plugin,
  marketplace, and bundled-skill distribution structure.
- [Anthropic Skills](https://github.com/anthropics/skills) demonstrates a small, self-contained
  skill anatomy with separate specification and template surfaces.
- [Superpowers](https://github.com/obra/superpowers) demonstrates systematic debugging, fresh
  verification, cross-harness packaging, and dedicated behavior evals.
- [GitHub Spec Kit](https://github.com/github/spec-kit) shows how intent, artifacts, documentation,
  and release surfaces can form a coherent public project.
- [Awesome Copilot](https://github.com/github/awesome-copilot) shows the value of resource taxonomy,
  machine-readable catalogs, community guidance, and install-time caution.

HappyCoding makes different trade-offs. It does not require every task to produce a specification,
run a full TDD loop, or dispatch subagents. Those mechanisms remain available when acceptance risk
justifies them.

## Keep the runtime small as the repository grows

The public repository can add translations, evaluation data, release automation, and contributor
guidance without loading them into every coding task. `SKILL.md` contains the hot path. Conditional
detail lives one reference hop away. Human-facing material lives under `docs/` or at repository root.

That separation is how the project can become broad without making every invocation heavy.
