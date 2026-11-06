# no-guard

Languages: [Indonesia](README.md) · **English** · [简体中文](README.zh.md)

**Hermes injection for gate removal** — for **Hermes Agent 2026.9.24**
(commit `e3dd27ee2d8b011737a4eea8e3eb3d711ab78690`), the
`c419cf7c864ac0ee511dbd9f7091a8bba0b567ee` variant, and **v0.23.0**
(commit `2bd378ed1b8d6bf2192cb26e0a55ff3091e6bd19`). The same version as
the injection mod.

> **Gate removal does not mean your agent can hack NASA.**

Gate removal changes approval behaviour in the supported Hermes installation.
It is not a model capability upgrade, not access to other systems, and not a
guarantee of any result beyond the injection itself.

### What stays untouched

Changes made by `no-guard` are limited to Hermes program files and the
injection status/backup files in the Hermes home directory. It does **not**
modify persona, `.env`, `config.yaml`, skills, memory, sessions, or connection
settings (Telegram and other platforms). There is no re-setup: your
connections, accounts, and Hermes settings stay exactly as they were.
`config.yaml` is only read for the compatibility check. Everything is
reversible with `--uninstall`.

---

## Installation

Requires a **free, machine-bound license**. Validation is offline; the product
contacts no server after the license is received.

```bash
# 0. verify release integrity (must print PASS)
python3 tools/verify.py

# 1. print this machine's fingerprint
./bin/no-guard --machine

# 2. send the 64-hex value to @nohalu_free_license_bot
#      /license <fingerprint>
#    then save the reply as nohalu.license in the repo root

# 3. preview the plan — writes nothing
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --dry-run

# 4. apply
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard install

# 5. check the result
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --status
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --verify
```

Running `./bin/no-guard` **with no arguments only shows help** and changes
nothing. `install` is the command that applies the injection.

To revert:

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --uninstall
```

Details and optional env vars: [`docs/INSTALL.en.md`](docs/INSTALL.en.md).
Troubleshooting: [`docs/TROUBLESHOOTING.en.md`](docs/TROUBLESHOOTING.en.md).

## Updating

Already installed an earlier release? Update the repo and re-apply with the new
binary — your existing license stays valid:

```bash
git pull
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --uninstall
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard install
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --verify
```

Do not run `install` from the old release after `git pull` — always use
`./bin/no-guard` from the updated working tree.

The `--uninstall` step is not a formality: `install` over an existing
installation does not overwrite every component, so leftovers from the old
version can stay active. The order above is the only supported update path.

If `git pull` refuses with `You are not currently on a branch`, the repo sits on
a tag checkout. Use:

```bash
git fetch --tags origin
git reset --hard origin/main
```

## Commands

| Command | Function |
| --- | --- |
| `install` | apply the injection to the Hermes workspace (consent prompt) |
| `--dry-run` | preview the plan, no changes |
| `--status` | injection status in the Hermes workspace |
| `--verify` | verify integrity of the installed injection |
| `--audit` | semantic audit |
| `--repair` | re-apply after Hermes is updated |
| `--uninstall` | restore the original state |
| `--machine` | print this machine's fingerprint for license issuance |
| `--license-info` | inspect the local license (read-only, needs a valid license) |
| `--help` | help |

Without a license only `--help` and `--machine` are available; every other
mode requires a license valid for this machine.

## Structure

```
bin/no-guard              launcher
lib/no-guard.bundle       injection component
manifest.json             release identity + checksum
VERSION                   version and Hermes target
docs/                     compatibility, installation, license, troubleshooting
tools/verify.py           release checksum verification
```

## Compatibility

See [`docs/COMPATIBILITY.en.md`](docs/COMPATIBILITY.en.md). Use only on the
Hermes versions listed above.

## License

Code and release are under [`LICENSE`](LICENSE) (MIT). The machine-bound usage
license is issued free of charge by `@nohalu_free_license_bot`; see
[`docs/LICENSE.en.md`](docs/LICENSE.en.md).

---

*no-guard · free license · Hermes Agent 2026.9.24 (e3dd27ee), c419cf7c, and v0.23.0*
