# 🔗 AI Data Lineage & Audit Trail

**Objective:**  
Provide end-to-end visibility of every AI decision — from user input to logged outcome — ensuring full auditability under HIPAA, GDPR, ISO 23894, and the EU AI Act.

> **Core Principle:** “If you can’t trace it, you can’t trust it.”

Each LLM interaction, dataset, and model artifact must be **discoverable, versioned, and reproducible** — forming a continuous chain of custody.

---

## 🪜 7-Step Lineage Lifecycle

| Step | Phase | Description | Typical System |
|------|------|-------------|----------------|
| **1️⃣ Ingest** | Capture | User input (prompt) enters via gateway with `trace_id` and metadata headers. | `trustgate-fastapi` |
| **2️⃣ Redact** | Sanitize | PII/PHI masked via rules engine or Unity Catalog functions. | Databricks / DLT |
| **3️⃣ Hash** | Fingerprint | Content hashed (`sha256`) for tamper detection and audit integrity. | Python UDF / Spark UDF |
| **4️⃣ Store** | Persist | Logs written to immutable storage with retention policy (e.g., Delta Lake WORM). | Cloud Data Lake |
| **5️⃣ Index** | Discover | Metadata indexed for query & replay (model, timestamp, `trace_id`). | Unity Catalog / OpenSearch |
| **6️⃣ Replay** | Verify | Auditors can replay prompts and compare outputs for reproducibility. | Evaluation Harness |
| **7️⃣ Retain / Purge** | Govern | Expired data pruned per policy; non-repudiation proofs retained. | Lifecycle Mgmt |

---

## 🧭 Governance Controls (What we prove)

| Control | Implementation | Evidence |
|--------|-----------------|---------|
| **Trace IDs** | UUID4 per request on HTTP/WebSocket | `prompt_templates/traceability.md` |
| **Redaction Policy** | Mask PHI/PII before storage | UC masking logs / policy docs |
| **Immutable Storage** | WORM or Delta Time-Travel | Delta checkpoints / access policies |
| **Access Logs** | Immutable audit trails | Cloud provider audit logs |
| **Data Retention** | 365-day default (exceptions allowed) | Governance policy register |
| **Replay Proof** | Hash comparison across runs | Evaluation harness results |

---

## 🧮 Example OTEL Trace Snapshot

```json
{
  "trace_id": "8f1b9c7a-12cd-4a1f-bf21-7dfb3f310e12",
  "span_name": "LLMRequest",
  "attributes": {
    "user_region": "US-East",
    "model": "gpt-4o",
    "input_hash": "sha256:9c1a...7e2f",
    "masked_fields": ["name", "dob"],
    "storage_uri": "delta://ai/logs/prompts/2025/10/28",
    "policy_version": "v1.3.0",
    "retention_days": 365
  },
  "status": "OK",
  "end_time": "2025-10-28T17:15:30Z"
}
