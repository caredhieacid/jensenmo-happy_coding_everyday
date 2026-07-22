# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The canonical source for the `jensenmo-happy-coding-everyday` Codex skill ("HappyCoding Everyday") — a single automatic coding-workflow dispatcher that routes requests into three lanes (Everyday / Collaboration / Delivery). The shipped artifact is markdown instructions plus packaging metadata, not application code; the Python here is validation and release tooling only (stdlib-only, no third-party runtime deps).

## Commands

```bash
# Full deterministic gate (run before claiming completion — required by AGENTS.md)
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_repository.py

# Single test module / case
python3 -m unittest tests.test_scenarios
python3 -m unittest tests.test_scenarios.BehavioralScenarioTests.test_scenarios_are_well_formed_and_unique

# Official Codex skill validator (needs PyYAML; CI pins the validator from openai/codex)
python3 /path/to/skill-creator/scripts/quick_validate.py skills/jensenmo-happy-coding-everyday

# Behavior scenarios: runs `codex exec` in a fresh fixture workspace, writes evidence
# to .scenario-runs/. Grading is human — the runner never marks a pass.
python3 scripts/run_scenarios.py [scenario-id ...] [--dry-run]

# Deterministic plugin archive + SHA-256 (version must match .codex-plugin/plugin.json)
python3 scripts/package_release.py --output-dir dist
```

## Architecture

Three concerns are deliberately separated:

- **Runtime skill** — `skills/jensenmo-happy-coding-everyday/`. `SKILL.md` holds only the rules needed on every coding turn; conditional depth lives in `references/` (`lanes.md`, `contracts-and-evidence.md`) and is loaded on demand. Keeping `SKILL.md` compact is a hard constraint, not a style preference.
- **Distribution wrappers** — `.codex-plugin/plugin.json` (plugin manifest pointing at `skills/`, no duplicated instructions) and `.agents/plugins/marketplace.json` (marketplace catalog that pins install to the tag matching the manifest version). A `v*` tag must match the manifest version or release verification fails.
- **Human docs** — `docs/` and the READMEs live outside the skill folder so they never enter runtime context. `README.md` is canonical; translated READMEs must preserve commands, paths, safety claims, and language navigation (see `docs/i18n/`).

### Three layers of confidence (do not conflate them)

1. **Structural** — `tests/test_*.py` + `scripts/validate_repository.py` check manifests, local links, translations, and scenario schemas.
2. **Behavioral** — `tests/scenarios/*.json` each define a pressure, a user-shaped prompt, acceptable lanes, observable invariants, and forbidden behaviors; `tests/fixtures/<id>/` holds the disposable repo a scenario runs in. `scripts/run_scenarios.py` produces evidence for a human grader.
3. **Real-task** — only actual coding runs prove behavior. Never claim a scenario "passed" because its JSON validated or an earlier run succeeded; a pass requires grading a fresh-agent run.

## Change discipline (from AGENTS.md — binding)

- One dispatcher only. New behavior goes into the existing skill or its `references/`, never a new top-level workflow skill. Preserve the three lanes: Everyday is the default; Collaboration and Delivery require explicit evidence.
- Every behavior change must name the pressure scenario it improves; add or update the scenario in `tests/scenarios/` **before** changing routing behavior.
- Do not copy upstream workflow text (Superpowers, Spec Kit, etc.) — credit ideas, write original rules.
- Git: Tier 2 PR workflow. Feature branch → PR → `main`, squash integration, never force-push or delete `main`. No AI signature lines in commits.
- Never commit secrets, local machine paths, generated caches (`.scenario-runs/` is gitignored), or raw agent transcripts.
- Completion reports state: what changed, what fresh validation ran, what was **not** verified, and residual risk.
