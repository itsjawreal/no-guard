# 安装

语言：[Indonesia](INSTALL.md) · [English](INSTALL.en.md) · **简体中文**

## 1. 校验发布包

```bash
python3 tools/verify.py
```

结果必须为 `PASS`。若输出 `MISMATCH`，请勿使用该发布包。

## 2. 免费许可

```bash
./bin/no-guard --machine
```

把输出的 64 位十六进制值发给 `@nohalu_free_license_bot`：

```
/license <fingerprint>
```

把回复的文档保存为仓库根目录下的 `nohalu.license`。

## 3. 预览计划

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --dry-run
```

`--dry-run` 不写入任何内容。请先阅读输出，并仅在 Hermes 版本与
[`COMPATIBILITY.zh.md`](COMPATIBILITY.zh.md) 一致时继续。若退出码非 0，请阅读
stderr 中的提示 —— workspace 未找到或版本不匹配。

## 4. 应用

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard install
```

`install` 才是执行写入的命令。直接运行 `./bin/no-guard` 且不带参数只显示帮助，
不会改动任何内容。

不会被改动的内容：persona、`.env`、`config.yaml`（仅读取）、skills、记忆、会话，
以及 Telegram／其他平台的连接配置。无需重新配置 Hermes，也无需重新连接账号。
详见 [`README.zh.md`](../README.zh.md)。

然后检查：

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --status
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --verify
```

## 还原

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --uninstall
```

## 可选环境变量

| 变量 | 功能 |
| --- | --- |
| `NO_GUARD_LICENSE` | 许可文件路径（默认 `$HOME/.hermes/nohalu.license`） |
| `HERMES_WORKSPACE` | 强制指定目标 workspace |
| `HERMES_PYTHON` | `--audit` 使用的解释器 |
| `NO_RESTART=1` | 不重启 gateway |
| `ASSUME_YES=1` | 跳过确认提示（脚本化使用） |
