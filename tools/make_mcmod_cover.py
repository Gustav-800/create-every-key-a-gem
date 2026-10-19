from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT.parent / "_assets"
OUT = ROOT / "assets" / "mcmod-cover.png"
OUT_SMALL = ROOT / "assets" / "mcmod-cover-240.png"

W, H = 960, 600


def main() -> None:
    blueprint = Image.open(ASSETS / "blueprint.png").convert("RGB")
    # Remove the source image's thin white border, but keep the full 16:10 composition.
    inset = 44
    blueprint = blueprint.crop((inset, inset, blueprint.width - inset, blueprint.height - inset))
    background = blueprint.resize((W, H), Image.LANCZOS)

    item = Image.open(ASSETS / "typewriter_item.png").convert("RGBA")
    bbox = item.getbbox()
    if bbox:
        item = item.crop(bbox)

    target = 330
    ratio = min(target / item.width, target / item.height)
    item = item.resize(
        (max(1, round(item.width * ratio)), max(1, round(item.height * ratio))),
        Image.LANCZOS,
    )

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pos = ((W - item.width) // 2, (H - item.height) // 2)
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
    canvas.alpha_composite(shadow, (0, 10))
    canvas.alpha_composite(outline)
    canvas.alpha_composite(layer)

    canvas = canvas.convert("RGB")
    canvas.save(OUT, "PNG", optimize=True)
    canvas.resize((240, 150), Image.LANCZOS).save(OUT_SMALL, "PNG", optimize=True)
    print("wrote", OUT)
    print("wrote", OUT_SMALL)


if __name__ == "__main__":
    main()
