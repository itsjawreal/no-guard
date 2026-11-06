# 故障排查

语言：[Indonesia](TROUBLESHOOTING.md) · [English](TROUBLESHOOTING.en.md) · **简体中文**

| 现象 | 检查 |
| --- | --- |
| `no license found` | 设置 `NO_GUARD_LICENSE`，或放到 `$HOME/.hermes/nohalu.license` |
| `license: signature not valid` | 许可并非来自官方签发方 → 重新申请 |
| `license not valid on this host` | 许可签给了另一台机器 → 在本机运行 `--machine` 并重新申请 |
| `license: bad format` / `missing signature` | 文件不是完整许可；从机器人重新下载 |
| 参数未知 / 同时指定两个模式 | 查看 `./bin/no-guard --help`；每次执行只能有一个动作 |
| 安装还没来得及回答就显示 `dibatalkan oleh user` | 使用最新版本，或加 `ASSUME_YES=1` 跳过确认 |
| `--dry-run` 退出码非 0 | 阅读 stderr 提示（workspace 未找到／不匹配）；这不是静默失败 |
| `tools/verify.py` 输出 MISMATCH | 发布包损坏或不完整 → 重新下载，不要应用 |
| `--verify` 失败 | 已安装注入发生偏离 → 运行 `--repair`（不是 `tools/verify.py`） |
| 隐藏 workspace 下 `/mod` 出现漂移提示，或 `--status` 在 gateway 安装后启动时仍建议重启 | 使用最新版本；这是状态显示的修正，注入状态本身不变 |
| 更新后 `/mod` 仍显示 `STALE — 25 entri` 或 `bytecode basi` | 确认新版本确实已应用；若仍出现，先运行 `--uninstall` 再 `install` —— 在旧安装之上直接 `install` 不会覆盖 `mod_status.py` |
| `--verify` 返回 rc `3` | 注入已生效，但 gateway 导入的是另一个 workspace；把 `HERMES_WORKSPACE=` 指向 gateway 实际使用的 workspace —— 这不是注入失败 |
| Hermes 版本不同 | 参见 [`COMPATIBILITY.zh.md`](COMPATIBILITY.zh.md)，不要强制使用 |
| gateway 未变化 | 检查 `--status`；确认 gateway 使用同一 workspace（设置 `HERMES_WORKSPACE=`） |
| Telegram 连接断开 | 与注入无关；连接配置未被改动，按常规检查 gateway 服务 |

`tools/verify.py` 检查**发布包校验和**（二进制 + bundle）。
`./bin/no-guard --verify` 检查**已安装注入的状态**。两者不同，不能互相替代。

## 退出码

| 代码 | 含义 |
| --- | --- |
| `0` | 成功／符合预期 |
| `1` | 通用错误（阅读 stderr 提示） |
| `2` | 审计／校验发现不符合预期的状态 |
| `3` | 注入已激活但未影响运行时，或 repair 未完成 |
| `4` | 没有任何注入成功应用 |
| `5` | 还原不干净／旧状态仍存在 |
| `6` | 本发布包不支持该 Hermes 目标 |
| `64` | 参数未知或同时指定两个模式 |
| `67` | 发布包内部错误 |
| `77` | 许可缺失、无效，或不适用于本机 |
| `78` | 校验密钥内部错误 |
| `130` | 已取消（Ctrl-C／信号） |

## 帮助

```bash
./bin/no-guard --help
```
