# PHASE 6 REPORT — SEGMENT ETA MODELING & GRAPH INTELLIGENCE VALIDATION

Project:
Optimizing Delivery ETAs with Graph-Based Network Intelligence

Phase:
Phase 6 — Segment-Level ETA Modeling

Status:
Completed Successfully

---

## Objective

Quantify whether graph-derived intelligence improves ETA prediction beyond traditional logistics features.

This phase represents the first direct measurement of business value generated from graph analytics.

Primary Research Question:

"Do graph-derived features improve ETA prediction beyond traditional operational features?"

---

## Modeling Strategy

Target Variable:

factor = actual_time / osrm_time

Validation Strategy:

GroupShuffleSplit

Grouping Variable:

trip_uuid

Reason:

Prevent trip-level leakage.

Verification:

0 overlapping trips between train and test sets.

---

## Leakage Controls

Excluded Features:

actual_time

segment_actual_time

od_end_time

factor_check

source_delay

destination_delay

corridor_delay

segment_factor

cutoff_factor

Only features available at prediction time were used.

---

## Model Experiments

### Random Forest Baseline

Features:

Phase 2 engineered logistics features only.

Results:

MAE:
0.4178

RMSE:
0.9823

R²:
0.6006

---

### Random Forest Graph Model

Features:

Baseline Features

*

Centrality Features

*

Community Features

*

Node2Vec Embeddings

Results:

MAE:
0.4129

RMSE:
0.9370

R²:
0.6366

Improvement:

MAE:
1.16%

RMSE:
4.61%

Conclusion:

Graph signal detected but not fully exploited.

---

## LightGBM Baseline

Features:

Traditional logistics features only.

Results:

MAE:
0.4446

RMSE:
1.0105

R²:
0.5774

---

## LightGBM Graph Model

Features:

Baseline Features

*

Centrality Features

*

Community Features

*

Node2Vec Embeddings

Results:

MAE:
0.4063

RMSE:
0.9320

R²:
0.6405

Improvement:

MAE:
8.62%

RMSE:
7.77%

R²:
+0.0631

Conclusion:

Graph intelligence provides significant predictive value.

Project hypothesis validated.

---

## Feature Importance Findings

Top-ranked features included multiple Node2Vec embedding dimensions.

Examples:

src_embedding_26

src_embedding_12

src_embedding_4

dst_embedding_21

dst_embedding_28

Interpretation:

Graph embeddings capture latent structural information not represented by traditional logistics features.

---

## Graph Ablation Study

Purpose:

Quantify contribution of individual graph intelligence components.

---

### Baseline

MAE:
0.4443

---

### Baseline + Centrality

MAE:
0.4232

Gain:
4.75%

Finding:

Network importance significantly influences ETA behavior.

---

### Baseline + Centrality + Community

MAE:
0.4232

Gain:
4.75%

Finding:

Community assignments contribute negligible standalone predictive value.

---

### Full Graph Model

MAE:
0.4076

Gain:
8.25%

Finding:

Node2Vec embeddings provide substantial additional predictive signal beyond classical graph metrics.

---

## Edge Intelligence Experiment

Added Features:

same_community

pagerank_difference

betweenness_difference

hub_score_difference

authority_score_difference

embedding_cosine_similarity

Results:

Full Graph:

MAE:
0.4076

Full Graph + Edge:

MAE:
0.4056

Additional Gain:

0.48%

Conclusion:

Edge-level graph intelligence contributes modest but measurable value.

Most graph value originates from node-level intelligence.

---

## Final Production Candidate

Model:

LightGBM

Features:

Baseline Logistics Features

*

Centrality Metrics

*

Community Features

*

Node2Vec Embeddings

*

Edge Intelligence Features

Performance:

MAE:
0.4056

RMSE:
0.9366

R²:
0.6370

---

## Key Research Findings

Graph intelligence improves ETA prediction.

Centrality metrics explain approximately half of graph-derived gains.

Node2Vec embeddings explain the remaining majority of graph-derived gains.

Community assignments provide limited standalone value.

Edge intelligence contributes incremental improvements.

Graph-aware ETA prediction outperforms traditional logistics-only models.

---

## Business Impact

The project successfully demonstrates that logistics network structure contains predictive information not captured by traditional operational features.

Graph intelligence enables:

* More accurate ETA prediction
* Better identification of critical facilities
* Better understanding of corridor behavior
* Improved operational decision support

---

## Phase Outcome

Status:

SUCCESS

Research Question:

Answered

Graph Intelligence Value:

Validated

Production Candidate:

Established

Next Phase:

Phase 7 — Explainability (SHAP Analysis)
