# Phase 1 Report — Exploratory Data Analysis & Logistics Intelligence

## Project

Optimizing Delivery ETAs with Graph-Based Network Intelligence

---

## Phase Objective

The objective of Phase 1 was to perform a logistics-focused exploratory data analysis (EDA), validate potential prediction targets, investigate data quality issues, understand network structure, and prepare the foundation for graph-based machine learning.

---

## Dataset Overview

### Dataset Size

* Rows: 144,867
* Columns: 24

### Key Discovery

The dataset is not shipment-level data.

Each row represents a route segment (route leg) within a larger trip.

* Unique Trips: 14,817
* Total Records: 144,867

This implies that a single trip can contain multiple route legs, making the dataset naturally suitable for graph modeling.

---

## Missing Value Analysis

Only two columns contain missing values:

| Column           | Missing Count | Missing % |
| ---------------- | ------------- | --------- |
| source_name      | 293           | 0.20%     |
| destination_name | 261           | 0.18%     |

All operational metrics are complete.

### Conclusion

The dataset quality is excellent and requires minimal missing-value treatment.

---

## Route Type Analysis

| Route Type | Count  |
| ---------- | ------ |
| FTL        | 99,660 |
| Carting    | 45,207 |

### Observations

* FTL dominates network movement.
* Carting still represents a substantial portion of operations.
* No severe class imbalance exists.

---

## Actual Time Analysis

### Statistics

* Mean: 416.93
* Median: 132
* 99th Percentile: 2599
* Maximum: 4532

### Findings

The distribution is highly right-skewed.

A small subset of routes contributes disproportionately to overall delays.

---

## OSRM Time Analysis

### Statistics

* Mean: 213.87
* Median: 64
* Maximum: 1686

### Findings

OSRM consistently underestimates actual operational delivery times.

Operational realities such as:

* Hub congestion
* Loading/unloading delays
* Scheduling delays
* Cutoff constraints

are not captured by OSRM.

---

## Target Validation

### Factor

Definition:

factor = actual_time / osrm_time

Validation Result:

* Verification Accuracy: 100%
* Computation Error: Near Zero

### Statistics

* Mean: 2.12
* Median: 1.86
* 95th Percentile: 3.61
* Maximum: 77.39

### Decision

factor is selected as the primary modeling target.

---

## Segment Factor Investigation

### Statistics

* Mean: 2.22
* Minimum: -23.44
* Maximum: 574.25

### Findings

* Negative segment_factor rows: 2,365
* segment_osrm_time < 1 rows: 2,347

Extreme values are caused by unstable denominator values.

### Decision

segment_factor is rejected as the primary prediction target.

---

## Facility Analysis

### Unique Facilities

1,657

### Findings

The logistics network contains a large number of operational hubs.

Certain facilities appear significantly more frequently than others, indicating major distribution centers.

---

## Corridor Analysis

### Unique Corridors

2,783

### Findings

Several corridors account for a large fraction of total network movement.

These corridors will later become graph edges.

---

## Delay Analysis

High-delay facilities and corridors were identified.

However, corridor rankings require frequency thresholds before business conclusions can be trusted.

Future analyses will apply minimum traffic constraints to eliminate unstable rankings.

---

## Network Structure

### Graph Design

Nodes:

* Facilities

Edges:

* Corridors

Graph Type:

* Directed

### Statistics

* Nodes: 1,657
* Edges: 2,783
* Density: 0.0010

### Interpretation

The logistics network is extremely sparse.

This structure is highly suitable for graph analytics and graph machine learning.

---

## Key Business Findings

1. OSRM significantly underestimates operational delivery times.

2. Typical deliveries take approximately 2.1× longer than OSRM predictions.

3. Carting operations exhibit larger delay multipliers than FTL operations.

4. The network follows a hub-and-spoke structure.

5. Certain facilities likely act as operational bottlenecks.

6. Corridor-level intelligence is expected to improve ETA prediction.

---

## Phase Decisions

### Accepted

* factor as primary target
* Directed graph representation
* Facilities as nodes
* Corridors as edges

### Rejected

* segment_factor as primary target

---

## Phase 2 Objectives

1. Target Finalization
2. Leakage Audit
3. Datetime Feature Engineering
4. Route Feature Engineering
5. Hub-Level Feature Engineering
6. Corridor-Level Feature Engineering
7. Train/Validation Strategy
8. Feature Store Creation

---

## Phase Status

Completed Successfully.
