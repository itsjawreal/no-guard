# Compatibility

Languages: [Indonesia](COMPATIBILITY.md) · **English** · [简体中文](COMPATIBILITY.zh.md)

`no-guard` targets **Hermes Agent 2026.9.24**
(commit `e3dd27ee2d8b011737a4eea8e3eb3d711ab78690`) and the
`c419cf7c864ac0ee511dbd9f7091a8bba0b567ee` variant — the same version as the
injection mod.

| Item | Value |
| --- | --- |
| Hermes | 2026.9.24 / `e3dd27ee…` |
| Variant | `c419cf7c…` |
| OS | Linux (WSL2 supported) |
| Python | interpreter shipped with the Hermes installation |
| Architecture | x86_64 |

Run `./bin/no-guard --dry-run` then `./bin/no-guard install` to apply. If the
Hermes version does not match, do not continue; use a release that matches
your installation.

> Gate removal is not a capability upgrade: **it does not mean your agent can
> hack NASA.**
