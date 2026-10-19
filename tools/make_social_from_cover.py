from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT.parent / "_assets"
OUT = ROOT / "assets" / "github-social.png"

W, H = 1280, 640

CREAM = (243, 230, 200)
BRASS = (200, 150, 86)
TEAL = (92, 205, 188)
MUTED = (178, 174, 166)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)


def main() -> None:
    blueprint = Image.open(ASSETS / "blueprint.png").convert("RGB")
    inset = 44
    blueprint = blueprint.crop((inset, inset, blueprint.width - inset, blueprint.height - inset))
    scale = W / blueprint.width
    blueprint = blueprint.resize((W, round(blueprint.height * scale)), Image.LANCZOS)
    top = max(0, (blueprint.height - H) // 2)
    background = blueprint.crop((0, top, W, top + H))

    item = Image.open(ASSETS / "typewriter_item.png").convert("RGBA")
    bbox = item.getbbox()
    if bbox:
        item = item.crop(bbox)
    target = 330
    ratio = min(target / item.width, target / item.height)
    item = item.resize((round(item.width * ratio), round(item.height * ratio)), Image.LANCZOS)

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pos = (170, (H - item.height) // 2)
    layer.alpha_composite(item, pos)
    alpha = layer.getchannel("A")

    outline_mask = alpha.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(1.0))
    outline_mask = outline_mask.point(lambda v: 255 if v > 72 else 0)
    outline = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    outline.putalpha(outline_mask)

    shadow_mask = outline_mask.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.42))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow.putalpha(shadow_mask)

    canvas = background.convert("RGBA")
    canvas.alpha_composite(shadow, (0, 12))
    canvas.alpha_composite(outline)
    canvas.alpha_composite(layer)

    # Darken the text side slightly so the cream type keeps its contrast.
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for x in range(430, W):
        alpha = int((x - 430) / (W - 430) * 105)
        od.line((x, 0, x, H), fill=(7, 14, 24, alpha))
    canvas.alpha_composite(overlay)

    draw = ImageDraw.Draw(canvas)
    draw.rectangle((24, 24, W - 25, H - 25), outline=(91, 63, 33), width=2)

    draw.text((560, 120), "CREATE", font=font("georgiab.ttf", 25), fill=BRASS)
    draw.text((560, 155), "EVERY KEY A GEM", font=font("georgiab.ttf", 56), fill=CREAM)
    draw.text((560, 245), "机械动力：字字珠玑", font=font("msyhbd.ttc", 36), fill=(222, 190, 132))
    draw.line((562, 305, 1170, 305), fill=(94, 65, 34), width=2)
    draw.text(
        (562, 330),
        "A client-side keyguard for the wireless typewriter.",
        font=font("msyh.ttc", 22),
        fill=(205, 199, 186),
    )
    draw.text(
        (562, 370),
        "Minecraft 1.21.1   ·   NeoForge   ·   Client-side",
        font=font("georgiab.ttf", 17),
        fill=TEAL,
    )
    draw.text((562, 455), "Create: Aeronautics  ·  Simulated", font=font("msyh.ttc", 16), fill=MUTED)

    canvas.convert("RGB").save(OUT, "PNG", optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
