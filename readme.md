# Optimizing Delivery ETAs with Graph-Based Network Intelligence

## Project Overview

This project aims to improve delivery ETA prediction for a logistics network using Machine Learning and Graph Analytics.

Traditional ETA systems such as OSRM estimate travel times based primarily on road networks and shortest paths. However, real-world logistics operations are affected by multiple factors such as:

* Hub congestion
* Corridor delays
* Route scheduling
* Transportation mode (FTL vs Carting)
* Operational bottlenecks

This project builds a graph-based logistics intelligence system capable of:

* Improving ETA prediction beyond OSRM
* Detecting bottleneck hubs
* Identifying delayed corridors
* Recommending FTL vs Carting transportation modes
* Generating business recommendations for network optimization

---

## Business Problem

Logistics companies frequently experience discrepancies between planned and actual delivery times.

Current routing systems do not fully account for:

* Operational delays
* Hub-level inefficiencies
* Network congestion effects
* Historical route behavior

This project addresses these limitations through graph-aware ETA prediction and logistics network intelligence.

---

## Dataset

Approximate Size:

* 144,867 records
* 24 features

Key Columns:

* trip_creation_time
* route_type
* source_center
* destination_center
* actual_time
* osrm_time
* factor
* segment_actual_time
* segment_factor

Target Variables:

Primary:

* segment_factor

Secondary:

* factor

---

## Project Objectives

### Business Objectives

* Improve ETA accuracy
* Reduce delivery delays
* Detect bottleneck hubs
* Identify delayed corridors
* Optimize transportation mode selection

### Machine Learning Objectives

* Predict route delays
* Predict segment-level delays
* Compare against OSRM baseline
* Build explainable ETA prediction models

### Graph Analytics Objectives

* Build logistics network graph
* Compute hub importance metrics
* Detect critical network nodes
* Identify delay-prone corridors

---

## Technology Stack

### Data Science

* Python
* Pandas
* NumPy
* Scikit-Learn

### Machine Learning

* LightGBM
* XGBoost

### Graph Analytics

* NetworkX
* iGraph
* Louvain Community Detection

### Explainability

* SHAP

### Visualization

* Matplotlib
* Seaborn
* Plotly

---

## Project Structure

data/

* raw/
* cleaned/
* feature_store/

notebooks/

* 00_data_audit.ipynb
* 01_eda.ipynb
* 02_feature_engineering.ipynb
* 03_segment_model.ipynb
* 04_graph_build.ipynb

src/

* data_loader.py
* data_audit.py
* feature_engineering.py
* graph_builder.py
* graph_metrics.py

models/

reports/

dashboard/

presentations/

---

## Planned Workflow

Phase 0:

* Project Design
* Architecture
* Repository Setup

Phase 1:

* Data Audit
* Exploratory Data Analysis

Phase 2:

* Feature Engineering

Phase 3:

* Baseline ML Models

Phase 4:

* LightGBM ETA Prediction

Phase 5:

* Graph Construction

Phase 6:

* Graph Intelligence Layer

Phase 7:

* Business Recommendations

Phase 8:

* Dashboard and Final Report

---

## Expected Outcomes

* Improved ETA prediction over OSRM
* Hub bottleneck detection
* Corridor intelligence
* Transportation mode recommendations
* Executive-level logistics insights
