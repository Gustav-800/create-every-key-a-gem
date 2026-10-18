from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

SIZE = 2048
OUT = Path(__file__).resolve().parent.parent / "src" / "main" / "resources" / "icon.png"


def lerp(a: int, b: int, t: float) -> int:
    return round(a + (b - a) * t)


def vertical_gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    width, height = size
    image = Image.new("RGB", size)
    pixels = image.load()
    for y in range(height):
        t = y / max(1, height - 1)
        color = tuple(lerp(top[i], bottom[i], t) for i in range(3))
        for x in range(width):
            pixels[x, y] = color
    return image


def radial_background() -> Image.Image:
    image = Image.new("RGB", (SIZE, SIZE))
    pixels = image.load()
    cx = cy = SIZE / 2
    max_dist = math.hypot(cx, cy)
    for y in range(SIZE):
        for x in range(SIZE):
            d = math.hypot(x - cx, y - cy) / max_dist
            d = min(1.0, d)
            # warm charcoal center, near-black edges
            t = d ** 1.4
            base = (
                lerp(38, 11, t),
                lerp(36, 12, t),
                lerp(41, 16, t),
            )
            pixels[x, y] = base
    return image


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def paste_rounded(base: Image.Image, box: tuple[int, int, int, int], fill, radius: int, outline=None, width: int = 0):
    x0, y0, x1, y1 = box
    layer = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle((0, 0, layer.width - 1, layer.height - 1), radius=radius, fill=fill, outline=outline, width=width)
    base.alpha_composite(layer, (x0, y0))


def main() -> None:
    background = radial_background().convert("RGBA")

    # faint typewriter-paper glow
    glow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((260, 240, 1788, 1768), fill=(177, 126, 63, 26))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    background.alpha_composite(glow)

    # Key shadow
    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((390, 500, 1668, 1770), radius=250, fill=(0, 0, 0, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(55))
    background.alpha_composite(shadow)

    # Brass body / side
    body = vertical_gradient((1320, 1330), (198, 141, 73), (111, 67, 27)).convert("RGBA")
    body_mask = rounded_mask(body.size, 240)
    background.paste(body, (374, 430), body_mask)

    # Brass outer rim
    rim = vertical_gradient((1260, 1270), (226, 174, 103), (143, 91, 42)).convert("RGBA")
    rim_mask = rounded_mask(rim.size, 225)
    background.paste(rim, (404, 405), rim_mask)

    # Cream keycap top
    top = vertical_gradient((1200, 1190), (248, 237, 211), (214, 190, 150)).convert("RGBA")
    top_mask = rounded_mask(top.size, 205)
    background.paste(top, (434, 385), top_mask)

    draw = ImageDraw.Draw(background)

    # Soft inner bevel on the keycap
    draw.rounded_rectangle((452, 403, 1616, 1557), radius=190, outline=(255, 250, 235, 150), width=10)
    draw.rounded_rectangle((466, 417, 1602, 1543), radius=178, outline=(120, 86, 45, 90), width=6)

    # Brass setting ring around the gem
    gem_center = (1034, 990)
    ring_r = 336
    draw.ellipse(
        (gem_center[0] - ring_r, gem_center[1] - ring_r, gem_center[0] + ring_r, gem_center[1] + ring_r),
        fill=(146, 94, 43),
        outline=(92, 55, 20),
        width=12,
    )
    inner_r = 306
    draw.ellipse(
        (gem_center[0] - inner_r, gem_center[1] - inner_r, gem_center[0] + inner_r, gem_center[1] + inner_r),
        fill=(49, 31, 18),
        outline=(229, 177, 107),
        width=8,
    )

    # Faceted gem (round brilliant style, octagonal table)
    cx, cy = gem_center
    outer_r = 286
    table_r = 136
    outer = []
    table = []
    for i in range(8):
        angle = math.radians(22.5 + i * 45)
        outer.append((cx + outer_r * math.cos(angle), cy + outer_r * math.sin(angle)))
        table.append((cx + table_r * math.cos(angle), cy + table_r * math.sin(angle)))

    # Crown facets: one clean trapezoid per side, lit from the upper left.
    crown_colors = [
        (62, 188, 172),   # right
        (34, 132, 126),   # lower right
        (26, 104, 101),   # bottom
        (38, 148, 140),   # lower left
        (58, 178, 164),   # left
        (116, 230, 211),  # upper left (key light)
        (96, 210, 194),   # top
        (78, 198, 182),   # upper right
    ]
    for i in range(8):
        p1 = outer[i]
        p2 = outer[(i + 1) % 8]
        t1 = table[i]
        t2 = table[(i + 1) % 8]
        draw.polygon([p1, p2, t2, t1], fill=crown_colors[i], outline=(16, 76, 74), width=5)

    # Table
    draw.polygon(table, fill=(150, 242, 226), outline=(16, 73, 72), width=6)
    table_highlight = [
        (cx - 46, cy - 82),
        (cx + 34, cy - 96),
        (cx + 58, cy - 34),
        (cx - 18, cy - 20),
    ]
    draw.polygon(table_highlight, fill=(213, 255, 246, 190))

    # Crisp rim
    draw.ellipse((cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r), outline=(15, 55, 55), width=10)

    # Fine vignette
    vignette = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    for i in range(120):
        alpha = int(2.2 * i)
        vd.rectangle((i, i, SIZE - i, SIZE - i), outline=(0, 0, 0, alpha), width=1)
    background.alpha_composite(vignette)

    background = background.resize((512, 512), Image.LANCZOS).convert("RGB")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    background.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
