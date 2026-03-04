<div align="center">

# The Forsythe Attribution and Measurement Framework
**A Global First-Principles Architecture for Enterprise Marketing Science**

<img width="1376" alt="Hero Banner" src="Hero.jpg" />

[![Architect](https://img.shields.io/badge/Architect-Michael_Forsythe_Robinson-1a365d?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/michael-forsythe-robinson-082255391/)
[![Status](https://img.shields.io/badge/Status-10_Papers_Published-success?style=for-the-badge&logo=zenodo)](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Robinson%2C%20Michael%20Forsythe%22)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-11_Live_Dashboards-orange?style=for-the-badge&logo=vercel)](https://portfolio-hub-kappa-murex.vercel.app/)

An end-to-end causal inference infrastructure bridging the gap between media spend and revenue reality.

</div>

---

## About the Framework

With the deprecation of third-party cookies and the degradation of pixel tracking, traditional last-click attribution is mathematically obsolete. Most "modern" attribution is simply weighted correlation disguised as data science.

This repository serves as the central hub for the **Forsythe Attribution Framework** -- a comprehensive, peer-verifiable technical architecture combining Bayesian Marketing Mix Modeling, Causal Inference, and Real-Time Streaming Identity Resolution. It is designed for data teams at brands spending $1M+/month on media who require measurement infrastructure they can mathematically defend.

The framework spans 10 published technical whitepapers, each addressing a specific failure point in modern marketing analytics, and 11 production dashboards demonstrating working implementations.

---

## System Architecture

The theoretical frameworks are operationalized via a Kafka-native streaming pipeline designed for sub-100ms real-time attribution, identity resolution, and budget optimization.

<div align="center">
<img width="1376" alt="Data Pipeline Architecture" src="datapipeline(2).jpg" />
</div>

### Engineering Principles

**Epistemic Bound Measurement.** Every model outputs a confidence interval. If we cannot bound the error, we do not report the ROAS.

**First-Principles Causality.** We move past last-touch correlation by utilizing Markov Chain state modeling for temporal causality and Shapley value decomposition for game-theoretic fairness in credit allocation.

**Bayesian Uncertainty Quantification.** Bounding epistemic vs. aleatoric error so media buyers understand the actual confidence interval of the reported return, not just a point estimate.

**Privacy-First Identity Resolution.** All identity resolution is handled via probabilistic clustering (Gaussian Mixture Models), removing reliance on deprecating third-party cookies and maintaining GDPR/CCPA compliance by design.

---

## The 10-Paper Measurement Stack

Each paper is published on Zenodo with a permanent DOI and compiled in LaTeX. Full HTML versions are hosted via [GitHub Pages](https://Michaelrobins938.github.io/attribution-assets/).

| Pillar | Research Paper | DOI | Live Dashboard |
|:---|:---|:---|:---|
| Foundation | A First-Principles Hybrid Attribution Framework | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18557680-1a365d.svg)](https://doi.org/10.5281/zenodo.18557680) | [Streaming Engine](https://streaming-attribution-dashboard.vercel.app/) |
| Optimization | Bayesian Media Mix Modeling | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599386-1a365d.svg)](https://doi.org/10.5281/zenodo.18599386) | [MMM Optimizer](https://mmm-dashboard-mu.vercel.app/) |
| Psychographics | Behavioral Profiling and Causal Uplift | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599425-1a365d.svg)](https://doi.org/10.5281/zenodo.18599425) | [Profiling Suite](https://behavioral-profiling-dashboard.vercel.app/) |
| Calibration | The Causal Calibration System | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18599433-1a365d.svg)](https://doi.org/10.5281/zenodo.18599433) | [Causal Inference Suite](https://causal-inference-dashboard.vercel.app/) |
| Identity | Probabilistic Identity Resolution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860338-1a365d.svg)](https://doi.org/10.5281/zenodo.18860338) | [Identity Graph Demo](https://identity-resolution-demo.vercel.app/) |
| Broadcast | Live Event Attribution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860339-1a365d.svg)](https://doi.org/10.5281/zenodo.18860339) | [Live Event Dashboard](https://live-event-attribution-dashboard.vercel.app/) |
| Pipelines | Real-Time Streaming Attribution | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860342-1a365d.svg)](https://doi.org/10.5281/zenodo.18860342) | [Streaming Engine](https://streaming-attribution-dashboard.vercel.app/) |
| Geo-Testing | Incrementality Testing at Scale | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860345-1a365d.svg)](https://doi.org/10.5281/zenodo.18860345) | [Incrementality Lab](https://incrementality-testing-dashboard.vercel.app/) |
| Data Engineering | Marketing Data Connectors | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860349-1a365d.svg)](https://doi.org/10.5281/zenodo.18860349) | [Connector Hub](https://frontend-pi-eight-70.vercel.app/) |
| Reconciliation | The MMM-Incrementality Bridge | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18860350-1a365d.svg)](https://doi.org/10.5281/zenodo.18860350) | [MMM Bridge](https://mmm-dashboard-mu.vercel.app/) |

### Additional Production Systems

| System | Dashboard | Description |
|:---|:---|:---|
| Experimentation Platform | [A/B and Bandit Testing](https://experimentation-platform-dashboard.vercel.app/) | Multi-armed bandit experiment management with sequential testing |
| Demand Forecasting | [Forecast System](https://demand-forecasting-dashboard-wine.vercel.app/) | Time-series forecasting with hierarchical reconciliation |
| Portfolio Hub | [Command Center](https://portfolio-hub-kappa-murex.vercel.app/) | Central navigation across all deployed systems |

---

## Technical Stack

| Layer | Technology |
|:---|:---|
| Attribution Engine | Markov-Shapley hybrid with cooperative game-theoretic credit allocation |
| Marketing Mix Modeling | Bayesian hierarchical models (PyMC, PyStan) with adstock and Hill saturation |
| Identity Resolution | Probabilistic graph with S_ij scoring, Gaussian Mixture clustering, device fingerprinting |
| Real-Time Processing | Apache Kafka, Apache Flink SQL, sub-100ms latency, exactly-once semantics |
| Causal Inference | DAG-based modeling, propensity scoring, geo-lift experiments, synthetic control |
| Incrementality Testing | Randomized holdout design, Difference-in-Differences, Bayesian Structural Time Series |
| Feature Store | Delta Lake with versioned feature pipelines |
| Frontends | Next.js, deployed on Vercel |

---

## About the Architect

<img align="right" width="180" height="180" src="https://github.com/user-attachments/assets/15b51b17-befe-4ea2-bdad-618d3757112e" style="border-radius:50%;">

**Michael Forsythe Robinson** is a Marketing Science Engineer and AI Systems Architect.

He specializes in the design and engineering of production-grade measurement systems that transform complex behavioral signals into defensible causal estimates. His work sits at the intersection of Bayesian statistics, streaming data infrastructure, and cooperative game theory -- applied to the specific problem of marketing budget allocation under uncertainty.

As the founder of **Forsythe Publishing and Marketing**, he provides fractional technical advisory for enterprise brands and high-growth agencies building in-house measurement capabilities.

- **Portfolio:** [Command Center](https://portfolio-hub-kappa-murex.vercel.app/)
- **LinkedIn:** [Michael Forsythe Robinson](https://www.linkedin.com/in/michael-forsythe-robinson-082255391/)
- **Email:** Forsythepublishing@gmail.com
- **Newsletter:** [The Measurement Standard](https://substack.com/@mforsytherobinson)
- **Orchid:** [Open Researcher](https://orcid.org/my-orcid?orcid=0009-0002-8487-759X)

---

## Citation

```bibtex
@techreport{robinson2026attribution,
  author       = {Robinson, Michael Forsythe},
  title        = {The Forsythe Attribution and Measurement Framework},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18557680},
  url          = {https://doi.org/10.5281/zenodo.18557680},
  note         = {10-paper technical portfolio covering the full attribution stack}
}
```

## License

All research papers are published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Implementation code is MIT licensed.
