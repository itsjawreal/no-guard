# Troubleshooting

Languages: [Indonesia](TROUBLESHOOTING.md) · **English** · [简体中文](TROUBLESHOOTING.zh.md)

| Symptom | Check |
| --- | --- |
| `no license found` | set `NO_GUARD_LICENSE`, or place it at `$HOME/.hermes/nohalu.license` |
| `license: signature not valid` | licence did not come from the official issuer → request again |
| `license not valid on this host` | licence was issued for another machine → run `--machine` here, request a new licence |
| `license: bad format` / `missing signature` | file is not a complete licence; download it again from the bot |
| unknown argument / two modes at once | check `./bin/no-guard --help`; one action per execution |
| `--dry-run` exits with non-zero rc | read the message on stderr (workspace not found / does not match); this is not a silent failure |
| `tools/verify.py` MISMATCH | release is damaged or incomplete → download again, do not apply |
| `--verify` fails | installed injection has drifted → run `--repair` (not `tools/verify.py`) |
| different Hermes version | see [`COMPATIBILITY.en.md`](COMPATIBILITY.en.md), do not force it |
| gateway unchanged | check `--status`; make sure the gateway uses the same workspace (set `HERMES_WORKSPACE=`) |
| Telegram connection dropped | not part of the injection; connection settings are unchanged, check the gateway service as usual |

`tools/verify.py` checks the **release checksum** (binary + bundle).
`./bin/no-guard --verify` checks the **state of the installed injection**. They
are different and do not replace each other.

## Exit codes

| Code | Meaning |
| --- | --- |
| `0` | success / as expected |
| `1` | general error (read the message on stderr) |
| `2` | audit / verification found a mismatched condition |
| `3` | injection active but not affecting the runtime, or repair not finished |
| `4` | no injection was successfully applied |
| `5` | restore not clean / old state still present |
| `6` | Hermes target not supported by this release |
| `64` | unknown argument or two modes at once |
| `67` | internal release error |
| `77` | licence missing, invalid, or not for this machine |
| `78` | internal verification-key error |
| `130` | cancelled (Ctrl-C / signal) |

## Help

```bash
./bin/no-guard --help
```
