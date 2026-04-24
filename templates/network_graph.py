import os
import graphviz

os.makedirs("figures", exist_ok=True)

def build_graph():
    dot = graphviz.Digraph(comment="Transformer Data Flow")
    dot.attr(rankdir="TB", dpi="300", bgcolor="white",
             fontname="Times New Roman", fontsize="10",
             nodesep="0.4", ranksep="0.5")
    dot.attr("node", shape="box", style="rounded,filled",
             fillcolor="#B3D9F2", fontname="Times New Roman", fontsize="10",
             color="black", penwidth="1")
    dot.attr("edge", color="gray", arrowsize="0.7", fontname="Times New Roman", fontsize="9")

    edges = [
        ("Input", "Encoder", ""),
        ("Encoder", "Attention", ""),
        ("Attention", "FFN", ""),
        ("FFN", "Decoder", ""),
        ("Decoder", "Output", ""),
        ("Attention", "Encoder", "residual"),
    ]
    for src, dst, label in edges:
        if label:
            dot.edge(src, dst, label=label, style="dashed")
        else:
            dot.edge(src, dst)
    return dot

dot = build_graph()
dot.format = "pdf"
dot.render("figures/network_graph", cleanup=True)

dot = build_graph()
dot.format = "png"
dot.render("figures/network_graph", cleanup=True)

print("Saved: figures/network_graph.pdf, figures/network_graph.png")
