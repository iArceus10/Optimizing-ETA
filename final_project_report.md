# DELHIVERY GRAPH-AWARE LOGISTICS INTELLIGENCE PLATFORM

## Final Technical Documentation

### Optimizing Delivery ETAs with Graph-Based Network Intelligence

---

# Executive Summary

Modern logistics networks operate as highly interconnected systems where delays are rarely isolated events. Traditional ETA prediction models primarily rely on shipment-level attributes and often fail to capture the influence of network structure, hub dependencies, corridor relationships, and operational bottlenecks.

This project investigates whether graph-derived intelligence can improve ETA prediction while simultaneously providing operational decision-support capabilities.

Using approximately 145,000 shipment records from Delhivery's logistics network, a graph representation of the transportation network was constructed, where facilities were modeled as nodes and shipment corridors as directed edges.

Graph-theoretic metrics, community structures, Node2Vec embeddings, and edge-level intelligence features were integrated into machine learning models and evaluated against traditional non-graph baselines.

The study demonstrates that graph-derived intelligence improves ETA prediction performance by 8.25% while revealing critical facilities, high-impact corridors, operational dependencies, and infrastructure prioritization opportunities.

The final deliverable evolved beyond an ETA prediction system and became a Graph-Aware Logistics Intelligence Platform supporting executive decision-making, network analysis, bottleneck identification, facility prioritization, corridor prioritization, and operational strategy development.

---

# Table of Contents

1. Problem Statement
2. Business Context
3. Dataset Overview
4. Project Objectives
5. Methodology
6. Data Engineering
7. Graph Construction
8. Network Analytics
9. Representation Learning
10. ETA Modeling
11. Explainability
12. Operations Intelligence
13. Dashboard Development
14. Results
15. Business Impact
16. Limitations
17. Future Work
18. Conclusion

---

# 1. Problem Statement

Logistics organizations rely heavily on accurate ETA predictions to support customer experience, operational planning, fleet utilization, and service-level compliance.

Traditional ETA models focus primarily on:

* Shipment characteristics
* Distance
* Routing information
* Temporal features

However, logistics networks possess rich relational structures that are often ignored.

Facilities interact with each other repeatedly through transportation corridors, creating network effects that influence delays and congestion patterns.

The central research question addressed in this project was:

Can graph-derived intelligence improve ETA prediction while simultaneously identifying critical network dependencies and operational bottlenecks?

---

# 2. Business Context

Delhivery operates a large-scale logistics network consisting of sorting centers, hubs, transit facilities, and delivery locations connected through transportation corridors.

Operational decisions depend on understanding:

* Which facilities are most critical?
* Which corridors contribute most to delays?
* Where should capacity investments be prioritized?
* How does network structure affect ETA accuracy?
* Can graph intelligence provide measurable business value?

The project aimed to answer these questions through graph analytics and machine learning.

---

# 3. Dataset Overview

Dataset Characteristics

Total Records: 144,867

Unique Trips: 14,817

Facilities: 1,657

Transportation Corridors: 2,783

Target Variable:

factor = actual_time / osrm_time

Where:

actual_time = observed shipment transit duration

osrm_time = shortest-path travel estimate generated using OSRM

A factor greater than 1 indicates ETA inflation relative to expected travel duration.

---

# 4. Project Objectives

Primary Objectives

1. Construct a logistics network graph.

2. Extract graph-derived intelligence.

3. Improve ETA prediction accuracy.

4. Quantify graph contribution.

5. Identify critical facilities.

6. Identify critical corridors.

7. Generate operational recommendations.

8. Develop an executive intelligence dashboard.

Secondary Objectives

* Interpret graph-derived value.
* Measure business impact.
* Enable network planning decisions.
* Support infrastructure prioritization.

---

# 5. Project Methodology

The project followed a phased development framework.

Phase 0

Business Understanding

Data Audit

Roadmap Design

Phase 1

Exploratory Data Analysis

Phase 2

Feature Engineering

Phase 3

Graph Construction

Phase 4

Network Analytics

Phase 5

Representation Learning

Phase 6

Machine Learning Modeling

Phase 7

Explainability

Phase 8

Operations Intelligence

Phase 9

Executive Intelligence Platform

