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

## Keep one automatic coding entrance

This skill is designed to be the sole always-on coding dispatcher. If another installed skill also
triggers on generic coding activity (editing, reviewing, testing, debugging), every task pays for
two overlapping instruction sets and routing authority becomes ambiguous. Keep exactly one such
entrance: disable or narrow the other skill so it loads only for its specific domain, or on
explicit invocation. Domain standards that trigger on narrower evidence (a particular framework,
Git operations, observability work) coexist fine.

## Complementary ecosystem skills

HappyCoding is a dispatcher, not a monopoly. Narrow, conditionally triggered skills compose well
with it because they own one domain and fire on specific evidence rather than on every coding
task. Skills that have proven useful alongside this workflow:

- **GitHub flow** — the official `gh-fix-ci` and `gh-address-comments` skills (installable via
  `skill-installer` from [openai/skills](https://github.com/openai/skills)) pair well with the
  Tier-style branch-and-PR discipline this repository itself uses.
- **Session handoff** — a handoff/summary skill complements the Delivery lane when work must
  survive a context boundary.
- **Adversarial review** — a Socratic plan-stress-testing skill can serve as the independent
  reviewer the Collaboration and Delivery lanes call for.
- **Web context** — a search/scrape skill strengthens the tool-freedom rule when tasks depend on
  current external documentation.

What to avoid: all-in-one workflow harnesses that trigger on generic coding activity, impose
mandatory staged ceremonies, or ship dozens of modes and subagents. They recreate the duplicate
ownership problem described in [design-philosophy.md](design-philosophy.md) and compete with the
single automatic entrance above. Review any third-party skill's instructions before installing;
skills are prompt-injection surfaces.

## Troubleshooting

If the skill does not appear:

1. confirm the folder contains `SKILL.md`;
2. confirm the symlink target exists or the plugin is enabled;
3. start a new task so discovery runs with fresh metadata;
4. check for another skill with the same `name`;
5. invoke `$jensenmo-happy-coding-everyday` explicitly to separate discovery from implicit routing.
