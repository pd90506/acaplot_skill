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

methods = ["CNN", "RNN", "Transformer"]
datasets = ["SST-2", "MNLI", "QQP", "QNLI"]
scores = np.array([
    [92.1, 84.3, 88.7, 90.2],
    [89.5, 82.1, 86.2, 87.8],
    [94.2, 87.6, 91.3, 93.1],
])
stds = np.array([
    [0.8, 1.2, 0.9, 0.7],
    [1.0, 1.5, 1.1, 0.9],
    [0.6, 0.8, 0.7, 0.5],
])

x = np.arange(len(datasets))
width = 0.25
palette = sns.color_palette("colorblind", len(methods))

fig, ax = plt.subplots(figsize=(3.5, 2.5))
for i, (method, color) in enumerate(zip(methods, palette)):
    ax.bar(x + i * width, scores[i], width, yerr=stds[i],
           label=method, color=color, edgecolor="black", linewidth=0.5,
           capsize=2, error_kw={"linewidth": 0.8})

ax.set_xticks(x + width)
ax.set_xticklabels(datasets)
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(75, 100)
ax.legend()
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("figures/grouped_bar.pdf")
fig.savefig("figures/grouped_bar.png")
print("Saved: figures/grouped_bar.pdf, figures/grouped_bar.png")
