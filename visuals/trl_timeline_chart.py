import matplotlib.pyplot as plt
from collections import Counter

def plot_trl_timeline(metadata):
    years = [int(m["published"][:4]) for m in metadata]
    counts = Counter(years)

    x = sorted(counts.keys())
    y = [counts[yr] for yr in x]

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, y, marker="o")
    ax.set_title("Research Activity Over Time (TRL Proxy)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Publications")

    return fig
