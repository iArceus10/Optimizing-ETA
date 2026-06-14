# NETWORK OPERATIONS STRATEGY MEMO

## Delhivery Logistics Network

### Graph-Aware Operational Prioritization Framework

Prepared For:

Head of Network Operations

Prepared By:

Graph-Aware Logistics Intelligence Platform

Date:

Final Project Submission

---

# Executive Summary

A graph-based analysis of Delhivery's logistics network was conducted using 144,867 shipment records, 1,657 facilities, and 2,783 transportation corridors.

The objective was to identify critical network dependencies, high-impact facilities, operational bottlenecks, and corridor-level risks that contribute disproportionately to ETA inflation.

The analysis demonstrates that a small number of facilities and corridors account for a significant portion of operational dependency across the network.

Most notably, facility IND000000ACB emerged consistently as the dominant network hub and highest-priority operational dependency.

This memo summarizes the most critical findings and recommends immediate operational interventions.

---

# Network Overview

| Metric          | Value    |
| --------------- | -------- |
| Facilities      | 1,657    |
| Corridors       | 2,783    |
| Trips           | 14,817   |
| Records         | 144,867  |
| Graph Density   | 0.001014 |
| Weak Components | 64       |

The network exhibits low density but high concentration around a limited number of hubs.

This concentration creates operational efficiencies but also increases systemic risk when critical facilities experience delays or congestion.

---

# Top 5 Bottleneck Facilities

The following facilities repeatedly appeared across centrality analysis, source impact analysis, destination impact analysis, and operational prioritization frameworks.

| Rank | Facility     |
| ---- | ------------ |
| 1    | IND000000ACB |
| 2    | IND562132AAA |
| 3    | IND160002AAC |
| 4    | IND421302AAG |
| 5    | IND501359AAE |

These facilities represent the highest-priority candidates for capacity planning, infrastructure investment, and operational monitoring.

---

# Super Hub Spotlight

Facility:

IND000000ACB

Observed Characteristics:

* Highest network degree
* Top source facility
* Top destination facility
* Highest corridor participation
* Highest operational impact

Operational Implication:

This facility functions as the primary network dependency.

Disruptions at this facility are likely to propagate throughout multiple downstream corridors and facilities.

Recommended Actions:

* Increase processing capacity
* Improve dispatch scheduling
* Strengthen contingency planning
* Implement real-time congestion monitoring
* Prioritize infrastructure upgrades

---

# Top 5 High-Priority Corridors

The following corridors emerged as the operational backbone of the logistics network.

| Rank | Corridor                    |
| ---- | --------------------------- |
| 1    | IND000000ACB → IND562132AAA |
| 2    | IND562132AAA → IND000000ACB |
| 3    | IND000000ACB → IND712311AAA |
| 4    | IND000000ACB → IND501359AAE |
| 5    | IND000000ACB → IND421302AAG |

These corridors carry substantial shipment volume and exhibit elevated operational impact.

---

# Corridor Intervention Framework

## Corridor Group A

Critical Backbone Corridors

Characteristics:

* Highest volume
* Highest dependency
* Network-wide influence

Recommended Actions:

* Capacity expansion
* Dedicated monitoring
* Dynamic routing support
* SLA-focused management

---

## Corridor Group B

High-Priority Corridors

Characteristics:

* Significant volume
* Regional importance

Recommended Actions:

* Weekly performance reviews
* Corridor balancing
* Demand forecasting

---

## Corridor Group C

Medium-Priority Corridors

Characteristics:

* Lower dependency
* Localized impact

Recommended Actions:

* Standard monitoring
* Periodic optimization

---

# ETA Reduction Playbook

The explainability analysis identified the primary drivers of ETA inflation.

Top Drivers:

1. trip_to_cutoff_minutes
2. trip_to_scan_minutes
3. source_volume
4. corridor_volume
5. route_type

Recommended interventions are summarized below.

| Driver          | Intervention                 |
| --------------- | ---------------------------- |
| Cutoff Delay    | Reduce dispatch waiting time |
| Scan Delay      | Improve scan turnaround      |
| Source Volume   | Capacity planning            |
| Corridor Volume | Corridor balancing           |
| Route Type      | Route optimization           |

Expected Outcome:

Reduced ETA inflation and improved delivery consistency.

---

# FTL vs Carting Framework

Graph analysis supports transportation mode prioritization.

## Full Truck Load (FTL)

Recommended For:

* High-volume corridors
* Backbone corridors
* Stable demand corridors
* Long-haul routes

Benefits:

* Higher utilization
* Lower unit cost
* Reduced handling delays

---

## Carting

Recommended For:

* Regional corridors
* Variable demand corridors
* Lower-volume routes
* Flexible operations

Benefits:

* Greater responsiveness
* Lower fixed commitment
* Better adaptability

---

# Operational Exposure Framework

The project dataset does not contain shipment value, margin, customer revenue, or contractual penalty information.

Therefore direct revenue-at-risk could not be calculated.

Instead, operational exposure should be evaluated using:

Operational Exposure Index

Exposure = Corridor Volume × ETA Inflation

This framework identifies corridors where operational improvements are expected to produce the largest business impact.

---

# Illustrative Financial Impact Framework

The following example demonstrates how graph intelligence can support financial prioritization when commercial data becomes available.

Illustrative Assumptions

* Average shipment value = ₹2,000
* SLA penalty = ₹50 per delayed shipment
* Delay reduction after upgrade = 20%

Example Corridor

IND000000ACB → IND562132AAA

Observed Volume:

4,976 shipments

Assumed Delayed Shipments:

20%

Potential Delayed Shipments:

995

Potential SLA Exposure:

₹49,750

Illustrative Recovery After Intervention:

₹9,950

Actual business impact would depend on shipment mix, customer contracts, margins, and service-level agreements.

---

# Strategic Roadmap

Immediate (0–3 Months)

* Upgrade monitoring of IND000000ACB
* Track critical corridors daily
* Reduce cutoff delays
* Improve scan turnaround

Medium Term (3–12 Months)

* Corridor balancing program
* Capacity expansion planning
* Graph-aware routing integration

Long Term (12+ Months)

* Real-time graph intelligence platform
* Dynamic bottleneck monitoring
* Delay-aware graph embeddings
* Graph Neural Network deployment

---

# Final Recommendation

The analysis indicates that network structure plays a measurable role in ETA performance and operational efficiency.

Rather than treating delays as isolated shipment events, Delhivery should adopt a network-centric operating model that continuously monitors facility dependencies, corridor risks, and graph-derived bottlenecks.

Priority should be placed on:

1. IND000000ACB
2. Backbone corridors
3. Cutoff-delay reduction
4. Scan-delay reduction
5. Graph-aware operational planning

These interventions are expected to produce the highest operational return and greatest reduction in network-wide delay propagation.

---

Prepared By:

Delhivery Graph-Aware Logistics Intelligence Platform

Status:

FINAL RECOMMENDATION MEMO
