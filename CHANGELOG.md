# Changelog

All notable changes to HappyCoding Everyday are recorded here. The project uses semantic versions
for plugin releases.

## Unreleased

### Added

- scenario runner (`scripts/run_scenarios.py`) that executes fixtures against a fresh `codex exec`
  context and records gradable evidence;
- disposable fixture repositories for the `tiny-fix` and `vague-request-minimal-code` scenarios;
- `vague-request-minimal-code` pressure scenario for underspecified requests;
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
- the compact contract fields are stated in English with the original Chinese gloss.

## 0.1.0 — pending first tag

- Initial public Alpha release with one automatic dispatcher, three execution lanes, progressive
  disclosure, structural tests, and baseline pressure evaluations.
