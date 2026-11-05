# Compatibility

`no-guard` menargetkan **Hermes Agent 2026.9.24**
(commit `e3dd27ee2d8b011737a4eea8e3eb3d711ab78690`) dan varian
`c419cf7c864ac0ee511dbd9f7091a8bba0b567ee` — versi yang sama dengan mod
injection-nya.

| Item | Nilai |
| --- | --- |
| Hermes | 2026.9.24 / `e3dd27ee…` |
| Varian | `c419cf7c…` |
| OS | Linux (WSL2 didukung) |
| Python | interpreter bawaan instalasi Hermes |
| Arsitektur | x86_64 |

Jalankan `./bin/no-guard --dry-run` lalu `./bin/no-guard install` untuk
menerapkan. Jika versi Hermes tidak cocok, jangan lanjutkan; gunakan rilis yang
sesuai dengan instalasi kamu.

> Gate removal bukan peningkatan kemampuan: **bukan berarti dengan removal ini
> agent lo bakal bisa hack NASA.**
