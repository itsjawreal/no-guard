# Troubleshooting

Bahasa: **Indonesia** · [English](TROUBLESHOOTING.en.md) · [简体中文](TROUBLESHOOTING.zh.md)

| Gejala | Periksa |
| --- | --- |
| `no license found` | set `NO_GUARD_LICENSE`, atau taruh di `$HOME/.hermes/nohalu.license` |
| `license: signature not valid` | lisensi bukan dari penerbit resmi → minta lagi |
| `license not valid on this host` | lisensi terbit untuk mesin lain → jalankan `--machine` di mesin ini, minta lisensi baru |
| `license: bad format` / `missing signature` | file bukan lisensi utuh; unduh ulang dari bot |
| argumen tidak dikenal / dua mode sekaligus | cek `./bin/no-guard --help`; satu aksi per eksekusi |
| `--dry-run` keluar dengan rc bukan 0 | baca pesan di stderr (workspace tidak ditemukan / tidak cocok); ini bukan kegagalan diam |
| `tools/verify.py` MISMATCH | rilis rusak atau tidak lengkap → unduh ulang, jangan diterapkan |
| `--verify` gagal | injeksi terpasang menyimpang → jalankan `--repair` (bukan `tools/verify.py`) |
| Versi Hermes beda | lihat [`COMPATIBILITY.md`](COMPATIBILITY.md), jangan dipaksakan |
| Gateway tidak berubah | cek `--status`; pastikan workspace yang dipakai gateway sama (set `HERMES_WORKSPACE=`) |
| Koneksi Telegram putus | bukan bagian dari injeksi; konfigurasi koneksi tidak diubah, cek layanan gateway seperti biasa |

`tools/verify.py` memeriksa **checksum rilis** (biner + bundle).
`./bin/no-guard --verify` memeriksa **kondisi injeksi yang terpasang**. Keduanya
berbeda dan tidak saling menggantikan.

## Exit code

| Kode | Arti |
| --- | --- |
| `0` | berhasil / sesuai |
| `1` | kesalahan umum (baca pesan di stderr) |
| `2` | audit / verifikasi menemukan kondisi tidak sesuai |
| `3` | injeksi aktif tetapi tidak berefek ke runtime, atau repair belum selesai |
| `4` | tidak ada injeksi yang berhasil diterapkan |
| `5` | restore tidak bersih / state lama masih ada |
| `6` | target Hermes tidak didukung oleh rilis ini |
| `64` | argumen tidak dikenal atau dua mode sekaligus |
| `67` | kesalahan internal rilis |
| `77` | lisensi tidak ada, tidak valid, atau bukan untuk mesin ini |
| `78` | kesalahan internal kunci verifikasi |
| `130` | dibatalkan (Ctrl-C / sinyal) |

## Bantuan

```bash
./bin/no-guard --help
```
