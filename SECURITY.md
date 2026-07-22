# Security Policy

## Supported versions

Until the first stable release, security fixes target the latest commit on `main` and the newest
published release only.

## Report a vulnerability

Please use GitHub's private vulnerability reporting or a private security advisory for this
repository. Do not open a public issue when a report contains an exploitable workflow bypass,
credential exposure, unsafe release behavior, or a destructive-action authorization flaw.

Include:

- the affected commit or release;
- the smallest reproduction or pressure scenario;
- the expected safety boundary;
- observed impact and any known workaround.

Never include real secrets, customer data, or private repository content. Use redacted fixtures.

## Scope

Security-relevant issues include:

- instructions that allow destructive or production actions without current authorization;
- plugin or marketplace packaging that loads unexpected code or services;
- CI workflows that expose credentials to untrusted pull requests;
- release artifacts that do not match the tagged source;
- documentation that instructs users to overwrite broad or ambiguous paths.

General routing preferences and feature requests belong in the public issue tracker.
