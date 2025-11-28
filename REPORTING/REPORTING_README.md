# REPORTING — Model Cards & Compliance Dashboards

This folder generates **executive-ready reporting artifacts** from evaluation results.

Model Cards, dashboards, and summaries support:
- EU AI Act Annex IV documentation  
- NIST RMF “Measure” & “Govern” evidence  
- Internal audit  
- Release readiness reviews  
- Annual model re-certification  

## 📘 Contents

| File | Purpose |
|------|---------|
| `generate_model_card.py` | Converts evaluation JSON → `MODEL_CARD.md` |
| `model_card_template.md` | Structure for human-readable model documentation |
| `html_dashboard_template.html` | Lightweight compliance dashboard |
| `compliance_dashboard.ipynb` | (Optional) Notebook to render PASS/FAIL indicators |

## 📊 Model Card Workflow

1. Evaluator produces `evaluations.json`.  
2. This JSON is fed into `generate_model_card.py`.  
3. Output: `MODEL_CARD.md` — audit-ready documentation.  
4. Optional dashboards summarize risks, fairness, drift, cost, approvals.  

## 🧭 Ownership

- **Primary:** Architecture, AI Platform  
- **Secondary:** Compliance, Product, Engineering Leads  

## 🏛 Alignment

Supports:
- **EU AI Act Annex IV — Technical Documentation**  
- **ISO 42001 — Documentation & Reporting**  
- **NIST AI RMF — Govern & Measure functions**

Reporting is the final stage of the governance pipeline, enabling fully auditable model lifecycles.
