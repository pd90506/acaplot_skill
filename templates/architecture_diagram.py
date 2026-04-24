import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

os.makedirs("figures", exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Computer Modern"],
    "font.size": 10,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

fig, ax = plt.subplots(figsize=(7, 2.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

blocks = [
    (0.3, 0.8, 1.4, 1.2, "Input\n(224x224)", "#E8F4FD"),
    (2.1, 0.8, 1.4, 1.2, "Conv\nBlock 1", "#B3D9F2"),
    (3.9, 0.8, 1.4, 1.2, "Conv\nBlock 2", "#80BFE6"),
    (5.7, 0.8, 1.4, 1.2, "FC\nLayers", "#4DA6D9"),
    (7.5, 0.8, 1.4, 1.2, "Softmax\nOutput", "#1A8CCC"),
]

for (x, y, w, h, label, color) in blocks:
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor="black",
                          linewidth=1)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, label,
            ha="center", va="center", fontsize=9,
            fontfamily="sans-serif")

for i in range(len(blocks) - 1):
    x1 = blocks[i][0] + blocks[i][2]
    x2 = blocks[i + 1][0]
    y_mid = blocks[i][1] + blocks[i][3] / 2
    ax.annotate("", xy=(x2, y_mid), xytext=(x1, y_mid),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.5))

plt.tight_layout()
fig.savefig("figures/architecture_diagram.pdf")
fig.savefig("figures/architecture_diagram.png")
print("Saved: figures/architecture_diagram.pdf, figures/architecture_diagram.png")
