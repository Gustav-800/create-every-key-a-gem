# Test report / 测试记录

## Build

| | |
| --- | --- |
| Artifact | `create-every-key-a-gem-1.0.0.jar` |
| Size | 121,366 bytes |
| SHA-256 | `6456CB738E189EF2F8B58C898F74AC40FD4F2A4E4D020D2C52EF7199D90DB9DC` |
| JDK | OpenJDK 21.0.7 (Mojang `java-runtime-delta`) |
| Target | Minecraft 1.21.1, NeoForge 21.1.262, Mixin 0.8.7 |
| Build used for release | `build.ps1` |

> The Gradle/ModDevGradle build is configured in the repository, but this
> machine could not reach `maven.neoforged.net` (connection timeout), so it
> could not be used to produce the release jar. The PowerShell build compiles
> against the NeoForge jars already installed by the launcher and is the
> verified path.

## 1. Isolated mixin test

A separate game directory was launched with only:

- NeoForge 21.1.262
- `create-every-key-a-gem-1.0.0.jar`
- a test-only `simulated` stub mod (mod id `simulated`, version 1.3.2) providing
  `LinkedTypewriterInteractionHandler#getMode` and `#onKeyPress`

Launch flags included `-Dmixin.debug.verbose=true -Dmixin.debug.export=true`.

Evidence:

```
Create: Every Key a Gem 1.0.0 (every_key_a_gem)
Selecting config every_key_a_gem.mixins.json
Preparing every_key_a_gem.mixins.json (1)
Mixing KeyboardHandlerMixin from every_key_a_gem.mixins.json into net.minecraft.client.KeyboardHandler
```

The exported transformed class contained:

```
private void handler$zza000$every_key_a_gem$everykeyagem$captureTypewriterKeys(
    long, int, int, int, int, org.spongepowered.asm.mixin.injection.callback.CallbackInfo)
```

A standalone reflection test called `EveryKeyAGemClient.forwardToTypewriter(65, 30, 1, 0)`
against the stub and printed:

```
[stub] onKeyPress key=65 action=1
```

This verifies that `Class.forName`, `getMethod("getMode")` and
`getMethod("onKeyPress", int, int, int, int)` resolve and invoke correctly.

## 2. Real modpack test

The release jar was installed into:

```
<instance>\mods\create-every-key-a-gem-1.0.0.jar
```

The normal 70-mod instance was launched with `-Dmixin.debug.export=true`.

Evidence from `logs/latest.log`:

```
Create: Every Key a Gem 1.0.0 (every_key_a_gem)
Create Simulated 1.3.2 (simulated)
Create Aeronautics 1.3.2 (aeronautics_bundled)
...
mod/every_key_a_gem
```

The exported `KeyboardHandler.class` from the real instance contained:

```
private void handler$dan000$every_key_a_gem$everykeyagem$captureTypewriterKeys(
    long, int, int, int, int, org.spongepowered.asm.mixin.injection.callback.CallbackInfo)
```

The game reached the main menu without dependency, mixin or injection errors.

## Not automated

The actual in-world scenario (activate a typewriter, press a key that is also
another mod's shortcut, observe that no other screen opens) needs a human or a
scripted world. Please verify once after installing:

1. Activate the typewriter.
2. Press a mapped key that normally opens another mod's GUI.
3. Confirm the typewriter signal fires and the other GUI does not open.
4. Press `Esc` and confirm the typewriter exits normally.