---

# 6. Data Engineering

Feature engineering focused on creating predictive and operationally meaningful attributes.

Temporal Features

* trip_hour
* trip_weekday
* trip_month
* is_weekend

Operational Features

* trip_to_scan_minutes
* trip_to_cutoff_minutes

Volume Features

* source_volume
* destination_volume
* corridor_volume

Routing Features

* osrm_distance
* osrm_time
* osrm_speed

Resulting Feature Store

Rows: 144,867

Columns: 35

---

# 7. Graph Construction

The logistics network was represented as a directed graph.

Node Definition

Each facility represented a node.

Edge Definition

Each shipment corridor represented a directed edge.

Graph Statistics

Nodes: 1,657

Edges: 2,783

Density: 0.001014

Weak Components: 64

Strong Components: 545

Largest Weak Component Coverage: 81.65%

The resulting network exhibited sparse but highly structured connectivity.

---

# 8. Network Analytics

Graph-theoretic metrics were computed for each facility.

Centrality Measures

* Degree Centrality
* In-Degree
* Out-Degree
* Betweenness Centrality
* Closeness Centrality
* PageRank
* HITS Hub Score
* HITS Authority Score

Community Detection

Louvain Community Detection

Detected Communities: 94

Outputs

* node_centrality_features.csv
* community_features.csv

These features captured structural importance and network influence.

---

# 9. Graph Representation Learning

Node2Vec was used to learn latent facility representations.

Configuration

Dimensions: 32

Walk Length: 20

Number of Walks: 200

Window Size: 10

Generated Features

64 embedding features

Validation

* No missing values
* No zero vectors
* Stable embedding distributions

Node2Vec enabled the model to learn hidden network relationships beyond traditional centrality metrics.

---

# 10. Edge Intelligence

Additional corridor-level intelligence features were engineered.

Features

* same_community
* pagerank_difference
* betweenness_difference
* hub_score_difference
* authority_score_difference
* embedding_cosine_similarity

These features captured corridor-level relationships and inter-facility dynamics.

---

# 11. ETA Modeling

Models Evaluated

Random Forest

LightGBM

Training Strategy

GroupShuffleSplit

Grouping Variable:

trip_uuid

Random State:

42

Leakage Prevention

Verified removal of:

* actual_time
* segment_actual_time
* od_end_time
* factor_check
* source_delay
* destination_delay
* corridor_delay
* segment_factor
* cutoff_factor

Trip leakage detected:

0

---

# 12. Model Results

Random Forest

Baseline MAE: 0.4178

Graph MAE: 0.4129

Improvement: 1.16%

LightGBM

Baseline MAE: 0.4473

Graph MAE: 0.4082

RMSE: 0.9330

R²: 0.6397

LightGBM consistently outperformed Random Forest.

---

# 13. Ablation Study

Objective

Quantify the contribution of graph-derived feature families.

Results

Baseline MAE

0.4443

Baseline + Centrality

0.4232

Improvement: 4.75%

Baseline + Centrality + Community

0.4232

Improvement: 4.75%

Full Graph

0.4076

Improvement: 8.25%

Conclusion

Community information contributed minimally.

Embeddings contributed most of the performance gain.

---

# 14. Final Production Model

Model

LightGBM Full Graph + Edge

Performance

MAE: 0.405637

RMSE: 0.936562

R²: 0.636988

MAPE: 18.67%

Feature Count: 103

Training Records: 116,451

Testing Records: 28,416

Persisted Artifacts

* lgbm_final_graph_edge.pkl
* model_metadata.json
* metrics.json

---

# 15. Explainability

SHAP analysis was performed to interpret model behavior.

Top Drivers

* trip_to_cutoff_minutes
* osrm_speed
* route_type
* trip_hour
* betweenness_difference
* trip_to_scan_minutes
* source_volume
* corridor_volume
* embedding_cosine_similarity
* authority_score_difference

The analysis confirmed meaningful contributions from graph-derived features.

---

# 16. Graph Contribution Analysis

Contribution Breakdown

Embeddings

65.24%

Centrality

16.59%

Edge Intelligence

12.94%

Community

5.24%

Most Important Technical Finding

Node2Vec embeddings represented the dominant graph signal.

