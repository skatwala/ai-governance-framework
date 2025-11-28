# Model Card — customer-intent-llm (v1.3.2)

## 1. Overview

- **Use case:** Contact center intent classification
- **Owner:** AI Platform Team
- **Environment:** `prod`
- **Last evaluated:** 2025-01-10T12:34:56Z

## 2. Intended Use

- Primary purpose: Describe the real-world decision or workflow this model supports.
- Out-of-scope uses: Document uses that are explicitly disallowed.

## 3. Data

- Training set size: **120000** records
- Evaluation set size: **8000** records
- Sensitive attributes monitored: **gender, age_band, region**

## 4. Performance Metrics

| Metric | Value |
|--------|-------|
| accuracy | 0.91 |
| f1_macro | 0.88 |
| drift_psi | 0.12 |

## 5. Fairness & Bias Metrics

| Metric | Value |
|--------|-------|
| demographic_parity_difference | 0.06 |
| equal_opportunity_difference | 0.04 |

## 6. Policy & Governance Summary

- Policy set: **ai-governance-default** (v1.0.0)
- Drift status: **PASS**
- Fairness status: **FLAG**
- Toxicity status: **PASS**

## 7. Known Risks & Limitations

- Higher error rate for age_band=18-25
- Moderately elevated drift in region=APAC

## 8. Mitigations & Controls

- Added re-weighted loss for minority groups
- Quarterly fairness re-training schedule

## 9. Change Log

- Describe recent model updates, retraining, and policy changes here.
