<div align="center">

# 🏛️ The Forsythe Attribution & Measurement Framework
**A Global First-Principles Architecture for Enterprise Marketing Science**

[![Architect](https://img.shields.io/badge/Architect-Michael_Forsythe_Robinson-1a365d?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/michael-forsythe-robinson-082255391/)
[![Status](https://img.shields.io/badge/Status-10_Papers_Published-success?style=for-the-badge&logo=zenodo)](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Robinson%2C%20Michael%20Forsythe%22)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-11_Live_Dashboards-orange?style=for-the-badge&logo=vercel)](https://portfolio-hub-kappa-murex.vercel.app/)

*An end-to-end causal inference infrastructure bridging the gap between media spend and revenue reality.*

</div>

---

## 📖 Global System Architecture

The **Forsythe Framework** is not a collection of isolated scripts; it is an interlocking ecosystem where high-level marketing theory is operationalized through production-grade engineering.

```mermaid
graph TD
    subgraph "1. Data Ingestion & Signal Capture"
        A[Artemis Ingestion Engine] -->|Kafka Streaming| B{Unified Feature Store}
        A1[Live Event SDKs] --> B
        A2[Ad Network APIs] --> B
    end

    subgraph "2. Identity & Behavioral Layer"
        B --> C[Probabilistic Identity Resolution]
        C --> D[Behavioral Profiling Engine]
        D -->|Psychographic Priors| E{Causal Calibration}
    end

    subgraph "3. The Causal Engine (The Core)"
        E --> F[Bayesian MMM]
        E --> G[Markov-Shapley Attribution]
        F & G --> H[MMM-Incrementality Bridge]
    end

    subgraph "4. Deployment & Activation"
        H --> I[Live Production Dashboards]
        H --> J[Bidding Algorithm Feed]
        I --> K[Decision Intelligence]
    end

    click A "https://live-event-attribution-dashboard.vercel.app/"
    click C "https://identity-resolution-demo.vercel.app/"
    click F "https://mmm-dashboard-mu.vercel.app/"
    click I "https://portfolio-hub-kappa-murex.vercel.app/"

    classDef core fill:#1a365d,stroke:#fff,stroke-width:2px,color:#fff;
    classDef live fill:#2ea44f,stroke:#fff,stroke-width:2px,color:#fff;
    class B,E,H core;
    class I,A,C,F live;

```

---

## 📚 Technical Documentation & Interactive Demos

This framework is documented across 10 technical whitepapers (Zenodo) and proven via 11 interactive production dashboards (Vercel).

| Pillar | Research Paper (Theory) | Verifiable DOI | Live Dashboard (Execution) |
|:---:|:---|:---|:---|
| **Foundation** | Hybrid Attribution Framework | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18557680-1a365d.svg)](https://doi.org/10.5281/zenodo.18557680) | [🚀 Streaming Engine](https://streaming-attribution-dashboard.vercel.app/) |
| **Optimization** | Bayesian Media Mix Modeling | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599386-1a365d.svg)](https://doi.org/10.5281/zenodo.18599386) | [📊 MMM Optimizer](https://mmm-dashboard-mu.vercel.app/) |
| **Psychology** | Behavioral Profiling & Uplift | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599425-1a365d.svg)](https://doi.org/10.5281/zenodo.18599425) | [🧠 Profiling Hub](https://behavioral-profiling-dashboard.vercel.app/) |
| **Calibration** | The Causal Calibration System | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599433-1a365d.svg)](https://doi.org/10.5281/zenodo.18599433) | [🔬 Inference Suite](https://causal-inference-dashboard.vercel.app/) |
| **Identity** | Probabilistic ID Resolution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860338-1a365d.svg)](https://doi.org/10.5281/zenodo.18860338) | [🆔 Identity Demo](https://identity-resolution-demo.vercel.app/) |
| **Real-Time** | Live Event Attribution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860339-1a365d.svg)](https://doi.org/10.5281/zenodo.18860339) | [📺 WWE Raw Sync](https://live-event-attribution-dashboard.vercel.app/) |
| **Pipelines** | Real-Time Streaming Attribution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860342-1a365d.svg)](https://doi.org/10.5281/zenodo.18860342) | [🚀 Streaming Engine](https://streaming-attribution-dashboard.vercel.app/) |
| **Geo-Testing** | Incrementality Testing at Scale | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860345-1a365d.svg)](https://doi.org/10.5281/zenodo.18860345) | [🧪 Testing Lab](https://incrementality-testing-dashboard.vercel.app/) |
| **Data Eng** | Marketing Data Connectors | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860349-1a365d.svg)](https://doi.org/10.5281/zenodo.18860349) | [🔌 Connector Hub](https://frontend-pi-eight-70.vercel.app/) |
| **Reconciliation** | The MMM-Incrementality Bridge | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860350-1a365d.svg)](https://doi.org/10.5281/zenodo.18860350) | [📈 MMM Bridge](https://mmm-dashboard-mu.vercel.app/) |

| Extended Platform | Live Dashboard |
|:---|:---|
| Experimentation Platform | [⚗️ A/B & Bandit Testing](https://experimentation-platform-dashboard.vercel.app/) |
| Demand Forecasting | [📈 Forecast System](https://demand-forecasting-dashboard-wine.vercel.app/) |
| Portfolio Command Center | [🛰️ Central Hub](https://portfolio-hub-kappa-murex.vercel.app/) |

*(📖 Full HTML versions of all whitepapers are hosted via [GitHub Pages](https://Michaelrobins938.github.io/attribution-assets/).)*

---

## ⚙️ Core Engineering Principles

1. **Epistemic Bound Measurement:** Every model outputs a confidence interval. If we can't bound the error, we don't report the ROAS.
2. **First-Principles Causality:** We move past "last-touch" correlation by utilizing Markov Chain state modeling and Shapley value decomposition.
3. **Data Sovereignty:** All identity resolution is handled in-house via probabilistic clustering, removing reliance on depreciating 3rd-party signals.

---

## 👨‍💻 About the Architect

<img align="right" width="180" height="180" src="https://github.com/user-attachments/assets/15b51b17-befe-4ea2-bdad-618d3757112e" style="border-radius:50%;">

**Michael Forsythe Robinson** is a Marketing Science Engineer and AI Systems Architect.

He specializes in the engineering of high-scale data systems that transform complex behavioral signals into actionable causal truth. As the founder of **Forsythe Publishing & Marketing**, he provides technical advisory for enterprise brands and high-growth agencies.

* **Main Hub:** [Portfolio Command Center](https://portfolio-hub-kappa-murex.vercel.app/)
* **Direct Reach:** [LinkedIn](https://www.linkedin.com/in/michael-forsythe-robinson-082255391/) | `Forsythepublishing@gmail.com`

---

<div align="center">
<sub>All research assets are published under CC BY 4.0. Powered by the Forsythe Measurement Standard.</sub>
</div>
