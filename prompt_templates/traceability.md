# 🔍 Prompt Traceability & Provenance

**Objective:**  
Guarantee end-to-end visibility of each LLM interaction for regulatory audits and AI accountability.

---

## 1. Core Principle
> “Every AI decision must be traceable — from request to response.”

---

## 2. Required Metadata
| Field | Description | Example |
|--------|--------------|----------|
| **trace_id** | Unique request identifier (UUID4) | `8f1b9c7a-12cd-4a1f-bf21-7dfb3f310e12` |
| **model_name** | LLM version used | `gpt-4o-mini-2025-05-12` |
| **temperature** | Sampling parameter | `0.2` |
| **region** | Data residency location | `US-East` |
| **gateway_id** | API or proxy instance handling request | `fastapi-gw-01` |

---

## 3. Controls
- Add `trace_id` headers to **all API calls** (HTTP and WebSocket).  
- Store **prompt + metadata** in a compliance log (hashed or redacted as needed).  
- Enable **prompt replay** for auditors with masked content.  
- Use **OpenTelemetry traces** where available.

---

## 4. Example Log Record
```json
{
  "trace_id": "8f1b9c7a-12cd-4a1f-bf21-7dfb3f310e12",
  "model": "gpt-4o",
  "region": "eu-frankfurt",
  "role": "system",
  "prompt": "You are a diabetes device assistant...",
  "timestamp": "2025-10-25T15:32:41Z"
}
