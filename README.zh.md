# no-guard

语言：[Indonesia](README.md) · [English](README.en.md) · **简体中文**

**面向 Hermes 的门控移除注入组件** —— 适用于 **Hermes Agent 2026.9.24**
（提交 `e3dd27ee2d8b011737a4eea8e3eb3d711ab78690`）及
`c419cf7c864ac0ee511dbd9f7091a8bba0b567ee` 变体。与注入模块对应的版本完全一致。

> **门控移除并不代表你的 Agent 能黑进 NASA。**

门控移除只改变受支持 Hermes 安装中的审批行为。它不是模型能力提升，不是访问
其他系统的权限，也不保证注入范围之外的任何结果。

### 不会被改动的内容

`no-guard` 的改动仅限于 Hermes 程序文件，以及 Hermes 主目录中的注入状态与
备份文件。它**不会**修改 persona、`.env`、`config.yaml`、skills、记忆、会话，
也不会改动连接配置（Telegram 及其他平台）。无需重新配置：连接、账号和 Hermes
设置全部保持原样。`config.yaml` 仅在兼容性检查时被读取。所有改动都可以通过
`--uninstall` 还原。

---

## 安装

需要一份**免费的、绑定单台机器的许可**。校验完全离线；取得许可后产品不会连接
任何服务器。

```bash
# 0. 校验发布包完整性（必须输出 PASS）
python3 tools/verify.py

# 1. 输出本机指纹
./bin/no-guard --machine

# 2. 把 64 位十六进制值发给 @nohalu_free_license_bot
#      /license <fingerprint>
#    然后把回复保存为仓库根目录下的 nohalu.license

# 3. 预览计划 —— 不写入任何内容
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --dry-run

# 4. 应用
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard install

# 5. 检查结果
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --status
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --verify
```

直接运行 `./bin/no-guard` **且不带参数只显示帮助**，不会改动任何内容；`install`
才是执行写入的命令。

还原：

```bash
NO_GUARD_LICENSE=./nohalu.license ./bin/no-guard --uninstall
```

详细说明与可选环境变量：[`docs/INSTALL.zh.md`](docs/INSTALL.zh.md)。
故障排查：[`docs/TROUBLESHOOTING.zh.md`](docs/TROUBLESHOOTING.zh.md)。

## 命令

| 命令 | 功能 |
| --- | --- |
| `install` | 在 Hermes workspace 应用注入（需确认） |
| `--dry-run` | 预览计划，不做改动 |
| `--status` | 查看 Hermes workspace 中的注入状态 |
| `--verify` | 校验已安装注入的完整性 |
| `--audit` | 语义审计 |
| `--repair` | Hermes 更新后重新应用 |
| `--uninstall` | 还原到原始状态 |
| `--machine` | 输出本机指纹，用于签发许可 |
| `--license-info` | 查看本地许可（只读，需有效许可） |
| `--help` | 帮助 |

无许可时仅可使用 `--help` 与 `--machine`；其他模式都需要对本机有效的许可。

## 结构

```
bin/no-guard              启动器
lib/no-guard.bundle       注入组件
manifest.json             发布标识 + 校验和
VERSION                   版本与 Hermes 目标版本
docs/                     兼容性、安装、许可、故障排查
tools/verify.py           发布包校验和验证
```

## 兼容性

参见 [`docs/COMPATIBILITY.zh.md`](docs/COMPATIBILITY.zh.md)。仅可用于上方列出的
Hermes 版本。

## 许可

代码与发布包遵循 [`LICENSE`](LICENSE)（MIT）。绑定机器的使用许可由
`@nohalu_free_license_bot` 免费签发；详见 [`docs/LICENSE.zh.md`](docs/LICENSE.zh.md)。

---

*no-guard · 免费许可 · Hermes Agent 2026.9.24 / c419cf7c*
