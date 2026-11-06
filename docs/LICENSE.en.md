# Free licence

Languages: [Indonesia](LICENSE.md) · **English** · [简体中文](LICENSE.zh.md)

`no-guard` uses a **free licence bound to one machine**.

- Issuance: `@nohalu_free_license_bot` (Telegram), online once when requested.
- Validation: **offline** — the product contacts no server once the licence exists.
- Scope: one machine fingerprint, no expiration.
- Format: `nohalu.license` (a text document from the bot).

## Flow

```bash
./bin/no-guard --machine          # 64-hex
# → /license <64-hex> in the bot
# → save as nohalu.license
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --license-info
```

`--license-info` shows licence status without changing anything. This mode
still requires a licence valid for this machine; without one, only `--help` and
`--machine` are available.

## File lookup

The engine looks for the licence in this order:

1. `NO_GUARD_LICENSE`
2. `$HOME/.hermes/nohalu.license` (default location)

## Limits

A licence is not valid on another machine. For a second machine, request a new
licence using that machine's fingerprint. The bot limits issuance per account
per day.

## Code grant

See [`../LICENSE`](../LICENSE) (MIT, English text — the authoritative grant).
The usage licence above is permission to run the signed release; both are free.
