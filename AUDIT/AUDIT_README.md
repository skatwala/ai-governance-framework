# AUDIT — Traceability & Compliance Logging

This folder defines the **audit trail** required for responsible AI systems.

Every governance check — drift, fairness, safety, cost — must emit a structured audit event:
- Timestamp  
- Model version  
- Policy applied  
- Metric values  
- PASS / FAIL / FLAG  
- Severity  
- Trace ID for request-level tracking  

## 📘 Contents

| File | Purpose |
|------|---------|
| `audit_log_schema.json` | Formal schema for audit events (Annex IV compliant) |
| `sample_audit_event.json` | Example PASS/FAIL record showing real structure |

## 🧭 Ownership

- **Primary:** Compliance, Internal Audit, Risk  
- **Secondary:** Enterprise Architecture  
- **Consumers:** MLOps, Observability, Engineering  

## 📜 Why This Exists

Regulators expect:
- **EU AI Act Article 12 — Logging & Monitoring**  
- **ISO 42001 — Continuous Monitoring & Corrective Action**  
- **NIST AI RMF — Govern / Measure / Manage**  

Logs must be:
- Structured  
- Immutable  
- Retained  
- Searchable  
- Linked to policies  

## 🛠 How Audit Works

1. Evaluator runs checks.  
2. Each check creates an audit event aligned to this schema.  
3. Events feed dashboards, reports, and audit reviews.  
4. High-severity events trigger governance workflows.  

The audit layer ensures **trust, transparency, and traceability**.
