# Marketing Attribution Framework — Complete Portfolio

**Michael Forsythe Robinson** | Marketing Science Engineer  
Zenodo Community: [Marketing Attribution Framework](https://zenodo.org/communities/attribution)  
GitHub: [Michaelrobins938/attribution-assets](https://github.com/Michaelrobins938/attribution-assets)

---

## Published Papers (4)

### 1. First-Principles Attribution: A Defensible Framework
**DOI:** [10.5281/zenodo.18557680](https://doi.org/10.5281/zenodo.18557680)  
**Status:** Published | **Citations:** Tracking via Google Scholar

A Markov-Shapley hybrid attribution engine that combines transition probability modeling with cooperative game theory. Implements behavioral profiling to calibrate attribution weights based on customer decision-making patterns.

**Key contributions:**
- Hybrid Markov-Shapley attribution with Shapley value decomposition
- Behavioral profiling integration for weight calibration
- Worked example: $600K TV spot analysis showing $1,095 CPA vs $3,200 LTV

---

### 2. Bayesian Marketing Mix Modeling
**DOI:** [10.5281/zenodo.18599386](https://doi.org/10.5281/zenodo.18599386)  
**Status:** Published

Bayesian hierarchical MMM with media carryover effects, adstock decay modeling, and prior calibration from industry benchmarks. Includes Python implementation with PyStan/PyMC3.

**Key contributions:**
- Bayesian hierarchical structure with informative priors
- Adstock and saturation modeling (Hill functions)
- Integration with incrementality testing for validation

---

### 3. Incrementality Testing and iROAS Framework
**DOI:** [10.5281/zenodo.18599425](https://doi.org/10.5281/zenodo.18599425)  
**Status:** Published

Geo-lift testing methodology for measuring true incremental impact. Includes iROAS calculation framework, sample size determination, and statistical power analysis.

**Key contributions:**
- Geo-experiment design with matched market selection
- iROAS calculation: (Revenue_lift - Cost) / Cost
- Case study: 40.6% gap between MMM predictions and geo-test results

---

### 4. Probabilistic Identity Resolution in Cross-Channel Marketing
**DOI:** [10.5281/zenodo.18599433](https://doi.org/10.5281/zenodo.18599433)  
**Status:** Published

Identity graph construction using probabilistic matching with S_ij scoring. Handles mobile device fingerprinting, cookieless attribution, and cross-device user resolution.

**Key contributions:**
- Probabilistic matching with confidence scoring
- Mobile device fingerprinting methodology
- 5-node identity graph with attribution credit allocation

---

## In Press (6) — Publishing Week 1

### 5. Real-Time Attribution for Live Events: TV, Radio, and Broadcast Sync
**Status:** In Press → Zenodo upload pending

Sub-second attribution pipeline for live event response. Z-score spike detection for identifying attribution anomalies during broadcasts.

**Key contributions:**
- Real-time Z-score anomaly detection (threshold: Z > 500)
- Broadcast sync via audio fingerprinting
- Case study: NFL Sunday Night Football attribution spike

---

### 6. Real-Time Streaming Attribution: Kafka-Native Pipeline Architecture
**Status:** In Press → Zenodo upload pending

Kafka + Flink SQL architecture for sub-500ms attribution latency. Includes exactly-once processing guarantees and state management.

**Key contributions:**
- Kafka topic design for event ingestion
- Flink SQL windowing for session attribution
- State backend: RocksDB with checkpointing

---

### 7. Marketing Data Connectors: Canonical Schema Architecture
**Status:** In Press → Zenodo upload pending

Unified schema for ingesting data from Facebook, Google, Snapchat, TikTok, and offline sources. Includes transformation logic and data quality checks.

**Key contributions:**
- Canonical event schema (event_id, user_id, timestamp, channel, spend, revenue)
- Platform-specific parsers with field mapping
- Data quality validation rules

---

### 8. Bridging Marketing Mix Modeling and Incrementality Testing
**Status:** In Press → Zenodo upload pending

Methodology for reconciling MMM predictions with geo-lift test results. Addresses the systematic 40% gap observed in practice.

**Key contributions:**
- Gap analysis framework: MMM vs geo-test discrepancy
- Budget reallocation methodology ($1.4M TV budget case study)
- Combined model: MMM priors + incrementality validation

---

### 9. Behavioral Profiling Framework for Attribution Calibration
**Status:** In Press → Zenodo upload pending

Customer segmentation based on decision-making patterns. Integrates with attribution engine to calulate channel weights.

**Key contributions:**
- Behavioral segment identification
- Weight calibration by segment
- Integration with Markov-Shapley engine

---

### 10. Causal Inference Framework for Marketing Interventions
**Status:** In Press → Zenodo upload pending

DAG-based causal modeling for marketing intervention analysis. Includes propensity score matching and instrumental variable approaches.

**Key contributions:**
- DAG construction for marketing causality
- Confounder identification and adjustment
- Instrumental variable selection for media effects

---

## Citation

```bibtex
@techreport{robinson2026attribution,
  author = {Robinson, Michael Forsythe},
  title = {Marketing Attribution Framework: 10-Paper Technical Portfolio},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18557680}
}
```
