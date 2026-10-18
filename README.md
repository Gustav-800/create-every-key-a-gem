# Create: Every Key a Gem

**机械动力：字字珠玑** — a client-side keyguard for the wireless redstone typewriter in
[Create: Aeronautics](https://modrinth.com/mod/create-aeronautics).

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Minecraft](https://img.shields.io/badge/Minecraft-1.21.1-62b47a.svg)](https://www.minecraft.net/)
[![NeoForge](https://img.shields.io/badge/NeoForge-21.1.228%2B-f16436.svg)](https://neoforged.net/)

> 字字珠玑：每一个按键，都应落成你想要的信号。

## The problem / 问题

The wireless typewriter claims the keyboard, but Simulated cleans up vanilla
`KeyMapping` clicks only at the very end of NeoForge's `InputEvent.Key` dispatch.
By then vanilla has already queued the key mapping, and other mods' key listeners
may already have run. Press a key that is also another mod's shortcut and that
mod's screen opens, which forces the typewriter to disconnect.

无线红石打字机本应接管键盘，但 Simulated 直到 `InputEvent.Key` 分发末尾才清理
`KeyMapping`。此时原版已经排入按键，其他模组的监听器也可能已经执行——按下绑定了
其它模组快捷键的键，就会弹出那个模组的界面，打字机随之断开。

## What it does / 功能

While the typewriter is **active** (or while binding a key from a typewriter item):

- the key event is handed to Simulated's own typewriter handler first, so the
  typewriter still sends its frequency packet and plays its sound;
- the event is then cancelled at the head of `KeyboardHandler#keyPress`, before
  vanilla `KeyMapping` and before NeoForge `InputEvent.Key`;
- therefore no other mod's shortcut can fire while you are typing.

`Esc` still exits the typewriter, and `F2` / `F11` remain available.

打字机**激活**时（以及手持打字机物品绑定按键时）：

- 先把按键交给 Simulated 自己的打字机处理器，频率包、声音、按键记录都照常；
- 然后在 `KeyboardHandler#keyPress` 的入口取消事件，早于原版 `KeyMapping` 和
  NeoForge `InputEvent.Key`；
- 因此打字时不会再触发其他模组的快捷键。

`Esc` 仍可退出打字机，`F2` / `F11` 保留原版功能。

## Requirements / 环境

| | |
| --- | --- |
| Minecraft | 1.21.1 |
| NeoForge | 21.1.228 or newer |
| Create: Aeronautics | 1.3.2+ (bundled Simulated 1.3.2+) |
| Side | **Client only** — do not install on a dedicated server |

## Download / 下载

- [GitHub Releases](https://github.com/Gustav-800/create-every-key-a-gem/releases)
- Modrinth: `https://modrinth.com/mod/create-every-key-a-gem`（审核通过后可用）

## Installation / 安装

1. Install Minecraft 1.21.1 with NeoForge 21.1.228+.
2. Install Create: Aeronautics (and its dependencies, Create and Sable).
3. Drop `create-every-key-a-gem-1.0.0.jar` into the instance's `mods` folder.
4. Restart the game completely.

## How it works / 原理

The addon uses a small Mixin at the head of
`net.minecraft.client.KeyboardHandler#keyPress`. Simulated's handler is accessed
reflectively, so the addon does not need to compile against Simulated's jar. If
Simulated changes its API, the addon logs a warning and fails open (normal
keyboard behaviour) instead of crashing.

本模组在 `KeyboardHandler#keyPress` 的 HEAD 注入。对 Simulated 的处理器使用反射调用，
因此编译不依赖 Simulated 的 jar；如果将来 Simulated 修改 API，模组会记录警告并回退到
正常键盘行为，而不是让游戏崩溃。

## Compatibility / 兼容性

- Client-side only; works on any server because it never sends extra packets.
- Does not touch mouse shortcuts; only keyboard input is claimed.
- The typewriter's key-editor GUI is a normal `Screen` and is left alone.
- Not affiliated with Create, Create: Aeronautics, or Simulated.

## Building / 构建

### PowerShell (verified)

Requires a local 1.21.1 NeoForge installation with the client jar in `libraries`:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\build.ps1 `
  -MinecraftDir 'C:\path\to\.minecraft'
```

The jar is written to `build/libs/create-every-key-a-gem-1.0.0.jar`.

### Gradle (for contributors)

```bash
./gradlew build       # macOS / Linux
.\gradlew.bat build   # Windows
```

The Gradle build downloads NeoForge from `maven.neoforged.net`. If that host is
unreachable on your network (common on some connections), use the PowerShell
build above; it compiles against the NeoForge jars already installed by the
launcher.

## License / 许可

MIT — see [LICENSE](LICENSE).
