import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("figures", exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Computer Modern"],
    "font.size": 10,
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

methods = ["Baseline", "+Data", "+Augment", "+Pretrain", "Ours"]
means = [72.3, 75.1, 76.8, 78.2, 81.5]
stds = [1.2, 0.9, 1.1, 0.8, 0.7]

fig, ax = plt.subplots(figsize=(3.5, 2.5))
x = np.arange(len(methods))
colors = sns.color_palette("colorblind", len(methods))
ax.bar(x, means, yerr=stds, capsize=3, color=colors, edgecolor="black", linewidth=0.5)
ax.set_xticks(x)
ax.set_xticklabels(methods, rotation=30, ha="right")
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(65, 85)
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("figures/bar_chart.pdf")
fig.savefig("figures/bar_chart.png")
print("Saved: figures/bar_chart.pdf, figures/bar_chart.png")
