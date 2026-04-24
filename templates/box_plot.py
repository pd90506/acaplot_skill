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
data = {
    "Model A": np.random.normal(85, 5, 50),
    "Model B": np.random.normal(82, 7, 50),
    "Model C": np.random.normal(88, 4, 50),
    "Model D": np.random.normal(80, 8, 50),
}

fig, ax = plt.subplots(figsize=(3.5, 2.5))
palette = sns.color_palette("colorblind", len(data))
sns.boxplot(data=list(data.values()), palette=palette, ax=ax,
            width=0.5, linewidth=1, fliersize=3)
ax.set_xticklabels(list(data.keys()))
ax.set_ylabel("Accuracy (%)")
ax.set_title("Model Performance Distribution")
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("figures/box_plot.pdf")
fig.savefig("figures/box_plot.png")
print("Saved: figures/box_plot.pdf, figures/box_plot.png")
