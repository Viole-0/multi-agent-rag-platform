def velocity_style(velocity):
    if "Rapidly" in velocity:
        return "🟢 Rapid Growth"
    if "Stable" in velocity:
        return "🟡 Stable"
    return "🔴 Slowing"
