# PHASE 5 REPORT — GRAPH REPRESENTATION LEARNING

Project:

Optimizing Delivery ETAs with Graph-Based Network Intelligence

---

# OBJECTIVE

Generate latent graph representations capable of capturing structural relationships beyond traditional graph metrics.

The goal is to create graph-aware features for downstream ETA prediction models.

---

# INPUTS

logistics_graph.pkl

graph_feature_store.csv

node_centrality_features.csv

community_features.csv

---

# GRAPH SUMMARY

Nodes: 1,657

Edges: 2,783

Density: 0.001014

Weak Components: 64

Strong Components: 545

Largest Weak Component Coverage: 81.65%

The network remains sparse, hierarchical, and strongly hub-oriented.

---

# NODE EMBEDDINGS

Method:

Node2Vec

Configuration:

Dimensions = 32

Walk Length = 20

Num Walks = 200

Window Size = 10

Workers = 4

Seed = 42

---

# EMBEDDING STORE

Generated:

graph_node_embeddings.csv

Shape:

1657 × 33

Columns:

facility

embedding_1

...

embedding_32

---

# EMBEDDING VALIDATION

Vector Norm Analysis

Results:

Count: 1657

Mean Norm: 4.06

Minimum Norm: 1.84

Maximum Norm: 7.20

Findings:

No NaN vectors.

No zero vectors.

Embedding distribution appears healthy.

---

# NEAREST NEIGHBOR ANALYSIS

Purpose:

Validate whether Node2Vec captured meaningful structural relationships.

Result:

Embeddings grouped facilities into operationally similar neighborhoods.

Example:

Major hubs tended to retrieve facilities sharing regional and neighborhood structure.

Important Observation:

Embeddings did not simply reproduce centrality rankings.

Interpretation:

Centrality metrics capture global importance.

Node2Vec embeddings capture latent structural similarity.

This indicates complementary information rather than redundancy.

---

# EDGE INTELLIGENCE FEATURES

Generated:

same_community

pagerank_difference

betweenness_difference

hub_score_difference

authority_score_difference

embedding_cosine_similarity

Output:

graph_edge_features.csv

---

# GRAPH ML FEATURE STORE

Created:

graph_ml_feature_store.csv

Shape:

1657 × 43

Contents:

Graph Metrics

Community Features

Node Embeddings

Purpose:

Direct integration into ETA prediction models.

---

# KEY INSIGHTS

1. The logistics network contains meaningful latent structure beyond centrality metrics.

2. Node2Vec successfully learned operational neighborhoods.

3. Graph embeddings provide complementary information to traditional graph features.

4. The network exhibits sufficient structural richness for graph-aware machine learning.

5. Graph intelligence is now ready for predictive modeling.

---

# OUTPUTS GENERATED

graph_node_embeddings.csv

graph_edge_features.csv

graph_ml_feature_store.csv

---

# DEFERRED ENHANCEMENTS

Not Implemented:

Weighted Node2Vec

Delay-Aware Node2Vec

Dual Embedding Architecture

Edge Embeddings

Reason:

Model uplift has not yet been measured.

These remain future optimization opportunities.

---

# PHASE STATUS

Completed Successfully

---

# NEXT PHASE

03_segment_model.ipynb

Segment-Level ETA Prediction

Primary Goal:

Quantify predictive uplift provided by graph intelligence relative to traditional logistics features.
