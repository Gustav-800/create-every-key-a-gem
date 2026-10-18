package dev.everykeyagem;

import java.lang.reflect.Method;
import net.minecraft.client.Minecraft;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Decides when keyboard input belongs exclusively to the typewriter and hands
 * the event to Simulated's own handler.
 *
 * <p>The Simulated classes are accessed reflectively on purpose: this addon
 * only needs three public members, and reflection keeps the build independent
 * of Simulated's jar. If Simulated changes those members, the addon fails open
 * (normal keyboard behaviour) instead of crashing the game.</p>
 */
public final class EveryKeyAGemClient {
    private static final Logger LOGGER = LoggerFactory.getLogger("Every Key a Gem");

    private static final String HANDLER_CLASS =
            "dev.simulated_team.simulated.content.blocks.redstone.linked_typewriter.LinkedTypewriterInteractionHandler";
    private static final String ACTIVE = "ACTIVE";
    private static final String BINDING_FROM_ITEM = "BINDING_FROM_ITEM";

    /** GLFW_KEY_F2 - keep screenshots usable while typing. */
    private static final int GLFW_KEY_F2 = 291;
    /** GLFW_KEY_F11 - keep fullscreen toggling usable while typing. */
    private static final int GLFW_KEY_F11 = 292;

    private static boolean resolutionAttempted;
    private static Method getModeMethod;
    private static Method onKeyPressMethod;
    private static boolean reflectionBroken;

    private EveryKeyAGemClient() {
    }

    public static boolean shouldCapture(long windowHandle, int key) {
        Minecraft minecraft = Minecraft.getInstance();
        if (minecraft.player == null || minecraft.screen != null) {
            return false;
        }
        if (windowHandle != minecraft.getWindow().getWindow()) {
            return false;
        }
        // Let a couple of harmless window/system keys through.
        if (key == GLFW_KEY_F2 || key == GLFW_KEY_F11) {
            return false;
        }
        if (!resolveHandler()) {
            return false;
        }

        try {
            Object mode = getModeMethod.invoke(null);
            if (mode == null) {
                return false;
            }
            String modeName = mode instanceof Enum<?> enumeration ? enumeration.name() : mode.toString();
            return ACTIVE.equals(modeName) || BINDING_FROM_ITEM.equals(modeName);
        } catch (ReflectiveOperationException | RuntimeException | LinkageError exception) {
            disableReflection("read typewriter mode", exception);
            return false;
        }
    }

    public static void forwardToTypewriter(int key, int scanCode, int action, int modifiers) {
        if (!resolveHandler()) {
            return;
        }
        try {
            onKeyPressMethod.invoke(null, key, scanCode, action, modifiers);
        } catch (ReflectiveOperationException | RuntimeException | LinkageError exception) {
            disableReflection("forward key event", exception);
        }
    }

    private static boolean resolveHandler() {
        if (reflectionBroken) {
            return false;
        }
        if (!resolutionAttempted) {
            resolutionAttempted = true;
            try {
                Class<?> handler = Class.forName(HANDLER_CLASS);
                getModeMethod = handler.getMethod("getMode");
                onKeyPressMethod = handler.getMethod("onKeyPress", int.class, int.class, int.class, int.class);
            } catch (ReflectiveOperationException | RuntimeException | LinkageError exception) {
                disableReflection("find Simulated's typewriter handler", exception);
            }
        }
        return getModeMethod != null && onKeyPressMethod != null;
    }

    private static void disableReflection(String action, Throwable throwable) {
        if (!reflectionBroken) {
            reflectionBroken = true;
            LOGGER.warn(
                    "Every Key a Gem could not {}; typewriter key protection is disabled. "
                            + "This usually means the installed Create: Aeronautics / Simulated version is not supported.",
                    action,
                    throwable
            );
        }
    }
}
