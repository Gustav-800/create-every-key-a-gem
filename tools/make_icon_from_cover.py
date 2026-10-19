from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
COVER = ROOT / "assets" / "mcmod-cover.png"
OUT = ROOT / "src" / "main" / "resources" / "icon.png"


def main() -> None:
    cover = Image.open(COVER).convert("RGB")
    side = cover.height
    left = (cover.width - side) // 2
    icon = cover.crop((left, 0, left + side, side)).resize((512, 512), Image.LANCZOS)
    icon.save(OUT, "PNG", optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
