# EXECUTIVE SUMMARY

## Delhivery Graph-Aware Logistics Intelligence Platform

### Optimizing Delivery ETAs with Graph-Based Network Intelligence

---

# Business Challenge

Modern logistics networks operate as interconnected systems where delays are influenced not only by route characteristics but also by facility dependencies, corridor relationships, network congestion, and operational bottlenecks.

Traditional ETA prediction approaches focus primarily on shipment-level features and often fail to capture the structural dynamics of the underlying transportation network.

Delhivery's logistics ecosystem consists of thousands of facilities and transportation corridors operating simultaneously across a nationwide network. Understanding how network structure affects delivery performance presents a significant opportunity for improving ETA accuracy and operational decision-making.

The objective of this project was to determine whether graph-derived intelligence could improve ETA prediction while simultaneously identifying critical facilities, high-risk corridors, and operational bottlenecks.

---

# Approach

The logistics network was modeled as a directed graph where:

- Facilities represent nodes
- Transportation corridors represent directed edges

The project was executed across nine phases covering:

- Data Engineering
- Feature Engineering
- Graph Construction
- Network Analytics
- Representation Learning
- ETA Modeling
- Explainability
- Operations Intelligence
- Dashboard Development

Graph-derived features included:

- Centrality Metrics
- Community Structures
- Node2Vec Embeddings
- Edge Intelligence Features

These graph features were integrated into machine learning models and benchmarked against traditional non-graph baselines.

---

# Dataset Overview

| Metric           | Value    |
| ---------------- | -------- |
| Shipment Records | 144,867  |
| Trips            | 14,817   |
| Facilities       | 1,657    |
| Corridors        | 2,783    |
| Graph Density    | 0.001014 |

---

# Network Intelligence Findings

The logistics network exhibits a sparse but highly interconnected structure with a small number of facilities exerting disproportionate influence over network performance.

A critical facility was repeatedly identified throughout the analysis:

IND000000ACB

This facility emerged as:

- Highest-degree hub
- Top source facility
- Top destination facility
- Critical network dependency
- Highest operational impact facility

The repeated appearance of this facility across independent analyses validates its strategic importance within the logistics network.

---

# ETA Modeling Results

Final Production Model:

LightGBM Full Graph + Edge

Performance:

| Metric | Value  |
| ------ | ------ |
| MAE    | 0.4056 |
| RMSE   | 0.9366 |
| R²     | 0.6370 |
| MAPE   | 18.67% |

Graph-enhanced models consistently outperformed traditional baselines.

---

# Graph Value Assessment

Ablation studies were conducted to quantify the contribution of graph-derived intelligence.

| Configuration         | MAE    |
| --------------------- | ------ |
| Baseline              | 0.4443 |
| Baseline + Centrality | 0.4232 |
| Full Graph            | 0.4076 |

Overall Improvement:

8.25%

This demonstrates that graph-derived information provides substantial predictive value beyond conventional shipment-level features.

---

# Most Important Technical Finding

Graph contribution analysis revealed:

| Graph Signal      | Contribution |
| ----------------- | ------------ |
| Embeddings        | 65.24%       |
| Centrality        | 16.59%       |
| Edge Intelligence | 12.94%       |
| Community         | 5.24%        |

The dominant source of graph value originated from Node2Vec embeddings.

This indicates that latent network relationships contribute significantly more predictive power than traditional graph metrics alone.

---

# Facility Intelligence

Top Priority Facilities:

1. IND000000ACB
2. IND562132AAA
3. IND160002AAC
4. IND421302AAG
5. IND501359AAE

These facilities represent the most critical operational dependencies within the network and should receive highest priority for capacity planning, infrastructure investment, and operational monitoring.

---

# Corridor Intelligence

Top Priority Corridors:

- IND000000ACB → IND562132AAA
- IND562132AAA → IND000000ACB
- IND000000ACB → IND712311AAA
- IND000000ACB → IND501359AAE
- IND000000ACB → IND421302AAG

These corridors form the backbone of the logistics network and exhibit the highest operational impact.

---

# Strategic Recommendations

Immediate Actions

1. Prioritize infrastructure investment at IND000000ACB.

2. Increase monitoring of backbone corridors.

3. Reduce dispatch cutoff delays.

4. Improve facility scan turnaround times.

5. Implement corridor balancing initiatives.

Strategic Actions

1. Integrate graph intelligence into network planning.

2. Establish continuous network dependency monitoring.

3. Expand graph-aware routing capabilities.

4. Develop real-time logistics intelligence systems.

---

# Dashboard Platform

All project outputs were operationalized through a multi-page Streamlit platform.

Modules include:

- Executive Dashboard
- Facility Intelligence
- Corridor Intelligence
- Graph Intelligence
- ETA Prediction
- Network Visualization
- Operations Command Center

The platform transforms analytical outputs into executive decision-support capabilities.

---

# Business Impact

The project successfully demonstrates that graph intelligence provides value beyond ETA prediction.

Graph-derived insights enabled:

- Critical facility identification
- Corridor prioritization
- Bottleneck discovery
- Network dependency analysis
- Infrastructure prioritization
- Operational strategy development

The project therefore evolved from a predictive modeling exercise into a comprehensive network intelligence platform.

---

# Final Conclusion

The study confirms that graph-derived intelligence materially improves ETA prediction performance while simultaneously providing meaningful operational insights.

Graph features improved predictive performance by 8.25%, with Node2Vec embeddings contributing over 65% of total graph-derived value.

More importantly, the project demonstrates that logistics networks can be managed more effectively when treated as interconnected systems rather than collections of independent shipments.

The final outcome is a production-ready Graph-Aware Logistics Intelligence Platform capable of supporting executive decision-making, network planning, and operational optimization.

---

## Final Deliverable

**Delhivery Graph-Aware Logistics Intelligence Platform**

Status: COMPLETE

Phases Delivered: 0–9

Outcome:

Graph Intelligence → Operational Intelligence → Executive Decision Support
