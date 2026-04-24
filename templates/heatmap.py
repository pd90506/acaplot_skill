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

classes = ["Cat", "Dog", "Bird", "Fish", "Horse"]
cm = np.array([
    [45, 2, 1, 0, 2],
    [3, 40, 0, 1, 1],
    [1, 0, 38, 5, 1],
    [0, 1, 4, 42, 3],
    [2, 1, 0, 2, 44],
])
cm_normalized = cm / cm.sum(axis=1, keepdims=True)

fig, ax = plt.subplots(figsize=(3.5, 3))
sns.heatmap(cm_normalized, annot=True, fmt=".2f", cmap="Blues",
            xticklabels=classes, yticklabels=classes, ax=ax,
            vmin=0, vmax=1, linewidths=0.5, linecolor="gray")
ax.set_xlabel("Predicted")
ax.set_ylabel("True")
ax.set_title("Confusion Matrix")
plt.tight_layout()
fig.savefig("figures/heatmap.pdf")
fig.savefig("figures/heatmap.png")
print("Saved: figures/heatmap.pdf, figures/heatmap.png")
