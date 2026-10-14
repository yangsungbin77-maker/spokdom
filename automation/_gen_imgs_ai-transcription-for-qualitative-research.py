# Generates 4 original graphics for ai-transcription-for-qualitative-research (no AI image API, no logos).
# Figures match research json (as of October 2026): Otter free 300 min/mo (30-min cap, 3 lifetime imports),
# Word (M365) 300 min/mo uploads, Rev free 45 AI min/mo, Sonix 30 min one-time trial, noScribe local/unlimited.
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from PIL import Image

BG, ELEV, ELEV2, BORDER = "#0b0e14", "#141a26", "#1b2230", "#344056"
TEXT, MUTED, ACC, ACC_DIM = "#e7ebf3", "#9aa6bd", "#3ef58b", "#19c46c"
WARN, DANGER, BLUE = "#f5c542", "#ff6b6b", "#5aa9ff"
OUT = "C:/Users/use/spokdom/src/assets/posts/"
plt.rcParams["font.family"] = ["Arial", "DejaVu Sans"]


def save(fig, name, size):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100, facecolor=BG)
    plt.close(fig)
    buf.seek(0)
    Image.open(buf).convert("RGB").resize(size, Image.LANCZOS).save(OUT + name, "WEBP", quality=88)
    print("saved", name)


def box(ax, x, y, w, h, fc=ELEV, ec=BORDER, lw=1.5, r=0.02):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, transform=ax.transAxes))


# 1) HERO 16:9 — waveform -> transcript with speaker labels, lock = local option
fig = plt.figure(figsize=(16, 9))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
fig.patch.set_facecolor(BG)
import numpy as np
xs = np.linspace(0.06, 0.44, 90)
rng = np.random.default_rng(7)
for i, x in enumerate(xs):
    h = 0.03 + 0.17 * abs(np.sin(i / 6.0)) * rng.uniform(0.4, 1.0)
    col = ACC if (i // 15) % 2 == 0 else BLUE
    ax.plot([x, x], [0.5 - h, 0.5 + h], color=col, lw=3.2, solid_capstyle="round", alpha=0.9)
ax.annotate("", xy=(0.54, 0.5), xytext=(0.47, 0.5),
            arrowprops=dict(arrowstyle="-|>", color=TEXT, lw=3, mutation_scale=30))
box(ax, 0.57, 0.2, 0.37, 0.6, fc=ELEV, ec=BORDER, r=0.02)
lines = [("P1", ACC, 0.70, 0.26), ("INT", BLUE, 0.62, 0.20), ("P1", ACC, 0.54, 0.25),
         ("INT", BLUE, 0.46, 0.16), ("P1", ACC, 0.38, 0.24), ("P1", ACC, 0.30, 0.18)]
for lab, col, y, w in lines:
    box(ax, 0.595, y - 0.022, 0.06, 0.044, fc=col, ec=col, r=0.01)
    ax.text(0.625, y, lab, ha="center", va="center", fontsize=15, weight="bold", color=BG)
    box(ax, 0.67, y - 0.012, w, 0.024, fc=ELEV2, ec=ELEV2, r=0.008)
ax.add_patch(Circle((0.9, 0.78), 0.055, transform=ax.transAxes, fc=BG, ec=ACC, lw=3))
ax.add_patch(FancyBboxPatch((0.876, 0.745), 0.048, 0.042, boxstyle="round,pad=0,rounding_size=0.006",
                            fc=ACC, ec=ACC, transform=ax.transAxes))
ax.add_patch(matplotlib.patches.Arc((0.9, 0.795), 0.032, 0.05, theta1=0, theta2=180,
                                    transform=ax.transAxes, color=ACC, lw=3))
ax.text(0.06, 0.88, "AI transcription for qualitative research", fontsize=34, weight="bold", color=TEXT)
ax.text(0.06, 0.12, "Interview audio  \u2192  speaker-labelled transcript  \u2192  privacy checked first",
        fontsize=20, color=MUTED)
save(fig, "ai-transcription-for-qualitative-research.webp", (1600, 900))

# 2) BODY 16:9 — free tier minutes bar chart
fig = plt.figure(figsize=(16, 9)); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.25, 0.16, 0.68, 0.64]); ax.set_facecolor(BG)
tools = ["noScribe (local)", "Microsoft Word Transcribe*", "Otter.ai Basic", "Rev Free", "Sonix trial"]
vals = [330, 300, 300, 45, 30]
cols = [ACC, BLUE, BLUE, WARN, WARN]
labels = ["No cloud quota \u2014 limited by your computer", "300 min / month (uploads)",
          "300 min / month \u2014 30-min cap per conversation, 3 lifetime imports",
          "45 AI min / month", "30 min, one-time"]
y = np.arange(len(tools))[::-1]
ax.barh(y, vals, color=cols, height=0.58)
ax.barh(y[0], 330, color=ACC, height=0.58, hatch="//", edgecolor=BG)
for yi, v, lab in zip(y, vals, labels):
    ax.text(min(v, 330) + 6, yi, lab, va="center", fontsize=17, color=TEXT)
