def self_evaluate(insights, documents):
    confidence = "High"

    if len(documents) < 3:
        confidence = "Low"

    return {
        "insights": insights,
        "confidence": confidence,
        "sources_used": len(documents)
    }
