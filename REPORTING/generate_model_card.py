"""Simple Model Card generator.

Usage:
  python generate_model_card.py --metrics-file evaluations.json --output-file MODEL_CARD.md

Expected input JSON structure (example):
{
  "model_id": "customer-intent-llm",
  "model_version": "v1.3.2",
  "owner": "AI Platform Team",
  "use_case": "Contact center intent classification",
  "environment": "prod",
  "last_evaluated": "2025-01-10T12:34:56Z",
  "data": {
    "train_size": 120000,
    "eval_size": 8000,
    "sensitive_attributes": ["gender", "age_band", "region"]
  },
  "metrics": {
    "accuracy": 0.91,
    "f1_macro": 0.88,
    "psI_drift": 0.12
  },
  "fairness": {
    "demographic_parity_difference": 0.06,
    "equal_opportunity_difference": 0.04
  },
  "risks": [
    "Higher error rate for age_band=18-25",
    "Moderately elevated drift in region=APAC"
  ],
  "mitigations": [
    "Added re-weighted loss for minority groups",
    "Quarterly fairness re-training schedule"
  ],
  "policy_summary": {
    "policy_set_id": "ai-governance-default",
    "policy_version": "1.0.0",
    "drift_status": "PASS",
    "fairness_status": "FLAG",
    "toxicity_status": "PASS"
  }
}
"""

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def load_metrics(path: Path) -> Dict[str, Any]:
  with path.open("r", encoding="utf-8") as f:
    return json.load(f)


def generate_model_card(data: Dict[str, Any]) -> str:
  model_id = data.get("model_id", "unknown-model")
  model_version = data.get("model_version", "unknown-version")
  owner = data.get("owner", "N/A")
  use_case = data.get("use_case", "N/A")
  env = data.get("environment", "N/A")
  last_eval = data.get("last_evaluated", "N/A")

  d = data.get("data", {})
  train_size = d.get("train_size", "N/A")
  eval_size = d.get("eval_size", "N/A")
  sensitive_attrs = d.get("sensitive_attributes", [])

  metrics = data.get("metrics", {})
  fairness = data.get("fairness", {})
  risks = data.get("risks", [])
  mitigations = data.get("mitigations", [])
  ps = data.get("policy_summary", {})

  lines = []
  lines.append(f"# Model Card — {model_id} ({model_version})")
  lines.append("")
  lines.append("## 1. Overview")
  lines.append("")
  lines.append(f"- **Use case:** {use_case}")
  lines.append(f"- **Owner:** {owner}")
  lines.append(f"- **Environment:** `{env}`")
  lines.append(f"- **Last evaluated:** {last_eval}")
  lines.append("")

  lines.append("## 2. Intended Use")
  lines.append("")
  lines.append("- Primary purpose: Describe the real-world decision or workflow this model supports.")
  lines.append("- Out-of-scope uses: Document uses that are explicitly disallowed.")
  lines.append("")

  lines.append("## 3. Data")
  lines.append("")
  lines.append(f"- Training set size: **{train_size}** records")
  lines.append(f"- Evaluation set size: **{eval_size}** records")
  if sensitive_attrs:
    attrs_str = ", ".join(str(a) for a in sensitive_attrs)
    lines.append(f"- Sensitive attributes monitored: **{attrs_str}**")
  lines.append("")

  if metrics:
    lines.append("## 4. Performance Metrics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    for name, value in metrics.items():
      lines.append(f"| {name} | {value} |")
    lines.append("")

  if fairness:
    lines.append("## 5. Fairness & Bias Metrics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    for name, value in fairness.items():
      lines.append(f"| {name} | {value} |")
    lines.append("")

  if ps:
    lines.append("## 6. Policy & Governance Summary")
    lines.append("")
    lines.append(f"- Policy set: **{ps.get('policy_set_id', 'N/A')}** (v{ps.get('policy_version', 'N/A')})")
    lines.append(f"- Drift status: **{ps.get('drift_status', 'N/A')}**")
    lines.append(f"- Fairness status: **{ps.get('fairness_status', 'N/A')}**")
    lines.append(f"- Toxicity status: **{ps.get('toxicity_status', 'N/A')}**")
    lines.append("")

  if risks:
    lines.append("## 7. Known Risks & Limitations")
    lines.append("")
    for r in risks:
      lines.append(f"- {r}")
    lines.append("")

  if mitigations:
    lines.append("## 8. Mitigations & Controls")
    lines.append("")
    for m in mitigations:
      lines.append(f"- {m}")
    lines.append("")

  lines.append("## 9. Change Log")
  lines.append("")
  lines.append("- Describe recent model updates, retraining, and policy changes here.")
  lines.append("")

  return "\n".join(lines)


def main() -> None:
  parser = argparse.ArgumentParser(description="Generate a Markdown model card from evaluation JSON.")
  parser.add_argument("--metrics-file", type=str, required=True, help="Path to JSON file with evaluation data.")
  parser.add_argument("--output-file", type=str, required=True, help="Path to output Markdown file.")
  args = parser.parse_args()

  metrics_path = Path(args.metrics_file)
  output_path = Path(args.output_file)

  data = load_metrics(metrics_path)
  md = generate_model_card(data)

  output_path.write_text(md, encoding="utf-8")
  print(f"Model card written to {output_path}")


if __name__ == "__main__":
  main()
