# Changelog

All notable changes to HappyCoding Everyday are recorded here. The project uses semantic versions
for plugin releases.

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
