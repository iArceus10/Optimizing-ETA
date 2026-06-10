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

import utils.data_loader as dl

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="ETA Prediction",
    page_icon="⏱️",
    layout="wide"
)

st.title("⏱️ ETA Prediction")

st.markdown(
    """
    ETA prediction is one capability within the
    Delhivery Graph-Aware Logistics Intelligence Platform.

    The production model combines operational,
    temporal, network and graph-derived intelligence
    to estimate delivery delay behavior.
    """
)

# ==================================================
# LOAD DATA
# ==================================================

metrics = dl.load_model_metrics()

metadata = dl.load_model_metadata()

# ==================================================
# MODEL OVERVIEW
# ==================================================

st.subheader("Production Model")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Model",
    "LightGBM"
)

c2.metric(
    "Target",
    metadata["target"]
)

c3.metric(
    "Features",
    metadata["feature_count"]
)

st.divider()

# ==================================================
# PERFORMANCE
# ==================================================

st.subheader("Model Performance")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "MAE",
    f"{metrics['MAE']:.4f}"
)

c2.metric(
    "RMSE",
    f"{metrics['RMSE']:.4f}"
)

c3.metric(
    "R²",
    f"{metrics['R2']:.4f}"
)

c4.metric(
    "MAPE",
    f"{metrics['MAPE']:.2f}%"
)

st.divider()

# ==================================================
# TRAINING SUMMARY
# ==================================================

st.subheader("Training Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Train Rows",
    f"{metadata['train_rows']:,}"
)

c2.metric(
    "Test Rows",
    f"{metadata['test_rows']:,}"
)

c3.metric(
    "Feature Count",
    metadata["feature_count"]
)

st.divider()

# ==================================================
# ETA CALCULATION
# ==================================================

st.subheader("ETA Calculation Logic")

st.code(
    """
factor = actual_time / osrm_time

Predicted ETA =
Predicted Factor × OSRM Time
    """,
    language="text"
)

st.info(
    """
    The model predicts a delay factor rather than
    predicting time directly.

    This makes the model portable across route lengths,
    distances and operational conditions.
    """
)

st.divider()

# ==================================================
# DELAY RISK FRAMEWORK
# ==================================================

st.subheader("Delay Risk Framework")

risk_data = {
    "Risk Level": [
        "Low Risk",
        "Moderate Risk",
        "High Risk"
    ],
    "Factor Range": [
        "< 1.2",
        "1.2 - 1.8",
        "> 1.8"
    ],
    "Operational Meaning": [
        "Near expected transit time",
        "Moderate delay probability",
        "Significant delay probability"
    ]
}

st.dataframe(
    risk_data,
    use_container_width=True
)

st.divider()

# ==================================================
# WHAT DRIVES ETA
# ==================================================

st.subheader("Primary ETA Drivers")

drivers = [
    "Trip-to-cutoff time",
    "OSRM speed",
    "Route type",
    "Trip hour",
    "Trip-to-scan time",
    "Source volume",
    "Corridor volume",
    "Embedding cosine similarity",
    "Betweenness difference",
    "Authority score difference"
]

for driver in drivers:
    st.write(f"• {driver}")

st.divider()

# ==================================================
# GRAPH INTELLIGENCE IMPACT
# ==================================================

st.subheader("Graph Intelligence Impact")

st.success(
    """
    Graph-derived intelligence improved model
    performance from MAE 0.4443 to 0.4076.

    Total improvement:

    8.25%

    Node2Vec embeddings contributed the majority
    of graph-derived predictive value.
    """
)

st.divider()

# ==================================================
# PLATFORM PERSPECTIVE
# ==================================================

st.subheader("Platform Perspective")

st.info(
    """
    ETA prediction is not the primary outcome
    of this project.

    The larger value comes from:

    • Facility Intelligence

    • Corridor Intelligence

    • Graph Intelligence

    • Network Visualization

    • Operational Decision Support

    ETA prediction serves as one component
    of the broader Graph-Aware Logistics
    Intelligence Platform.
    """
)

st.divider()

# ==================================================
# FINAL SUMMARY
# ==================================================

st.success(
    """
    Final Production Model:

    LightGBM Full Graph + Edge

    MAE: 0.4056

    R²: 0.6370

    MAPE: 18.67%

    Graph intelligence successfully improved ETA
    prediction while simultaneously enabling
    network-level operational decision support.
    """
)