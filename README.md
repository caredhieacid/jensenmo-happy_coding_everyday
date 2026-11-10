<div align="center">

<img src="docs/assets/hero.jpg" alt="One route splits into three lines of different weight and rejoins at a check mark" width="100%">

<h1>HappyCoding Everyday</h1>

<p><strong>The habits of a great engineer, built into your AI coding assistant.</strong></p>

<p>Small changes stay quick. Big changes get done carefully. Install it once in Codex or Claude Code and every coding task gets better, with nothing to configure.</p>

[![Release](https://img.shields.io/github/v/release/caredhieacid/jensenmo-happy_coding_everyday?color=2f7d5b)](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/releases)
[![CI](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml/badge.svg)](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-f59e0b)](#project-status)
[![Codex Plugin](https://img.shields.io/badge/Codex-plugin-10a37f)](.codex-plugin/plugin.json)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](.claude-plugin/plugin.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-1f2328.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

[Why HappyCoding](#why-happycoding) · [Quick start](#quick-start) · [Examples](#examples) · [Test results](#test-results) · [How it works](#how-it-works) · [Docs](docs/README.md)

</div>

## Why HappyCoding

- **Works the moment it's installed.** No modes, no special prompts, no config. Describe the task the way you always do.
- **Gets it right, not just "done."** It finds the real cause, fixes every place that needs it, and runs the check that proves the fix.
- **Never bloats your work.** A typo fix is a one-line diff. No plans, extra agents, or features nobody asked for.
- **Asks only what only you can decide.** One short question with clear options and a recommendation, instead of a wrong guess you have to undo.
- **Safe by default.** API keys go in a local file instead of your code, nothing gets pushed or deployed without you, and your project's rules always come first.
- **Tiny footprint.** The part loaded on every task is about one page; the rest is read only when a task needs it.
- **Measured, not assumed.** In clean Codex sessions, the same 18 tasks met every check 18 of 36 times without HappyCoding and 29 of 36 times with it.

## Quick start

**Codex:** two commands in your terminal.

```bash
codex plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday
codex plugin add jensenmo-happy-coding-everyday@jensenmo-happy-coding
```

**Claude Code:** two commands in your terminal.

```bash
claude plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday
claude plugin install jensenmo-happy-coding-everyday@jensenmo-happy-coding
```

In each pair, the first command adds this GitHub repository as a plugin source, and the second
installs the plugin. HappyCoding isn't in an official plugin directory yet, so no account or
approval is involved. Inside a Claude Code session, `/plugin marketplace add` and `/plugin install`
do the same; in Codex, you can also install from the **Plugins** screen after the first command.

You need git and a recent version of Codex or Claude Code. If `plugin` isn't a recognized command,
update the tool first. Both tools install the latest release, never unreleased work.

That's it. Start a new task and ask for things as you normally would:

```text
Fix the login bug, keep my other changes, and tell me what you checked.
```

```text
Review this API contract without changing anything. Point to where each field is produced and used.
```

```text
Add tenant isolation across the database, permissions, UI, and rollout. Keep a way to roll back.
```

To call it by name, type `$jensenmo-happy-coding-everyday` in Codex or
`/jensenmo-happy-coding-everyday:jensenmo-happy-coding-everyday` in Claude Code.

<details>
<summary><strong>Other ways to install</strong></summary>

**Link the skill folder directly** (handy if you want to edit it and see changes right away):

```bash
git clone https://github.com/caredhieacid/jensenmo-happy_coding_everyday.git
cd jensenmo-happy_coding_everyday
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/jensenmo-happy-coding-everyday" \
  "$HOME/.agents/skills/jensenmo-happy-coding-everyday"
```

Codex supports linked skill folders. If something already exists at that path, check it before
replacing it. Older installs under `~/.codex/skills` may still work, but `$HOME/.agents/skills` is
the current location.

**Claude Code:** you can also link the same folder into `~/.claude/skills/` instead of installing
the plugin. Use one or the other, not both, or the skill loads twice.

The behavior tests so far run on Codex. On Claude Code, the plugin has been checked with
`claude plugin validate` and a test install.

**Other tools that support Agent Skills:** the skill uses the open Agent Skills format, which many
tools now read, such as GitHub Copilot, Cursor, Gemini CLI, and OpenCode. To use HappyCoding there,
copy or link the `skills/jensenmo-happy-coding-everyday` folder into that tool's skills folder (see
its docs for the location). So far, only Codex and Claude Code have been tested.

Keep just one skill that takes over all coding work: turn off other skills that do the same job,
and keep skills that only cover one area. See [Getting started](docs/getting-started.md).

</details>

## The problem it solves

AI coding assistants are capable, but left on their own they tend to go wrong in one of two ways.

| Not enough | Too much |
| --- | --- |
| Changes the first line that looks suspicious instead of finding the real cause | Writes a plan and starts several agents to fix a typo |
| The same logic exists in two places; only one gets fixed | Runs every test and another review round for a one-line change |
| Says "done" without running anything | Adds validation frameworks, settings, and README sections nobody asked for |
| One of three requirements quietly gets dropped | Builds pages full of gradients, emoji, and marketing copy that look like a template |
| You ask it to put an API key in the code, and it does | Asks you to pick a workflow mode before it starts |

Heavy workflow tools fix the left column, but then every task has to go through the right one.
HappyCoding fixes both: it decides how much process each task needs from its size and risk, so
you get careful work without the overhead.

## What you get

| Feature | What it means |
| --- | --- |
| **Process that fits the task** | Small tasks are done directly. Only changes that touch security, data, or production get extra checks. You never pick a mode. |
| **It actually checks its work** | It reproduces the problem first, runs the relevant check after the last edit, and tells you what it didn't check. |
| **Nothing half-fixed** | It looks for every other place the change affects (callers, duplicate code, config, docs) and updates them, or says why not. |
| **Asks only when it matters** | If a wrong guess would mean redoing work, it asks one short question with two to four options and a recommendation. If the code can answer it, it doesn't ask. |
| **No extras** | No features, settings, decoration, or docs you didn't ask for. |
| **Covers the usual cases** | Before reporting, it checks a short list for the kind of change it made: edge cases, compatibility, data, money and dates, and loading and error states in the UI. |
| **Safe by default** | API keys go in a git-ignored local file instead of code and commits. Nothing is committed, pushed, or deployed unless you ask. Your project's own rules come first. |
| **Tells you what you didn't ask** | Its report can end with up to three things worth knowing: a risk, a missing piece, or a simpler option. |
| **Clean, plain UI** | New pages reuse your existing components and styles. With no design yet, it builds a tidy page on the simplest stack that fits, with no decoration and no repeated headings. |
| **The whole job in one go** | It works out every part a change needs (backend, page, docs, tests) and delivers them together, instead of waiting to be asked for each piece. |
| **Security review on request** | It traces real flaws to their lines, says how each could be abused and how to fix it, and leaves safe code alone. |
| **No forced tech stack** | It uses the stack and patterns your project already has, and doesn't push heavyweight practices onto a small script. |
| **Clear reports** | The result comes first, in your language: what changed, what was checked, what's left, and what to do next. |

## Examples

These are real replies from test runs, unedited. The test machine is set to reply in Chinese, so
the replies below are translated.

**It asks when only you can decide.** Request: *"Change the date format on invoices."*

> Which date format would you like? Issued and due dates currently show as `2026-10-22`.
>
> - `22/10/2026` (day/month/year)
> - `10/22/2026` (month/day/year)
> - `22 Oct 2026` (recommended: avoids day/month confusion)
>
> Once you confirm, I'll update both places and run the tests.

It didn't change any file before getting an answer.

**It follows your project's structure.** Request: *"Add an endpoint that returns how many open tasks a project has."*

> Added `GET /projects/{id}/tasks/open-count`, returning `{"open_count": 2}`.
>
> - Counts only the project's `open` tasks; returns 0 when there are none.
> - A non-integer ID returns 400; an unknown project returns 404.
> - Kept the existing three layers and updated the endpoint docs.
>
> Ran `python3 -m unittest discover -s tests`: all 8 tests pass; `git diff --check` passes. The change is local only and not committed.

**A one-line fix stays one line.** Request: *"A production button label has one typo. Change only that string…"*

> Changed `Sumbit order` to `Submit order` in `CheckoutButton.jsx:5`; that string is the only change.
>
> Checked the diff and `git diff --check` passes. The full suite was not run, and nothing was committed or deployed.

<details>
<summary><strong>It explains results in plain words</strong></summary>

Request (originally in Chinese): *"I just started learning to code. My budget program's total looks
wrong, like a lot of money is missing. Can you fix it? I don't really know Git, so don't break
my stuff."*

> Fixed. The program was skipping the first entry, **1,200 of rent**, so the total now shows
> correctly as **1383.00**.
>
> Only one line in `budget.py` changed. Your ledger data is untouched, and no branch was switched
> and nothing was committed. Checked with the full ledger, a single entry, and an empty ledger;
> all correct.
>
> Run it the same way as before:
>
> ```bash
> python3 budget.py expenses.csv
> ```

</details>

## Test results

Does it actually help? We ran the same 18 tasks in clean Codex sessions, with and without HappyCoding, twice each. Separate reviewers scored every run against a checklist written before the run.

| | Without | With HappyCoding |
| --- | --- | --- |
| Runs that met every check | 18 of 36 | **29 of 36** |
| Average quality score (1 to 5) | 3.4 | **4.2** |

Where it changed the result most:

- **"List these orders on a page, with a status filter."** Without: a full dashboard with a sidebar, stat cards, search, sorting, and its own server. With: three plain files that do what was asked.
- **"Make a good-looking home page for my café."** Without: invented slogans, and a page that needs `npm run dev` before it opens. With: a designed page that uses only the owner's words and opens with a double-click.
- **"I can't program. Make me a small tool to track my spending."** Without: charts, categories, and CSV export nobody asked for. With: add, fix, delete, and monthly totals, plus a note on where the data lives and how to keep a copy.
- **A security review.** Both found the planted flaws. Only the runs with HappyCoding also said what was checked and found sound.

It helps a smaller, cheaper model even more. On `gpt-6-luna`, 19 tasks met every check 9 of 38 times without HappyCoding and 20 of 38 times with it, mostly because it started running its own tests.

On tasks a strong model already handles well, such as tracing a bug to its cause or following a project's commit rules, results were the same with and without.

The project has 30 test scenarios and 19 sample projects. The full record, including what failed, is in [docs/pressure-tests.md](docs/pressure-tests.md).

**Built with itself.** HappyCoding is developed using HappyCoding. So far: 16 merged pull requests,
CI on every pull request, and release packages that can be verified and can't be changed after
publishing.

If HappyCoding saves you time, please star the repo. It's the easiest way to help other
developers find it.

## How it works

```mermaid
flowchart LR
    A["Your request"] --> C{"How big and how risky?"}
    C -->|"Small and clear"| D["Everyday<br/>one assistant makes the change<br/>and runs the relevant check"]
    C -->|"Can be split, or lots to read"| E["Collaboration<br/>helpers research in parallel<br/>one of them edits files"]
    C -->|"Security, data, or production"| F["Delivery<br/>step-by-step plan, review,<br/>and a way to roll back"]
    D --> G["Report: result and what was checked"]
    E --> G
    F --> G
```

| Mode | When | What it does | Example |
| --- | --- | --- | --- |
| **Everyday** | One clear task that one person can own | Reads the code, makes the smallest change, runs the check that proves it | Fix a parser bug and open a normal PR |
| **Collaboration** | The work splits into unrelated parts, or there is a lot of code to read | Several helpers investigate at once; only one edits shared files | Look into an unrelated login 401 and a CSV column-order bug at the same time |
| **Delivery** | Security, database migrations, production, or a rollout across teams | Writes down the plan, checks each step, gets an independent review, prepares a rollback | Add tenant isolation across the database, permissions, UI, and rollout |

Once the risky part is done, it goes back to Everyday. Opening a pull request, touching many
files, or running an end-to-end test locally does not, by itself, make a task Delivery.

**Light on context.** Only `SKILL.md` (about one page) is loaded for every task. The other files
are read only when needed:

| File | When it's read |
| --- | --- |
| [`SKILL.md`](skills/jensenmo-happy-coding-everyday/SKILL.md) | Every coding task |
| [`engineering-baseline.md`](skills/jensenmo-happy-coding-everyday/references/engineering-baseline.md) | The change involves Git, API keys, data, APIs, backend modules, dependencies, setup, LLM calls, or tests |
| [`ui.md`](skills/jensenmo-happy-coding-everyday/references/ui.md) | The change adds or alters a screen, a component, or interface text |
| [`security-review.md`](skills/jensenmo-happy-coding-everyday/references/security-review.md) | You ask for a security review, or the change alters sign-in, permissions, secrets, or payments |
| [`change-checklist.md`](skills/jensenmo-happy-coding-everyday/references/change-checklist.md) | Before reporting, after changing logic, data, an API, or UI, or fixing a bug |
| [`lanes.md`](skills/jensenmo-happy-coding-everyday/references/lanes.md) | It isn't clear which mode to use |
| [`contracts-and-evidence.md`](skills/jensenmo-happy-coding-everyday/references/contracts-and-evidence.md) | Work is handed to another assistant |

## Design principles

1. **Say it once.** It works out the process; you never pick a mode.
2. **Start light.** Add process only when there is a concrete reason.
3. **A check has to prove the result.** "The command ran" is not enough.
4. **Many can read, one edits.** Shared files have a single editor.
5. **Check again after the last edit.** An earlier passing run doesn't count.
6. **Ask only what only you can decide.** Decide the rest and say what was assumed.
7. **Do only what was asked.**
8. **Your project's rules come first.**
9. **Read-only means read-only.** A review or investigation doesn't change code.
10. **Looking things up is always fine.** Searching, reading docs, or opening a browser needs no extra process; process is for changes and risk.

More in [Design philosophy](docs/design-philosophy.md) and [Architecture](docs/architecture.md).

## Compared with similar projects

HappyCoding is written from scratch. It learns from these projects but doesn't copy their
instructions or need them installed.

| Project | Good at | What HappyCoding does |
| --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | Systematic debugging, re-checking after changes, behavior tests | Just as strict, but only as much as each task needs, instead of the full process every time |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Spec documents and plans built around what you want | Writes plans only for big, long-running work, not for everyday edits |
| [Anthropic Skills](https://github.com/anthropics/skills) | Well-structured, self-contained skills | Keeps the always-loaded part short and puts human docs outside it |
| [OpenAI Plugins](https://github.com/openai/plugins) | Codex plugin packaging and the plugin marketplace | One skill, packaged as an installable plugin |
| [Awesome Copilot](https://github.com/github/awesome-copilot) | Clear categories and easy community entry | Test scenarios a script can read, issue templates, and easy-to-follow docs |

## What it won't do

- It isn't a new AI framework or runtime.
- It doesn't force multiple agents, plan documents, TDD, or running every test.
- It doesn't replace your team's engineering rules; it follows them.
- Being able to run on its own doesn't mean it will deploy, delete data, migrate a database, or force-push.
- It doesn't measure success by the number of agents, documents, or tool calls.

## Testing and releases

- **Automated checks:** skill format, plugin packaging, doc links, translations, and test scenario format.
- **Behavior tests:** realistic requests in new sessions, scored against a checklist.
- **Real use:** the only real proof that a change works in your project.

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_repository.py
python3 scripts/run_scenarios.py [scenario-id ...]
```

Every pull request builds a preview of the plugin package. Pushing a `v*` tag that matches the
version in `.codex-plugin/plugin.json` creates a GitHub Release with the package and its SHA-256
checksum. Releases are built from `main`, the package can be verified, and a release can't be
changed after publishing. See [how the tests work](docs/evaluation-methodology.md).

## Repository layout

```text
.
├── .claude-plugin/                 # Claude Code plugin and marketplace
├── .codex-plugin/                  # Codex plugin manifest
├── .agents/plugins/                # Plugin marketplace entry
├── .github/                        # CI, release automation, issue templates
├── docs/                           # Design notes, test records, images
├── scripts/                        # Checks, packaging, test runner
├── skills/
│   └── jensenmo-happy-coding-everyday/
│       ├── SKILL.md                # The part loaded for every task
│       ├── agents/openai.yaml      # Codex settings for the skill
│       └── references/             # Read only when needed
└── tests/                          # Checks, test scenarios, sample projects
```

## Documentation

- [Documentation index](docs/README.md)
- [Getting started](docs/getting-started.md)
- [Architecture](docs/architecture.md)
- [Design philosophy](docs/design-philosophy.md)
- [How the behavior tests work](docs/evaluation-methodology.md)
- [Test record](docs/pressure-tests.md)
- [Roadmap](docs/roadmap.md)
- [Translation guide](docs/i18n/translation-guide.md)

## Project status

HappyCoding Everyday is in **Alpha** and ready to use: the core features, the plugin package, the
automated checks, and a full set of scored test scenarios are in place. New releases keep tuning
its judgment based on real use. As with any tool, review what it does before deploying to
production. See [CHANGELOG.md](CHANGELOG.md) and [the roadmap](docs/roadmap.md).

## Contributing

- Suggest a real test scenario or a behavior change: see [Contributing](CONTRIBUTING.md).
- Report a security issue: see [Security](SECURITY.md).
- Get help: see [Support](SUPPORT.md).
- Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE) © 2026 Jensen Mo
