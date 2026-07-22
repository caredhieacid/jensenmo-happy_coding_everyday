# Contributing

HappyCoding Everyday optimizes for correct behavior with low process overhead. Contributions are welcome, especially concrete scenarios that reveal under- or over-orchestration.

## Propose a behavior change

1. Describe a realistic coding request and the pressure involved.
2. State the current routing decision and why it is harmful.
3. State the desired observable behavior without prescribing unnecessary implementation.
4. Add or update the scenario in `tests/scenarios.md`.
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
