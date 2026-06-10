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
    page_title="Corridor Intelligence",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Corridor Intelligence")

st.markdown(
    """
    Corridor-level intelligence for identifying
    delay concentration, routing bottlenecks,
    and operational intervention opportunities.
    """
)

# ==================================================
# Load Data
# ==================================================

impact_df = dl.load_top_impact_corridors()
risk_df = dl.load_high_risk_corridors()
priority_df = dl.load_corridor_priorities()

# ==================================================
# KPI SECTION
# ==================================================

st.subheader("Corridor Overview")

top_corridor = impact_df.iloc[0]

highest_impact = impact_df["impact_score"].max()

critical_count = (
    priority_df["Priority"] == "Critical"
).sum()

high_count = (
    priority_df["Priority"] == "High"
).sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Most Critical Corridor",
    top_corridor["corridor"]
)

c2.metric(
    "Highest Impact Score",
    f"{highest_impact:,.0f}"
)

c3.metric(
    "Critical Corridors",
    int(critical_count)
)

c4.metric(
    "High Priority Corridors",
    int(high_count)
)

st.divider()

# ==================================================
# TOP IMPACT CORRIDORS
# ==================================================

st.subheader("Top Impact Corridors")

fig1 = px.bar(
    impact_df.head(10),
    x="corridor",
    y="impact_score",
    text="impact_score",
    title="Corridor Impact Ranking"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.dataframe(
    impact_df,
    use_container_width=True
)

st.divider()

# ==================================================
# HIGH RISK CORRIDORS
# ==================================================

st.subheader("High Risk Corridors")

fig2 = px.bar(
    risk_df.head(10),
    x="corridor",
    y="impact_score",
    text="impact_score",
    title="High Risk Corridor Ranking"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.dataframe(
    risk_df,
    use_container_width=True
)

st.divider()

# ==================================================
# PRIORITY MATRIX
# ==================================================

st.subheader("Corridor Priority Matrix")

priority_colors = {
    "Critical": "#d62728",
    "High": "#ff7f0e",
    "Medium": "#2ca02c"
}

fig3 = px.scatter(
    priority_df,
    x="shipments",
    y="impact_score",
    color="Priority",
    hover_name="corridor",
    size="impact_score",
    color_discrete_map=priority_colors
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.dataframe(
    priority_df,
    use_container_width=True
)

st.divider()

# ==================================================
# CRITICAL CORRIDOR SPOTLIGHT
# ==================================================

st.subheader("⭐ Critical Corridor Spotlight")

spotlight = priority_df.iloc[0]

c1, c2, c3 = st.columns(3)

c1.metric(
    "Corridor",
    spotlight["corridor"]
)

c2.metric(
    "Shipments",
    int(spotlight["shipments"])
)

c3.metric(
    "Priority",
    spotlight["Priority"]
)

st.success(
    f"""
    {spotlight['corridor']} emerged as the most
    strategically important corridor in the network.

    Impact Score: {spotlight['impact_score']:.0f}

    Recommendation:
    {spotlight['Recommended_Action']}
    """
)

st.divider()

# ==================================================
# OPERATIONAL RECOMMENDATIONS
# ==================================================

st.subheader("Recommended Corridor Actions")

recommendations = (
    priority_df[
        ["corridor", "Priority", "Recommended_Action"]
    ]
)

st.dataframe(
    recommendations,
    use_container_width=True
)

st.success(
    """
    Corridor intelligence enables route-level
    optimization, capacity balancing,
    FTL prioritization,
    and operational intervention planning.
    """
)

corridor = st.selectbox(
    "Search Corridor",
    priority_df["corridor"]
)

# ==================================================
# CORRIDOR LOOKUP
# ==================================================

st.subheader("Corridor Lookup")

selected_corridor = st.selectbox(
    "Select Corridor",
    priority_df["corridor"]
)

corridor_row = priority_df[
    priority_df["corridor"]
    == selected_corridor
].iloc[0]

c1, c2, c3 = st.columns(3)

c1.metric(
    "Priority",
    corridor_row["Priority"]
)

c2.metric(
    "Impact Score",
    f"{corridor_row['impact_score']:.0f}"
)

c3.metric(
    "Shipments",
    int(
        corridor_row["shipments"]
    )
)

st.info(
    corridor_row[
        "Recommended_Action"
    ]
)