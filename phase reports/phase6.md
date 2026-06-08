# PHASE 3 REPORT — GRAPH CONSTRUCTION

Project:
Optimizing Delivery ETAs with Graph-Based Network Intelligence

Phase:
Phase 3 — Graph Construction

Status:
Completed Successfully

---

## Objective

Transform Delhivery's logistics network into a graph representation capable of supporting network analytics, centrality computation, community detection, graph machine learning, and ETA prediction.

---

## Graph Design

Graph Type:

Directed Network (NetworkX DiGraph)

Node Definition:

Facility / Logistics Center

Edge Definition:

Observed Shipment Corridor

Direction:

Source Facility → Destination Facility

Edge Weight:

Median Delay Factor

factor = actual_time / osrm_time

---

## Network Statistics

Nodes:
1,657

Edges:
2,783

Density:
0.001014

Weakly Connected Components:
64

Strongly Connected Components:
545

Largest Weak Component:
1,353 nodes

Coverage:
81.65%

---

## Hub Analysis

Dominant Hub:

IND000000ACB

Degree:
94

The facility acts as the primary structural backbone of the logistics network and connects multiple regional sub-networks.

Major Secondary Hubs:

IND562132AAA

IND160002AAC

IND421302AAG

IND501359AAE

These facilities form the second-tier backbone supporting nationwide connectivity.

---

## Corridor Analysis

Highest Volume Corridor:

IND000000ACB → IND562132AAA

Volume:
4,976

Median Factor:
1.684

This corridor represents one of the most operationally important routes within the network.

---

Most Delayed Corridor:

IND212402AAA → IND211002AAB

Median Factor:
31.79

Volume:
65

This corridor demonstrates extreme delay behaviour and represents a candidate for operational investigation.

---

## Key Findings

The logistics network is highly sparse.

A small number of facilities dominate connectivity.

Hub-and-spoke characteristics are clearly visible.

The network structure suggests graph-derived features may carry predictive information beyond traditional tabular logistics features.

Network topology validates the use of:

* Centrality Metrics
* Community Detection
* Node Embeddings
* Graph-Based ETA Modeling

---

## Outputs Generated

logistics_graph.pkl

node_features.csv

edge_features.csv

top_hubs.csv

top_corridors.csv

graph_summary.csv

---

## Business Impact

Phase 3 successfully transformed operational shipment data into a reusable network intelligence asset.

The graph became the foundation for:

* Phase 4 Centrality Engineering
* Phase 5 Node2Vec Representation Learning
* Phase 6 Graph-Aware ETA Modeling
* Phase 7 Explainability
* Phase 8 Executive Recommendations

Without Phase 3, graph intelligence could not be quantified.

This phase established the core infrastructure enabling the project's eventual 8.62% ETA prediction improvement through graph-aware modeling.
