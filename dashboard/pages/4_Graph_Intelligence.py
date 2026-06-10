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
    page_title="Graph Intelligence",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Graph Intelligence")

st.markdown(
    """
    This page explains WHY graph-derived intelligence
    improved ETA prediction and how graph analytics
    became an operational decision-support capability.

    Core Question:

    Can logistics network structure improve ETA prediction?

    Answer:

    Yes. Graph intelligence improved model performance
    while simultaneously identifying critical facilities,
    corridors, bottlenecks and dependencies.
    """
)

# ==================================================
# LOAD DATA
# ==================================================

ablation = dl.load_ablation_results()

graph_contrib = dl.load_graph_contribution()

family_contrib = dl.load_graph_family_contribution()

component_df = dl.load_graph_component_breakdown()

findings = dl.load_executive_findings()

# ==================================================
# KPI SECTION
# ==================================================

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

graph_gain = (
    (baseline_mae - full_graph_mae)
    / baseline_mae
) * 100

embedding_share = (
    graph_contrib.loc[
        graph_contrib["Component"] == "Embeddings",
        "Graph_%"
    ].iloc[0]
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Baseline MAE",
    f"{baseline_mae:.4f}"
)

c2.metric(
    "Graph MAE",
    f"{full_graph_mae:.4f}"
)

c3.metric(
    "Graph Improvement",
    f"{graph_gain:.2f}%"
)

c4.metric(
    "Embedding Contribution",
    f"{embedding_share:.2f}%"
)

st.divider()

# ==================================================
# GRAPH VALUE VALIDATION
# ==================================================

st.subheader(
    "Graph Value Validation"
)

fig_ablation = px.bar(
    ablation,
    x="Model",
    y="MAE",
    text="MAE",
    title="Model Ablation Study"
)

fig_ablation.update_layout(
    xaxis_title="Model Variant",
    yaxis_title="MAE"
)

st.plotly_chart(
    fig_ablation,
    use_container_width=True
)

st.dataframe(
    ablation,
    use_container_width=True
)

st.divider()

# ==================================================
# CONTRIBUTION BREAKDOWN
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
        hole=0.50
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader(
        "Contribution Details"
    )

    st.dataframe(
        graph_contrib,
        use_container_width=True
    )

st.divider()

# ==================================================
# FAMILY CONTRIBUTION
# ==================================================

st.subheader(
    "Graph Signal Families"
)

fig_family = px.bar(
    family_contrib,
    x=family_contrib.columns[0],
    y=family_contrib.columns[1],
    text=family_contrib.columns[1]
)

st.plotly_chart(
    fig_family,
    use_container_width=True
)

st.dataframe(
    family_contrib,
    use_container_width=True
)

st.divider()

# ==================================================
# COMPONENT BREAKDOWN
# ==================================================

st.subheader(
    "Graph Component Analysis"
)

if len(component_df.columns) >= 2:

    fig_component = px.bar(
        component_df,
        x=component_df.columns[0],
        y=component_df.columns[1],
        text=component_df.columns[1]
    )

    st.plotly_chart(
        fig_component,
        use_container_width=True
    )

st.dataframe(
    component_df,
    use_container_width=True
)

st.divider()

# ==================================================
# EMBEDDING SPOTLIGHT
# ==================================================

st.subheader(
    "⭐ Node2Vec Embedding Spotlight"
)

c1, c2 = st.columns([1, 2])

with c1:

    st.metric(
        "Contribution",
        f"{embedding_share:.2f}%"
    )

with c2:

    st.success(
        """
        Node2Vec embeddings generated the largest
        performance improvement across all graph
        feature families.

        The results indicate that latent network
        position carries substantially more ETA
        signal than traditional centrality metrics.

        This became the single most important
        technical conclusion of the project.
        """
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
# GRAPH INTELLIGENCE STORY
# ==================================================

st.subheader(
    "From Prediction to Network Intelligence"
)

st.success(
    """
    The project began as an ETA prediction initiative.

    Graph-derived features improved prediction accuracy
    by 8.25%, validating the hypothesis that logistics
    network structure contains predictive information.

    However, the more important outcome was operational.

    Graph analytics identified:

    • Critical facilities

    • Critical corridors

    • Network dependencies

    • Infrastructure priorities

    • Capacity bottlenecks

    • Operational intervention opportunities

    The platform therefore evolved from a machine
    learning project into a Graph-Aware Logistics
    Intelligence Platform.
    """
)

st.divider()

# ==================================================
# FINAL TAKEAWAYS
# ==================================================

st.subheader(
    "Key Takeaways"
)

st.markdown(
    """
    ### 1. Graph Features Work

    ETA prediction improved by 8.25%.

    ### 2. Embeddings Dominate

    Node2Vec contributed 65.24% of graph value.

    ### 3. Community Effects Are Small

    Community signals provided limited incremental gain.

    ### 4. Network Structure Matters

    Logistics performance is strongly influenced by
    facility connectivity and corridor topology.

    ### 5. Graph Intelligence Creates Business Value

    The primary outcome is operational decision support,
    not merely ETA prediction.
    """
)