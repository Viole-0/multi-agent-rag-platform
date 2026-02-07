def evaluate_trl(documents):
    score = 0

    for doc in documents:
        text = doc.lower()

        if "experiment" in text or "benchmark" in text:
            score += 1
        if "prototype" in text or "framework" in text:
            score += 2
        if "deployment" in text or "production" in text:
            score += 3
        if "industry" in text or "real-world" in text:
            score += 2

    if score <= 3:
        return "TRL 1–3 (Early Research)"
    elif score <= 8:
        return "TRL 4–6 (Prototype / Validation)"
    else:
        return "TRL 7–9 (Production / Deployment)"
