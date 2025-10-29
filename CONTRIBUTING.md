# Contributing Guidelines

Thank you for improving the **AI Governance Framework**!  
Please follow this minimal checklist before submitting pull requests.

## 1. Compliance Review Checklist
- [ ] No hard-coded API keys, secrets, or PII
- [ ] All new prompts follow “Do not diagnose / prescribe” rule
- [ ] Risk and budget entries use provided templates
- [ ] Metrics updated under `Governance/metrics-dashboard.md`

## 2. Structure & Naming
- Use snake_case for files, kebab-case for folders
- Each ADR should follow `adr-###-short-description.md`

## 3. Linting & Docs
- Run `markdownlint` locally if available
- Ensure README and diagrams stay current after major changes

## 4. License
All contributions are under the **MIT License** (see `LICENSE`).

---
_For governance questions, open a Discussion tagged **policy**._
