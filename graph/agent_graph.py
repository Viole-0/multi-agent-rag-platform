from agents.retrieval_agent import retrieve_docs
from agents.trend_agent import analyze_trends
from agents.trl_agent import evaluate_trl
from agents.trend_velocity_agent import compute_trend_velocity
from agents.forecast_agent import forecast_trend
from agents.trl_timeline_agent import trl_timeline
from agents.evaluator_agent import self_evaluate
from agents.narrative_agent import generate_narrative

def run_pipeline(query: str):
    # --- Retrieval ---
    docs, metadata = retrieve_docs(query, return_metadata=True)

    # --- Analysis ---
    trends = analyze_trends(docs)
    trl = evaluate_trl(docs)
    velocity = compute_trend_velocity(docs, metadata)
    forecast = forecast_trend(trl, velocity)
    timeline = trl_timeline(metadata)
    narrative = generate_narrative(trends, trl, velocity, forecast)

    insights = {
        "trends": trends,
        "trl": trl,
        "velocity": velocity,
        "forecast": forecast,
        "trl_timeline": timeline,
        "narrative": narrative
    }

    evaluated = self_evaluate(insights, docs)

    # ✅ ADD METADATA TO FINAL OUTPUT
    evaluated["metadata"] = metadata

    return evaluated
