# POLICIES — Policy Layer (Governance-Owned)

Policies define **WHAT** must be enforced.

Engineers implement **HOW** it is enforced.

This folder contains the formal AI governance policies that drive:
- Drift thresholds  
- Fairness requirements  
- Toxicity & hallucination limits  
- Cost guardrails  
- Logging & audit retention  
- Approval workflows  

## 📘 Contents

| File | Purpose |
|------|---------|
| `policies.yaml` | Main policy configuration, editable by Compliance & Architecture |
| `policy-schema.json` | JSON schema ensuring structure and correctness |
| `examples/` | Optional sample policy sets for different model families |

## 🧭 Ownership

- **Primary Owners:** Compliance, Legal, Privacy, Enterprise Architecture  
- **Secondary Editors:** Risk teams, Product Governance  
- **Consumers:** MLOps, Engineering, LLM Gateway teams  

Engineering *cannot* modify policies without governance approval.

## 🛠 How Policies Are Used

1. The **Policy Manager** loads `policies.yaml`.  
2. Evaluators use thresholds to compute PASS / FAIL / FLAG.  
3. Violations trigger escalation rules defined here.  
4. Audit events incorporate `policy_version`, thresholds, and actions.  

## 🏛 Alignment

This structure aligns to:
- **NIST AI RMF – Govern Function**
- **ISO/IEC 42001 – AI Management System**
- **EU AI Act – Articles 9, 10, 12 (Risk, Data, Logging)**

Policies are the foundation of trusted AI.
