# Execution Lanes

Use the lowest lane that satisfies the acceptance contract. Lane choice is an internal routing decision, not a question the user must answer.

## Everyday

Choose Everyday unless an escalation trigger is present.

Typical work:

- a contained bug, feature, review, configuration change, or repository question;
- one primary module or a small number of tightly related files;
- a coupled path across multiple layers that still has one owner and one bounded acceptance result;
- a change one agent can safely understand and verify in the current context.

Sequence:

1. Inspect the relevant path and repository state.
2. Establish the expected behavior and smallest proof.
3. Patch only what acceptance requires.
4. Run focused validation after the final edit.
5. Report result and gaps.

Do not add a goal file, subagent, worktree, design document, or full-suite run by habit. Use one only when the repository or task provides a concrete reason.

## Collaboration

Escalate when at least one condition is true:

- two or more tasks are independent and can be checked without shared state;
- the read surface is large enough that bounded parallel research protects the main context;
- an independent reviewer would materially reduce a known risk;
- the user explicitly requests subagents or parallel agent work.

Rules:

- Keep the main agent responsible for scope, decisions, integration, and final evidence.
- Send workers narrow contracts. Prefer read-only parallel work.
- Allow parallel writes only when file ownership and interfaces are genuinely disjoint.
- Serialize shared-file, shared-schema, migration, and contract changes.
- Use a few agents, not the maximum available count. Stop delegating when coordination costs exceed saved work.

Return to Everyday after the independent work is merged unless Delivery triggers appear.

## Delivery

Escalate when any condition makes failure expensive or coordination durable:

- database migration, security boundary, permission model, production change, or destructive operation;
- cross-frontend/backend/infrastructure behavior with multiple owners or release stages;
- multi-session work that needs durable state;
- a coordinated release, rollout, real environment, or E2E acceptance path is central to the request;
- many dependent steps require explicit gates and rollback thinking.

A routine feature branch and pull request are delivery mechanics, not a Delivery trigger by
themselves. Keep bounded work in Everyday unless risk, coordination, duration, or acceptance evidence
independently requires escalation.

Use the installed `cto-orchestration` workflow as an internal subroutine when available. The user still speaks to this skill as the single entrance. If it is unavailable, preserve the same essentials: durable goal contract, staged ownership, independent review, real-path evidence, and explicit approval for irreversible steps.

Delivery is not permission to expand scope. De-escalate after the high-risk boundary is crossed.

## Upgrade and Downgrade Signals

Upgrade when evidence reveals wider coupling, unresolved ownership, material security/data risk, or a real-path acceptance requirement. Downgrade when investigation proves the issue local and independently verifiable.

Never upgrade because a workflow is fashionable, because agents are available, because multiple
files or layers are named, or because the task merely sounds important.
