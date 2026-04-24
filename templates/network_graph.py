import os
import networkx as nx
import matplotlib.pyplot as plt

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

G = nx.DiGraph()
edges = [
    ("Input", "Encoder"),
    ("Encoder", "Attention"),
    ("Attention", "FFN"),
    ("FFN", "Decoder"),
    ("Decoder", "Output"),
    ("Attention", "Encoder"),
]
G.add_edges_from(edges)

fig, ax = plt.subplots(figsize=(3.5, 2.5))
pos = nx.spring_layout(G, seed=42, k=1.5)
nx.draw(G, pos, ax=ax, with_labels=True,
        node_color="#B3D9F2", node_size=600,
        font_size=8, font_family="sans-serif",
        edge_color="gray", arrows=True,
        arrowsize=12, linewidths=1,
        edgecolors="black")
plt.tight_layout()
fig.savefig("figures/network_graph.pdf")
fig.savefig("figures/network_graph.png")
print("Saved: figures/network_graph.pdf, figures/network_graph.png")
