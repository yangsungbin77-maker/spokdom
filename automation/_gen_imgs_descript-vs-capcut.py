# -*- coding: utf-8 -*-
"""descript-vs-capcut 글 이미지 2장 (matplotlib 자체 제작, 로고 없음). 수치=공식/교차검증 2026-10."""
import os, io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image

OUT = r"C:/Users/use/spokdom/src/assets/posts"
BG, ELEV, BORDER = "#0b0e14", "#141a26", "#344056"
TEXT, MUTED = "#e7ebf3", "#9aa6bd"
ACCENT, BLUE = "#3ef58b", "#5aa9ff"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["text.parse_math"] = False


def save(fig, name, size):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100, facecolor=BG)
    plt.close(fig)
    img = Image.open(buf).convert("RGB").resize(size, Image.LANCZOS)
    p = os.path.join(OUT, name)
    img.save(p, "WEBP", quality=90, method=6)
    print("saved", p, img.size)


# ---------- Hero 1600x900: side-by-side comparison ----------
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis("off")
ax.text(8, 8.15, "Descript vs CapCut", ha="center", va="center", fontsize=46, color=TEXT, weight="bold")
ax.text(8, 7.45, "Text-based editing vs timeline editing  ·  US list prices as of October 2026",
        ha="center", va="center", fontsize=19, color=MUTED)

cards = [
    (0.7, "DESCRIPT", ACCENT, "Edit the transcript, the video follows", [
        ("Best for", "Podcasts, interviews, tutorials"),
        ("Platforms", "Mac · Windows · Web"),
        ("Free plan", "1 hr/mo · 720p · watermark"),
        ("Entry paid", "$16/mo annual · $24 monthly"),
        ("Top export", "4K (Creator, Business)"),
    ]),
    (8.3, "CAPCUT", BLUE, "Visual timeline, templates and effects", [
        ("Best for", "TikTok, Reels, Shorts"),
        ("Platforms", "iOS · Android · Web · Desktop"),
        ("Free plan", "Basic tools + free templates"),
        ("Entry paid", "Pro $19.99/mo · $179.99/yr"),
        ("Top export", "4K (Pro)"),
    ]),
]
for x, name, col, sub, rows in cards:
    ax.add_patch(FancyBboxPatch((x, 0.75), 7.0, 6.1, boxstyle="round,pad=0.02,rounding_size=0.25",
                                facecolor=ELEV, edgecolor=col, linewidth=3))
    ax.text(x + 0.45, 6.25, name, fontsize=34, color=col, weight="bold", va="center")
    ax.text(x + 0.45, 5.6, sub, fontsize=17, color=MUTED, va="center")
    for i, (k, v) in enumerate(rows):
        y = 4.85 - i * 0.8
        ax.plot([x + 0.45, x + 6.55], [y + 0.4, y + 0.4], color=BORDER, linewidth=1)
        ax.text(x + 0.45, y, k, fontsize=17, color=MUTED, va="center")
        ax.text(x + 2.3, y, v, fontsize=19, color=TEXT, va="center", weight="bold")
ax.text(8, 0.35, "spokdom.com  ·  confirm current prices on each official pricing page",
        ha="center", va="center", fontsize=14, color=MUTED)
save(fig, "descript-vs-capcut.webp", (1600, 900))


# ---------- Body 1200x900 (4:3): first-year cost by plan ----------
labels = ["Descript\nHobbyist", "Descript\nCreator", "CapCut\nPro", "Descript Hobbyist\n+ CapCut Pro"]
monthly = [288, 420, 239.88, 527.88]
annual = [192, 288, 179.99, 371.99]
fig, ax = plt.subplots(figsize=(12, 9), dpi=100)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
fig.subplots_adjust(left=0.1, right=0.97, top=0.82, bottom=0.17)
xs = range(len(labels)); w = 0.38
b1 = ax.bar([i - w / 2 for i in xs], monthly, w, color=BORDER, edgecolor=MUTED, label="Paid monthly x 12")
b2 = ax.bar([i + w / 2 for i in xs], annual, w, color=ACCENT, label="Paid annually")
for bars in (b1, b2):
    for r in bars:
        v = r.get_height()
        ax.text(r.get_x() + r.get_width() / 2, v + 8, f"${v:,.0f}" if v == int(v) else f"${v:,.2f}",
                ha="center", va="bottom", fontsize=16, color=TEXT, weight="bold")
ax.set_xticks(list(xs)); ax.set_xticklabels(labels, fontsize=16, color=TEXT)
ax.tick_params(axis="y", colors=MUTED, labelsize=14); ax.tick_params(axis="x", length=0)
ax.set_ylim(0, 600)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))
for s in ("top", "right"): ax.spines[s].set_visible(False)
for s in ("left", "bottom"): ax.spines[s].set_color(BORDER)
ax.grid(axis="y", color=BORDER, linewidth=0.8, alpha=0.6); ax.set_axisbelow(True)
fig.text(0.1, 0.92, "Descript vs CapCut: first-year cost by plan", fontsize=28, color=TEXT, weight="bold")
fig.text(0.1, 0.865, "US list prices as of October 2026, before tax. CapCut varies by region.", fontsize=16, color=MUTED)
leg = ax.legend(loc="upper left", fontsize=15, frameon=False)
for t in leg.get_texts(): t.set_color(TEXT)
fig.text(0.97, 0.03, "spokdom.com", ha="right", fontsize=13, color=MUTED)
save(fig, "descript-vs-capcut-pricing-by-plan.webp", (1200, 900))
