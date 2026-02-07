def trl_to_numeric(trl_text):
    if "1–3" in trl_text:
        return 2
    if "4–6" in trl_text:
        return 5
    return 8
