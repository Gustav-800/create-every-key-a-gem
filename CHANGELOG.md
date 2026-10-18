# Changelog

## 1.0.0 — 2026-10-18

### Added

- Client-side keyguard for the Create: Aeronautics wireless redstone typewriter.
- Keyboard events are claimed at the head of `KeyboardHandler#keyPress` while the
  typewriter is active or while binding a key from a typewriter item.
- Keys are forwarded to Simulated's typewriter handler before being cancelled.
- `Esc` exits the typewriter; `F2` and `F11` remain available.
- Reflection-based Simulated integration: the addon fails open if the installed
  Simulated version changes its API.

### Requirements

- Minecraft 1.21.1
- NeoForge 21.1.228+
- Create: Aeronautics 1.3.2+ (Simulated 1.3.2+)
- Client only
