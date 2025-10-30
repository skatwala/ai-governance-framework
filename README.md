# 🧭 AI Governance Framework — Executive Overview

**Purpose:**  
A practical, auditable governance layer for safe enterprise AI adoption — ensuring every model, prompt, and decision is traceable, compliant, and cost-controlled.

---

## 🧩 What’s Inside

| Layer | Contents | Purpose |
|-------|-----------|----------|
| **Governance** | Risk register, scorecard, operating model | Define accountability & KPIs |
| **Finance** | Budget playbooks, architecture cost models | Track fiscal discipline |
| **Decisions** | ADRs & regulation tracker | Document key trade-offs |
| **Prompt Governance** | Safety, traceability, cost, security templates | Enforce compliance-by-design |

---

## 🪜 Quick Adoption Steps

1. Copy `Governance/risk-register-template.*` → log your top 10 AI risks.  
2. Add `trace_id` logging from `prompt_templates/traceability.md` in your LLM gateway.  
3. Embed guardrails from `safety-guardrails.md` to block unsafe content.  
4. Track AI spend monthly via `Finance/ai-budget-tracker.md`.  
5. Record vendor choices & rationale in `Decisions/adr-001-llm-vendor-selection.md`.

---

## 🧭 Governance KPIs

| Metric | Target | Current | Trend |
|---------|---------|----------|--------|
| Risk Coverage | ≥ 80 % | 71 % | ↑ |
| Residual Risk | ≤ 6 | 5.2 | ↔ |
| Compliance SLA | ≥ 90 % | 88 % | ↑ |
| Budget Variance | ± 10 % | +6 % | ↓ |
| Incident MTTR | < 24 h | 20 h | ↑ |

---

## 🌍 Alignment

- **NIST AI RMF:** Map / Measure / Manage / Govern  
- **EU AI Act:** Annex IV (Technical Documentation), Article 9 (Risk Management)  
- **ISO 23894:** AI Risk Management Framework  

> *“AI systems don’t fail on accuracy — they fail on trust.”*  
> This framework builds the **trust layer** for responsible scaling.

**Related Pages:** [Executive Overview](docs/README.md) | [Standards Mapping](Governance/standards-mapping.md) | [Case Study](CASE-STUDY.md)

**Supporting Docs:** [Changelog](CHANGELOG.md) | [Security Policy](SECURITY.md)

## 📂 Download Center

| File | Type | Link |
|------|------|------|
| Risk Register Template | Excel | [Download](./Governance/risk-register-template.xlsx) |
| AI Budget Tracker | Excel | [Download](./Finance/Budget-Playbook.xlsx) |
| Operating Model Deck | PowerPoint | [Download](./Governance/Operating-Model.pptx) |

> Tip: these files open directly in Office Online if you’re logged in to Microsoft 365.


_Last updated: {{ site.time | date: "%Y-%m-%d" }}_