Graph value was driven primarily by latent network relationships rather than explicit centrality metrics.

---

# 17. Facility Intelligence

Critical facilities were identified using graph centrality, volume, and operational impact.

Top Facilities

IND000000ACB

IND562132AAA

IND421302AAG

IND411033AAA

IND501359AAE

Super Hub Discovery

IND000000ACB repeatedly appeared as:

* Top Hub
* Top Source Facility
* Top Destination Facility
* Critical Dependency
* Highest Impact Facility

This emerged as the most important facility within the network.

---

# 18. Corridor Intelligence

Critical corridors were identified using volume, risk, and operational impact.

Top Corridors

IND000000ACB → IND562132AAA

IND562132AAA → IND000000ACB

IND000000ACB → IND712311AAA

IND000000ACB → IND501359AAE

IND000000ACB → IND421302AAG

These corridors represent the operational backbone of the network.

---

# 19. Bottleneck Identification

A dedicated bottleneck classification model was not developed.

Instead, bottlenecks emerged through:

* Graph centrality analysis
* Impact analysis
* Risk analysis
* Percentile-based prioritization

Facility Bottlenecks

Derived from:

* Top hubs
* Source impact
* Destination impact
* Hub prioritization

Corridor Bottlenecks

Derived from:

* Corridor impact rankings
* Corridor risk rankings
* Corridor prioritization

This approach provided operationally actionable bottleneck intelligence without requiring a separate classification model.

---

# 20. Operations Intelligence

Phase 8 transformed the project from predictive analytics into decision-support intelligence.

Outputs

Facility Prioritization

Corridor Prioritization

ETA Reduction Playbook

Capacity Planning Guidance

FTL vs Carting Framework

Deployment Roadmap

Operations Strategy Memo

---

# 21. Executive Recommendations

Immediate Actions

1. Prioritize upgrades for IND000000ACB.

2. Monitor backbone corridors continuously.

3. Reduce dispatch cutoff delays.

4. Improve scan turnaround times.

5. Expand capacity on high-volume corridors.

6. Implement graph-aware routing decisions.

Strategic Actions

1. Integrate graph intelligence into planning workflows.

2. Establish network dependency monitoring.

3. Develop corridor risk management programs.

4. Build real-time graph intelligence capabilities.

---

# 22. Dashboard Platform

Phase 9 operationalized project outputs through a Streamlit dashboard.

Modules

Executive Dashboard

Facility Intelligence

Corridor Intelligence

Graph Intelligence

ETA Prediction

Network Visualization

Operations Command Center

The dashboard serves as an executive-facing logistics intelligence platform.

---

# 23. Limitations

1. No GraphSAGE implementation.

2. No Graph Neural Networks.

3. No delay-aware embeddings.

4. No weighted Node2Vec.

5. No revenue-at-risk data.

6. No real-time inference pipeline.

7. No dedicated bottleneck classifier.

These limitations represent future opportunities rather than project deficiencies.

---

# 24. Future Roadmap

Priority 1

Weighted Node2Vec

Priority 2

Delay-Aware Node2Vec

Priority 3

Dual Embedding Architecture

Priority 4

Graph Neural Networks

Priority 5

Real-Time Graph Intelligence

Priority 6

Dynamic Network Monitoring

---

# 25. Final Conclusion

This project successfully demonstrated that graph-derived intelligence materially improves ETA prediction while simultaneously uncovering critical network structures and operational dependencies.

Graph features improved ETA prediction performance by 8.25%, with Node2Vec embeddings contributing more than 65% of total graph-derived value.

More importantly, the project evolved beyond predictive modeling and established graph intelligence as a practical operational decision-support capability.

The final platform provides visibility into facility criticality, corridor risk, network dependencies, operational bottlenecks, and strategic infrastructure priorities.

The most important outcome of this work is not the predictive model itself.

It is the demonstration that logistics networks can be understood, optimized, and managed more effectively when treated as graphs rather than isolated shipments.

---

## Final Deliverable

**Delhivery Graph-Aware Logistics Intelligence Platform**

Status: COMPLETE

Phases Completed: 0–9

Final Outcome:

Graph Intelligence → Operational Intelligence → Executive Decision Support
