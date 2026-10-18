# 发布元数据 / Release metadata

GitHub 用户名：`Gustav-800`；Modrinth / MC百科 链接在发布后补上。

## 名称 / Names

| 字段 | 值 |
| --- | --- |
| 中文名 | 机械动力：字字珠玑 |
| 英文名 | **Create: Every Key a Gem** |
| 内部 mod id | `every_key_a_gem` |
| Modrinth slug | `create-every-key-a-gem` |
| GitHub 仓库 | `create-every-key-a-gem` |
| 简称 | 暂不填写（百科指南不建议生造缩写；社区常用后可补 `EKAG`） |
| 版本 | `1.0.0` |
| 许可证 | MIT |
| 作者 | Gustav-800（如要换署名，改这里、`LICENSE`、`neoforge.mods.toml`） |

### 英文名说明

**推荐：Create: Every Key a Gem**

- “字字珠玑”直译是 “every word a gem”；打字机输出的是按键，所以把 word 换成 key。
- `Every Key a Gem` 保留了“每一个……都像珠玉”的结构，同时把“键盘/按键”点出来。
- 短、好记、可搜索；`Create:` 前缀说明它是机械动力系附属。
- 备选：
  - **Create: Every Word a Gem** — 更直译，但和“按键”关系弱。
  - **Create: Keygem** — 更品牌化、更短，但“信”稍弱，且容易被误认为物品名。
  - **Create: Pearls of the Keyboard** — 更诗意，但偏长。

## 短简介 / Summary

**English (Modrinth, ≤256 chars):**

> Keeps the Create: Aeronautics wireless typewriter in control of your keyboard: while it is active, mapped shortcut keys no longer trigger other mods. Client-side, no config.

**中文（百科/群宣）：**

> 让机械动力：航空学的无线红石打字机真正接管键盘——打字时，绑定的快捷键不再触发其他模组的功能。仅客户端，无需配置。

## MC百科“编辑器”简介

> 让机械动力：航空学的无线红石打字机真正接管键盘。激活打字机后，绑定的快捷键不再触发其他模组的界面，无线红石频率、声音和按键动画保持原样。仅客户端，不添加物品或方块。

## 分类与标签 / Categories & tags

| 平台 | 填写 |
| --- | --- |
| Modrinth 分类 | `Utility`、`Technology` |
| Modrinth 环境 | **Client only** |
| Modrinth 加载器 | NeoForge |
| Modrinth 游戏版本 | 1.21.1 |
| 百科分类 | 辅助 |
| 百科元素 | 辅助、红石（以百科实际选项为准） |
| 百科模式 | SSP / SMP |
| 百科标签 | 打字机、快捷键、客户端、红石、航空学、机械动力 |
| GitHub topics | `minecraft`, `minecraft-mod`, `neoforge`, `create`, `create-aeronautics`, `typewriter`, `keybind`, `redstone`, `client-side` |

## 依赖 / Dependencies

| 关系 | 项目 | 说明 |
| --- | --- | --- |
| 必需 | Create (`create`) | 机械动力本体 |
| 必需 | Create: Aeronautics (`create-aeronautics`) | 提供 Simulated 与打字机 |
| 必需 | Sable (`sable`) | Create: Aeronautics 的前置；由父模组带入 |
| 必需 | NeoForge 21.1.228+ | 加载器 |
| 可选 | 无 | 没有软联动 |

> 本模组在 `neoforge.mods.toml` 中声明的是对 `simulated`（Create: Aeronautics 内嵌）的必需依赖。Modrinth / 百科页面按用户视角填写 Create 与 Create: Aeronautics 即可。

## 链接 / Links

| 字段 | 值 |
| --- | --- |
| GitHub | `https://github.com/Gustav-800/create-every-key-a-gem` |
| Issues | `https://github.com/Gustav-800/create-every-key-a-gem/issues` |
| Modrinth | `https://modrinth.com/mod/create-every-key-a-gem`（发布后） |
| MC百科 | 发布后填写 |
| 父模组 Modrinth | https://modrinth.com/mod/create-aeronautics |
| 父模组 MC百科 | https://www.mcmod.cn/class/26350.html |
| Create Modrinth | https://modrinth.com/mod/create |
| Create MC百科 | https://www.mcmod.cn/class/2021.html |
| Sable Modrinth | https://modrinth.com/mod/sable |

## 版本文件 / Version file

| 字段 | 值 |
| --- | --- |
| 文件名 | `create-every-key-a-gem-1.0.0.jar` |
| 版本号 | `1.0.0` |
| 版本标题 | `1.0.0 — Initial release` |
| 发布通道 | Release |
| 游戏版本 | 1.21.1 |
| 加载器 | NeoForge |
| 依赖 | Create（必需）、Create: Aeronautics（必需） |
| Changelog | 见 `CHANGELOG.md` 的 1.0.0 段 |

## GitHub Release 文案

标题：

```
Create: Every Key a Gem 1.0.0
```

正文：

```markdown
## Create: Every Key a Gem 1.0.0

First release. A client-side keyguard for the Create: Aeronautics wireless typewriter.

### Fixed

- Mapped shortcut keys no longer trigger other mods while the typewriter is active.
- Keys are still delivered to the typewriter: frequency packets, sounds and key animations work as before.
- `Esc` exits the typewriter; `F2` and `F11` remain available.

### Requirements

- Minecraft 1.21.1
- NeoForge 21.1.228+
- Create: Aeronautics 1.3.2+ (bundled Simulated 1.3.2+)
- Client only

### Install

Drop the jar into your `mods` folder and restart the game.
```
