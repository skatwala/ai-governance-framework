# 🔒 Security Policy — AI Governance Framework

The AI Governance Framework is designed to model compliance and auditability for enterprise AI systems.  
Even though this repository contains **non-confidential templates**, we maintain a clear disclosure and response process to ensure continued trust and integrity.

---

## 🧭 Supported Versions

| Version | Supported | Notes |
|----------|------------|-------|
| **v0.9.x** | ✅ Active | Public reference release (non-confidential) |
| **v0.8.x and below** | ❌ Unsupported | Internal drafts / deprecated structure |

---

## 🛠️ Reporting a Vulnerability

If you discover a security vulnerability, data-exposure risk, or policy flaw within this framework:

1. **Do not open a public GitHub issue.**  
   Instead, contact the maintainer directly:
   - 📧 **skatwala@gmail.com**
   - 🔗 [LinkedIn / Saptarshi Katwala](https://www.linkedin.com/in/saptarshi-katwala/)
2. Include a clear description of:
   - The affected file(s) or policy template
   - Expected vs. actual behavior
   - Any mitigation or patch suggestions
3. You will receive acknowledgment within **3 business days** and a proposed resolution plan within **10 business days**.

---

## 🧩 Security Design Principles

- **Least Privilege:** Every API key, role, or dataset referenced in templates assumes scoped access only.  
- **Traceability:** Every transaction carries a `trace_id` for full forensic auditability.  
- **Immutability:** Governance artifacts and logs must support write-once, read-many (WORM) retention.  
- **Encryption:** All data examples assume at least AES-256 or KMS-managed encryption.  
- **Separation of Duties:** No individual control both defines and approves the same governance policy.  
- **Human Oversight:** Templates mandate escalation to a human reviewer for any automated AI decision in regulated domains.

---

## 🪶 Responsible Disclosure Philosophy

> “Transparency without accountability is noise; accountability without transparency is power.”

The AI Governance Framework exists to demonstrate *how security and governance intersect*.  
Even non-production templates are treated with production-grade discipline.  
Contributors are encouraged to submit improvements that strengthen privacy, observability, or audit resilience.

---

_Last reviewed: 2025-10-29_  
_Maintainer: Saptarshi Katwala (TrustGate Suite)_
