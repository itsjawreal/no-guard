# 免费许可

语言：[Indonesia](LICENSE.md) · [English](LICENSE.en.md) · **简体中文**

`no-guard` 使用**免费的、绑定单台机器的许可**。

- 签发：`@nohalu_free_license_bot`（Telegram），仅申请时需要联网一次。
- 校验：**离线** —— 取得许可后产品不会连接任何服务器。
- 范围：一个机器指纹，无有效期限制。
- 格式：`nohalu.license`（机器人回复的文本文档）。

## 流程

```bash
./bin/no-guard --machine          # 64 位十六进制
# → 在机器人中发送 /license <64-hex>
# → 保存为 nohalu.license
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --license-info
```

`--license-info` 只查看许可状态，不做任何改动。该模式仍需要对本机有效的许可；
无许可时仅可使用 `--help` 与 `--machine`。

## 文件查找顺序

引擎按以下顺序查找许可：

1. `NO_GUARD_LICENSE`
2. `$HOME/.hermes/nohalu.license`（默认位置）

## 限制

许可在另一台机器上无效。第二台机器请用该机器的指纹重新申请。机器人对每个账号
每天的签发次数有限制。

## 代码授权

参见 [`../LICENSE`](../LICENSE)（MIT，英文原文为正式授权文本）。上面的使用许可
是运行已签名发布包的权限；两者均为免费。
