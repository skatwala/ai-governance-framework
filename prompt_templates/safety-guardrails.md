# 🛡️ Prompt Safety Guardrails

**Objective:**  
Ensure that all LLM prompts operate within clinical, legal, and regulatory boundaries — preventing the system from prescribing, diagnosing, or generating harmful guidance.

---

## 1. Core Principle
> “When in doubt, *defer to human expertise*.”

Prompts must always:
- Avoid **medical advice**, **diagnosis**, or **treatment suggestions**.  
- Respond only within the scope of **device operation**, **sensor troubleshooting**, or **data interpretation**.  
- Redirect users to **qualified healthcare professionals** for medical decisions.

---

## 2. Governance Controls
| Control | Implementation |
|----------|----------------|
| **Explicit Role Prompting** | Prefix system message with: *“You are a device assistant, not a healthcare professional.”* |
| **Restricted Vocabulary** | Block lists for words like *prescribe*, *dose*, *medication*, etc. |
| **Audit Scenarios** | Maintain sample dangerous user prompts and test system responses quarterly. |

---

## 3. Example
> ❌ **Don’t say:** “Take 10 units of insulin.”  
> ✅ **Say:** “Your readings appear high. Please verify your sensor connection and consult your doctor if readings remain elevated.”
