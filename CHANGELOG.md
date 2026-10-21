# Changelog

All notable changes to HappyCoding Everyday are recorded here. The project uses semantic versions
for plugin releases.

## 0.3.0 — 2026-10-21

### Added

- `references/engineering-baseline.md`: original, vendor-neutral defaults for Git, secrets,
  security, data, interfaces, logging, dependencies, environment setup, UI, LLM features, and tests.
  Each part applies only when a task touches that area, to the code the task changes;
- an explicit precedence order: the user's request, then repository instructions and decision
  records, then narrower domain skills, then these defaults. Secret leaks, lost work, broken shared
  branches, and the authorization boundary are never traded away;
- plain-language reports in the user's language with the exact next step, and a safe route (plus a
  one-sentence risk note) when a requested shortcut would leak a secret, lose work, or break a
  shared branch;
- `plain-language-request`, `unsafe-shortcut`, `repo-conventions`, `endpoint-authorization`,
  `missing-setup`, and `local-acceptance` pressure scenarios, with fixtures for the first three;
- structural tests that keep `SKILL.md` within 60 lines, require every reference to be linked from
  it, and reject machine paths or e-mail addresses in the runtime skill;
- a "Safe defaults, no setup" README section in every locale.

### Changed

- `SKILL.md` is restructured to about 50 lines while keeping the 0.2.0 safeguards: the sufficiency
  gate, verifiable targets, least code, the repository-complete sweep, requirement replay, and
  dirty-worktree handling;
- the skill description names the covered coding activities again so implicit invocation stays
  reliable, and a structural test guards it;
- a local end-to-end check alone no longer suggests Delivery;
- worker context is chosen explicitly, because some hosts let workers inherit conversation history;
- an installed orchestration skill is an optional Delivery adapter, and its absence does not block
  safe local work;
- the runtime skill no longer contains a rule about this repository's own scenario files;
- the final report is a short checklist: user-visible behavior changes, evidence tied to each
  requirement, unverified risk and where the change stands (local, committed, pushed, deployed),
  and exact user steps. Brevity cuts process narration, never these items, and unattempted actions
  are reported as not attempted;
- fixes prefer a mechanism the code already has and do not restructure (merge duplicates, move
  logic, add module dependencies) unless the task requires it; the 0.2.0 rule against handling
  states or callers the code does not have is restored, and vague requests become the smallest
  set of checkable targets;
- before replying, the agent reads its whole diff to list user-visible behavior changes;
- the engineering baseline is read only for changes that alter its subject or before a commit or
  PR, not for text-only or single-expression fixes.
- `scripts/run_scenarios.py` runs each fixture at a neutral temporary path outside the repository,
  so the agent under test cannot read this repository's instructions or infer the scenario from the
  path; fixture READMEs no longer name their scenario.

## 0.2.0 — 2026-07-23

First published tag. Everything below, plus the 0.1.0 baseline, ships in this release.

### Added

- scenario runner (`scripts/run_scenarios.py`) that executes fixtures against a fresh `codex exec`
  context and records gradable evidence;
- disposable fixture repositories for the `tiny-fix` and `vague-request-minimal-code` scenarios;
- `vague-request-minimal-code` pressure scenario for underspecified requests;
- `decoy-cause`, `partial-update`, and `dropped-requirement` pressure scenarios with runnable
  fixtures whose READMEs stay in-world so runs are not primed;
- `ui-behavior-verification` pressure scenario and an explicit tool-freedom rule: read-only and
  observational tools (web search, browser, computer use, bounded exploration workers) are free in
  every lane, while writes stay gated;
- guidance on complementary ecosystem skills in getting-started;
- worker dispatch prompt shape and host-subagent guidance for the Collaboration lane;
- Codex plugin manifest and remote marketplace catalog;
- deterministic CI preview packaging and tag-driven GitHub Release automation;
- machine-readable behavior regression scenarios;
- multilingual README files and translation governance;
- public documentation, community templates, security, and support policies.

### Changed

- routine pull requests no longer imply Delivery lane;
- read-only audits are explicit first-class outcomes;
- lane selection now distinguishes coupled cross-layer work from independent work;
- dirty-worktree and mid-task-constraint handling are explicit;
- vague requests must become verifiable targets, and delivered code is bounded to stated
  acceptance (no speculative flexibility, abstraction, or impossible-state handling);
- the compact contract fields are stated in English with the original Chinese gloss;
- a sufficiency gate before editing: state where the target behavior is produced and what depends
  on it, or keep reading instead of patching the first plausible line;
- cheap read-only checks are preferred over assumptions when they can settle a material question;
- changes are repository-complete, not file-complete: duplicated logic, call sites, configuration,
  and coupled artifacts are enumerated by search before closing;
- completion replays the original request, mapping every stated requirement to evidence or an
  explicit not-done;
- README design principles gain "Looking is free" (canonical and zh-CN).

## 0.1.0 — never tagged

- Initial public Alpha release with one automatic dispatcher, three execution lanes, progressive
  disclosure, structural tests, and baseline pressure evaluations.
