# Repository Instructions

This repository is the canonical source for the `jensenmo-happy-coding-everyday` Codex skill.

## Scope

- Keep one automatic coding dispatcher. New behavior belongs in the existing skill or its references, not in another top-level workflow skill.
- Keep `SKILL.md` compact and move conditional detail into `references/`.
- Preserve the three lanes: Everyday is the default; Collaboration and Delivery require explicit evidence.
- Do not copy upstream workflow text. Credit ideas and write original rules.

## Change Discipline

- Every behavior change must name the pressure scenario it improves.
- Update or add a scenario before changing routing behavior.
- Run `python3 -m unittest discover -s tests -p 'test_*.py'` and the Codex skill validator before claiming completion.
- Keep routine changes on a feature branch and publish through a pull request after the initial empty-repository bootstrap.
- Never commit secrets, local machine paths, generated caches, or raw agent transcripts.

## Completion Evidence

Report changed behavior, focused validation, anything not verified, and residual risk. Do not claim a pressure scenario passed unless it was run against a fresh agent context.
