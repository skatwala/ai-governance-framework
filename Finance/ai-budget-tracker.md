# AI Budget Tracker (Starter)

Track estimated vs. actual costs by category. Update monthly.

| Month | LLM Inference ($) | Vector DB ($) | Data Platform ($) | MLOps/Infra ($) | Security/Compliance ($) | Labor ($) | Total ($) |
|------:|-------------------:|--------------:|------------------:|----------------:|-------------------------:|----------:|----------:|
| 2025-10 | 4,200 | 1,050 | 1,800 | 2,400 | 900 | 18,000 | 28,350 |
| 2025-11 | 5,100 | 1,200 | 1,900 | 2,400 | 900 | 18,000 | 29,500 |

**Cost Categories**
- **LLM Inference:** tokens, context window premium, eval runs
- **Vector DB:** storage, RAG queries, index builds
- **Data Platform:** ETL, Lakehouse, storage/egress
- **MLOps/Infra:** AKS/EKS, GPUs/CPUs, observability, CI/CD
- **Security/Compliance:** DLP, key mgmt, audits, pen-tests
- **Labor:** Eng, PM, QA, Data, governance

**Policies**
- Budget variance alert at ±10% month-over-month
- Tag all cloud resources with `cost_center=AI` and `env={dev|prod}`
