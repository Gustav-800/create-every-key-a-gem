from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ICON = ROOT / "src" / "main" / "resources" / "icon.png"
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

CREAM = (243, 230, 200)
BRASS = (200, 150, 86)
TEAL = (92, 205, 188)
MUTED = (170, 166, 158)
BG = (18, 20, 24)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"C:/Windows/Fonts/{path}", size)


def rounded_icon(size: int) -> Image.Image:
    icon = Image.open(ICON).convert("RGB").resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size - 1, size - 1), radius=size // 8, fill=255)
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(icon, (0, 0), mask)
    return result


def make_mcmod_cover() -> None:
    width, height = 240, 150
    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)

    # Soft warm glow behind the icon.
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((-30, 10, 150, 160), fill=(177, 126, 63, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(24))
    image = Image.alpha_composite(image.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(image)

    # Thin brass frame.
    draw.rectangle((4, 4, width - 5, height - 5), outline=(92, 62, 31), width=1)

    image.paste(rounded_icon(100), (12, 25), rounded_icon(100))

    title_font = font("msyhbd.ttc", 24)
    kicker_font = font("msyhbd.ttc", 11)
    en_font = font("georgiab.ttf", 7)
    small_font = font("msyh.ttc", 8)

    draw.text((128, 27), "机械动力", font=kicker_font, fill=BRASS)
    draw.text((126, 44), "字字珠玑", font=title_font, fill=CREAM)
    draw.text((128, 84), "CREATE: EVERY KEY", font=en_font, fill=(214, 203, 178))
    draw.text((128, 94), "A GEM", font=en_font, fill=(214, 203, 178))
    draw.line((128, 109, 224, 109), fill=(94, 65, 34), width=1)
    draw.text((128, 114), "打字机按键保护", font=small_font, fill=TEAL)

    image.save(OUT / "mcmod-cover.png", "PNG", optimize=True)
    print("wrote", OUT / "mcmod-cover.png")


def make_social() -> None:
    width, height = 1280, 640
    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)

    # Warm radial glow.
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-120, -120, 760, 760), fill=(177, 126, 63, 42))
    gd.ellipse((760, -260, 1500, 460), fill=(31, 111, 106, 34))
    glow = glow.filter(ImageFilter.GaussianBlur(110))
    image = Image.alpha_composite(image.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(image)

    # Faint brass frame.
    draw.rectangle((34, 34, width - 35, height - 35), outline=(76, 52, 27), width=2)

    icon = rounded_icon(350)
    image.paste(icon, (98, 145), icon)

    title_font = font("georgiab.ttf", 61)
    cn_font = font("msyhbd.ttc", 39)
    sub_font = font("msyh.ttc", 22)
    meta_font = font("georgiab.ttf", 18)

    draw.text((520, 150), "CREATE", font=font("georgiab.ttf", 26), fill=BRASS)
    draw.text((520, 186), "EVERY KEY A GEM", font=title_font, fill=CREAM)
    draw.text((520, 282), "机械动力：字字珠玑", font=cn_font, fill=(222, 190, 132))

    draw.line((522, 345, 1150, 345), fill=(94, 65, 34), width=2)

    draw.text((522, 372), "A client-side keyguard for the wireless typewriter.", font=sub_font, fill=(198, 192, 180))
    draw.text((522, 408), "Minecraft 1.21.1   ·   NeoForge   ·   Client-side", font=meta_font, fill=TEAL)

    draw.text((522, 500), "Create: Aeronautics  ·  Simulated", font=font("msyh.ttc", 17), fill=MUTED)

    image.save(OUT / "github-social.png", "PNG", optimize=True)
    print("wrote", OUT / "github-social.png")


if __name__ == "__main__":
    make_mcmod_cover()
    make_social()
