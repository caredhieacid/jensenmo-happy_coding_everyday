## What changed

<!-- Describe the behavior, documentation, test, or automation change. -->

## Pressure scenario or reason

<!-- Name the scenario improved. For non-behavior changes, explain the concrete maintenance need. -->

## Evidence

- [ ] `python3 -m unittest discover -s tests -p 'test_*.py'`
- [ ] `python3 scripts/validate_repository.py`
- [ ] official Codex skill validator
- [ ] `git diff --check`

<!-- Add focused behavior or packaging evidence and say what was not verified. -->

## Scope and risk

<!-- State exclusions, compatibility impact, translation status, and remaining risk. -->

## Safety

- [ ] No secrets, private source, local machine paths, generated caches, or raw transcripts.
- [ ] The change does not add another top-level coding-workflow dispatcher.
