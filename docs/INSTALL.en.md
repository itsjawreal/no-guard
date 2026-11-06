# Install

Languages: [Indonesia](INSTALL.md) · **English** · [简体中文](INSTALL.zh.md)

## 1. Verify the release

```bash
python3 tools/verify.py
```

The result must be `PASS`. If it prints `MISMATCH`, do not use that release.

## 2. Free license

```bash
./bin/no-guard --machine
```

Send the 64-hex value to `@nohalu_free_license_bot`:

```
/license <fingerprint>
```

Save the replied document as `nohalu.license` in the repo root.

## 3. Preview the plan

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --dry-run
```

`--dry-run` writes nothing. Read the output and continue only if the Hermes
version matches [`COMPATIBILITY.en.md`](COMPATIBILITY.en.md). If it exits with
a non-zero rc, read the message on stderr — the workspace was not found or does
not match.

## 4. Apply

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard install
```

`install` is the command that writes. Running `./bin/no-guard` with no
arguments only shows help and changes nothing.

What stays untouched: persona, `.env`, `config.yaml` (read only), skills,
memory, sessions, and connection settings for Telegram/other platforms. There
is no need to set Hermes up again or reconnect accounts. See
[`README.en.md`](../README.en.md#what-stays-untouched).

Then check:

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --status
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --verify
```

## Revert

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --uninstall
```

## Optional env vars

| Var | Function |
| --- | --- |
| `NO_GUARD_LICENSE` | license path (default `$HOME/.hermes/nohalu.license`) |
| `HERMES_WORKSPACE` | force the target workspace |
| `HERMES_PYTHON` | interpreter for `--audit` |
| `NO_RESTART=1` | do not restart the gateway |
| `ASSUME_YES=1` | skip the consent prompt (scripting) |
