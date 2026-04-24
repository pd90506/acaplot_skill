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
tokens = ["The", "cat", "sat", "on", "the", "mat"]
n = len(tokens)
attention = np.random.dirichlet(np.ones(n), size=n)
for i in range(n):
    attention[i, i] += 0.3
attention = attention / attention.sum(axis=1, keepdims=True)

fig, ax = plt.subplots(figsize=(3.5, 3))
sns.heatmap(attention, annot=True, fmt=".2f", cmap="YlOrRd",
            xticklabels=tokens, yticklabels=tokens, ax=ax,
            vmin=0, vmax=attention.max(), linewidths=0.5, linecolor="white")
ax.set_xlabel("Key")
ax.set_ylabel("Query")
ax.set_title("Self-Attention Weights")
ax.xaxis.set_ticks_position("top")
ax.xaxis.set_label_position("top")
plt.tight_layout()
fig.savefig("figures/attention_heatmap.pdf")
fig.savefig("figures/attention_heatmap.png")
print("Saved: figures/attention_heatmap.pdf, figures/attention_heatmap.png")
