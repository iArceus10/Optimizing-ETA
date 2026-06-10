from pathlib import Path
import pandas as pd
import json

# ==================================================
# Project Root
# ==================================================

ROOT = Path(__file__).resolve().parents[2]

REPORTS = ROOT / "reports"
GRAPH = ROOT / "data" / "graph_data"
MODELS = ROOT / "models"

# ==================================================
# Executive Dashboard
# ==================================================

def load_model_results():
    return pd.read_csv(
        REPORTS / "phase6_model_results.csv"
    )


def load_ablation_results():
    return pd.read_csv(
        REPORTS / "phase6_ablation_results.csv"
    )


def load_graph_contribution():
    return pd.read_csv(
        REPORTS / "phase7_graph_contribution_breakdown.csv"
    )


def load_executive_findings():
    return pd.read_csv(
        REPORTS / "phase7_executive_findings.csv"
    )


def load_graph_summary():
    return pd.read_csv(
        GRAPH / "graph_summary.csv"
    )


def load_model_metrics():

    with open(
        MODELS / "lgbm_final_graph_edge_metrics.json"
    ) as f:

        return json.load(f)


def load_model_metadata():

    with open(
        MODELS / "model_metadata.json"
    ) as f:

        return json.load(f)
    
# ==================================================
# Facility Intelligence
# ==================================================

def load_top_source_facilities():
    return pd.read_csv(
        REPORTS / "phase7_top_source_facilities.csv"
    )


def load_top_destination_facilities():
    return pd.read_csv(
        REPORTS / "phase7_top_destination_facilities.csv"
    )


def load_hub_priorities():
    return pd.read_csv(
        REPORTS / "phase8_hub_priorities.csv"
    )


def load_top_hubs():
    return pd.read_csv(
        GRAPH / "top_hubs.csv"
    )

# ==================================================
# Corridor Intelligence
# ==================================================

def load_top_impact_corridors():
    return pd.read_csv(
        REPORTS / "phase7_top_impact_corridors.csv"
    )


def load_high_risk_corridors():
    return pd.read_csv(
        REPORTS / "phase7_high_risk_corridors.csv"
    )


def load_corridor_priorities():
    return pd.read_csv(
        REPORTS / "phase8_corridor_priorities.csv"
    )

# ==================================================
# Graph Intelligence
# ==================================================

def load_centrality_features():
    return pd.read_csv(
        GRAPH / "node_centrality_features.csv"
    )


def load_community_features():
    return pd.read_csv(
        GRAPH / "community_features.csv"
    )


def load_graph_family_contribution():
    return pd.read_csv(
        REPORTS / "phase7_graph_family_contribution.csv"
    )

# ==================================================
# Graph Intelligence
# ==================================================

def load_graph_component_breakdown():
    return pd.read_csv(
        REPORTS / "phase7_graph_component_breakdown.csv"
    )

# ==================================================
# Network Visualization
# ==================================================

import pickle

def load_logistics_graph():

    with open(
        GRAPH / "logistics_graph.pkl",
        "rb"
    ) as f:

        return pickle.load(f)


def load_top_corridors():
    return pd.read_csv(
        GRAPH / "top_corridors.csv"
    )
# ==================================================
# Operations Command Center
# ==================================================

def load_eta_reduction_actions():
    return pd.read_csv(
        REPORTS / "phase8_eta_reduction_actions.csv"
    )


def load_deployment_roadmap():
    return pd.read_csv(
        REPORTS / "phase8_deployment_roadmap.csv"
    )


def load_future_roadmap():
    return pd.read_csv(
        REPORTS / "phase8_future_roadmap.csv"
    )