# 🧭 AI System Risk Register

This document tracks potential risks across AI system lifecycle stages — data ingestion, model training, deployment, and compliance.

| ID | Category | Risk Description | Likelihood | Impact | Mitigation | Owner | Review Frequency |
|----|-----------|------------------|-------------|---------|-------------|--------|------------------|
| R1 | Data | PII leakage during ingestion | Medium | High | Apply masking at source using Unity Catalog policies | Data Engineering | Quarterly |
| R2 | Model | Model bias across demographic segments | High | High | Implement fairness audits and stratified test sets | Data Science | Quarterly |
| R3 | Compliance | Lack of reproducibility during audit | Medium | High | Use Delta Lake with time-travel rollback for every training run | ML Engineering | Monthly |
| R4 | Vendor | External API downtime (e.g. STT provider) | Medium | Medium | Implement retry decorator & fallback vendor logic | AI Ops | Monthly |
| R5 | Security | Expired API tokens or unauthorized access | Low | High | Rotate secrets via K8s secrets manager; enable trace ID logging | Security | Monthly |

---

**Next Review:** January 2026  
**Maintained By:** Director of AI Integration & Compliance Systems
