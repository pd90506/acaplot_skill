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

sns.set_palette("colorblind")

epochs = np.arange(1, 101)
train_loss = 1.0 / np.sqrt(epochs) + np.random.normal(0, 0.02, len(epochs))
val_loss = 1.0 / np.sqrt(epochs) + 0.05 + np.random.normal(0, 0.03, len(epochs))

fig, ax = plt.subplots(figsize=(3.5, 2.5))
ax.plot(epochs, train_loss, label="Train")
ax.plot(epochs, val_loss, label="Validation")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.legend()
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("figures/training_curves.pdf")
fig.savefig("figures/training_curves.png")
print("Saved: figures/training_curves.pdf, figures/training_curves.png")
