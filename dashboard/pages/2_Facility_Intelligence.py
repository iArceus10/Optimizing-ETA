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

from utils.data_loader import (
    load_top_source_facilities,
    load_top_destination_facilities,
    load_hub_priorities,
    load_top_hubs
)

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Facility Intelligence",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Facility Intelligence")

st.markdown(
    """
    Facility-level intelligence for identifying
    critical hubs, operational bottlenecks,
    and infrastructure investment priorities.
    """
)

# ==================================================
# Load Data
# ==================================================

source_df = load_top_source_facilities()

destination_df = load_top_destination_facilities()

priority_df = load_hub_priorities()

hub_df = load_top_hubs()

# ==================================================
# KPI SECTION
# ==================================================

st.subheader("Facility Overview")

top_source = source_df.iloc[0]

top_destination = destination_df.iloc[0]

highest_impact = source_df["impact_score"].max()

tier1_count = (
    priority_df["Priority"] == "Tier 1"
).sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Top Source Facility",
    top_source["source_center"]
)

c2.metric(
    "Top Destination Facility",
    top_destination["destination_center"]
)

c3.metric(
    "Highest Impact Score",
    f"{highest_impact:,.0f}"
)

c4.metric(
    "Tier 1 Facilities",
    int(tier1_count)
)

st.divider()

# ==================================================
# TOP NETWORK HUBS
# ==================================================

st.subheader("Top Network Hubs")

fig_hubs = px.bar(
    hub_df.head(10),
    x="facility",
    y="degree",
    text="degree",
    title="Top Facilities by Network Degree"
)

st.plotly_chart(
    fig_hubs,
    use_container_width=True
)

st.dataframe(
    hub_df,
    use_container_width=True
)

st.divider()

# ==================================================
# TOP SOURCE FACILITIES
# ==================================================

st.subheader("Top Source Facilities")

fig_source = px.bar(
    source_df.head(10),
    x="source_center",
    y="impact_score",
    text="impact_score",
    title="Source Facility Impact Ranking"
)

st.plotly_chart(
    fig_source,
    use_container_width=True
)

st.dataframe(
    source_df,
    use_container_width=True
)

st.divider()

# ==================================================
# TOP DESTINATION FACILITIES
# ==================================================

st.subheader("Top Destination Facilities")

fig_dest = px.bar(
    destination_df.head(10),
    x="destination_center",
    y="impact_score",
    text="impact_score",
    title="Destination Facility Impact Ranking"
)

st.plotly_chart(
    fig_dest,
    use_container_width=True
)

st.dataframe(
    destination_df,
    use_container_width=True
)

st.divider()

# ==================================================
# HUB PRIORITIZATION
# ==================================================

st.subheader("Hub Prioritization")

priority_colors = {
    "Tier 1": "#d62728",
    "Tier 2": "#ff7f0e",
    "Tier 3": "#2ca02c"
}

fig_priority = px.scatter(
    priority_df,
    x="shipments",
    y="impact_score",
    color="Priority",
    hover_name="source_center",
    color_discrete_map=priority_colors,
    size="impact_score",
    title="Facility Priority Matrix"
)

st.plotly_chart(
    fig_priority,
    use_container_width=True
)

st.dataframe(
    priority_df,
    use_container_width=True
)

st.divider()

# ==================================================
# SUPER HUB SPOTLIGHT
# ==================================================

st.subheader("⭐ Super Hub Spotlight")

acb = source_df[
    source_df["source_center"] == "IND000000ACB"
]

if not acb.empty:

    row = acb.iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Facility",
        row["source_center"]
    )

    c2.metric(
        "Shipments",
        f"{int(row['shipments']):,}"
    )

    c3.metric(
        "Impact Score",
        f"{row['impact_score']:,.0f}"
    )

st.success(
    """
    IND000000ACB emerged as the most critical
    network facility across graph analysis,
    source impact analysis,
    destination impact analysis,
    and corridor participation analysis.

    This facility represents the strongest
    operational dependency in the logistics network.
    """
)

st.divider()

# ==================================================
# EXECUTIVE ACTIONS
# ==================================================

st.subheader("Recommended Actions")

actions = {
    "Tier 1": "Immediate capacity review and infrastructure investment",
    "Tier 2": "Targeted optimization and performance monitoring",
    "Tier 3": "Routine operational monitoring"
}

for tier, action in actions.items():

    st.info(
        f"**{tier}** → {action}"
    )

st.divider()

st.success(
    """
    Facility intelligence transforms graph insights
    into operational decisions by identifying
    where infrastructure investments will generate
    the highest network-wide impact.
    """
)

facility_code = st.selectbox(
    "Search Facility",
    sorted(
        set(
            source_df["source_center"]
        )
        |
        set(
            destination_df["destination_center"]
        )
    )
)

# ==================================================
# FACILITY LOOKUP
# ==================================================

st.subheader("Facility Lookup")

facility_list = sorted(
    set(
        source_df["source_center"]
    ).union(
        set(
            destination_df[
                "destination_center"
            ]
        )
    )
)

selected_facility = st.selectbox(
    "Select Facility",
    facility_list
)

source_match = source_df[
    source_df["source_center"]
    == selected_facility
]

dest_match = destination_df[
    destination_df["destination_center"]
    == selected_facility
]

hub_match = hub_df[
    hub_df["facility"]
    == selected_facility
]

c1, c2, c3 = st.columns(3)

if not hub_match.empty:

    c1.metric(
        "Network Degree",
        int(
            hub_match.iloc[0]["degree"]
        )
    )

if not source_match.empty:

    c2.metric(
        "Source Impact",
        f"{source_match.iloc[0]['impact_score']:.0f}"
    )

if not dest_match.empty:

    c3.metric(
        "Destination Impact",
        f"{dest_match.iloc[0]['impact_score']:.0f}"
    )

if selected_facility == "IND000000ACB":

    st.success(
        """
        ⭐ Super Hub Detected

        This facility emerged as the most
        critical dependency across all
        graph intelligence analyses.
        """
    )