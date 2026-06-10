from pathlib import Path
import sys

# ==================================================
# Make dashboard root importable
# ==================================================

DASHBOARD_ROOT = Path(__file__).resolve().parent.parent

if str(DASHBOARD_ROOT) not in sys.path:
    sys.path.insert(0, str(DASHBOARD_ROOT))

# ==================================================
# Imports
# ==================================================

import streamlit as st
import plotly.express as px

from utils.data_loader import (
    load_graph_summary,
    load_model_metrics,
    load_model_metadata,
    load_ablation_results,
    load_graph_contribution,
    load_executive_findings
)

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    # 📊 Executive Dashboard

    ### Graph-Aware Logistics Intelligence Platform
    """
)

st.markdown(
    """
    Graph-Aware Logistics Intelligence Platform

    Executive overview of network performance,
    graph intelligence value,
    operational bottlenecks,
    and business impact.
    """
)

# ==================================================
# Load Data
# ==================================================

graph_summary = load_graph_summary()

metrics = load_model_metrics()

metadata = load_model_metadata()

ablation = load_ablation_results()

graph_contrib = load_graph_contribution()

findings = load_executive_findings()

# ==================================================
# KPI SECTION
# ==================================================

st.subheader("Network Overview")

nodes = int(graph_summary.loc[0, "nodes"])
edges = int(graph_summary.loc[0, "edges"])

communities = 94

records = (
    metadata["train_rows"]
    + metadata["test_rows"]
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Facilities", f"{nodes:,}")
c2.metric("Corridors", f"{edges:,}")
c3.metric("Communities", f"{communities:,}")
c4.metric("Records", f"{records:,}")

st.divider()

# ==================================================
# MODEL PERFORMANCE
# ==================================================

st.subheader("Final Production Model")

c1, c2, c3, c4 = st.columns(4)

c1.metric("MAE", f"{metrics['MAE']:.4f}")
c2.metric("RMSE", f"{metrics['RMSE']:.4f}")
c3.metric("R²", f"{metrics['R2']:.4f}")
c4.metric("MAPE", f"{metrics['MAPE']:.2f}%")

st.divider()

# ==================================================
# GRAPH ADVANTAGE
# ==================================================

st.subheader("Graph Intelligence Value")

baseline_mae = (
    ablation.loc[
        ablation["Model"] == "Baseline",
        "MAE"
    ].iloc[0]
)

full_graph_mae = (
    ablation.loc[
        ablation["Model"] == "Full Graph",
        "MAE"
    ].iloc[0]
)

improvement = (
    (baseline_mae - full_graph_mae)
    / baseline_mae
) * 100

c1, c2, c3 = st.columns(3)

c1.metric(
    "Baseline MAE",
    f"{baseline_mae:.4f}"
)

c2.metric(
    "Graph MAE",
    f"{full_graph_mae:.4f}"
)

c3.metric(
    "Improvement",
    f"{improvement:.2f}%"
)

st.divider()

# ==================================================
# GRAPH CONTRIBUTION
# ==================================================

left, right = st.columns(2)

with left:

    st.subheader(
        "Graph Contribution Breakdown"
    )

    fig = px.pie(
        graph_contrib,
        names="Component",
        values="Graph_%",
        hole=0.45
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

with right:

    st.subheader(
        "Graph Component Contributions"
    )

    st.dataframe(
        graph_contrib,
        width="stretch"
    )

st.divider()

# ==================================================
# ABLATION STUDY
# ==================================================

st.subheader(
    "Graph Value Validation"
)

fig2 = px.bar(
    ablation,
    x="Model",
    y="MAE",
    text="MAE"
)

fig2.update_layout(
    xaxis_title="Model Variant",
    yaxis_title="MAE"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

st.divider()

# ==================================================
# EXECUTIVE FINDINGS
# ==================================================

st.subheader(
    "Executive Findings"
)

for _, row in findings.iterrows():

    st.info(
        f"""
        **{row['Finding']}**

        {row['Evidence']}
        """
    )

st.divider()

# ==================================================
# FINAL SUMMARY
# ==================================================

st.success(
    """
    Graph-enhanced ETA prediction improved MAE
    from 0.4443 to 0.4076 (8.25% improvement).

    Node2Vec embeddings contributed 65.24%
    of graph-derived intelligence.

    Critical facilities and corridors were
    successfully identified for operational action.
    """
)

