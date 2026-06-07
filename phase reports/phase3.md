# PHASE 3 REPORT — GRAPH CONSTRUCTION & NETWORK INTELLIGENCE

Project:

Optimizing Delivery ETAs with Graph-Based Network Intelligence

---

# Objective

Construct a directed logistics network from facility movement data and validate whether graph-based representations can capture operational structure beyond traditional tabular features.

---

# Graph Design

Nodes:

Facilities

Edges:

Directed corridors between facilities

Graph Type:

NetworkX Directed Graph (DiGraph)

Edge Weight:

Median corridor factor

factor = actual_time / osrm_time

---

# Network Statistics

| Metric                   |    Value |
| ------------------------ | -------: |
| Nodes                    |    1,657 |
| Edges                    |    2,783 |
| Density                  | 0.001014 |
| Weak Components          |       64 |
| Strong Components        |      545 |
| Largest Weak Component   |    1,353 |
| Giant Component Coverage |   81.65% |

---

# Network Interpretation

The logistics network is extremely sparse.

Only approximately 0.1% of all possible facility-to-facility connections exist.

This confirms a highly optimized hub-and-spoke operating structure rather than a fully connected transportation network.

A giant connected component contains 81.65% of all facilities, indicating the existence of a national-scale logistics backbone.

---

# Hub Analysis

Top Facility:

IND000000ACB

Degree:

94

This facility is the most connected node in the entire network.

Result:

Confirmed as a super-hub.

Other Major Hubs:

IND562132AAA

IND160002AAC

IND421302AAG

IND501359AAE

These facilities likely represent major operational transfer centers within the network.

---

# Corridor Analysis

Top Corridor:

IND000000ACB → IND562132AAA

Volume:

4,976

Median Factor:

1.684

Return Corridor:

IND562132AAA → IND000000ACB

Volume:

3,316

Traffic concentration around IND000000ACB is exceptionally high and confirms its role as a central routing facility.

---

# Delayed Corridor Analysis

Most Delayed Supported Corridor:

IND212402AAA → IND211002AAB

Median Factor:

31.79

Volume:

65

Median Actual Time:

1003

Median OSRM Time:

20

Interpretation:

Observed delays are likely driven by operational holding and scheduling effects rather than physical transportation time.

---

# Key Findings

1. The logistics network is highly sparse and graph-friendly.

2. A national backbone component exists.

3. IND000000ACB is the dominant structural hub.

4. Traffic is concentrated among a small number of corridors.

5. Operational delays are often driven by network behavior rather than route distance.

6. Graph-derived features are expected to provide predictive signal beyond traditional feature engineering.

---

# Outputs Generated

graph_data/

* logistics_graph.pkl
* node_features.csv
* edge_features.csv
* top_hubs.csv
* top_corridors.csv
* graph_summary.csv

---

# Phase Status

Completed Successfully.

---

# Next Phase

Graph Metrics & Centrality Engineering

Deliverables:

* Degree Centrality
* In-Degree Centrality
* Out-Degree Centrality
* Betweenness Centrality
* Closeness Centrality
* PageRank
* HITS Scores
* Community Detection
* Graph Feature Store

Purpose:

Create graph intelligence features for downstream ETA prediction models.
