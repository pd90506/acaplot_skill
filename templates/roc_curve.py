import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc

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
n = 200
y_true = np.random.randint(0, 2, n)
models = {
    "Model A (AUC=0.92)": np.clip(y_true * 0.8 + np.random.normal(0, 0.15, n), 0, 1),
    "Model B (AUC=0.85)": np.clip(y_true * 0.6 + np.random.normal(0, 0.2, n), 0, 1),
    "Model C (AUC=0.78)": np.clip(y_true * 0.4 + np.random.normal(0, 0.25, n), 0, 1),
}

fig, ax = plt.subplots(figsize=(3.5, 3))
colors = ["#0072B2", "#E69F00", "#009E73"]
for (label, scores), color in zip(models.items(), colors):
    fpr, tpr, _ = roc_curve(y_true, scores)
    roc_auc = auc(fpr, tpr)
    ax.plot(fpr, tpr, color=color, lw=1.5, label=label)

ax.plot([0, 1], [0, 1], "k--", lw=0.8, alpha=0.5)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("ROC Curve")
ax.legend(loc="lower right")
ax.set_xlim([0, 1])
ax.set_ylim([0, 1.05])
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("figures/roc_curve.pdf")
fig.savefig("figures/roc_curve.png")
print("Saved: figures/roc_curve.pdf, figures/roc_curve.png")
