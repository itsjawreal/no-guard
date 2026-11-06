# 兼容性

语言：[Indonesia](COMPATIBILITY.md) · [English](COMPATIBILITY.en.md) · **简体中文**

`no-guard` 面向 **Hermes Agent 2026.9.24**
（提交 `e3dd27ee2d8b011737a4eea8e3eb3d711ab78690`）及
`c419cf7c864ac0ee511dbd9f7091a8bba0b567ee` 变体 —— 与注入模块对应的版本完全一致。

| 项目 | 值 |
| --- | --- |
| Hermes | 2026.9.24 / `e3dd27ee…` |
| 变体 | `c419cf7c…` |
| 操作系统 | Linux（支持 WSL2） |
| Python | Hermes 安装自带的解释器 |
| 架构 | x86_64 |

依次运行 `./bin/no-guard --dry-run` 与 `./bin/no-guard install` 即可应用。若 Hermes
版本不匹配，请勿继续；请使用与你的安装版本对应的发布包。

> 门控移除并非能力升级：**这并不代表你的 Agent 能黑进 NASA。**
