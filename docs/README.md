# AI Governance Framework — Executive Overview

**Purpose.** Practical artifacts to run AI with trust: safety, traceability, cost control, and governance KPIs.

## What’s inside
- **Governance:** risk register, scorecard, operating model, standards mapping.
- **Finance:** budget playbooks, architecture cost models.
- **Decisions:** ADRs and regulation tracker.
- **Prompt Governance:** safety, traceability, cost, and security templates.

## 30-minute adoption quickstart
1) Copy `Governance/risk-register-template.*` and log top 10 risks.  
2) Add `trace_id` + prompt logging per `prompt_templates/traceability.md`.  
3) Enforce “do-not-diagnose/prescribe” from `safety-guardrails.md`.  
4) Enable cost logging from `cost-optimization.md` + budget alerts.  
5) Record vendor choice as an ADR and review quarterly.

_Last updated: {{ site.time | date: "%Y-%m-%d" }}_
