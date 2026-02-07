def trl_timeline(metadata):
    years = [int(m["published"][:4]) for m in metadata]

    if len(set(years)) == 1:
        return "TRL appears stable over time."
    elif max(years) - min(years) >= 3:
        return "TRL shows gradual upward progression."
    else:
        return "TRL is evolving but still volatile."
