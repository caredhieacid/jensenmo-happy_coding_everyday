# Translation Guide

## Source of truth

`README.md` is the canonical source. A translation may explain the same idea naturally in its
language, but it must not introduce a new capability, compatibility claim, installation path, or
safety promise.

Runtime files under `skills/` are not translated. Multiple runtime-language variants would create
behavior drift for one skill name.

## Current locales

The machine-readable list lives in [manifest.json](manifest.json). Its source digest makes every
canonical README change an explicit localization event. English is the source. Simplified Chinese
is maintained with the source. Japanese, Korean, and Spanish are useful review drafts and explicitly
welcome native-speaker correction.

## Updating a translation

1. Read the English diff and identify changed claims, commands, links, and headings.
2. Preserve commands, paths, skill names, lane names, and code examples exactly unless the example
   is natural-language user input.
3. Use the shared [glossary](glossary.md) for core terms.
4. Keep the language switcher complete and symmetric.
5. Update `source_sha256` in the locale manifest after reviewing every translation impact.
6. Run `python3 scripts/validate_repository.py` and the repository unit tests.
7. State whether a native speaker reviewed the change.

Automated translation can create a draft. It must not be described as reviewed or maintained until
a competent speaker has checked technical meaning, safety boundaries, and natural language.

## Adding a locale

Add a locale only when the translation contains useful content and someone can review future drift.
Do not create empty placeholders. Add the README file, update every language switcher, add a manifest
entry, and document review status honestly.
