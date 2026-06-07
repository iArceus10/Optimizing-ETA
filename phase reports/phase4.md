# PHASE 4 REPORT — GRAPH METRICS & CENTRALITY ENGINEERING

Project:

Optimizing Delivery ETAs with Graph-Based Network Intelligence

---

OBJECTIVE

Generate graph-derived intelligence features that quantify structural importance, routing influence, accessibility, and regional clustering within the logistics network.

---

INPUTS

logistics_graph.pkl

node_features.csv

edge_features.csv

---

GRAPH SUMMARY

Nodes: 1,657

Edges: 2,783

Density: 0.001014

Weak Components: 64

Strong Components: 545

Largest Weak Component Coverage: 81.65%

The network remains highly sparse and exhibits strong hub-and-spoke behavior.

---

CENTRALITY METRICS GENERATED

1. Degree Centrality

2. In-Degree Centrality

3. Out-Degree Centrality

4. Betweenness Centrality

5. Closeness Centrality

6. PageRank

7. HITS Hub Score

8. HITS Authority Score

---

COMMUNITY DETECTION

Algorithm:

Louvain Community Detection

Results:

Communities: 94

Mean Size: 17.63

Median Size: 5

Largest Community: 122

The network naturally partitions into operational clusters, indicating regional structure and routing sub-networks.

---

SUPER-HUB DISCOVERY

Facility:

IND000000ACB

Ranked #1 in:

* Degree Centrality
* Betweenness Centrality
* Closeness Centrality
* PageRank
* Hub Score
* Authority Score

Conclusion:

IND000000ACB is the dominant structural node in the entire logistics network.

Operational disruption at this facility would likely affect connectivity, routing efficiency, and ETA performance across large portions of the network.

---

SECOND-TIER BACKBONE HUBS

IND562132AAA

IND501359AAE

IND421302AAG

IND160002AAC

IND712311AAA

These facilities consistently appear among the highest-ranked nodes across multiple centrality metrics.

They likely represent major regional transfer centers.

---

KEY INSIGHTS

1. The logistics network is highly centralized.

2. A national backbone structure exists.

3. A single dominant super-hub governs large-scale connectivity.

4. Community structure indicates natural operational regions.

5. Graph-derived intelligence provides information not available through traditional feature engineering.

6. The network exhibits sufficient structural richness for Graph Representation Learning.

---

EXPORTS CREATED

node_centrality_features.csv

community_features.csv

graph_feature_store.csv

---

PHASE STATUS

Completed Successfully.

---

NEXT PHASE

07_graph_ml.ipynb

Graph Representation Learning

Deliverables:

* Node2Vec Embeddings
* Graph Node Embeddings Store
* Edge Intelligence Features
* Graph ML Feature Store

Purpose:

Capture latent structural information beyond classical centrality measures and prepare graph-aware features for ETA prediction models.
