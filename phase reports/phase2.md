# PHASE 2 REPORT — FEATURE ENGINEERING & DATA PREPARATION

Project:
Optimizing Delivery ETAs with Graph-Based Network Intelligence

---

## Objective

The objective of Phase 2 was to transform the audited logistics dataset into a reusable modeling and graph-ready feature store while performing leakage analysis and establishing a production-safe train/test strategy.

---

## Dataset

Rows: 144,867

Columns Before Engineering: 24

Columns After Engineering: 35

Primary Target:

factor

Definition:

factor = actual_time / osrm_time

Target validation confirmed 100% consistency.

---

## Leakage Audit

Removed / Rejected:

* actual_time
* segment_actual_time
* od_end_time
* factor_check

Rejected Aggregated Features:

* source_delay
* destination_delay
* corridor_delay

Reason:

Target leakage through aggregation of factor.

---

## Datetime Engineering

Created:

* trip_hour
* trip_weekday
* trip_month
* is_weekend

Operational Timing Features:

* trip_to_scan_minutes
* trip_to_cutoff_minutes

Findings:

trip_to_scan_minutes

56.57% of observations are zero.

Likely weak predictor.

trip_to_cutoff_minutes

Contains meaningful operational scheduling information.

---

## Network Volume Features

Facility Features:

* source_volume
* destination_volume

Findings:

Maximum source volume:

23,347

Maximum destination volume:

15,192

Strong hub concentration observed.

---

## Corridor Features

Created:

* corridor_volume

Findings:

Maximum corridor volume:

4,976

Confirms dominant corridors in the logistics network.

---

## Operational Features

Created:

* osrm_speed

Purpose:

Capture route efficiency characteristics beyond raw distance and travel time.

---

## Feature Validation

Correlation analysis against target:

Highest absolute correlations remained relatively weak.

Key conclusion:

Operational delay behavior is unlikely to be explained by single variables.

Interaction effects and graph structure are expected to contribute significant predictive power.

---

## Train / Test Strategy

Method:

GroupShuffleSplit

Grouping Variable:

trip_uuid

Reason:

Multiple rows belong to the same trip.

Prevents trip-level leakage.

Results:

Train:

116,451 rows

Test:

28,416 rows

---

## Outputs Created

feature_store.csv

graph_ready_dataset.csv

---

## Key Insights

1. Factor remains the strongest target candidate.

2. Leakage prevention required removal of several seemingly useful features.

3. Facility traffic is highly concentrated.

4. Corridor traffic is highly concentrated.

5. The logistics network exhibits clear hub-and-spoke behavior.

6. Graph-derived features are likely to provide greater predictive power than standalone engineered features.

---

## Phase Status

Completed Successfully.

---

## Next Phase

Graph Construction

Deliverables:

* 05_graph_build.ipynb
* src/graph_builder.py

Goals:

* Directed logistics graph
* NetworkX implementation
* Graph metrics
* Network visualization
* Hub verification
* Graph data exports
