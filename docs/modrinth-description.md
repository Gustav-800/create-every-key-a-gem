# Create: Every Key a Gem

**A client-side keyguard for the wireless redstone typewriter in [Create: Aeronautics](https://modrinth.com/mod/create-aeronautics).**

Press a key on the typewriter and it should send a redstone frequency — not open your backpack, map, or quest book. This addon makes that true.

## The problem

The typewriter is supposed to take over the keyboard while it is active. Internally, however, Simulated clears the vanilla `KeyMapping` state only at the very end of NeoForge's `InputEvent.Key` dispatch. By that point:

- vanilla has already queued the key mapping;
- other mods' `InputEvent.Key` listeners may already have run;
- any mod that handles raw key input is not affected by the cleanup at all.

So a key that is both a typewriter key and another mod's shortcut opens that mod's screen. The typewriter sees a screen, disconnects you, and the performance is interrupted.

## What it does

While the typewriter is **active**, or while you are **binding a key from a typewriter item**:

1. the key event is passed to Simulated's own typewriter handler first — frequency packets, sounds and key animations still work;
2. the event is then cancelled at the very beginning of `KeyboardHandler#keyPress`, before vanilla `KeyMapping` and before NeoForge `InputEvent.Key`;
3. no other mod's keyboard shortcut can fire.

`Esc` still exits the typewriter. `F2` (screenshot) and `F11` (fullscreen) remain available. Mouse shortcuts are not touched.

## How it works

A small Mixin injects at the head of `net.minecraft.client.KeyboardHandler#keyPress`. Simulated's handler is accessed reflectively, so this addon does not bundle or recompile any Simulated code. If a future Simulated version changes its API, the addon logs a warning and fails open — normal keyboard behavior — instead of crashing.

No server component, no extra packets, no world data.

## Requirements

| | |
| --- | --- |
| Minecraft | 1.21.1 |
| NeoForge | 21.1.228 or newer |
| Create: Aeronautics | 1.3.2+ (bundled Simulated 1.3.2+) |
| Create / Sable | required by Create: Aeronautics |
| Side | **Client only** |

## Installation

1. Install Minecraft 1.21.1 with NeoForge 21.1.228+.
2. Install Create: Aeronautics and its dependencies.
3. Put `create-every-key-a-gem-1.0.0.jar` into your `mods` folder.
4. Restart the game completely.

## Notes

- The addon only handles the **active typewriter** and **item binding** states. The typewriter's key-editor GUI is a normal screen and keeps its normal behavior, including JEI and other screen shortcuts.
- If you use a mod that polls physical keys directly through GLFW instead of `KeyMapping` or `InputEvent.Key`, that mod may still see the key. Most keybind mods use the standard paths and are covered.
- Not affiliated with Create, Create: Aeronautics, or Simulated.

## FAQ

**Does the server need this mod?**
No. It is client-side only and never sends its own packets.

**Will it work with a standalone Simulated installation?**
Yes, as long as `simulated` 1.3.2+ is present and provides the typewriter handler. The bundled Create: Aeronautics jar is the common case.

**Does it change the typewriter's behavior?**
No. The event is still delivered to Simulated's handler; the addon only stops it from continuing to vanilla and other mods.

**Can I configure which keys are blocked?**
Not in 1.0.0. The typewriter already owns the keyboard while active, so every keyboard event is claimed. `Esc`, `F2` and `F11` are the deliberate exceptions.

## Credits

- Create: Aeronautics / Simulated by the Simulated Team — this addon targets their typewriter.
- Mixin by SpongePowered.
- Icon and code by Gustav-800.

## License

MIT.

---

## 中文说明

**机械动力：字字珠玑** 是 Create: Aeronautics 无线红石打字机的客户端按键保护附属。

打字机激活后本应接管键盘，但 Simulated 直到 `InputEvent.Key` 分发末尾才清理原版按键状态。此时原版已经排入按键，其他模组的监听器也可能已经执行；如果某个键同时是打字机键和其他模组的快捷键，就会弹出那个模组的界面，打字机随即断开。

本模组在 `KeyboardHandler#keyPress` 入口处接管按键：先把事件交给打字机处理器，保证频率包、声音和按键动画正常，然后取消事件，使其不再进入原版 `KeyMapping` 和 NeoForge `InputEvent.Key`。因此打字时不会触发其他模组的键盘快捷键。

- `Esc` 仍可退出打字机；`F2` / `F11` 保留。
- 仅客户端，服务器不需要安装。
- 不添加物品、方块或网络包。
- 对 Simulated 使用反射调用；将来 API 变化时会记录警告并回退到正常键盘行为，不会崩溃。

安装：把 jar 放进 `mods`，完全重启游戏。
