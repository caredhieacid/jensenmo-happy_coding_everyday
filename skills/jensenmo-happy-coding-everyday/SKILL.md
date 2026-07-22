---
name: jensenmo-happy-coding-everyday
description: "Use when a task involves reading, editing, reviewing, testing, debugging, refactoring, configuring, or publishing source code or a software repository. This is the automatic and sole coding-workflow entrance: it selects the lightest safe execution lane without requiring the user to name a mode."
---

# JensenMo HappyCoding Everyday

## Purpose

Own the coding workflow from request to evidence. The user does not need to ask for a mode, a plan, tests, review, or subagents. Infer the smallest workflow that safely reaches the requested outcome, preserve repository-local instructions, and keep process overhead proportional to risk.

## Route Every Coding Task

1. Read the request and the nearest repository instructions.
2. Lock a compact contract: `目标 / 范围 / 验收 / 不要做`.
   - Keep it internal for clear, low-risk work.
   - State assumptions only when they affect behavior, scope, data, or an irreversible action.
3. Select the lowest sufficient lane from the table below. Upgrade only when concrete evidence crosses a trigger.
4. Execute with surgical changes and fresh validation.
5. Report the outcome, evidence, unverified items, and residual risk.

Match the action to the request. Questions, reviews, audits, status checks, and diagnoses are valid
read-only outcomes; do not turn them into implementation, publication, or external writes unless the
user requested that change. If the user changes a constraint mid-task, reconcile it with the active
contract, keep compatible progress, and discard only work that now conflicts.

| Lane | Use when | Topology | Required rigor |
| --- | --- | --- | --- |
| **Everyday** | Default: one bounded task, local change, low coupling | One agent | Inspect, minimal patch, targeted validation |
| **Collaboration** | Two or more independent investigations/tasks, a large read surface, or useful independent review | Main agent plus a few bounded workers | Read in parallel, write on one controlled line, inspect primary evidence |
| **Delivery** | Cross-system change, migration/security/production risk, long chain, multi-session work, or formal PR/E2E delivery | Orchestrator with contracted workers and independent review | Durable goal, staged gates, real-path acceptance, explicit approvals |

Read [lanes.md](references/lanes.md) only when lane selection or escalation is non-obvious. For Collaboration or Delivery, also read [contracts-and-evidence.md](references/contracts-and-evidence.md).

## Working Rules

### Think before changing

- Inspect the relevant code, tests, history, and runtime evidence before choosing a fix.
- If multiple interpretations materially change the result, present the smallest set of choices. Otherwise make a bounded assumption and continue.
- Prefer the simplest adequate path. Do not create speculative abstractions, opportunistic refactors, or unrelated cleanup.

### Debug from evidence

- Reproduce or otherwise establish the failure before fixing it.
- Trace cause across the real control/data path; do not patch only the visible symptom.
- Change one hypothesis at a time. If the same path fails twice, stop, summarize evidence, and reassess instead of pushing harder.

### Keep writes controlled

- Inspect repository status before editing. Preserve unrelated user changes, and stop for direction
  when the requested work cannot be separated safely from ambiguous existing edits.
- A worker may write only within an explicit, non-overlapping scope.
- When work shares files or contracts, keep one writer and use other agents for read-only research or review.
- Never treat a worker summary as proof for a critical claim; inspect the cited file, diff, command output, or runtime evidence.

### Verify proportionally, but always freshly

- For a behavior change or bug fix, prefer a failing test or reproduction before implementation when feasible.
- Run the narrowest test that proves the requested behavior, then add broader checks according to blast radius.
- If no test harness exists, use the strongest available check and name the gap.
- Never claim success from an earlier run, a worker assertion, or the absence of obvious errors. Re-run the relevant verification after the final change.

### Protect irreversible boundaries

Local edits and read-only checks are reversible. Deletion, force push, production migration/deployment, permission changes, secret writes, and external messages require explicit authorization unless the current user request already grants it. Resolve exact targets before acting.

## Completion Contract

Lead with the achieved outcome. Then state, compactly:

- what changed;
- what fresh verification ran and its result;
- what was not verified;
- remaining assumptions or risks;
- any approval or user decision still required.

Do not manufacture ceremony. Everyday work needs no goal document, board, retrospective, multi-agent team, or full test suite unless the task itself warrants one.

## Common Rationalizations

| Thought | Correction |
| --- | --- |
| “A full process is always safer.” | Excess process adds context and failure surface. Start Everyday and escalate on evidence. |
| “It is tiny, so no check is needed.” | Use a tiny check: focused test, search, diff inspection, build target, or direct reproduction. |
| “More agents will be faster.” | Delegate only independent, self-contained work; coordination is a real cost. |
| “Parallel writers can merge later.” | Shared files and contracts get one writer. Parallelize reading and independent review. |
| “The command passed earlier.” | Completion requires fresh evidence after the final edit. |
| “While here, this code could be cleaner.” | If it is not required for acceptance, leave it alone. |
| “The user must choose a mode.” | Lane selection is the skill's responsibility. Ask only for material choices or authorization. |
