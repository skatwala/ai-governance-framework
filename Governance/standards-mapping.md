# 🌐 Standards Mapping — NIST AI RMF · EU AI Act · ISO 23894

This mapping shows how artifacts in this repository align with key global AI governance frameworks.

| Control Area | Repo Artifact / Process | NIST AI RMF Function | EU AI Act Reference | ISO 23894 Clause |
|---------------|--------------------------|-----------------------|--------------------|------------------|
| **Risk Management** | `risk-register-template.*` | MAP / MEASURE / MANAGE | Art. 9 – Risk Management System | 6.1 – 6.3 |
| **Data Governance & Traceability** | `traceability.md`, `security-controls.md` | MAP / MEASURE | Annex IV (d) – Technical Docs | 7.1 |
| **Technical Documentation** | `CASE-STUDY.md`, `ADR-001` | GOVERN | Annex IV (a–f) | 7.4 |
| **Human Oversight & Safety** | `safety-guardrails.md` | GOVERN | Art. 14 – Human Oversight | 8.2 |
| **Transparency & Explainability** | `prompt_templates/` + `trace_id` logs | MEASURE / MANAGE | Art. 13 – Transparency | 7.5 |
| **Post-Market Monitoring** | `governance-scorecard.md`, `metrics-dashboard.md` | MANAGE / GOVERN | Art. 61 – PMS Plan | 9.1 |
| **Budget & Resource Control** | `ai-budget-tracker.md`, `Budget-Playbook.xlsx` | MANAGE | — | — |
| **Change Control / Continuous Improvement** | `CHANGELOG.md`, monthly scorecard reviews | GOVERN | Art. 17 – Quality Management | 9.3 |

> **Interpretation:**   
> The AI Governance Framework provides both *policy coverage* (documents & metrics) and *operational evidence* (logs, ADRs, cost tracking) demanded by global regulators.

_Last updated: {{ site.time | date: "%Y-%m-%d" }}_
