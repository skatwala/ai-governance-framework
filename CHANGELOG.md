# 🧾 Changelog — AI Governance Framework

All notable changes to this repository are documented here for transparency, auditability, and governance maturity.  
Version numbers follow [Semantic Versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`.

---

## [v0.9.0] — 2025-10-29

### ✨ Added
- Initial public release of the **AI Governance Framework**  
  - Governance, Finance, Decisions, and Prompt Governance layers established.  
  - Integrated links to sister repos:
    - [`trustgate-fastapi`](https://github.com/skatwala/trustgate-fastapi)  
    - [`trustgate-evals`](https://github.com/skatwala/trustgate-evals)  
    - [`compliance-ai-reference-arch`](https://github.com/skatwala/compliance-ai-reference-arch)
- Added prompt governance templates:
  - `safety-guardrails.md` – defines red lines (“do not diagnose / prescribe”)  
  - `traceability.md` – metadata schema and `trace_id` enforcement  
  - `cost-optimization.md` – caching and tiered model selection  
  - `security-controls.md` – injection and PII protection
- Added financial templates: `Budget-Playbook.xlsx`, `ai-budget-tracker.md`
- Added risk register and governance scorecard with executive KPIs
- Added `CASE-STUDY.md`, `standards-mapping.md`, and `data-lineage.md` (v0.9 milestone)

### 🧭 Improved
- Consistent style and emoji headers across all governance artifacts  
- `_config.yml` cleaned and optimized for GitHub Pages  
- Mermaid diagrams validated across README and subpages  
- Added internal cross-links for better navigation

### 🛡️ Compliance Alignment
- Verified coverage against **NIST AI RMF**, **ISO 23894**, **HIPAA §164.312(b)**, and **EU AI Act Annex IV(d)**
- Introduced data lineage model ensuring traceable, replayable AI decisions

---

## [Planned v1.0.0] — Target: November 2025
- Add **automated scorecard updater** (via GitHub Actions)
- Publish **JSON schema** for trace logs and lineage proofs
- Release **FastAPI gateway integration example** showing full policy compliance
- Expand governance metrics to include **post-market monitoring** (AI incident register)
- Add **annual review protocol** under `/Governance/review-checklist.md`

---

_Repository Owner:_ **Saptarshi Katwala**  
_Location:_ `https://github.com/skatwala/ai-governance-framework`  
_Last updated:_ **2025-10-29**
