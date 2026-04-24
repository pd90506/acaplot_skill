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
epochs = np.arange(1, 51)

fig, axes = plt.subplots(1, 3, figsize=(7, 2.2))

ax = axes[0]
for lr, label in [(0.01, "lr=0.01"), (0.001, "lr=0.001"), (0.0001, "lr=0.0001")]:
    loss = np.exp(-lr * epochs) + np.random.normal(0, 0.02, len(epochs))
    ax.plot(epochs, loss, label=label, lw=1.2)
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.set_title("(a) Learning Rate")
ax.legend(fontsize=8)
sns.despine(ax=ax)

ax = axes[1]
train_acc = 1 - np.exp(-0.05 * epochs) + np.random.normal(0, 0.01, len(epochs))
val_acc = 1 - np.exp(-0.04 * epochs) + np.random.normal(0, 0.015, len(epochs))
ax.plot(epochs, train_acc * 100, label="Train", lw=1.2)
ax.plot(epochs, val_acc * 100, label="Val", lw=1.2)
ax.set_xlabel("Epoch")
ax.set_ylabel("Accuracy (%)")
ax.set_title("(b) Accuracy")
ax.legend(fontsize=8)
sns.despine(ax=ax)

ax = axes[2]
methods = ["CNN", "RNN", "Trans."]
datasets = ["SST-2", "MNLI", "QQP"]
scores = np.array([
    [92.1, 84.3, 88.7],
    [89.5, 82.1, 86.2],
    [94.2, 87.6, 91.3],
])
x = np.arange(len(datasets))
width = 0.25
palette = sns.color_palette("colorblind", len(methods))
for i, (method, color) in enumerate(zip(methods, palette)):
    ax.bar(x + i * width, scores[i], width, label=method, color=color, edgecolor="black", linewidth=0.5)
ax.set_xticks(x + width)
ax.set_xticklabels(datasets)
ax.set_ylabel("Accuracy (%)")
ax.set_title("(c) Benchmark")
ax.legend(fontsize=8)
sns.despine(ax=ax)

plt.tight_layout()
fig.savefig("figures/subplot_layout.pdf")
fig.savefig("figures/subplot_layout.png")
print("Saved: figures/subplot_layout.pdf, figures/subplot_layout.png")
