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

np.random.seed(42)
n = 100
cluster1 = np.random.randn(n, 2) + [-2, 1]
cluster2 = np.random.randn(n, 2) + [2, -1]
cluster3 = np.random.randn(n, 2) + [0, 3]

fig, ax = plt.subplots(figsize=(3.5, 2.5))
palette = sns.color_palette("colorblind", 3)
ax.scatter(cluster1[:, 0], cluster1[:, 1], s=10, alpha=0.7, label="Class A", color=palette[0])
ax.scatter(cluster2[:, 0], cluster2[:, 1], s=10, alpha=0.7, label="Class B", color=palette[1])
ax.scatter(cluster3[:, 0], cluster3[:, 1], s=10, alpha=0.7, label="Class C", color=palette[2])
ax.set_xlabel("t-SNE Dim 1")
ax.set_ylabel("t-SNE Dim 2")
ax.legend(markerscale=2)
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("figures/scatter.pdf")
fig.savefig("figures/scatter.png")
print("Saved: figures/scatter.pdf, figures/scatter.png")
