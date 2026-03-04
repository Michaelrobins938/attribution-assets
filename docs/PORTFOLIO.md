---
layout: default
title: "Complete Portfolio"
description: "All 10 published papers with DOIs, abstracts, and key contributions."
---

# Complete Portfolio

**Michael Forsythe Robinson** -- Marketing Science Engineer

All 10 papers are published on Zenodo with permanent DOIs.

---

## I. A First-Principles Hybrid Attribution Framework

**DOI:** [10.5281/zenodo.18557680](https://doi.org/10.5281/zenodo.18557680)

A Markov-Shapley hybrid attribution engine combining transition probability modeling with cooperative game theory. Implements behavioral profiling to calibrate attribution weights based on customer decision-making patterns.

**Key contributions:**
- Hybrid Markov-Shapley attribution with Shapley value decomposition
- Behavioral profiling integration for weight calibration
- Worked example: $600K TV spot analysis showing $1,095 CPA vs $3,200 LTV

---

## II. Bayesian Media Mix Modeling: Axiomatic Budget Optimization

**DOI:** [10.5281/zenodo.18599386](https://doi.org/10.5281/zenodo.18599386)

Bayesian hierarchical MMM with media carryover effects, adstock decay modeling, and prior calibration from industry benchmarks.

**Key contributions:**
- Bayesian hierarchical structure with informative priors
- Adstock and saturation modeling (Hill functions)
- Integration with incrementality testing for validation

---

## III. Behavioral Profiling and Causal Uplift

**DOI:** [10.5281/zenodo.18599425](https://doi.org/10.5281/zenodo.18599425)

Customer segmentation based on decision-making patterns using meta-learner architectures (S-learner, T-learner, X-learner) with propensity score correction.

**Key contributions:**
- Four-quadrant decision taxonomy (Persuadables, Sure Things, Sleeping Dogs, Lost Causes)
- Behavioral segment identification and weight calibration
- Integration with Markov-Shapley engine

---

## IV. The Causal Calibration System

**DOI:** [10.5281/zenodo.18599433](https://doi.org/10.5281/zenodo.18599433)

A testing framework that generates synthetic datasets with known ground-truth causal effects and subjects attribution models to five rigorous stress tests.

**Key contributions:**
- Synthetic ground-truth generation for attribution validation
- Five stress tests: Last-Touch Bias, Correlated Channels, Interaction Effects, Delayed Effects, Confounders
- Calibration scoring (0-100) with specific failure mode identification

---

## V. Probabilistic Identity Resolution

**DOI:** [10.5281/zenodo.18860338](https://doi.org/10.5281/zenodo.18860338)

Identity graph construction using probabilistic matching with S_ij scoring. Handles cross-device resolution, mobile device fingerprinting, and cookieless attribution.

**Key contributions:**
- Probabilistic matching with confidence scoring via Gaussian Mixture Models
- Cross-device graph with household-level linkage
- Privacy-preserving hashing for GDPR/CCPA compliance

---

## VI. Live Event Attribution

**DOI:** [10.5281/zenodo.18860339](https://doi.org/10.5281/zenodo.18860339)

Sub-second attribution pipeline for live event response. Z-score spike detection for identifying attribution anomalies during broadcasts.

**Key contributions:**
- Real-time Z-score anomaly detection for broadcast sync
- Time-friction analysis and exponential decay modeling
- Broadcast-aware attribution window management

---

## VII. Real-Time Streaming Attribution

**DOI:** [10.5281/zenodo.18860342](https://doi.org/10.5281/zenodo.18860342)

Kafka + Flink SQL architecture for sub-100ms attribution latency with exactly-once processing guarantees.

**Key contributions:**
- Kafka topic design for event ingestion at scale
- Flink SQL windowing for session attribution
- State backend: RocksDB with incremental checkpointing

---

## VIII. Incrementality Testing at Scale

**DOI:** [10.5281/zenodo.18860345](https://doi.org/10.5281/zenodo.18860345)

Geo-lift testing methodology combining randomized holdout experiments with synthetic control methods for measuring true incremental impact.

**Key contributions:**
- Geo-experiment design with matched market selection
- iROAS calculation framework with power analysis
- Case study: 40.6% gap between MMM predictions and geo-test results

---

## IX. Marketing Data Connectors

**DOI:** [10.5281/zenodo.18860349](https://doi.org/10.5281/zenodo.18860349)

Unified connector architecture normalizing data from 40+ platforms into a canonical attribution event model.

**Key contributions:**
- Canonical event schema for cross-platform normalization
- OAuth2 authentication and intelligent rate limiting
- Schema validation and incremental sync

---

## X. The MMM-Incrementality Bridge

**DOI:** [10.5281/zenodo.18860350](https://doi.org/10.5281/zenodo.18860350)

A Bayesian reconciliation framework that jointly estimates channel contributions using both aggregate MMM signals and individual-level attribution data.

**Key contributions:**
- Gap analysis framework: MMM vs geo-test discrepancy
- Budget reallocation methodology ($1.4M TV budget case study)
- Unified spend recommendations with calibrated uncertainty

---

## Citation

```bibtex
@techreport{robinson2026attribution,
  author       = {Robinson, Michael Forsythe},
  title        = {The Forsythe Attribution and Measurement Framework},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18557680}
}
```
