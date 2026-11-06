# Install

Bahasa: **Indonesia** · [English](INSTALL.en.md) · [简体中文](INSTALL.zh.md)

## 1. Verifikasi rilis

```bash
python3 tools/verify.py
```

Hasil harus `PASS`. Kalau `MISMATCH`, jangan pakai rilis itu.

## 2. Lisensi gratis

```bash
./bin/no-guard --machine
```

Kirim 64-hex yang muncul ke `@nohalu_free_license_bot`:

```
/license <fingerprint>
```

Simpan dokumen balasan sebagai `nohalu.license` di root repo ini.

## 3. Cek rencana

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --dry-run
```

`--dry-run` tidak menulis apa pun. Baca hasilnya, lalu lanjutkan hanya kalau
versi Hermes sesuai [`COMPATIBILITY.md`](COMPATIBILITY.md). Kalau keluar dengan
rc bukan 0, baca pesan di stderr — workspace tidak ditemukan atau tidak cocok.

## 4. Terapkan

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard install
```

`install` adalah perintah yang menulis. `./bin/no-guard` tanpa argumen hanya
menampilkan bantuan dan tidak mengubah apa pun.

Yang tidak tersentuh: persona, `.env`, `config.yaml` (hanya dibaca), skills,
memori, sesi, dan konfigurasi koneksi Telegram/platform lain. Tidak perlu
setup Hermes dari awal atau menyambungkan ulang akun. Rincian ada di
[`README.md`](../README.md#yang-tidak-berubah).

Lalu cek:

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --status
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --verify
```

## Kembali ke semula

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --uninstall
```

## Env opsional

| Var | Fungsi |
| --- | --- |
| `NO_GUARD_LICENSE` | path lisensi (default `$HOME/.hermes/nohalu.license`) |
| `HERMES_WORKSPACE` | paksa workspace target |
| `HERMES_PYTHON` | interpreter untuk `--audit` |
| `NO_RESTART=1` | tanpa restart gateway |
| `ASSUME_YES=1` | skip prompt (scripting) |
