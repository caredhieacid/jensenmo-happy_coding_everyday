# Contributing

HappyCoding Everyday optimizes for correct behavior with low process overhead. Contributions are welcome, especially concrete scenarios that reveal under- or over-orchestration.

Read [the Code of Conduct](CODE_OF_CONDUCT.md) before participating. Security-sensitive findings
belong in the private path described by [SECURITY.md](SECURITY.md), not in a public issue.

## Propose a behavior change

1. Describe a realistic coding request and the pressure involved.
2. State the current routing decision and why it is harmful.
3. State the desired observable behavior without prescribing unnecessary implementation.
4. Add or update the scenario in `tests/scenarios.md` or `tests/scenarios/*.json`.
5. Make the smallest skill or reference change that fixes it.
6. Run structural validation and repeat the scenario in a fresh agent context.

Please avoid broad wording changes without a failing scenario. A new top-level skill is not accepted when the behavior fits one of the existing lanes.

## Pull requests

Keep pull requests focused. Include:

- the scenario being improved;
- before/after behavior;
- validation evidence;
- any remaining tradeoff or untested case.

By contributing, you agree that your contribution is licensed under the MIT License.

## Local validation

Run all deterministic checks before opening a pull request:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_repository.py
python3 /path/to/skill-creator/scripts/quick_validate.py \
  skills/jensenmo-happy-coding-everyday
git diff --check
```

The official skill validator requires PyYAML. CI runs a pinned validator revision and dependency.

For behavior changes, deterministic tests are not enough. Run the affected scenario in a fresh
agent context following [the evaluation methodology](docs/evaluation-methodology.md). Do not claim a
scenario passed when only its JSON schema was validated.

## Documentation and translations

`README.md` is the canonical README. Keep user documentation outside the runtime skill directory.
Translation changes must preserve commands, paths, safety claims, and language navigation; follow
[the translation guide](docs/i18n/translation-guide.md) and state native-review status honestly.
