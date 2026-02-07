from datetime import datetime

def compute_trend_velocity(documents, metadata):
    recent = 0
    older = 0

    current_year = datetime.now().year

    for meta in metadata:
        year = int(meta["published"][:4])
        if year >= current_year - 1:
            recent += 1
        else:
            older += 1

    if recent > older:
        return "Rapidly Increasing 📈"
    elif recent == older:
        return "Stable ➖"
    else:
        return "Slowing Down 📉"
