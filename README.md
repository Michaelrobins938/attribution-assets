<div align="center">

# The Forsythe Attribution & Measurement Framework
**A First-Principles Approach to Post-Cookie Marketing Science**

[![Author](https://img.shields.io/badge/Author-Michael_Forsythe_Robinson-1a365d?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/michael-forsythe-robinson-082255391/)
[![Status](https://img.shields.io/badge/Status-10_Papers_Published-success?style=for-the-badge&logo=zenodo)](https://zenodo.org/)
[![Pages](https://img.shields.io/badge/Live_Docs-GitHub_Pages-blue?style=for-the-badge&logo=github)](https://Michaelrobins938.github.io/attribution-assets/)

*Bridging the gap between "Marketing Spend" and "Causal Reality" for enterprise media budgets.*

</div>

---

## Executive Summary

With the deprecation of third-party cookies and the degradation of pixel tracking, traditional last-click attribution is mathematically obsolete. This repository serves as the central hub for the **Forsythe Attribution Framework**—a comprehensive 10-paper technical architecture combining **Bayesian Marketing Mix Modeling (MMM)**, **Causal Inference**, and **Real-Time Streaming Identity Resolution**.

> *"Most attribution is just weighted correlation with extra steps. We build systems grounded in first-principles causal frameworks."*

---

## The 10-Paper Technical Portfolio (Zenodo Published)

This complete measurement stack has been formally codified and published. Each paper addresses a specific failure point in modern marketing analytics and provides a mathematically defensible, production-ready solution.

| Part | Technical Focus & Title | Verifiable DOI Link |
|:---:|:---|:---|
| **I** | **Core Framework:** A First-Principles Hybrid Attribution Framework | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18557680-1a365d.svg)](https://doi.org/10.5281/zenodo.18557680) |
| **II** | **Optimization:** Bayesian Media Mix Modeling: Axiomatic Budget Optimization | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599386-1a365d.svg)](https://doi.org/10.5281/zenodo.18599386) |
| **III** | **Psychographics:** Behavioral Profiling and Causal Uplift | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599425-1a365d.svg)](https://doi.org/10.5281/zenodo.18599425) |
| **IV** | **Game Theory:** The Causal Calibration System | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599433-1a365d.svg)](https://doi.org/10.5281/zenodo.18599433) |
| **V** | **Entity Resolution:** Probabilistic Identity Resolution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860338-1a365d.svg)](https://doi.org/10.5281/zenodo.18860338) |
| **VI** | **Broadcast Sync:** Live Event Attribution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860339-1a365d.svg)](https://doi.org/10.5281/zenodo.18860339) |
| **VII** | **Kafka Pipelines:** Real-Time Streaming Attribution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860342-1a365d.svg)](https://doi.org/10.5281/zenodo.18860342) |
| **VIII** | **Geo-Testing:** Incrementality Testing at Scale | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860345-1a365d.svg)](https://doi.org/10.5281/zenodo.18860345) |
| **IX** | **Data Engineering:** Marketing Data Connectors | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860349-1a365d.svg)](https://doi.org/10.5281/zenodo.18860349) |
| **X** | **Reconciliation:** The MMM-Incrementality Bridge | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860350-1a365d.svg)](https://doi.org/10.5281/zenodo.18860350) |

*(Note: Full HTML versions of these whitepapers are hosted dynamically via [GitHub Pages](https://Michaelrobins938.github.io/attribution-assets/).)*

---

## System Architecture: The Artemis Streaming Engine

The theoretical frameworks above are operationalized via the **Artemis Engine**, a Kafka-native streaming pipeline designed for sub-100ms real-time attribution and identity resolution.

<details>
<summary><b>View System Architecture (Mermaid Diagram)</b></summary>
<br>

```mermaid
graph TD
    subgraph Data Ingestion
        A[Web/App SDKs] -->|Events| C(Apache Kafka)
        B[Server-Side APIs] -->|Conversions| C
        M[Ad Network APIs] -->|Spend/Impressions| C
    end

    subgraph Identity & Enrichment
        C --> D{Probabilistic Identity Graph}
        D -->|Device Fingerprint| E[Gaussian Mixture Models]
        D -->|Deterministic Keys| F[Cross-Device Resolution]
    end

    subgraph Causal Engine
        E --> G[(Delta Lake Feature Store)]
        F --> G
        G --> H((Markov Chain Modeling))
        G --> I((Shapley Value Calculation))
        H --> J[Bayesian UQ / Confidence Bounds]
        I --> J
    end

    subgraph Output
        J --> K[Real-Time Dashboard API]
        J --> L[Bidding Algorithm Optimization]
    end

    classDef core fill:#1a365d,stroke:#fff,stroke-width:2px,color:#fff;
    classDef stream fill:#2ea44f,stroke:#fff,stroke-width:2px,color:#fff;
    class C,G core;
    class H,I,J stream;

```

</details>

### Key Technical Pillars

1. **Markov Chain State Modeling:** For temporal causality, mapping the actual customer journey rather than relying on heuristic positions (First/Last Touch).
2. **Shapley Value Decomposition:** Ensuring game-theoretic fairness in distributing marginal credit to overlapping media channels.
3. **Bayesian Uncertainty Quantification (UQ):** Bounding epistemic vs. aleatoric error so media buyers understand the confidence interval of the reported ROAS.
4. **GDPR/CCPA Compliant Resolution:** Utilizing probabilistic clustering (Gaussian Mixtures) rather than relying on deprecating third-party cookies.

---

## Live Implementation & Open Source Code

While this repository houses the academic and theoretical assets, the active implementation of these frameworks can be viewed across my broader portfolio:

* **[first-principles-attribution](https://github.com/Michaelrobins938/first-principles-attribution):** The core causal logic repository.
* **[probabilistic-identity-resolution](https://github.com/Michaelrobins938/probabilistic-identity-resolution):** Real-time identity graph logic.
* **[behavioral-profiling-attribution](https://github.com/Michaelrobins938/behavioral-profiling-attribution):** Psychographic clustering models.

---

## Advisory & Fractional Engagements

I design, audit, and build production-grade measurement infrastructure for brands spending $1M+/month on media, and I advise high-growth agencies looking to white-label enterprise measurement capabilities.

<div align="center">

**Connect to discuss your measurement architecture:**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Michael_Forsythe_Robinson-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/michael-forsythe-robinson-082255391/)
[![Email](https://img.shields.io/badge/Email-fpublishing7@gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:fpublishing7@gmail.com)
[![Substack](https://img.shields.io/badge/Substack-Newsletter-FF6719?style=for-the-badge&logo=substack)](https://substack.com/@mforsytherobinson)

*All research and frameworks within this repository are published under CC BY 4.0.*

</div>
