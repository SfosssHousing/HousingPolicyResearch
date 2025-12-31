# Evaluation Framework for Policy Proposal Generator

This folder contains a minimal evaluation framework to exercise and measure the outputs
from `scripts/generate_policy_proposal.py` (or direct OpenAI calls).

Files:
- `evaluate_policy_proposal.py`: runner that sends prompts to OpenAI, stores outputs, and computes simple metrics.
- `sample_prompts.json`: example prompt variations used by the runner.
- `requirements.txt`: minimal Python dependencies for the evaluation runner.

Quick start (zsh):
1. Create a Python environment and install deps:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r evaluation/requirements.txt
```
2. Set `OPENAI_API_KEY` in your environment (the script will refuse to run without it):
```bash
export OPENAI_API_KEY="sk-..."
python evaluation/evaluate_policy_proposal.py --runs 3
```

Outputs:
- `evaluation/results/`: markdown files for each model response.
- `evaluation/report.json`: summary metrics across runs.

Notes:
- The runner is conservative by default and will not post to Notion.
- It performs simple, interpretable metrics: length, presence of required sections, and keyword coverage.
