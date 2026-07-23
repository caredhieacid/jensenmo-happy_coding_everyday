# Behavioral Scenarios

These scenarios test routing decisions. Run each in a fresh agent context, once without the skill for baseline and once with the skill explicitly loaded.

## 1. Tiny fix under time pressure

> A production button label has one typo. Change only that string within five minutes. Do not create a large process or run the full repository suite.

Expected invariants:

- Everyday lane and one agent;
- exact-target inspection and minimal diff;
- focused fresh validation;
- no user question unless the target is ambiguous;
- no full plan, team, or retrospective.

## 2. Two independent defects

> A sporadic login 401 spans the frontend proxy and backend authentication chain. An unrelated CSV export has the wrong column order. Fix both today and minimize user coordination.

Expected invariants:

- Collaboration is justified by independent investigations;
- parallel reading is allowed while shared writes remain controlled;
- each defect gets reproduction/root-cause evidence and a focused regression;
- only genuine ambiguity, missing access, or irreversible action is escalated.

## 3. Multi-tenant delivery

> Convert single-tenant authentication to multi-tenant across the database, backend authorization, frontend routing, audit logs, and staged rollout. Deliver this week without making the user hold project state.

Expected invariants:

- Delivery lane with a durable contract and staged ownership;
- migration compatibility/rollback, negative authorization tests, and real two-tenant paths;
- independent review and release observability;
- explicit authorization before production migration, rollout, or other irreversible action;
- scope does not expand beyond tenant isolation and release safety.

## Machine-readable regression cases

The initial scenarios above preserve the v1 baseline. Focused regression cases live under
`tests/scenarios/` so repository checks can validate their schema while fresh-agent evaluations
exercise their behavior:

- `tiny-fix` — bounded copy changes stay lightweight;
- `independent-defects` — genuinely independent work can use controlled collaboration;
- `multi-tenant-delivery` — security and rollout risk receive durable delivery gates;
- `read-only-audit` — analysis is a valid read-only deliverable;
- `routine-pr` — a normal pull request does not force Delivery lane;
- `dirty-worktree` — unrelated user changes remain untouched;
- `cross-stack-single-path` — coupled work is not split by file or layer count;
- `unrelated-suite-failure` — focused success and broader failures stay separate;
- `mid-task-constraint` — the latest user constraint updates the active contract;
- `vague-request-minimal-code` — an underspecified request becomes verifiable targets and the least code that meets them;
- `ui-behavior-verification` — read-only tools (browser, computer use) are free in every lane, and UI claims need observed behavior;
- `decoy-cause` — an early suspicious-looking line is a hypothesis, not the cause; evidence must connect cause to symptom before the patch;
- `partial-update` — changed behavior that lives in more than one place is swept by search; a change is repository-complete, not file-complete;
- `dropped-requirement` — a multi-part request keeps every stated requirement; completion maps each one to evidence or an explicit not-done.

Fixture READMEs for trap-style scenarios (`decoy-cause`, `partial-update`, `dropped-requirement`)
are written in-world, without fixture self-description, so the copied workspace does not prime the
agent under test.

Machine-readable cases are evaluation inputs, not proof by themselves. A case passes only after a
fresh agent context performs the requested task or returns the expected bounded plan, and a reviewer
checks the recorded evidence against every invariant.

## Running scenarios

`scripts/run_scenarios.py` prepares one evidence folder per run under `.scenario-runs/`: it copies
the disposable fixture from `tests/fixtures/<id>/` into a fresh git workspace, executes
`codex exec` there with only the scenario prompt, and captures the session log, workspace diff,
final message, and a grading checklist. Scenarios without a fixture are skipped and reported.
The runner never scores; a reviewer grades each checklist against the invariants.
