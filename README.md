# acaplot_skill

A superpowers skill for generating publication-ready academic figures for CS/ML/AI papers.

## What It Does

Given a natural language description (and optional data), generates:
- Complete Python scripts (matplotlib + seaborn + networkx)
- Rendered PDF (vector) + PNG (300 DPI) output

## Supported Figure Types

| Type | Examples |
|------|----------|
| Data visualization | Training curves, bar charts, scatter plots, heatmaps, box plots |
| Architecture diagrams | Model pipelines, block diagrams, flowcharts |
| Mathematical figures | Function curves, geometric diagrams |
| Network graphs | Dependency graphs, relationship diagrams |

## Usage

Load the skill and describe the figure you need:

> "Plot training and validation loss curves from results.csv"

> "Draw a Transformer architecture diagram with 6 encoder layers"

> "Scatter plot of t-SNE embeddings colored by class label"

## Templates

See `templates/` for reference implementations of common figure types.

## Requirements

Python 3 with: matplotlib, seaborn, numpy, pandas, networkx, scikit-learn

### Setup

```bash
python3 -m venv .venv
.venv/bin/pip install matplotlib seaborn numpy pandas networkx scikit-learn
```
