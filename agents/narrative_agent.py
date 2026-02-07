def generate_narrative(trends, trl, velocity, forecast):
    top_trends = ", ".join([t[0] for t in trends[:3]])

    narrative = f"""
The analysis indicates that current research is strongly focused on {top_trends}.
The technology is presently assessed at {trl}, suggesting it is beyond early research
but not yet fully mature.

Trend velocity analysis shows that interest is {velocity.lower()}, indicating
active research momentum.

Based on current maturity and momentum, the technology is forecasted as follows:
{forecast}
"""

    return narrative.strip()
