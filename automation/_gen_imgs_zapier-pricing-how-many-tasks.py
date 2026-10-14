# Generates the 3 original data graphics for zapier-pricing-how-many-tasks (no AI image API).
# Figures match the post: workflows A/B/C, naive step count 2,130 vs billed 820,
# Zapier Professional annual tiers as of Oct 2026 (zapier.com/pricing).
import io
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

OUT = Path(__file__).resolve().parent.parent / "src" / "assets" / "posts"
BG, ELEV, BORDER = "#0b0e14", "#141a26", "#344056"
TEXT, MUTED, DIM = "#e7ebf3", "#9aa6bd", "#6b7689"
ACCENT, ACCENT_DIM = "#3ef58b", "#19c46c"
GREY = "#4a5568"
plt.rcParams.update({"font.family": "Segoe UI", "text.color": TEXT, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.edgecolor": BORDER})


def save(fig, name, size):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100, facecolor=BG)
    plt.close(fig)
    buf.seek(0)
    img = Image.open(buf).convert("RGB").resize(size, Image.LANCZOS)
    img.save(OUT / name, "WEBP", quality=88)
    print("saved", OUT / name, img.size)


def style(ax):
    ax.set_facecolor(BG)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color=BORDER, alpha=0.5, lw=0.8)
    ax.set_axisbelow(True)


# 1) HERO 16:9 — naive step count vs billed tasks
fig = plt.figure(figsize=(16, 9))
fig.patch.set_facecolor(BG)
fig.text(0.06, 0.86, "ZAPIER PRICING TASKS", color=ACCENT, fontsize=22, fontweight="bold")
fig.text(0.06, 0.73, "Counting steps vs counting tasks", color=TEXT, fontsize=44, fontweight="bold")
fig.text(0.06, 0.66, "Same 3 solo-founder Zaps, one month. Triggers, Filter and Formatter steps bill 0 tasks.",
         color=MUTED, fontsize=20)
ax = fig.add_axes([0.24, 0.12, 0.72, 0.45])
style(ax)
ax.grid(False)
labels = ["Every step counted\n(naive estimate)", "Billed tasks\n(actions only)"]
vals = [2130, 820]
ax.barh([1, 0], vals, color=[GREY, ACCENT], height=0.55)
ax.set_yticks([1, 0])
ax.set_yticklabels(labels, fontsize=20, color=TEXT)
ax.set_xlim(0, 3500)
ax.set_xticks([])
for s in ("bottom", "left"):
    ax.spines[s].set_visible(False)
ax.text(2130 + 30, 1, "2,130 tasks  ->  5,000 tier, $89/mo", va="center", fontsize=20, color=MUTED)
ax.text(820 + 30, 0, "820 tasks  ->  1,500 tier, $39/mo", va="center", fontsize=20, color=ACCENT, fontweight="bold")
fig.text(0.06, 0.04, "Professional plan, billed annually, list prices as of October 2026 (zapier.com/pricing).",
         color=DIM, fontsize=15)
save(fig, "zapier-pricing-how-many-tasks.webp", (1600, 900))

# 2) BODY 4:3 — per-workflow billed vs free steps
fig, ax = plt.subplots(figsize=(12, 9))
fig.patch.set_facecolor(BG)
style(ax)
wf = ["A  Lead form\n300 runs, 200 pass filter", "B  Stripe sale\n150 runs", "C  Invoice email\n60 runs"]
billed = [400, 300, 120]
free = [1100, 150, 60]  # trigger/filter/formatter executions that bill nothing (naive - billed)
x = range(3)
ax.bar(x, billed, color=ACCENT, width=0.55, label="Billed tasks (successful actions)")
ax.bar(x, free, bottom=billed, color=GREY, width=0.55, label="Steps that run but bill 0 tasks")
for i in x:
    ax.text(i, billed[i] / 2, f"{billed[i]}", ha="center", va="center", fontsize=20, color="#04140b", fontweight="bold")
    ax.text(i, billed[i] + free[i] + 30, f"{billed[i] + free[i]:,} step runs", ha="center", fontsize=15, color=MUTED)
ax.set_xticks(list(x))
ax.set_xticklabels(wf, fontsize=14, color=TEXT)
ax.set_ylabel("Per month", fontsize=14)
ax.set_ylim(0, 1700)
ax.legend(frameon=False, fontsize=14, loc="upper right", labelcolor=TEXT)
fig.text(0.07, 0.94, "Zapier task usage by workflow", fontsize=28, fontweight="bold", color=TEXT)
fig.text(0.07, 0.895, "Total billed: 820 tasks/month vs 2,130 step runs", fontsize=17, color=ACCENT)
fig.subplots_adjust(top=0.85, bottom=0.14, left=0.1, right=0.97)
save(fig, "zapier-pricing-tasks-by-workflow.webp", (1200, 900))

# 3) BODY 1:1 — Professional annual tier ladder with 820-task marker
tiers = [750, 1500, 2000, 5000, 10000]
price = [19.99, 39, 49, 89, 129]
fig, ax = plt.subplots(figsize=(10.8, 10.8))
fig.patch.set_facecolor(BG)
style(ax)
xs = range(len(tiers))
cols = [ACCENT if t == 1500 else ELEV for t in tiers]
bars = ax.bar(xs, price, color=cols, edgecolor=[ACCENT_DIM if t == 1500 else BORDER for t in tiers], lw=1.5, width=0.62)
for i, (t, p) in enumerate(zip(tiers, price)):
    ax.text(i, p + 3, f"${p:g}", ha="center", fontsize=20, fontweight="bold", color=ACCENT if t == 1500 else TEXT)
    ax.text(i, p + 11, f"{p / t * 100:.1f}¢/task", ha="center", fontsize=13, color=MUTED)
ax.set_xticks(list(xs))
ax.set_xticklabels([f"{t:,}" for t in tiers], fontsize=16, color=TEXT)
ax.set_xlabel("Tasks per month (tier)", fontsize=15)
ax.set_ylabel("USD per month, billed annually", fontsize=15)
ax.set_ylim(0, 160)
ax.annotate("820 tasks needed\n= smallest fit: 1,500", xy=(1, 54), xytext=(0.1, 105), fontsize=16, color=ACCENT,
            arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.8))
fig.text(0.08, 0.94, "Zapier Professional task tiers", fontsize=30, fontweight="bold", color=TEXT)
fig.text(0.08, 0.905, "List prices as of October 2026. Confirm on zapier.com/pricing.", fontsize=15, color=MUTED)
fig.subplots_adjust(top=0.86, bottom=0.1, left=0.11, right=0.97)
save(fig, "zapier-pricing-task-tiers.webp", (1080, 1080))
