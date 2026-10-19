from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT.parent / "_assets"
OUT = ROOT / "src" / "main" / "resources" / "icon.png"
OUT_HIRES = ROOT / "assets" / "icon-1024.png"

SIZE = 1024
BLACK = (6, 14, 26)


def crop_square(image: Image.Image) -> Image.Image:
    w, h = image.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return image.crop((left, top, left + side, top + side))


def main() -> None:
    blueprint = Image.open(ASSETS / "blueprint.png").convert("RGB")
    # The source has a thin white border; remove it before cropping to a square.
    inset = 24
    blueprint = blueprint.crop((inset, inset, blueprint.width - inset, blueprint.height - inset))
    background = crop_square(blueprint).resize((SIZE, SIZE), Image.LANCZOS)

    # A very soft radial falloff; the blueprint itself stays clearly visible.
    radial = Image.radial_gradient("L").resize((SIZE, SIZE), Image.LANCZOS)
    mask = radial.point(lambda v: 255 - int(v * 0.18))
    background = Image.composite(background, Image.new("RGB", (SIZE, SIZE), BLACK), mask)

    item = Image.open(ASSETS / "typewriter_item.png").convert("RGBA")
    bbox = item.getbbox()
    if bbox:
        item = item.crop(bbox)

    target = 600
    ratio = min(target / item.width, target / item.height)
    item = item.resize(
        (max(1, round(item.width * ratio)), max(1, round(item.height * ratio))),
        Image.LANCZOS,
    )

    icon_layer = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    pos = ((SIZE - item.width) // 2, (SIZE - item.height) // 2)
    icon_layer.alpha_composite(item, pos)
    alpha = icon_layer.getchannel("A")

    # White die-cut sticker outline, following the item silhouette.
    outline_mask = alpha.filter(ImageFilter.MaxFilter(51)).filter(ImageFilter.GaussianBlur(1.2))
    outline_mask = outline_mask.point(lambda v: 255 if v > 72 else 0)
    outline = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 255))
    outline.putalpha(outline_mask)

    # Soft shadow below the sticker.
    shadow_mask = outline_mask.filter(ImageFilter.GaussianBlur(22)).point(lambda v: int(v * 0.45))
    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    shadow.putalpha(shadow_mask)

    canvas = background.convert("RGBA")
    canvas.alpha_composite(shadow, (0, 16))
    canvas.alpha_composite(outline)
    canvas.alpha_composite(icon_layer)

    canvas = canvas.convert("RGB")
    canvas.resize((512, 512), Image.LANCZOS).save(OUT, "PNG", optimize=True)
    canvas.save(OUT_HIRES, "PNG", optimize=True)
    print("wrote", OUT)
    print("wrote", OUT_HIRES)


if __name__ == "__main__":
    main()
