# Compatibility

Bahasa: **Indonesia** · [English](COMPATIBILITY.en.md) · [简体中文](COMPATIBILITY.zh.md)

`no-guard` menargetkan **Hermes Agent 2026.9.24**
(commit `e3dd27ee2d8b011737a4eea8e3eb3d711ab78690`) dan varian
`c419cf7c864ac0ee511dbd9f7091a8bba0b567ee` dan **v0.23.0** (`2bd378ed1b8d6bf2192cb26e0a55ff3091e6bd19`) — versi yang sama dengan mod
injection-nya.

| Item | Nilai |
| --- | --- |
| Hermes | 2026.9.24 / `e3dd27ee…`, `c419cf7c…`, v0.23.0 / `2bd378ed…` |
| OS | Linux (WSL2 didukung) |
| Python | interpreter bawaan instalasi Hermes |
| Arsitektur | x86_64 |

Jalankan `./bin/no-guard --dry-run` lalu `./bin/no-guard install` untuk
menerapkan. Jika versi Hermes tidak cocok, jangan lanjutkan; gunakan rilis yang
sesuai dengan instalasi kamu.

> Gate removal bukan peningkatan kemampuan: **bukan berarti dengan removal ini
> agent lo bakal bisa hack NASA.**
