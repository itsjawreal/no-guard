# Free licence

Bahasa: **Indonesia** · [English](LICENSE.en.md) · [简体中文](LICENSE.zh.md)

`no-guard` memakai **lisensi gratis, terikat 1 mesin**.

- Penerbitan: `@nohalu_free_license_bot` (Telegram), online sekali saat minta.
- Validasi: **offline** — produk tidak menghubungi server setelah lisensi ada.
- Cakupan: satu fingerprint mesin, tanpa kedaluwarsa.
- Format: `nohalu.license` (dokumen teks dari bot).

## Alur

```bash
./bin/no-guard --machine          # 64-hex
# → /license <64-hex> di bot
# → simpan sebagai nohalu.license
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --license-info
```

`--license-info` menampilkan status lisensi tanpa mengubah apa pun. Mode ini
tetap memerlukan lisensi yang valid untuk mesin ini; tanpa lisensi, hanya
`--help` dan `--machine` yang bisa dipakai.

## Letak file

Engine mencari lisensi pada urutan ini:

1. `NO_GUARD_LICENSE`
2. `$HOME/.hermes/nohalu.license` (letak default)

## Batas

Lisensi tidak berlaku di mesin lain. Untuk mesin kedua, minta lisensi baru
dengan fingerprint mesin itu. Bot membatasi penerbitan per akun per hari.

## Grant kode

Lihat [`../LICENSE`](../LICENSE) (MIT). Lisensi pakai di atas adalah izin
menjalankan rilis yang sudah ditandatangani; keduanya gratis.
