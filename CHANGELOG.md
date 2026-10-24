# Changelog

All notable changes to HappyCoding Everyday are recorded here. The project uses semantic versions
for plugin releases.

## Unreleased

### Changed

- Claude Code installs the released tag over HTTPS, as Codex already does, instead of whatever is on
  the default branch. A `github` source would clone over SSH and fail for users without a GitHub SSH
  key, so the marketplace entry uses an HTTPS git URL; repository validation enforces both;
- README (all locales) and getting-started note that installs need git and a recent Codex or Claude
  Code, and getting-started gains install troubleshooting.

### Added

- `scripts/check_commit_messages.py` and a CI job that reject AI attribution lines (such as
  `Co-authored-by: Cursor` or `Generated with Claude Code`) in pull request commits, titles, and
  descriptions, so tools stop appearing as contributors.

## 0.3.1 — 2026-10-23

### Added

- plugin directory listing metadata: a square logo and small icon in `assets/`, a 30-character
  short description, a plain long description, the Developer Tools category, privacy and terms
  links, and plain starter prompts;
- Claude Code plugin and marketplace in `.claude-plugin/`: install with
  `claude plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday` and
  `claude plugin install jensenmo-happy-coding-everyday@jensenmo-happy-coding`. Repository
  validation keeps its name and version in step with the Codex manifest;
- `PRIVACY.md`: the plugin collects, stores, and sends no data;
- repository validation checks the listing against the directory's submission limits and requires
  the icons to exist under `assets/`, which the release package now includes.

### Changed

- README rewritten in plain language in every locale: the problem it solves, real replies from
  test runs, and test results, with a hero image and a social preview card in `docs/assets/`.
  Translations no longer carry "the English version prevails" notes;
- install instructions say plainly that the first command adds this repository as a plugin
  source (it is not in an official plugin directory) and add the `codex plugin add` command;
- `docs/pressure-tests.md` records the 0.3.0 fresh-agent evaluation: method, per-round results,
  consistent strengths, open weaknesses, and limits of the evidence.

## 0.3.0 — 2026-10-22

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
- a "Safe defaults, no setup" README section in every locale;
- confirm-before-building: a guess the user would have to undo (user-visible behavior, copy, or
  design; public names or interfaces; data; security; cost; scope) becomes one short question with
  concrete options and a recommended default, while facts the code settles are decided, not asked;
- build-only-what-was-asked: no unrequested features, options, UI elements, decoration, docs, or
  README sections;
- baseline guidance for UI that looks like the product rather than a template (no decorative
  gradients, emoji, unrequested heroes, card-wrapped blocks, badges, placeholder stats, or hype
  copy) and for repository structure (documented layers, inventories kept current, decision
  records only for architectural decisions, the documented gate before a commit);
- `references/change-checklist.md`: a one-table completeness scan by change type (logic, bug,
  public interface, endpoint, stored data, money/time/text, concurrency, hot paths, UI, dependency,
  removal). It runs during the final diff review of a non-trivial change; non-matching rows are
  skipped silently, and suggested extras are reported rather than built;
- `generated-ui-look`, `ambiguous-change`, `backend-layering`, and `edge-case-coverage` pressure
  scenarios with fixtures;
- `scripts/run_scenarios.py` closes stdin for `codex exec`, so a run can no longer wait forever on
  an inherited pipe.

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
