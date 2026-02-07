import networkx as nx
import matplotlib.pyplot as plt

def normalize(term):
    term = term.lower()
    if "large language model" in term or "llm" in term:
        return "Large Language Models"
    if "code" in term:
        return "Code Generation"
    if "numerical" in term:
        return "Numerical Reasoning"
    return term.title()

def plot_convergence(trends):
    G = nx.Graph()

    # Normalize + deduplicate
    nodes = list(set(normalize(t[0]) for t in trends[:6]))

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            G.add_edge(nodes[i], nodes[j])

    # Bigger canvas
    fig, ax = plt.subplots(figsize=(7, 7))

    # Stable layout with spacing
    pos = nx.spring_layout(G, seed=42, k=1.2)

    # Draw nodes and edges
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color="#B3E5FC",
        node_size=3200,
        ax=ax
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="#90A4AE",
        width=1.5,
        ax=ax
    )

    # Draw labels manually with offset
    for node, (x, y) in pos.items():
        ax.text(
            x,
            y + 0.05,  # vertical offset
            node,
            fontsize=10,
            ha="center",
            va="center",
            bbox=dict(
                facecolor="white",
                edgecolor="none",
                alpha=0.7,
                pad=1.5
            )
        )

    ax.set_title("Technology Convergence Map (Key Themes)", fontsize=12)
    ax.set_axis_off()

    # Add padding so labels never clip
    plt.margins(0.25)
    plt.tight_layout()

    return fig
