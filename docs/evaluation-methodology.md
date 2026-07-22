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
