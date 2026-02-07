def format_citations(metadata):
    citations = []
    for m in metadata:
        citations.append(
            f"• {m['title']} ({m['published'][:4]})"
        )
    return citations
