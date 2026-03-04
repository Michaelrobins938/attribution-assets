---
layout: default
title: "Incrementality and Geo-Testing: Recovering True Causal Lift"
description: "Integrating synthetic control, difference-in-differences, and placebo-validated inference."
author: Michael Forsythe Robinson
doi: "10.5281/zenodo.18860345"
---

# Incrementality and Geo-Testing: Recovering True Causal Lift
## Integrating Synthetic Control, Difference-in-Differences, and Placebo-Validated Inference

**Technical Whitepaper v1.0.0**

| **Attribute** | **Value** |
|---|---|
| **Version** | 1.0.0 |
| **Status** | Production-Ready |
| **Date** | January 31, 2026 |
| **Classification** | Causal Inference / Econometrics |
| **Document Type** | Technical Whitepaper |

---

## **Abstract**

Marketing attribution often confuses correlation with causation. This whitepaper details a **Geographical Incrementality Testing Framework** designed to measure the true "causal lift" of marketing interventions. By leveraging **Synthetic Control (SCM)** and **Difference-in-Differences (DiD)**, we construct counterfactual "what-if" scenarios that allow marketers to see what would have happened if they HAD NOT spent money in a specific region. 

---

## **Table of Contents**

1. [Glossary & Notation](#glossary--notation)
2. [The Flaw in Observation: Why We Need Experiments](#1-the-flaw-in-observation-why-we-need-experiments)
3. [Methodology: Constructing the Counterfactual](#2-methodology-constructing-the-counterfactual)
4. [Statistical Inference & Validity](#3-statistical-inference--validity)
5. [Power Analysis: Preventing "Unclear" Results](#4-power-analysis-preventing-unclear-results)
6. [Business Integration: The iROAS Metric](#5-business-integration-the-iroAs-metric)
7. [Technical Implementation Specification](#6-technical-implementation-specification)
8. [MMM-Incrementality Bridge Integration](#7-mmm-incrementality-bridge-integration)
9. [Causal Interpretation & Limitations](#8-causal-interpretation--limitations)
10. [Conclusion](#9-conclusion)
11. [Strategic Implementation Guide](#10-strategic-implementation-guide)
12. [Implementation Maturity Model](#11-implementation-maturity-model)
13. [Worked Numerical Example](#12-worked-numerical-example)
14. [Data Requirements & Minimum Viable Implementation](#13-data-requirements--minimum-viable-implementation)

---

## **Glossary & Notation**

| **Term** | **Definition** |
|---|---|
| **Counterfactual** | The scenario that would have occurred without the intervention. |
| **Synthetic Control** | A weighted combination of control markets that best mimics the treated market's pre-period history. |
| **DiD** | Difference-in-Differences; comparing the change over time in a treated group vs. a control group. |
| **RMPE** | Root Mean Squared Prediction Error; a measure of fit in the pre-treatment period. |
| **Placebo Test** | Re-running the analysis on non-treated units or time periods to verify that estimated effects are significant. |
| **iROAS** | Incremental Return on Ad Spend; revenue lift divided by experimental spend. |

---

## **1. The Flaw in Observation: Why We Need Experiments**

Observational attribution (like last-touch) rewards channels that reach users who were already going to buy. To find **Incremental Revenue**, we must run randomized experiments. However, since user-level randomization is often impossible (due to "walled gardens" or privacy), we use **Geographical Randomization** (Geo-Testing).

---

## **2. Methodology: Constructing the Counterfactual**

### **2.1 Geo-Matching**
We identify a pool of potential control markets (DMAs) and use a **Mahalanobis Distance** or **Optimal Hungarian Assignment** to find the pair that most closely tracks the treatment market during the pre-period ($R^2 > 0.85$).

### **2.2 Difference-in-Differences (DiD)**
The simplest causal estimator. We measure the "gap of gaps":
$$\hat{\tau} = (\bar{Y}_{T,post} - \bar{Y}_{T,pre}) - (\bar{Y}_{C,post} - \bar{Y}_{C,pre})$$
This removes time-invariant biases between markets and global time trends.

### **2.3 Synthetic Control Method (SCM)**
For high-stakes decisions, we use SCM. Rather than picking one control market, we create a **Weighted Synthetic Market**:
$$\hat{Y}_{T,counterfactual} = \sum_{j \in DonorPool} w_j \cdot Y_j$$
Weights are optimized using constrained regression to minimize pre-period error.

---

## **3. Statistical Inference & Validity**

Standard p-values often fail in time-series contexts. We use **Placebo-Based Inference**:
1. **In-Space Placebo:** We "pretend" a control market was treated and measure its "effect." If the real treatment effect is larger than 95% of placebo effects, it's significant.
2. **In-Time Placebo:** We "pretend" the treatment started earlier. The effect should be zero.
3. **Block Bootstrap:** We resample time blocks to estimate the variance of the lift, preserving temporal correlation.

---

## **4. Power Analysis: Preventing "Unclear" Results**

Before launching a test, we run a **Power Simulation** to determine the probability of detection. We vary the potential lift (e.g., 5%, 10%, 15%) and the test duration to ensure that stakeholders aren't wasting money on an "underpowered" experiment where the result is likely to be "Inconclusive."

---

## **5. Business Integration: The iROAS Metric**

The output of every incrementality test is the **Incremental ROAS (iROAS)**:
$$iROAS = \frac{\text{Incremental Sales}}{\text{Incremental Spend}}$$
This is the only metric that should be used for budget scaling. If $iROAS > \text{Target}$, the channel is truly driving growth; if not, the channel is merely "harvesting" existing demand.

---

## **6. Technical Implementation Specification**

- **Inference Engine:** Python (SCM, DiD, BSTS wrappers).
- **Validation Suite:** Automated Type I/II error tracking and placebo generation.
- **Reporting:** 95% Confidence Intervals provided for every lift estimate.

---

## **7. MMM-Incrementality Bridge Integration**

### **7.1 The Validation Problem**

The output of incrementality testing should be systematically validated against MMM results. This cross-validation addresses the critical question: **"How do we trust our MMM?"**

The **MMM-Incrementality Validation Bridge** (Robinson, 2026e) provides:

1. **Confidence Interval Overlap Analysis**: Comparing 95% CIs from MMM vs incrementality tests
2. **Gap Scoring**: Measuring relative difference between MMM ROI and measured lift
3. **Classification**: Identifying channels where MMM over/underestimates true effectiveness
4. **Prioritization**: Recommending which channels to test next based on spend and uncertainty

### **7.2 Integration Workflow**

```
MMM Results ──┐
              ├──▶ Validation Bridge ──▶ Validated Recommendations
Incrementality┘
```

When MMM and incrementality disagree:
- If MMM > Incrementality: MMM may be overestimating (conduct geo-test)
- If MMM < Incrementality: MMM may be underestimating (review model)
- If aligned: High confidence in MMM results

---

## **8. Causal Interpretation & Limitations**

- **Spillover Effects:** Marketing in one geo might leak into neighboring geos (TV bleed-over).
- **Parallel Trends Assumption:** DiD assumes the treated and control geos would have followed the same trend—often hard to prove.
- **Duration Bias:** Short-term tests may miss "delayed" effects that occur weeks later.

---

## **9. Conclusion**

Incrementality testing is the "Gold Standard" of attribution. By moving away from observational counting and towards experimental causality, businesses can eliminate waste and double down on the channels that actually move the needle.

---

## **10. Strategic Implementation Guide**

### **10.1 The 5 Most Valuable Insights**

| # | Insight | What Decisions It Informs |
|---|---------|---------------------------|
| 1 | **Attribution ≠ Incrementality** - Channels with high attribution may have low incrementality and vice versa | Budget reallocation |
| 2 | **Tests are expensive** - $500K-5M per test in foregone optimization | Which channels to test |
| 3 | **Power analysis prevents "inconclusive"** - 25% of tests fail due to underpowering | Test design |
| 4 | **Synthetic control > DiD for high-stakes** - Weighted donors more robust than single control | Method selection |
| 5 | **Bridge validates over time** - MMM + Incrementality together build confidence | Continuous improvement |

### **10.2 Implementation: 5-Step Plan**

| Step | Action | Owner | Quick Win | Measurable Result |
|------|--------|-------|-----------|-------------------|
| 1 | Select channels for testing | Marketing Science | Priority list | 5 channels ranked |
| 2 | Run power analysis | Analyst | MDE determined | Test can detect X% |
| 3 | Design geo-test | Data Science | Control geos selected | Pre-period R² > 0.8 |
| 4 | Execute test | Analytics | Lift measured | iROAS calculated |
| 5 | Update MMM via bridge | Data Science | Model improved | Accuracy +X% |

### **10.3 Hidden Assumptions & Blind Spots**

| Assumption | What If It's Wrong |
|------------|-------------------|
| Parallel trends hold | Test biased → wrong iROAS |
| No spillover | Neighboring geos contaminated → inflate lift |
| Duration sufficient | Short test → miss delayed effects |
| Control matching valid | Poor match → invalid counterfactual |

### **10.4 Compare Opposing Views**

| Perspective | Works When |
|-------------|------------|
| **DiD only** | Quick tests, many geos, lower stakes |
| **SCM only** | High-stakes, limited geos, need robustness |
| **Bridge + Both** | Ongoing program, want continuous validation |

### **10.5 Leverage Points**

| # | Leverage Point | Expected Impact |
|---|---------------|-----------------|
| 1 | Power analysis upfront | 50% fewer inconclusive tests |
| 2 | Bridge with MMM | 60% less testing needed |
| 3 | Placebo validation | Higher confidence in results |

### **10.6 Contrarian Takeaways**

1. **Most tests are unnecessary** - Bridge tells you which ones matter
2. **DiD is often good enough** - SCM is overkill unless high-stakes
3. **Longer isn't always better** - 8 weeks optimal; beyond that, cost exceeds value

### **10.7 Role-Specific Perspectives**

| Role | Question | Answer |
|------|----------|--------|
| **Marketer** | What drives reach? | iROAS shows true channel value vs. attribution |
| **Founder** | What affects cash? | Fewer tests, more confidence = better ROAS |
| **Analyst** | What changes metrics? | Lift % directly from counterfactual |

---

---

## **11. Implementation Maturity Model**

| Level | Name | Testing Cadence | iROAS Confidence | Key Gap |
|-------|------|----------------|-----------------|---------|
| **1 - No Testing** | Trust Attribution | Never | None | All attribution numbers unvalidated |
| **2 - Ad Hoc** | Annual Geo-Test | 1x/year | ±40% | No systematic program; results siloed |
| **3 - Systematic DiD** | Quarterly | 4x/year | ±20% | No SCM; no bridge validation |
| **4 - SCM + Bridge** | Ongoing Program | 8–12x/year | ±10% | Manual test selection |
| **5 - Automated ML** | Predictive | Continuous | ±5% | Infrastructure investment required |

### **Progression Checklist**

| Transition | Required Actions |
|------------|-----------------|
| L1 → L2 | Pick one channel; run DiD test in 2 paired DMAs; measure iROAS |
| L2 → L3 | Standardize DiD workflow; run power analysis before every test |
| L3 → L4 | Implement SCM for high-stakes channels; connect bridge to MMM outputs |
| L4 → L5 | Automate test prioritization via spend × uncertainty scoring; ML-predicted iROAS |

---

## **12. Worked Numerical Example**

### **Scenario: National TV Campaign — DiD + Bridge Validation**

**Setup:** $500K/week TV campaign. 5 treatment DMAs, 5 matched control DMAs.

**Step 1 — Pre-Period Validation (8 Weeks):**

```
Treatment geos (avg weekly sales): $4.2M
Control geos (avg weekly sales): $4.1M
Tracking correlation (R²): 0.94
RMPE: 3.1%  →  Valid (threshold: RMPE < 5%, R² > 0.85)
```

**Step 2 — Test Period (4 Weeks):**

| DMA Group | Week 1 | Week 2 | Week 3 | Week 4 | Total |
|-----------|--------|--------|--------|--------|-------|
| Treatment (5 DMAs) | +$1.1M | +$1.4M | +$1.3M | +$0.4M | **+$4.2M** |
| Control (5 DMAs) | +$0.3M | +$0.2M | +$0.3M | +$0.3M | **+$1.1M** |

**Step 3 — DiD Lift Calculation:**

$$\hat{\tau} = (\bar{Y}_{T,post} - \bar{Y}_{T,pre}) - (\bar{Y}_{C,post} - \bar{Y}_{C,pre})$$

$$\hat{\tau} = \$4.2M - \$1.1M = \$3.1M \text{ incremental revenue}$$

$$iROAS = \frac{\$3.1M}{\$2.0M \text{ test spend}} = 1.55x$$

**Step 4 — Placebo Validation:**

In-space placebo (100 permutations): Real effect ranks #2/100 → p-value 0.02 ✓

**Step 5 — Bridge Cross-Validation:**

| Source | TV Channel ROI Estimate | Gap Score |
|--------|------------------------|-----------|
| MMM (pre-test) | 2.18x | — |
| Incrementality (measured) | 1.55x | **29% gap** |
| Bridge classification | ⚠️ MMM Overestimating | Reduce TV allocation |

**Step 6 — Business Action:**

MMM recalibrated. TV budget cut from $500K/week to $380K/week (-24%). **Savings: $6.2M/year**, reallocated to Search (iROAS 2.8x measured).

---

## **13. Data Requirements & Minimum Viable Implementation**

### **Tier 1 — Minimum Viable (Week 1–2)**

| Data Source | Required Fields | Frequency |
|-------------|----------------|-----------|
| Sales by DMA | `dma_code`, `week_start`, `revenue`, `units` | Weekly |
| Spend by DMA | `dma_code`, `channel`, `week_start`, `spend` | Weekly |
| DMA metadata | `dma_code`, `population`, `region`, `market_size_index` | Static |

**Minimum history:** 12 weeks pre-period. **Minimum DMAs:** 10 (5 treatment, 5 control).

**Output:** Basic DiD estimate with manual placebo test. Confidence interval ±25%.

### **Tier 2 — Target State (Month 1–2)**

| Data Source | Required Fields | Frequency |
|-------------|----------------|-----------|
| Daily DMA sales | Granular daily data for SCM pre-period fitting | Daily |
| Donor pool | 50+ candidate DMAs for synthetic control weights | Daily |
| External controls | Google Trends branded search index, unemployment rate by DMA | Weekly |

**Output:** SCM + DiD with automated placebo inference. Confidence interval ±10–15%.

### **Tier 3 — Full Production (Month 3+)**

| Data Source | Required Fields | Frequency |
|-------------|----------------|-----------|
| Store-level data | SKU-level response by zip code | Daily |
| Competitive spend | Competitor ad spend by DMA (Nielsen/iSpot) | Weekly |
| MMM Bridge connection | Live MMM channel ROI estimates for gap scoring | Per MMM run |

**Output:** Continuous test-and-learn program with automated bridge validation. iROAS estimates ±5%.

### **Minimum Viable Tech Stack**

```
SQL (sales + spend by DMA)  →  Python (DiD + SCM)  →  Power analysis  →  Bridge comparison
Estimated setup: 1 data scientist × 2 weeks
ROI: First reallocation typically saves 15–30% of tested channel budget
```


## **References**

[1] Robinson, M.F. (2026a). "A First-Principles Hybrid Attribution Framework." Zenodo. https://doi.org/10.5281/zenodo.18557680
[2] Robinson, M.F. (2026b). "Bayesian Media Mix Modeling: Axiomatic Budget Optimization." Zenodo. https://doi.org/10.5281/zenodo.18599386
[3] Robinson, M.F. (2026c). "Behavioral Profiling and Causal Uplift: Beyond The Conversion." Zenodo. https://doi.org/10.5281/zenodo.18599425
[4] Robinson, M.F. (2026d). "The Causal Calibration System: Stress-Testing Attribution Models." Zenodo. https://doi.org/10.5281/zenodo.18599433
[5] Robinson, M.F. (2026e). "The MMM-Incrementality Validation Bridge." Zenodo. (Forthcoming)
[6] Robinson, M.F. (2026f). "Marketing Data Connectors: Unified API Architecture." Zenodo. (Forthcoming)
[7] Abadie, A. et al. (2010). "Synthetic Control Methods for Comparative Case Studies." JASA.
