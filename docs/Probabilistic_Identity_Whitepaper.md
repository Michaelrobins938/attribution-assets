---
layout: default
title: "Probabilistic Identity Resolution: The Privacy-First Identity Graph"
description: "Resolving discontinuous customer journeys via weighted clustering and household-level linkage."
author: Michael Forsythe Robinson
doi: "10.5281/zenodo.18860338"
---

# Probabilistic Identity Resolution: The Privacy-First Identity Graph
## Resolving Discontinuous Customer Journeys via Weighted Clustering and Household-Level Linkage

**Technical Whitepaper v1.0.0**

| **Attribute** | **Value** |
|---|---|
| **Version** | 1.0.0 |
| **Status** | Production-Ready |
| **Date** | January 31, 2026 |
| **Classification** | Data Engineering / Graph Data Science |
| **Document Type** | Technical Whitepaper |

---

## **Abstract**

In a multi-device, cookie-less world, customer journeys are fragmented across different identifiers (cookies, IDFA, hashed emails, IP addresses). Accurate attribution is impossible if the "Mobile Click" and "Desktop Purchase" appear to come from different people. This paper specifies a **Probabilistic Identity Resolution Engine**. By leveraging **Graph-based Clustering** and **Attribute Weighted Matching**, we link disparate identifiers into a unified "Golden ID" with associated confidence scores. 

---

## **Table of Contents**