ax.set_yticks(y); ax.set_yticklabels(tools, fontsize=19, color=TEXT)
ax.set_xlim(0, 760); ax.set_xticks([0, 60, 120, 180, 240, 300])
ax.tick_params(axis="x", colors=MUTED, labelsize=15)
ax.set_xlabel("Free transcription minutes (as of October 2026)", color=MUTED, fontsize=16)
for s in ["top", "right"]: ax.spines[s].set_visible(False)
for s in ["left", "bottom"]: ax.spines[s].set_color(BORDER)
fig.text(0.04, 0.9, "How much interview audio does each free tier cover?", fontsize=30, weight="bold", color=TEXT)
fig.text(0.04, 0.045, "*Needs a Microsoft 365 subscription (many universities provide one). Check each official page \u2014 limits change.",
         fontsize=15, color=MUTED)
save(fig, "ai-transcription-for-qualitative-research-free-minutes.webp", (1600, 900))

# 3) BODY 1:1 — privacy / offline matrix
fig = plt.figure(figsize=(12, 12)); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.text(0.5, 0.94, "AI transcription for qualitative research", ha="center", fontsize=26, weight="bold", color=TEXT)
ax.text(0.5, 0.895, "Where does the interview audio go?", ha="center", fontsize=22, color=MUTED)
cols_h = ["Runs offline", "Audio leaves\nyour device", "Training on\ncontent (per vendor)"]
rows = [
    ("noScribe", [("Yes", ACC), ("No", ACC), ("No", ACC)]),
    ("MacWhisper", [("Yes", ACC), ("No", ACC), ("No", ACC)]),
    ("Word Transcribe", [("No", WARN), ("Yes (M365)", WARN), ("Check tenant", WARN)]),
    ("Otter.ai", [("No", WARN), ("Yes", WARN), ("De-identified", DANGER)]),
    ("Trint", [("No", WARN), ("Yes", WARN), ("Not by listening", WARN)]),
    ("Rev / Sonix", [("No", WARN), ("Yes", WARN), ("Read terms", WARN)]),
]
x0, colw = 0.30, 0.225
for j, h in enumerate(cols_h):
    ax.text(x0 + colw * j + colw / 2, 0.81, h, ha="center", va="center", fontsize=17, color=TEXT, weight="bold")
for i, (name, cells) in enumerate(rows):
    yy = 0.71 - i * 0.105
    box(ax, 0.04, yy - 0.042, 0.92, 0.084, fc=ELEV if i % 2 == 0 else ELEV2, ec=BORDER, r=0.012)
    ax.text(0.06, yy, name, va="center", fontsize=20, color=TEXT, weight="bold")
    for j, (t, c) in enumerate(cells):
        cx = x0 + colw * j + colw / 2
        box(ax, cx - 0.095, yy - 0.025, 0.19, 0.05, fc=BG, ec=c, lw=2, r=0.012)
        ax.text(cx, yy, t, ha="center", va="center", fontsize=15, color=c, weight="bold")
ax.text(0.5, 0.06, "Green = audio stays on your machine. Based on vendor pages, October 2026.\nAlways confirm current terms with your IRB.",
        ha="center", fontsize=15, color=MUTED)
save(fig, "ai-transcription-for-qualitative-research-privacy-matrix.webp", (1200, 1200))

# 4) BODY 4:3 — decision flow
fig = plt.figure(figsize=(12, 9)); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.text(0.5, 0.94, "Which transcription tool for which research interview?", ha="center", fontsize=24, weight="bold", color=TEXT)

def node(x, y, w, h, t, ec, fs=16, fc=ELEV):
    box(ax, x - w / 2, y - h / 2, w, h, fc=fc, ec=ec, lw=2.2, r=0.02)
    ax.text(x, y, t, ha="center", va="center", fontsize=fs, color=TEXT, linespacing=1.3)

def arrow(x1, y1, x2, y2, lab=None, lx=0, ly=0):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=2, mutation_scale=20))
    if lab:
        ax.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, lab, fontsize=15, color=ACC, weight="bold", ha="center")

node(0.5, 0.80, 0.62, 0.09, "Is the data sensitive or identifiable\n(health, minors, undocumented, protected)?", BLUE)
node(0.2, 0.55, 0.32, 0.12, "Local / offline\nnoScribe (Win/Mac/Linux)\nMacWhisper (Mac)", ACC)
node(0.72, 0.58, 0.46, 0.09, "Does your university approve a\ncloud tool (e.g. Microsoft 365)?", BLUE)
node(0.55, 0.30, 0.34, 0.11, "Use the approved tool\n(Word Transcribe, 300 min/mo)", ACC)
node(0.86, 0.30, 0.26, 0.11, "Get IRB sign-off\nbefore Otter / Rev /\nSonix / Trint", WARN)
node(0.2, 0.28, 0.32, 0.1, "Publishing exact quotes?\nAdd a human check pass", WARN)
arrow(0.38, 0.755, 0.24, 0.615, "Yes", -0.03, 0.0)
arrow(0.62, 0.755, 0.70, 0.625, "No", 0.04, 0.0)
arrow(0.66, 0.535, 0.57, 0.355, "Yes", -0.04, 0.0)
arrow(0.80, 0.535, 0.85, 0.355, "No", 0.04, 0.0)
arrow(0.2, 0.49, 0.2, 0.33)
ax.text(0.5, 0.08, "Free limits as of October 2026 \u2014 confirm on each official page.", ha="center", fontsize=15, color=MUTED)
save(fig, "ai-transcription-for-qualitative-research-decision-flow.webp", (1200, 900))
