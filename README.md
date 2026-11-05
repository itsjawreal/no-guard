# no-guard

**Hermes injection for gate removal** — untuk **Hermes Agent 2026.9.24**
(commit `e3dd27ee2d8b011737a4eea8e3eb3d711ab78690`) dan varian
`c419cf7c864ac0ee511dbd9f7091a8bba0b567ee`. Versi yang sama dengan mod
injection-nya.

> **bukan berarti dengan removal ini agent lo bakal bisa hack NASA.**

Gate removal mengubah perilaku persetujuan pada instalasi Hermes yang didukung.
Ini bukan peningkatan kemampuan model, bukan akses ke sistem lain, dan bukan
jaminan hasil apa pun di luar cakupan injeksi itu sendiri.

---

## Instalasi

Butuh **lisensi gratis, terikat 1 mesin**. Validasi dilakukan offline; produk
tidak menghubungi server setelah lisensi diterima.

```bash
# 0. verifikasi keutuhan rilis (harus PASS)
python3 tools/verify.py

# 1. fingerprint mesin ini
./bin/no-guard --machine

# 2. kirim 64-hex itu ke @nohalu_free_license_bot
#      /license <fingerprint>
#    lalu simpan balasan sebagai nohalu.license di root repo ini

# 3. cek rencana — tidak menulis apa pun
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --dry-run

# 4. terapkan
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard install

# 5. cek hasil
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --status
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --verify
```

`./bin/no-guard` **tanpa argumen hanya menampilkan bantuan** dan tidak mengubah
apa pun. Perintah untuk menerapkan adalah `install`.

Kembali ke kondisi semula:

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --uninstall
```

Detail dan env opsional: [`docs/INSTALL.md`](docs/INSTALL.md). Pemecahan masalah:
[`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

## Perintah

| Perintah | Fungsi |
| --- | --- |
| `install` | terapkan injeksi pada workspace Hermes (consent prompt) |
| `--dry-run` | rencana penerapan, tanpa perubahan |
| `--status` | status injeksi pada workspace Hermes |
| `--verify` | verifikasi integritas injeksi terpasang |
| `--audit` | audit semantik |
| `--repair` | terapkan ulang setelah Hermes diperbarui |
| `--uninstall` | kembalikan ke kondisi semula |
| `--machine` | cetak fingerprint mesin untuk penerbitan lisensi |
| `--license-info` | cek lisensi lokal (read-only, butuh lisensi valid) |
| `--help` | bantuan |

Tanpa lisensi hanya `--help` dan `--machine` yang bisa dipakai; mode lain
memerlukan lisensi yang valid untuk mesin ini.

## Struktur

```
bin/no-guard              launcher
lib/no-guard.bundle       komponen injeksi
manifest.json             identitas rilis + checksum
VERSION                   versi dan target Hermes
docs/                     kompatibilitas, instalasi, lisensi, troubleshoot
tools/verify.py           verifikasi checksum rilis
```

## Kompatibilitas

Lihat [`docs/COMPATIBILITY.md`](docs/COMPATIBILITY.md). Gunakan hanya pada versi
Hermes yang tercantum di atas.

## Lisensi

Kode dan rilis ini berada di bawah [`LICENSE`](LICENSE) (MIT). Lisensi pakai
(machine-bound) diterbitkan gratis oleh `@nohalu_free_license_bot`; detail ada di
[`docs/LICENSE.md`](docs/LICENSE.md).

---

*no-guard · free license · Hermes Agent 2026.9.24 / c419cf7c*
