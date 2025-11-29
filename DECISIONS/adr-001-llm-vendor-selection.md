# ADR-001: LLM Vendor Selection

**Status:** Accepted  
**Date:** 2025-10-28

## Context
We require a primary LLM provider for production use in regulated workflows (PHI/PII). Needs: enterprise SLA, logging controls, regional data residency, and reasonable cost per 1K tokens.

## Decision
Select **Vendor A** as the primary LLM for production; **Vendor B** as fallback via gateway abstraction.

## Rationale
- Meets HIPAA-eligible deployment and regional hosting
- Provides explicit ban on training on our data
- Superior latency at 128k context in benchmarks
- Volume pricing with monthly commit reduces cost by ~18%

## Consequences
- Gateway must support hot-swap between A/B
- Evaluation harness runs monthly to detect regressions
- Contract reviews annually with exit clause (60 days)

## Alternatives Considered
- Single-vendor lock-in: rejected due to concentration risk
- Open-source model on self-hosted GPUs: delayed pending SRE capacity
