package dev.everykeyagem;

import net.neoforged.api.distmarker.Dist;
import net.neoforged.fml.common.Mod;

/**
 * Client-side addon for Create: Aeronautics (Simulated).
 *
 * <p>While the wireless typewriter owns the keyboard, this mod claims keyboard
 * events before vanilla or any other mod can process them.</p>
 */
@Mod(value = EveryKeyAGem.MODID, dist = Dist.CLIENT)
public final class EveryKeyAGem {
    public static final String MODID = "every_key_a_gem";

    public EveryKeyAGem() {
    }
}
