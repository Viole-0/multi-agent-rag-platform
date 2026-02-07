import sys
import os

# --------------------------------------------------
# Fix Python path so Streamlit can see project files
# --------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

# --------------------------------------------------
# Imports
# --------------------------------------------------
import streamlit as st

from graph.agent_graph import run_pipeline

from visuals.trend_chart import plot_trends
from visuals.trl_indicator import trl_to_numeric
from visuals.velocity_badge import velocity_style
from visuals.trl_timeline_chart import plot_trl_timeline
from visuals.convergence_graph import plot_convergence

from utils.citations import format_citations
from utils.pdf_export import export_pdf

from config.domains import DOMAINS

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Technology Intelligence Platform",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🧠 Multi-Agent Technology Intelligence Platform")
st.markdown(
    "Analyze emerging technologies using grounded multi-agent intelligence, "
    "trend analytics, maturity estimation, and forecasting."
)

# --------------------------------------------------
# Domain selector + query
# --------------------------------------------------
domain = st.selectbox("🌐 Select Technology Domain", list(DOMAINS.keys()))

query = st.text_input(
    "🔍 Enter technology focus",
    DOMAINS[domain]
)

# --------------------------------------------------
# Run analysis
# --------------------------------------------------
if st.button("Analyze Technology"):
    result = run_pipeline(query)

    insights = result["insights"]
    metadata = result["metadata"]

    # ==================================================
    # ROW 1 — Trends & TRL
    # ==================================================
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Emerging Technology Trends")
        fig = plot_trends(insights["trends"])
        st.pyplot(fig)

    with col2:
        st.subheader("⚙️ Technology Readiness Level (TRL)")
        trl_value = trl_to_numeric(insights["trl"])
        st.metric(
            label="Current TRL",
            value=trl_value,
            help=insights["trl"]
        )
        st.caption(insights["trl_timeline"])

    st.divider()

    # ==================================================
    # ROW 2 — Timeline & Convergence
    # ==================================================
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📅 TRL Timeline (Research Activity)")
        st.pyplot(plot_trl_timeline(metadata))

    with col4:
        st.subheader("🔗 Technology Convergence Map")
        st.pyplot(plot_convergence(insights["trends"]), width="stretch")

    st.divider()

    # ==================================================
    # ROW 3 — Momentum & Forecast
    # ==================================================
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("📊 Trend Momentum")
        st.markdown(velocity_style(insights["velocity"]))

    with col6:
        st.subheader("🔮 Forecast")
        st.info(insights["forecast"])

    st.divider()

    # ==================================================
    # Narrative
    # ==================================================
    st.subheader("🧾 Strategic Narrative")
    st.success(insights["narrative"])

    st.divider()

    # ==================================================
    # Source Citations
    # ==================================================
    st.subheader("📌 Source Citations")
    citations = format_citations(metadata)
    for c in citations:
        st.write(c)

    st.divider()

    # ==================================================
    # PDF Export
    # ==================================================
    st.subheader("📤 Export Report")

    file_path = export_pdf(insights)

    with open(file_path, "rb") as f:
        st.download_button(
            label="Download PDF Report",
            data=f,
            file_name="technology_intelligence_report.pdf",
            mime="application/pdf"
        )

    st.divider()

    # ==================================================
    # System Self-Evaluation
    # ==================================================
    st.subheader("✅ System Self-Evaluation")
    st.write("**Confidence Level:**", result["confidence"])
    st.write("**Sources Used:**", result["sources_used"])
