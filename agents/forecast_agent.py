def forecast_trend(trl, velocity):
    if "Rapidly" in velocity and "TRL 4–6" in trl:
        return "Likely to reach early production adoption in 1–2 years."
    if "Stable" in velocity:
        return "Expected to evolve incrementally with steady adoption."
    if "Slowing" in velocity:
        return "May consolidate or be replaced by alternative approaches."

    return "Insufficient data for forecasting."
