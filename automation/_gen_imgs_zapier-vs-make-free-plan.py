# Images for zapier-vs-make-free-plan (no AI image API).
# Hero = original data graphic. Body 1 = pricing-page screenshots captured Oct 17, 2026 (scratchpad, Playwright + Chrome).
# Body 2 = Make Free credit-burn chart (Spokdom calculation, see post).
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image

OUT = Path(__file__).resolve().parent.parent / "src" / "assets" / "posts"
SHOTS = Path(sys.argv[1]) if len(sys.argv) > 1 else None
BG, ELEV, BORDER = "#0b0e14", "#141a26", "#344056"
TEXT, MUTED = "#e7ebf3", "#9aa6bd"
ACCENT, WARN = "#3ef58b", "#f5a524"
plt.rcParams.update({"font.family": "Segoe UI", "text.color": TEXT})

fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis("off")
ax.text(0.8, 8.0, "Zapier vs Make free plan", fontsize=40, fontweight="bold", color=TEXT)
ax.text(0.8, 7.35, "Same price ($0). Different meter. Here's what actually gets counted.", fontsize=19, color=MUTED)
cards = [
    (0.8, "Zapier Free", "100", "tasks / month", ACCENT,
     ["Trigger checks: not billed", "Two-step Zaps only", "No Filter, Formatter, Paths", "Polls every 15 min"]),
    (8.3, "Make Free", "1,000", "credits / month", WARN,
     ["Trigger checks: 1 credit each", "Multi-step scenarios + routers", "2 active scenarios", "15-min minimum interval"]),
]
for x, name, big, unit, col, rows in cards:
    ax.add_patch(FancyBboxPatch((x, 0.7), 6.9, 5.9, boxstyle="round,pad=0.02,rounding_size=0.25",
                                fc=ELEV, ec=BORDER, lw=1.5))
    ax.text(x + 0.45, 5.85, name, fontsize=26, fontweight="bold", color=col)
    ax.text(x + 0.45, 4.45, big, fontsize=64, fontweight="bold", color=TEXT)
    ax.text(x + (2.75 if len(big) < 4 else 3.95), 4.65, unit, fontsize=20, color=MUTED)
    for i, r in enumerate(rows):
        ax.text(x + 0.5, 3.45 - i * 0.68, "•  " + r, fontsize=19, color=TEXT)
ax.text(0.8, 0.22, "Spokdom · free-plan limits as of Oct 17, 2026 (vendor pricing pages + Make Help Center). Limits change, so confirm before you build.", fontsize=13, color=MUTED)
fig.savefig(OUT / "_tmp_hero.png", facecolor=BG); plt.close(fig)
Image.open(OUT / "_tmp_hero.png").convert("RGB").resize((1600, 900), Image.LANCZOS).save(OUT / "zapier-vs-make-free-plan.webp", "WEBP", quality=88)
(OUT / "_tmp_hero.png").unlink()
print("hero ok")

if SHOTS:
    for name in ["zapier-vs-make-free-plan-pricing-pages", "zapier-vs-make-free-plan-credit-burn"]:
        im = Image.open(SHOTS / f"{name}.png").convert("RGB")
        im.save(OUT / f"{name}.webp", "WEBP", quality=90)
        print(name, im.size)
