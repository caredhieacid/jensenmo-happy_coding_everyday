# Contracts and Evidence

## Compact Task Contract

Use four fields. Do not ask the user to fill them when the request already answers them.

- **目标**: the observable outcome.
- **范围**: repositories, modules, environments, or artifacts in scope.
- **验收**: behavior and evidence required to call the task complete.
- **不要做**: explicit exclusions plus likely scope traps.

Keep this contract conversational for Everyday work. Persist it for long-running Delivery work.
When the user adds or replaces a constraint, update the active contract instead of starting a
parallel plan. Preserve completed work only when it still satisfies the latest contract.

## Worker Dispatch Contract

Every worker assignment must contain:

1. **Goal** — one bounded question or deliverable.
2. **Output format** — exact shape and level of detail to return.
3. **Tool/source boundary** — allowed repositories, files, environments, and whether writes are allowed.
4. **Scope and stop/report rule** — what not to touch and when to return blocked instead of expanding.

Workers return distilled conclusions with primary evidence: paths and line numbers, commands and relevant output, test names, request IDs, or artifact locations. The main agent spot-checks critical evidence before integrating it.

## Verification Ladder

Choose the lowest evidence that proves the behavior, then climb according to risk:

1. static inspection, search, diff check, formatter, or schema validation;
2. focused unit/component test or direct reproduction;
3. affected-module test, type check, build, or contract test;
4. integration/E2E on a representative path;
5. real environment validation, monitoring, rollback proof, and independent review.

Examples:

- Copy change: inspect target rendering path, focused UI test if present, and diff.
- Local bug: reproduce, add or identify the failing check, fix, run focused regression.
- Shared API contract: validate producer and consumer plus integration path.
- Migration/security/release: use the full ladder where applicable and include rollback/negative-path evidence.

## Evidence Rules

- Evidence must be fresh after the final relevant change.
- Record the exact command or path, exit/result, and what claim it proves.
- Separate focused success from unrelated existing failures.
- A passing build does not prove runtime behavior; a screenshot does not prove authorization or data integrity.
- If validation cannot run, say why, what substitute ran, and what risk remains.

## Review Boundaries

Use independent review when blast radius, security, data integrity, or merge risk makes a second perspective valuable. Review acceptance criteria and the actual diff, not style preferences. Fix blocking findings; record non-blocking suggestions without silently widening scope.