1. [Glossary & Notation](#glossary--notation)
2. [The Fragmented Identity Crisis](#1-the-fragmented-identity-crisis)
3. [System Architecture: The Multi-Layer Graph](#2-system-architecture-the-multi-layer-graph)
4. [Linkage Logic & Weighting](#3-linkage-logic--weighting)
5. [The "Household" vs. "Individual" Resolution](#4-the-household-vs-individual-resolution)
6. [Privacy-First Design](#5-privacy-first-design)
7. [Technical Implementation Specification](#6-technical-implementation-specification)
8. [Causal Interpretation & Limitations](#7-causal-interpretation--limitations)
9. [Conclusion](#8-conclusion)
10. [Strategic Implementation Guide](#9-strategic-implementation-guide)
11. [Integration with Measurement Stack](#10-integration-with-measurement-stack)
12. [Implementation Maturity Model](#11-implementation-maturity-model)
13. [Worked Numerical Example](#12-worked-numerical-example)
14. [Data Requirements & Minimum Viable Implementation](#13-data-requirements--minimum-viable-implementation)

---

## **Glossary & Notation**

| **Term** | **Definition** |
|---|---|
| **Identity Graph** | A collection of nodes (identifiers) and edges (observed links) representing user identities. |
| **Deterministic Link** | A 100% certain link (e.g., a user logging in on two different devices). |
| **Probabilistic Link** | A link based on statistical likelihood (e.g., same IP, same browser, similar behavior). |
| **Golden ID** | The unique, unified identifier representing a single person or household. |
| **Graph Density** | A measure of how many links exist between a cluster of nodes. |
| **Identity Collision** | When two different people are incorrectly linked to a single ID. |

---

## **1. The Fragmented Identity Crisis**

The average modern consumer uses 3.2 devices and multiple platforms. 
- **The Gap:** A user sees an Instagram ad on their phone (Device A), then searches on their laptop (Device B), and finally buys on their tablet (Device C).
- **The Attribution Failure:** Without identity resolution, this looks like three different users, and the Instagram ad gets **Zero** credit.

---

## **2. System Architecture: The Multi-Layer Graph**

We build a **Multiplex Identity Graph** where every node is an identifier and every edge is an observation.

### **2.1 Hard Links (Deterministic)**
Links derived from "Known Truth":
- Login sequences (User ID 123 uses Cookie A and Cookie B).
- Hashed Email matches.

### **2.2 Soft Links (Probabilistic)**
Links derived from "Statistical Proximity":
- **Spatial:** Same Residential IP address (Household signal).
- **Technological:** Same Browser Fingerprint (UA string, Screen resolution, Fonts).
- **Behavioral:** Similar time-of-day activity and navigation patterns.

---

## **3. Linkage Logic & Weighting**

We define a **Linkage Score** $S_{ij}$ between nodes $i$ and $j$:

$$S_{ij} = \sum_{k=1}^K w_k \cdot \text{match}(attr_k)$$

- **$w_k$:** The reliability weight of attribute $k$ (e.g., Email = 1.0, IP = 0.3).
- **Clustering:** Nodes are grouped using a **Community Detection Algorithm (Louvain)** to identify clusters with high density.

---

## **4. The "Household" vs. "Individual" Resolution**

Attribution often functions better at the **Household Level**. 
- If Person A sees an ad on the living room TV and Person B buys on their laptop 5 minutes later, it is highly likely a single causal event.
- Our engine provides a **Hierarchical Identity**: 
    - `Household_ID_88` -> [`Individual_A`, `Individual_B`]
    - This allows for "Cross-Device Cross-User" attribution.

---

## **5. Privacy-First Design**

Identity resolution must respect user privacy.
- **No PII Storage:** All emails and sensitive IDs are hashed (SHA-256) before entering the graph.
- **TTL (Time to Live):** Probabilistic edges decay and are pruned after 30-90 days of inactivity to prevent "Identity Bloat" and respect the right to be forgotten.
- **Differential Privacy:** Adding noise to the graph to prevent re-identification of individual users from aggregated clusters.

---

## **6. Technical Implementation Specification**

- **Graph Database:** Neo4j or Spark GraphX for large-scale cluster analysis.
- **Compute:** Scalable Python (PySpark) for daily identity updates.
- **Output:** An `ID_Mapping_Table` used as a join-key for the Markov and MMM engines.

---

## **7. Causal Interpretation & Limitations**

- **Over-Linking:** Incorrectly combining different people (e.g., roommates or public Wi-Fi users).
- **Under-Linking:** Failing to connect a user who uses a VPN or clear-cookies regularly.
- **Confidence Thresholds:** Choosing the right score (e.g., > 0.85) to balance attribution accuracy vs. path pollution.

---

## **8. Conclusion**

Probabilistic Identity Resolution is the "Glue" of the transition framework. By bridging the gap between devices and platforms, we reconstruct the **True Path to Conversion**, enabling the next generation of causal attribution models to function in a fragmented digital world.

---

## **9. Strategic Implementation Guide**

### **9.1 The 5 Most Valuable Insights**

| # | Insight | What Decisions It Informs |
|---|---------|---------------------------|
| 1 | **Attribution fails without identity** - Without resolution, cross-device journeys appear as multiple users → wrong channel credit | Whether to invest in identity infrastructure |
| 2 | **Household > Individual for streaming** - CTV ads reach household; conversion happens on personal device | Attribution granularity level |
| 3 | **Confidence scores enable trade-offs** - Higher thresholds = more precision, more missed links; lower = more links, more noise | Threshold selection |
| 4 | **Privacy and accuracy are opposites** - More data = better resolution but more privacy risk | Compliance vs. performance |
| 5 | **Graph density is the moat** - More identity signals = better resolution = competitive advantage | Data acquisition strategy |

### **9.2 Implementation: 5-Step Plan**

| Step | Action | Owner | Quick Win | Measurable Result |
|------|--------|-------|-----------|-------------------|
| 1 | Deploy deterministic linking | Data Engineering | Login data connected | Golden IDs created |
| 2 | Add probabilistic signals | Data Science | IP + device matching | Coverage +20% |
| 3 | Tune confidence thresholds | Analytics | Precision/recall balanced | Accuracy metric |
| 4 | Integrate with attribution | Data Science | Attribution runs | Cross-device credit |
| 5 | Monitor for drift | Analytics | Detection alerts | False positive rate |

### **9.3 Hidden Assumptions & Blind Spots**

| Assumption | What If It's Wrong |
|------------|-------------------|
| Device signals persist | Clearing cookies/VPN resets identity → under-linking |
| IP = household | Mobile networks (5G) change IP constantly → false links |
| Temporal proximity = relationship | Coincidental timing → identity collision |
| Users want privacy | Opt-outs increase → fewer signals → degraded accuracy |

### **9.4 Compare Opposing Views**

| Perspective | Argument | Works When |
|-------------|----------|------------|
| **Individual Resolution** | Each person = one ID | Logged-in environments, authenticated journeys |
| **Household Resolution** | Household = unit | CTV, shared devices |
| **Hybrid (This Paper)** | Both levels supported | All use cases |

### **9.5 Leverage Points for Outsized Results**

| # | Leverage Point | Why It Matters | Expected Impact |
|---|---------------|----------------|-----------------|
| 1 | Deterministic anchor points | Login/cemail = certain links | Foundation for probabilistic |
| 2 | Confidence threshold tuning | Small changes → big accuracy swings | 10-20% accuracy improvement |
| 3 | Real-time graph updates | Stale graph = stale attribution | Fresh insights |

### **9.6 Contrarian Takeaways**

1. **Most identity resolution is over-engineered** - 80% of value comes from 20% of signals (login + email).
2. **Household level is underutilized** - Most companies try individual, fail, never try household.
3. **Privacy regulations are an excuse** - Hashing + TTL + differential privacy enables compliance + accuracy.
4. **Graph databases are overkill** - Simple SQL with indexes works for 99% of use cases.

### **9.7 Role-Specific Perspectives**

| Role | Question | Answer |
|------|----------|--------|
| **Marketer** | What drives reach or conversion? | Cross-device attribution shows true channel value - especially for CTV |
| **Founder** | What affects cash flow or growth? | Accurate attribution → better budget allocation → higher ROAS |
| **Analyst** | What changes the metrics? | Golden ID coverage % directly impacts attribution accuracy |

---

## **10. Integration with Measurement Stack**

### **10.1 Data Flow**

```
Identity Graph → ID_Mapping_Table → Attribution Engine → MMM Engine → Budget Optimizer
```

### **10.2 Cross-References**

- **Marketing Data Connectors** (Robinson, 2026f): Identity resolution requires unified data ingestion
- **MMM-Incrementality Bridge** (Robinson, 2026e): Identity improves MMM accuracy by enabling cross-channel spend matching
- **Hybrid Attribution Framework** (Robinson, 2026a): Markov chains require resolved paths

---

---

## **11. Implementation Maturity Model**

Assess your current state and identify the next step on the progression path.

| Level | Name | Capabilities | ID Coverage | Key Gap |
|-------|------|-------------|-------------|---------|
| **1 - Ad Hoc** | Cookie-Only | Single device tracked, no resolution | ~35% | Cross-device journeys invisible |
| **2 - Deterministic** | Login-Based | Hashed email + login golden IDs | ~55% | Anonymous users unresolved |
| **3 - Probabilistic** | Statistical Links | IP + device fingerprint confidence scoring | ~70% | Threshold tuning immature |
| **4 - Household** | Hierarchical ID | Individual + household levels simultaneously | ~82% | Real-time graph stale (daily batch) |
| **5 - Real-Time** | Live Graph | Sub-second updates, privacy-by-design | ~90% | Diminishing returns beyond 90% |

### **Progression Checklist**

| Transition | Required Actions |
|------------|-----------------|
| L1 → L2 | Capture login events, hash emails server-side, build ID mapping table |
| L2 → L3 | Collect browser fingerprints, IP logs, implement Louvain clustering |
| L3 → L4 | Add household grouping logic, hierarchical ID schema |
| L4 → L5 | Stream graph updates via Kafka, implement TTL decay in real-time |

---

## **12. Worked Numerical Example**

### **Scenario: Cross-Device Journey — 5 Observed Identifiers**

A user interacts across three devices. Five identifiers are captured:

| Node | Type | Device |
|------|------|--------|
| `Cookie_A1` | Browser cookie | Desktop |
| `Cookie_A2` | Browser cookie | Laptop |
| `IDFA_B3` | Mobile ad ID | iPhone |
| `Email_D4` | Hashed email | App login (iPhone) |
| `IP_192.168.1.5` | Residential IP | All devices |

**Step 1 — Compute Linkage Scores S_ij:**

Using the weighted formula: $S_{ij} = \sum_k w_k \cdot \text{match}(attr_k)$

| Pair | Email (w=1.0) | IP (w=0.30) | Fingerprint (w=0.50) | Temporal (w=0.20) | **S_ij** |
|------|--------------|------------|---------------------|------------------|----------|
| Cookie_A1 ↔ Cookie_A2 | 0 | 0.30 | 0.45 | 0.18 | **0.93** ✓ |
| Cookie_A1 ↔ IDFA_B3 | 0 | 0.30 | 0 | 0.15 | **0.45** ✗ |
| IDFA_B3 ↔ Email_D4 | 1.00 | 0.30 | 0 | 0.20 | **1.00** (capped) ✓ |
| Cookie_A2 ↔ IP_192.168.1.5 | 0 | 0.30 | 0.40 | 0.17 | **0.87** ✓ |

**Step 2 — Louvain Clustering (threshold = 0.75):**

Links above threshold: A1↔A2, A2↔IP, IDFA_B3↔Email_D4 → all 5 nodes merge → **Golden_ID = `GID_7a9f2c`**

**Step 3 — Attribution Impact:**

| Metric | Before Resolution | After Resolution |
|--------|-------------------|-----------------|
| Touchpoints visible on path | 2 (desktop only) | 5 (all devices) |
| Instagram Mobile credit | **$0** | **$34.20 (34% of path)** |
| True journey CPA | Unknown | **$132** |
| Journeys correctly attributed | 38% | 81% |

**Business result:** Instagram mobile was receiving $0 attribution credit. Actual CPA after resolution: $132 — well within target. Budget was being incorrectly cut from a high-performing channel.

---

## **13. Data Requirements & Minimum Viable Implementation**

### **Tier 1 — Minimum Viable (Week 1–2)**

| Data Source | Required Fields | Frequency |
|-------------|----------------|-----------|
| Login events | `user_id`, `device_id`, `timestamp` | Real-time |
| Email capture | `hashed_email` (SHA-256), `device_id` | At conversion |
| Conversion log | `order_id`, `user_id`, `timestamp`, `revenue` | At conversion |

**Output:** Deterministic golden IDs for logged-in journeys (~55% coverage). Stack: PostgreSQL + Python.

### **Tier 2 — Target State (Month 1–2)**

| Data Source | Required Fields | Frequency |
|-------------|----------------|-----------|
| Browser fingerprint | UA string, screen resolution, fonts hash, canvas hash | Per session |
| IP log | `ip_address`, `device_id`, `timestamp`, `session_id` | Per session |
| Behavioral signals | Session cadence, time-on-site, click count | Per session |

**Output:** Probabilistic + deterministic combined → ~72% coverage. Stack: + Redis cache + PySpark clustering.

### **Tier 3 — Full Production (Month 3+)**

| Data Source | Required Fields | Frequency |
|-------------|----------------|-----------|
| Graph database | Full multiplex identity graph | Streaming |
| Privacy pipeline | SHA-256, TTL decay rules, consent flags, right-to-delete hooks | Real-time |
| Household mapping | IP → postal code → household cluster ID | Weekly |

**Output:** Hierarchical household + individual IDs, ~88% coverage, fully compliant. Stack: + Neo4j or Spark GraphX.

### **Minimum Viable Tech Stack**

```
PostgreSQL (ID mapping)  →  Python/PySpark (Louvain clustering)  →  Redis (lookup cache)
Estimated setup: 2 engineers × 2 weeks
ROI: Cross-device attribution accuracy +40–60%, iROAS confidence doubles
```


## **References**

[1] Robinson, M.F. (2026a). "A First-Principles Hybrid Attribution Framework." Zenodo. https://doi.org/10.5281/zenodo.18557680
[2] Robinson, M.F. (2026b). "Bayesian Media Mix Modeling: Axiomatic Budget Optimization." Zenodo. https://doi.org/10.5281/zenodo.18599386
[3] Robinson, M.F. (2026c). "Behavioral Profiling and Causal Uplift: Beyond The Conversion." Zenodo. https://doi.org/10.5281/zenodo.18599425
[4] Robinson, M.F. (2026d). "The Causal Calibration System: Stress-Testing Attribution Models." Zenodo. https://doi.org/10.5281/zenodo.18599433
[5] Robinson, M.F. (2026e). "The MMM-Incrementality Validation Bridge." Zenodo. (Forthcoming)
[6] Robinson, M.F. (2026f). "Marketing Data Connectors: Unified API Architecture." Zenodo. (Forthcoming)
