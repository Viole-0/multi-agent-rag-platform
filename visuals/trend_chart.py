import matplotlib.pyplot as plt

def plot_trends(trends):
    labels = [t[0] for t in trends]
    scores = [t[1] for t in trends]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(labels[::-1], scores[::-1])
    ax.set_title("Key Emerging Technology Trends")
    ax.set_xlabel("Importance Score")

    return fig
