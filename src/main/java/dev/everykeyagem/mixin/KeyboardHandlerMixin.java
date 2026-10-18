package dev.everykeyagem.mixin;

import dev.everykeyagem.EveryKeyAGemClient;
import net.minecraft.client.KeyboardHandler;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Claims typewriter keystrokes before NeoForge's {@code InputEvent.Key} hook and
 * before vanilla's {@code KeyMapping.click} handling.
 *
 * <p>Cancelling at HEAD means neither vanilla keybinds nor any other mod's key
 * listener ever sees the event while the typewriter owns the keyboard.</p>
 */
@Mixin(value = KeyboardHandler.class, remap = false)
public abstract class KeyboardHandlerMixin {
    @Inject(
            method = "keyPress(JIIII)V",
            at = @At("HEAD"),
            cancellable = true,
            remap = false
    )
    private void everykeyagem$captureTypewriterKeys(
            long windowHandle,
            int key,
            int scanCode,
            int action,
            int modifiers,
            CallbackInfo ci
    ) {
        if (EveryKeyAGemClient.shouldCapture(windowHandle, key)) {
            EveryKeyAGemClient.forwardToTypewriter(key, scanCode, action, modifiers);
            ci.cancel();
        }
    }
}
