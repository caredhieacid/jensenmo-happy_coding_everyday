# Behavior Evaluation Methodology

## What is being evaluated

HappyCoding is primarily a behavioral workflow. File existence and valid YAML are necessary, but
they cannot prove that a fresh agent will respect read-only scope, choose the right lane, control
writes, or report honest evidence.

Evaluation therefore uses three layers:

1. **repository validation** — deterministic tests for structure, manifests, links, translations,
   scenario schemas, and release packaging;
2. **fresh-context behavior evaluation** — a new agent receives the skill and one realistic request;
3. **real-task calibration** — failures and near misses from actual coding work become regression
   scenarios before workflow rules change.

## Scenario contract

Machine-readable cases under `tests/scenarios/` contain:

- a stable ID and title;
- the pressure that makes the case difficult;
- a user-shaped prompt;
- one or more acceptable lanes;
- observable invariants;
- explicitly forbidden behavior.

Multiple lanes may be valid when runtime evidence decides the boundary. For example, a read-only
audit stays Everyday when the path is bounded and may use Collaboration when the read surface has
independent partitions. The invariant matters more than a fashionable topology.

## Fresh-context protocol

`scripts/run_scenarios.py` automates the mechanical part: it copies the scenario's disposable
fixture from `tests/fixtures/<id>/` into a fresh git workspace at a neutral temporary path outside
this repository (so the agent cannot read this repository's instructions or infer the scenario from
the path), runs `codex exec` with only the scenario prompt, and records the prompt, session log, workspace diff, final message, and a grading
checklist under `.scenario-runs/`. Grading remains a human step.

1. Start a new agent context with repository instructions and the candidate skill available.
2. Provide only the scenario prompt and the normal tool environment. Do not reveal the expected lane,
   suspected bug, desired wording change, or previous evaluator conclusion.
3. Let the agent perform the requested work against a disposable fixture or return a bounded plan
   when mutation is intentionally prohibited.
4. Capture distilled evidence, not secrets or raw private transcripts.
5. Score every invariant as pass, fail, or not observable and record primary evidence.
6. Treat any forbidden behavior as a blocking failure.

## Evidence record

A useful record includes:

- date, host, model family, and skill commit;
- scenario ID and selected lane;
- user interruptions or questions;
- files or external state changed;
- exact verification commands and results;
- invariant verdicts with evidence pointers;
- remaining uncertainty.

Do not commit credentials, private source, or raw agent transcripts. A concise evaluation record is
enough to reproduce the reasoning without turning the repository into a session archive.

## Change discipline

A workflow behavior change must identify a pressure scenario it improves. Add or update the scenario
before changing routing instructions. After the change:

1. run repository checks;
2. run the focused scenario in a new context;
3. run adjacent scenarios that could regress;
4. record what remains untested;
5. avoid broad wording changes that have no observed failure.

Passing the scenario means the fresh run met the invariants. A JSON file, a persuasive plan, or an
earlier run is not a pass.

## Comparing with and without the skill

A comparison needs an environment where nothing else steers the agent:

- point `CODEX_HOME` at an empty folder that holds only a link to the login file and a config with
  the model, so no global instructions load;
- point `HOME` at an empty folder too, so skills installed for the user are not listed;
- for the "with" arm, link the skill folder into `$CODEX_HOME/skills/`; for the "without" arm, leave
  it out.

Then run each arm with a label and at least two repeats, and have a separate reviewer score every
run against its checklist:

```bash
HOME=/path/empty CODEX_HOME=/path/arm python3 scripts/run_scenarios.py --label with-skill --repeat 2
```

Give every arm the same environment note when one is needed. On macOS, agents that try to launch a
headless browser inside the sandbox crash it and trigger system crash dialogs; an `AGENTS.md` in
each arm's `CODEX_HOME` that says no browser is available avoids this.
