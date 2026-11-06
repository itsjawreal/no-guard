## 1.1.5 — error paths, honest diagnostics

Everything here was found by widening the check that inspects what the tool
actually prints, then running the release against a real Hermes tree in every
mode.

### Messages on the paths that only appear when something goes wrong

Failure messages are the ones a user reads most closely, and they were the least
covered. They are now written in the same plain language as the rest of the
output: what happened, and what to do about it.

### A diagnostic that blamed the wrong thing

`--audit` reported a workspace as "inconsistent or corrupt" whenever the Python
interpreter it found could not import a third-party package. The workspace was
fine — the interpreter was incomplete. It now names the actual cause and tells
you how to point the tool at a working interpreter:

```
✘ ERROR: interpreter Python yang dipakai tidak punya dependensi Hermes (ruamel)
         — set HERMES_PYTHON=/path/ke/venv/bin/python3 lalu ulangi
```

### Status labels

`stamp` is now `versi`, and the runtime section describes what it means
("perubahan terpasang, tapi kode lama masih dimuat") instead of naming internal
markers and bytecode.

### Verification performed

- Every mode run against a real Hermes tree, output read line by line
- Restore is byte-exact: 22,551 files compared before install and after
  `--uninstall`, zero differences, no leftover files
- Concurrent installs on one workspace, paths with spaces and non-ASCII,
  symlinked workspace, corrupted state file, read-only workspace, and a
  `kill -9` mid-install followed by a rerun — all behave correctly
- Existing licenses remain valid; the engine is unchanged

Hermes Agent 2026.9.24 / c419cf7c / v0.23.0
