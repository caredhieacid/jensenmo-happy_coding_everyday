# Getting Started

## Choose an installation path

Use the plugin path when you want an installable public package and the Codex plugin experience.
Use a direct skill symlink when you are developing the workflow locally or want every update to be
visible immediately.

## Install from the plugin marketplace

Add the GitHub repository as a marketplace source:

```bash
codex plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday
```

Then open **Plugins** in Codex, select **JensenMo HappyCoding**, and install
**HappyCoding Everyday**. Start a new task after installation so the new skill metadata is present
from the beginning of the context.

The plugin bundles instructions only. It does not add an MCP server, connector, hook, background
service, credential, or telemetry client.

## Install the skill directly

```bash
git clone https://github.com/caredhieacid/jensenmo-happy_coding_everyday.git
cd jensenmo-happy_coding_everyday
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/jensenmo-happy-coding-everyday" \
  "$HOME/.agents/skills/jensenmo-happy-coding-everyday"
```

Codex scans `$HOME/.agents/skills` for user-scoped skills and supports symlink targets. Repository
teams can instead place or link the skill under `.agents/skills` inside their repository.

Do not blindly replace an existing path. Inspect it first, especially when it may contain local
changes or point to another checkout. Older `~/.codex/skills` locations may remain compatible, but
`.agents/skills` is the current standardized discovery path.

## Confirm discovery

Start a new Codex task and explicitly invoke the skill once:

```text
$jensenmo-happy-coding-everyday inspect this repository and report the narrowest useful check.
```

Expected behavior:

- Codex reads the nearest repository instructions;
- it does not ask you to choose Everyday, Collaboration, or Delivery;
- it keeps a clear read-only request read-only;
- it reports what evidence it actually inspected or ran.

## Update

For a direct clone:

```bash
git -C /path/to/jensenmo-happy_coding_everyday pull --ff-only
```

For a marketplace installation, refresh the marketplace through the Codex plugin controls or CLI,
then start a new task. Review release notes before updating across a behavior change.

## Uninstall

For a direct skill, remove only the exact symlink after verifying its target:

```bash
readlink "$HOME/.agents/skills/jensenmo-happy-coding-everyday"
```

Then use your normal recoverable file-removal workflow. For a plugin installation, uninstall or
disable it from **Plugins**. Removing the marketplace source is a separate action:

```bash
codex plugin marketplace remove jensenmo-happy-coding
```

## Compatibility

- Direct skills are documented for the Codex app, CLI, and IDE extension.
- Plugin browsing and installation are documented for the Codex app and CLI; the IDE extension does
  not currently provide the plugin installation surface.
- The skill assumes the host exposes normal repository and verification tools. Optional subagents
  are used only when the selected lane and host capabilities justify them.
- Other coding agents are not claimed as supported until their trigger, instruction, and evaluation
  paths are tested independently.

## Troubleshooting

If the skill does not appear:

1. confirm the folder contains `SKILL.md`;
2. confirm the symlink target exists or the plugin is enabled;
3. start a new task so discovery runs with fresh metadata;
4. check for another skill with the same `name`;
5. invoke `$jensenmo-happy-coding-everyday` explicitly to separate discovery from implicit routing.
