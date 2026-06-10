from pathlib import Path
import sys

# ==================================================
# Import Fix
# ==================================================

DASHBOARD_ROOT = Path(__file__).resolve().parent.parent

if str(DASHBOARD_ROOT) not in sys.path:
    sys.path.insert(0, str(DASHBOARD_ROOT))

# ==================================================
# Imports
# ==================================================

import streamlit as st
import plotly.express as px

import utils.data_loader as dl

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Operations Command Center",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Operations Command Center")

st.markdown(
    """
    Executive decision-support layer for the
    Delhivery Graph-Aware Logistics Intelligence Platform.

    This page consolidates network intelligence,
    bottleneck prioritization, graph insights,
    operational recommendations and deployment strategy
    into a single executive view.
    """
)

# ==================================================
# LOAD DATA
# ==================================================

graph_summary = dl.load_graph_summary()

metrics = dl.load_model_metrics()

graph_contrib = dl.load_graph_contribution()

hub_priority = dl.load_hub_priorities()

corridor_priority = dl.load_corridor_priorities()

eta_actions = dl.load_eta_reduction_actions()

deployment = dl.load_deployment_roadmap()

future = dl.load_future_roadmap()

# ==================================================
# EXECUTIVE KPI ROW
# ==================================================

st.subheader("Network Health")

nodes = int(graph_summary.loc[0, "nodes"])
edges = int(graph_summary.loc[0, "edges"])

graph_gain = 8.25

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Facilities",
    f"{nodes:,}"
)

c2.metric(
    "Corridors",
    f"{edges:,}"
)

c3.metric(
    "Graph Improvement",
    f"{graph_gain:.2f}%"
)

c4.metric(
    "Production MAE",
    f"{metrics['MAE']:.4f}"
)

st.divider()

# ==================================================
# CRITICAL DEPENDENCIES
# ==================================================

st.subheader("Critical Network Dependencies")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Critical Facility",
    "IND000000ACB"
)

c2.metric(
    "Critical Corridor",
    "ACB → 562132"
)

c3.metric(
    "Network Dependency",
    "HIGH"
)

st.warning(
    """
    IND000000ACB repeatedly emerged as:

    • Top Hub

    • Top Source Facility

    • Top Destination Facility

    • Top Corridor Participant

    • Highest Impact Facility

    This facility represents the strongest
    operational dependency in the network.
    """
)

st.divider()

# ==================================================
# GRAPH INTELLIGENCE
# ==================================================

st.subheader("Graph Intelligence Drivers")

fig = px.bar(
    graph_contrib,
    x="Component",
    y="Graph_%",
    text="Graph_%"
)

fig.update_layout(
    yaxis_title="Contribution (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    graph_contrib,
    use_container_width=True
)

st.success(
    """
    Node2Vec embeddings contributed 65.24%
    of total graph-derived value and became
    the dominant graph signal in the project.
    """
)

st.divider()

# ==================================================
# OPERATIONAL BOTTLENECK INTELLIGENCE
# ==================================================

st.subheader("Operational Bottleneck Intelligence")

left, right = st.columns(2)

with left:

    st.markdown(
        "### Tier 1 Facilities"
    )

    tier1 = hub_priority[
        hub_priority["Priority"] == "Tier 1"
    ]

    st.dataframe(
        tier1.head(10),
        use_container_width=True
    )

with right:

    st.markdown(
        "### Critical Corridors"
    )

    critical = corridor_priority[
        corridor_priority["Priority"] == "Critical"
    ]

    st.dataframe(
        critical.head(10),
        use_container_width=True
    )

st.info(
    """
    Bottlenecks were identified through graph intelligence,
    impact analysis, ETA inflation analysis and percentile-
    based operational prioritization.

    No dedicated bottleneck classification model was trained.
    """
)

st.divider()

# ==================================================
# ETA REDUCTION PLAYBOOK
# ==================================================

st.subheader("ETA Reduction Playbook")

st.dataframe(
    eta_actions,
    use_container_width=True
)

fig_actions = px.bar(
    eta_actions,
    x="Driver",
    y=[1] * len(eta_actions)
)

fig_actions.update_layout(
    yaxis_visible=False,
    showlegend=False
)

st.plotly_chart(
    fig_actions,
    use_container_width=True
)

st.divider()

# ==================================================
# DEPLOYMENT ROADMAP
# ==================================================

st.subheader("Deployment Roadmap")

st.dataframe(
    deployment,
    use_container_width=True
)

st.success(
    """
    Current maturity level:

    Graph-Aware Operational Intelligence Platform

    The project evolved beyond ETA prediction
    into a decision-support capability.
    """
)

st.divider()

# ==================================================
# FUTURE ROADMAP
# ==================================================

st.subheader("Research & Innovation Roadmap")

st.dataframe(
    future,
    use_container_width=True
)

st.info(
    """
    Future graph research directions focus on
    richer network representations including
    weighted embeddings, delay-aware embeddings,
    dual embedding architectures and Graph Neural Networks.
    """
)

st.divider()

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.subheader("Executive Summary")

st.success(
    """
    KEY OUTCOMES

    • Graph features improved ETA prediction by 8.25%

    • Final Production MAE = 0.4056

    • Node2Vec embeddings generated 65.24% of graph value

    • IND000000ACB emerged as the dominant network dependency

    • Critical facilities and corridors were successfully prioritized

    • Graph intelligence enabled operational decision support

    FINAL CONCLUSION

    This project evolved from an ETA prediction initiative
    into a Graph-Aware Logistics Intelligence Platform.
    """
)

st.subheader("Intelligence Core")

st.metric(
    "Graph Value Gain",
    "+8.25%"
)

st.metric(
    "Embedding Dominance",
    "65.24%"
)

st.metric(
    "Critical Hub",
    "ACB"
)