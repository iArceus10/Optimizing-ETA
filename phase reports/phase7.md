# PHASE 7 FINAL REPORT

## Objective

Explain the behavior of the final production ETA model and convert predictive performance gains into operational business intelligence.

---

## Model Explained

LightGBM + Graph + Edge Intelligence

Performance:

MAE = 0.4056

RMSE = 0.9366

R² = 0.6370

---

## Key Explainability Findings

The strongest ETA drivers were:

* trip_to_cutoff_minutes
* osrm_speed
* route_type
* trip_hour
* trip_to_scan_minutes
* source_volume
* corridor_volume

Operational delays remain highly influential.

---

## Graph Intelligence Findings

Graph features contributed substantial predictive value.

Graph contribution breakdown:

Embeddings: 65.24%

Centrality: 16.59%

Edge Intelligence: 12.94%

Community: 5.24%

Conclusion:

Node2Vec embeddings are the primary source of graph intelligence.

---

## ETA Inflation Drivers

Operational Drivers:

* Long cutoff delays
* Long scan delays
* High corridor traffic
* High source facility load
* Certain route types

Graph Drivers:

* Low embedding similarity
* Large betweenness differences
* Authority-score imbalance
* Weak destination network positioning

---

## ETA Reduction Drivers

* Strong destination authority
* Favorable network positions
* High OSRM speed
* Efficient route structures
* Beneficial embedding relationships

---

## Facility Insights

Repeatedly high-risk facilities were identified through:

* Source risk analysis
* Destination risk analysis
* Impact score analysis

Several facilities demonstrated persistent ETA inflation behavior and should be prioritized for operational review.

---

## Corridor Insights

High-risk corridors exhibited:

* High delay factors
* High shipment volume
* Significant operational impact

Certain corridors connected through the network super-hub accounted for a disproportionate share of network delay risk.

---

## Network Insight

IND000000ACB emerged as the dominant logistics hub.

Evidence:

* Highest network influence
* Most important corridor participation
* Highest impact score
* Frequent appearance in bottleneck analysis

The network exhibits substantial dependence on this facility.

---

## Business Implications

Graph intelligence captures logistics behavior not visible through traditional operational features.

Embeddings encode latent network structure that significantly improves ETA prediction.

This validates graph-aware logistics intelligence as a meaningful operational capability.

---

## Phase Outcome

Phase 7 successfully transformed predictive performance gains into explainable business intelligence.

The project is now ready for executive recommendation development and deployment planning in Phase 8.
