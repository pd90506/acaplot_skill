# acaplot Skill Design Spec

## Overview

A superpowers skill that generates publication-ready academic figures for CS/ML/AI papers. Given a natural language description (and optional data), the skill produces complete Python scripts and rendered PDF + PNG output.

## Scope

### Supported Figure Types

| Category | Examples | Primary matplotlib Module |
|----------|----------|--------------------------|
| Data visualization | Line plots, bar charts, scatter plots, heatmaps, box plots, error bar plots, confusion matrices | `pyplot` + `seaborn` |
| Flow / architecture diagrams | Model architectures, pipeline diagrams, algorithm flowcharts | `patches` (FancyBboxPatch, FancyArrowPatch) + `annotations` |
| Mathematical / geometric figures | Function curves, geometric diagrams, 3D surface plots | `numpy` + `pyplot` |
| Network / relationship graphs | Dependency graphs, knowledge graphs, tree structures | `networkx` + `pyplot` |

### Out of Scope

- Excalidraw / draw.io / Mermaid / TikZ generation
- Interactive figures (Plotly, Bokeh)
- Presentation slides or poster layouts
- Non-CS/ML academic conventions (biology, physics-specific standards)

## Workflow

1. User describes the desired figure in natural language
2. User optionally provides data (file path or inline in conversation)
3. Skill generates a complete, self-contained Python script
4. Skill executes the script via Bash
5. Script outputs PDF + PNG to `./figures/` directory
6. Skill returns file paths of both images and the script

### Data Input Modes

- **File path**: User provides path to CSV/JSON/TSV file; script reads with `pandas` or `json`
- **Inline data**: User provides data directly in conversation; script embeds as Python dict/list
- **Simulated data**: When no real data is provided and user only needs a schematic, script generates representative data with `numpy`

## Toolchain

All figure generation uses Python 3 with the following libraries:

| Library | Purpose | Version Baseline |
|---------|---------|-----------------|
| `matplotlib` | Core plotting engine | >= 3.7 |
| `seaborn` | Statistical plot wrappers, color palettes | >= 0.12 |
| `numpy` | Numerical computation, data generation | >= 1.24 |
| `pandas` | Data I/O (CSV, JSON, TSV) | >= 2.0 |
| `networkx` | Graph/network data structures and layout | >= 3.0 |

These are standard in any scientific Python environment (conda, pip). The skill does not introduce exotic dependencies.

## Academic Style Guide (CS/ML)

### Fonts

- Text/annotations: serif (Times New Roman or Computer Modern)
- Axis labels/ticks: sans-serif (Helvetica/Arial) at publisher-standard sizes
- Matplotlib rcParams configuration applied at script top

### Font Sizes

| Element | Size (pt) |
|---------|-----------|
| Title / suptitle | 14 |
| Axis labels | 12 |
| Tick labels | 10 |
| Legend | 10 |
| Annotations | 10-12 |

### Figure Dimensions

- Single-column: 3.5 inches wide
- Double-column: 7.0 inches wide
- Height determined by aspect ratio (default ~2.5-4 inches)
- Custom sizes when user specifies

### Color Palette

- Default: seaborn colorblind-friendly palette (`seaborn.color_palette("colorblind")`)
- User can specify custom colors; skill respects explicit requests
- Gradients for heatmaps: `viridis`, `rocket`, or `coolwarm` depending on context

### Layout Rules

- Always call `plt.tight_layout()` before saving
- Minimize chart junk: no unnecessary gridlines, spines, or decorations
- Use `despine()` for seaborn figures
- Consistent padding and margins

## Output Specification

### File Location

- All outputs saved to `./figures/` relative to the working directory
- Directory created automatically if it does not exist

### Naming Convention

- Format: `{descriptive_name}.{pdf,png,py}`
- Example: `training_curves.pdf`, `training_curves.png`, `training_curves.py`
- Script file shares the same base name as its output figures

### File Formats

- **PDF**: Vector format, suitable for LaTeX inclusion. Saved with `bbox_inches='tight'`
- **PNG**: Raster at 300 DPI, suitable for previews and non-LaTeX workflows
- Both formats always generated together

### Script Qualities

- Self-contained: can be re-run independently without the skill
- Top-down structure: imports → style config → data loading → plotting → save
- No hardcoded absolute paths; uses `os.path.join` relative to script location
- No comments unless user requests them (per code style preferences)

## Code Templates

The skill will contain reference patterns for common CS/ML figure types:

### Training Curves (Loss/Accuracy)

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette("colorblind")
fig, ax = plt.subplots(figsize=(3.5, 2.5))
ax.plot(epochs, train_loss, label="Train")
ax.plot(epochs, val_loss, label="Val")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.legend()
sns.despine(ax=ax)
plt.tight_layout()
fig.savefig("figures/loss_curve.pdf", bbox_inches="tight")
fig.savefig("figures/loss_curve.png", dpi=300, bbox_inches="tight")
```

### Bar Chart with Error Bars (Ablation Study)

```python
fig, ax = plt.subplots(figsize=(3.5, 2.5))
x = range(len(methods))
ax.bar(x, means, yerr=stds, capsize=3, color=sns.color_palette("colorblind"))
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.set_ylabel("Accuracy (%)")
sns.despine(ax=ax)
plt.tight_layout()
```

### Architecture Diagram (Block Diagram)

```python
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(7, 2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

blocks = [
    (0.5, 1, 1.5, 1, "Input"),
    (2.5, 1, 1.5, 1, "Conv"),
    (4.5, 1, 1.5, 1, "ReLU"),
    (6.5, 1, 1.5, 1, "Pool"),
    (8.5, 1, 1.5, 1, "Output"),
]
for (x, y, w, h, label) in blocks:
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                          facecolor="lightblue", edgecolor="black")
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, label, ha="center", va="center", fontsize=10)

for i in range(len(blocks) - 1):
    x1 = blocks[i][0] + blocks[i][2]
    x2 = blocks[i+1][0]
    y_mid = blocks[i][1] + blocks[i][3] / 2
    ax.annotate("", xy=(x2, y_mid), xytext=(x1, y_mid),
                arrowprops=dict(arrowstyle="->", color="black"))
```

### Network Graph

```python
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")])
fig, ax = plt.subplots(figsize=(3.5, 2.5))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, ax=ax, with_labels=True, node_color="lightblue",
        node_size=500, font_size=10, edge_color="gray")
plt.tight_layout()
```

## Skill File Structure

```
acaplot_skill/
├── SKILL.md              # Main skill instructions
├── templates/            # Code template snippets
│   ├── training_curves.py
│   ├── bar_chart.py
│   ├── heatmap.py
│   ├── scatter.py
│   ├── architecture_diagram.py
│   └── network_graph.py
├── docs/
│   └── superpowers/
│       └── specs/
│           └── 2026-04-23-acaplot-skill-design.md
├── README.md
└── LICENSE
```

## Error Handling

- If script execution fails, skill reads the error output, fixes the script, and retries (up to 2 retries)
- Missing output directory: script creates `./figures/` automatically
- Missing dependencies: skill checks for required libraries before execution and reports which to install

## Success Criteria

- Generated scripts are self-contained and re-runnable
- Output figures meet CS/ML publication quality standards
- Skill handles all four figure categories (data viz, diagrams, math, networks)
- PDF output is vector and scalable
- PNG output is 300 DPI
