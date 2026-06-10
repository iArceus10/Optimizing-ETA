
import streamlit as st



st.set_page_config(
    page_title="Delhivery Logistics Intelligence",
    page_icon="assets/app1.png",
    layout="wide"
)



st.sidebar.markdown(
    """
    # 🌐 DL-GRAPH OS

    ### v1.0
    Graph-Aware Logistics Intelligence
    """
)

st.sidebar.divider()

st.sidebar.metric(
    "Facilities",
    "1,657"
)

st.sidebar.metric(
    "Corridors",
    "2,783"
)

st.sidebar.metric(
    "Graph Value",
    "+8.25%"
)

st.sidebar.metric(
    "Super Hub",
    "ACB"
)

st.sidebar.divider()

st.sidebar.info(
    """
    Graph Engine: ACTIVE

    Network Monitoring: ACTIVE

    ETA Intelligence: ACTIVE
    """
)

st.title(
    " Delhivery Graph-Aware Logistics Intelligence Platform"
)

st.markdown(
    """
    Executive Decision Support System built using:

    - Logistics Network Intelligence
    - Graph Analytics
    - Node2Vec Embeddings
    - ETA Prediction
    - Facility Intelligence
    - Corridor Intelligence
    """
)

st.success(
    "Use the sidebar to navigate through dashboard modules."
)