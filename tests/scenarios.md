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
