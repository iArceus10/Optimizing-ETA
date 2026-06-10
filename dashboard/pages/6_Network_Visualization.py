from pathlib import Path
import sys
import numpy as np

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
import plotly.graph_objects as go
import networkx as nx
import pandas as pd

import utils.data_loader as dl

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Network Visualization",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Network Visualization")

st.markdown(
    """
    Visual exploration of the Delhivery logistics network.

    This page highlights network structure,
    backbone corridors,
    critical facilities,
    and operational dependencies discovered
    through graph analytics.
    """
)

# ==================================================
# LOAD DATA
# ==================================================

graph_summary = dl.load_graph_summary()

hub_df = dl.load_top_hubs()

corridor_df = dl.load_top_corridors()

G = dl.load_logistics_graph()

# ==================================================
# NETWORK KPIs
# ==================================================

st.subheader("Network Overview")

nodes = int(graph_summary.loc[0, "nodes"])
edges = int(graph_summary.loc[0, "edges"])

density = graph_summary.loc[0, "density"]

weak = int(
    graph_summary.loc[0, "weak_components"]
)

strong = int(
    graph_summary.loc[0, "strong_components"]
)

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Facilities", f"{nodes:,}")
c2.metric("Corridors", f"{edges:,}")
c3.metric("Density", f"{density:.6f}")
c4.metric("Weak Components", weak)
c5.metric("Strong Components", strong)

st.divider()

# ==================================================
# SUPER HUB
# ==================================================

st.subheader("⭐ Super Hub Spotlight")

super_hub = hub_df.iloc[0]

c1, c2 = st.columns(2)

c1.metric(
    "Facility",
    super_hub["facility"]
)

c2.metric(
    "Degree",
    int(super_hub["degree"])
)

st.success(
    """
    IND000000ACB emerged as the dominant
    logistics facility across every major
    graph intelligence workflow.

    It appears as:

    • Highest-degree network hub

    • Top source facility

    • Top destination facility

    • Major corridor participant

    • Critical network dependency

    This facility represents the strongest
    concentration of network influence.
    """
)

st.divider()

# ==================================================
# TOP HUBS
# ==================================================

st.subheader("Critical Facilities")

top_hubs = hub_df.head(25)

fig_hubs = go.Figure()

fig_hubs.add_trace(
    go.Bar(
        x=top_hubs["facility"],
        y=top_hubs["degree"]
    )
)

fig_hubs.update_layout(
    title="Top Facilities by Network Degree",
    xaxis_title="Facility",
    yaxis_title="Degree"
)

st.plotly_chart(
    fig_hubs,
    use_container_width=True
)

st.dataframe(
    top_hubs,
    use_container_width=True
)

st.divider()

# ==================================================
# BACKBONE NETWORK
# ==================================================

st.subheader("Backbone Corridor Network")

top_edges = corridor_df.head(20)

backbone = nx.DiGraph()

for _, row in top_edges.iterrows():

    backbone.add_edge(
        row["source_center"],
        row["destination_center"],
        volume=row["corridor_volume"],
        median_factor=row["median_factor"],
        distance=row["median_distance"]
    )

# --------------------------------------------------
# Degree Map
# --------------------------------------------------

degree_map = {
    row["facility"]: row["degree"]
    for _, row in hub_df.iterrows()
}

# --------------------------------------------------
# Layout
# --------------------------------------------------

pos = nx.spring_layout(
    backbone,
    seed=42,
    k=0.7
)

# --------------------------------------------------
# Edges
# --------------------------------------------------

edge_traces = []

max_volume = max(
    [
        d["volume"]
        for _, _, d in backbone.edges(data=True)
    ]
)

for u, v, data in backbone.edges(data=True):

    x0, y0 = pos[u]
    x1, y1 = pos[v]

    width = (
        data["volume"] / max_volume
    ) * 8 + 1

    edge_trace = go.Scatter(
        x=[x0, x1],
        y=[y0, y1],
        mode="lines",
        hoverinfo="text",
        text=(
            f"{u} → {v}<br>"
            f"Volume: {data['volume']:,}<br>"
            f"Median Factor: {data['median_factor']:.2f}<br>"
            f"Distance: {data['distance']:.0f} km"
        ),
        line=dict(
            width=width
        )
    )

    edge_traces.append(
        edge_trace
    )

# --------------------------------------------------
# Nodes
# --------------------------------------------------

node_x = []
node_y = []

node_text = []
node_sizes = []
node_colors = []

for node in backbone.nodes():

    x, y = pos[node]

    degree = degree_map.get(
        node,
        1
    )

    node_x.append(x)
    node_y.append(y)

    node_text.append(
        f"{node}<br>"
        f"Degree: {degree}"
    )

    size = (
        np.log1p(degree)
        * 8
    )

    node_sizes.append(size)

    if node == "IND000000ACB":

        node_colors.append(
            "red"
        )

    else:

        node_colors.append(
            "steelblue"
        )

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    text=list(backbone.nodes()),
    textposition="top center",
    hoverinfo="text",
    hovertext=node_text,
    marker=dict(
        size=node_sizes,
        color=node_colors,
        line=dict(width=1)
    )
)

# --------------------------------------------------
# Figure
# --------------------------------------------------

fig_network = go.Figure()

for trace in edge_traces:
    fig_network.add_trace(trace)

fig_network.add_trace(
    node_trace
)

fig_network.update_layout(
    title="Top 20 Backbone Corridors",
    showlegend=False,
    height=750,
    xaxis_visible=False,
    yaxis_visible=False
)

st.plotly_chart(
    fig_network,
    use_container_width=True
)

st.divider()

st.error(
    """
    Network Dependency Alert

    IND000000ACB is visually highlighted in red.

    Node size represents facility degree.

    Edge width represents corridor volume.

    The visualization reveals a strong
    concentration of traffic around a small
    number of facilities and corridors,
    indicating potential operational
    dependency risk.
    """
)

# ==================================================
# CORRIDOR DEPENDENCY
# ==================================================

st.subheader(
    "Backbone Corridors"
)

st.dataframe(
    corridor_df.head(20),
    use_container_width=True
)

st.divider()

# ==================================================
# NETWORK INTELLIGENCE
# ==================================================

st.subheader(
    "Network Dependency Analysis"
)

st.info(
    """
    Graph analytics revealed significant
    concentration around a small number
    of facilities and corridors.

    The network backbone is heavily influenced
    by IND000000ACB and several high-volume
    long-haul corridors.

    Operational disruptions at these locations
    would likely create disproportionate
    network-wide impact.
    """
)

st.divider()

# ==================================================
# EXECUTIVE TAKEAWAYS
# ==================================================

st.subheader(
    "Executive Takeaways"
)

st.success(
    """
    Graph intelligence identified:

    • Critical facilities

    • Backbone corridors

    • Network concentration risk

    • Infrastructure priorities

    • Operational dependencies

    This page demonstrates that the project
    evolved beyond ETA prediction into a
    network planning and logistics intelligence
    capability.
    """
)