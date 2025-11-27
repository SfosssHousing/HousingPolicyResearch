#!/usr/bin/env python3
"""Evaluation runner for the policy proposal generator.

Sends a set of prompts to OpenAI, saves responses, and computes simple metrics.
"""
import argparse
import json
import os
import sys
from datetime import datetime
import re
import textwrap

try:
    # Prefer the new OpenAI client (openai>=1.0.0)
    from openai import OpenAI
    _OPENAI_NEW = True
except Exception:
    try:
        import openai  # type: ignore
        _OPENAI_NEW = False
    except Exception:
        print("Missing dependency 'openai'. Install with: pip install -r evaluation/requirements.txt")
        raise


REQUIRED_SECTIONS = [
    "Title",
    "Executive summary",
    "Background",
    "Proposed policy actions",
    "Estimated fiscal impact",
    "Implementation timeline",
    "Metrics to track success",
]


def load_prompts(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def call_openai(prompt, model="gpt-3.5-turbo", max_tokens=1600, temperature=0.6):
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("OPENAI_API_KEY not set. Set it and retry.")
        sys.exit(2)

    # Use new client if available
    if globals().get("_OPENAI_NEW"):
        client = OpenAI(api_key=key)
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        # New client returns objects; access the first choice
        try:
            return resp.choices[0].message.content.strip()
        except Exception:
            # fallback to possible dict-like structure
            return str(resp)
    else:
        # older openai package
        openai.api_key = key
        resp = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return resp["choices"][0]["message"]["content"].strip()


def mock_response(prompt: str) -> str:
    """Generate a deterministic mock response given a prompt (for CI/demo)."""
    title = "Sample Policy Proposal (Mock)"
    exec_sum = (
        "Executive summary: This mock proposal summarizes key actions to improve subsidy efficiency "
        "and equity in New York City."
    )
    background = "- Fragmented delivery systems\n- Administrative burden on applicants\n- Uneven access across communities"
    actions = "1. Standardize eligibility checks across agencies.\n2. Build a shared subsidy registry.\n3. Pilot targeted outreach in underserved neighborhoods."
    fiscal = "Estimated fiscal impact: $10M-$50M over 2 years (mock estimate)."
    timeline = "Q1: design; Q2: pilot; Q3-Q4: scale; Year 2: evaluation and refinement."
    metrics = "Metrics to track success: coverage rate, application processing time, disparity reduction."

    parts = [f"Title: {title}", "", exec_sum, "", "Background:", background, "", "Proposed policy actions:", actions, "", fiscal, "", "Implementation timeline:", timeline, "", "Metrics to track success:", metrics]
    return "\n".join(parts)


def analyze_text(text):
    metrics = {}
    metrics["word_count"] = len(text.split())
    # Check for presence of key headings by simple regex (case-insensitive)
    lower = text.lower()
    for sec in REQUIRED_SECTIONS:
        key = sec.lower()
        metrics[f"has_{key.replace(' ', '_')}"] = bool(re.search(rf"{re.escape(key)}", lower))
    # simple keyword coverage
    keywords = ["equity", "subsidy", "eligibility", "data", "timeline", "cost", "implementation"]
    for kw in keywords:
        metrics[f"kw_{kw}"] = lower.count(kw)
    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompts", default="evaluation/sample_prompts.json")
    parser.add_argument("--runs", type=int, default=1, help="How many times to run each prompt")
    parser.add_argument("--outdir", default="evaluation/results")
    args = parser.parse_args()

    prompts = load_prompts(args.prompts)
    if not prompts:
        print("No prompts found. Create evaluation/sample_prompts.json or pass --prompts.")
        sys.exit(1)

    os.makedirs(args.outdir, exist_ok=True)
    report = {"runs": [], "summary": {}}

    for p in prompts:
        name = p.get("name", "prompt")
        text = p.get("prompt")
        for i in range(args.runs):
            timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
            if args.mock:
                out = mock_response(text)
            else:
                try:
                    out = call_openai(text)
                except Exception as e:
                    print(f"OpenAI call failed for prompt {name}: {e}")
                    out = f"ERROR: {e}"

            filename = f"{name}_{i+1}_{timestamp}.md"
            filepath = os.path.join(args.outdir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Prompt: {name}\n\n")
                f.write(textwrap.dedent(text) + "\n\n")
                f.write("---\n\n")
                f.write(out)

            metrics = analyze_text(out)
            run_entry = {
                "prompt_name": name,
                "run_index": i + 1,
                "filename": filepath,
                "metrics": metrics,
            }
            report["runs"].append(run_entry)
            print(f"Saved run: {filepath} (words: {metrics['word_count']})")

    # Summarize simple aggregates
    total_runs = len(report["runs"])
    summary = {"total_runs": total_runs}
    # compute average word count
    if total_runs:
        avg_words = sum(r["metrics"]["word_count"] for r in report["runs"]) / total_runs
        summary["avg_word_count"] = avg_words
    report["summary"] = summary

    report_path = os.path.join("evaluation", "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Wrote report to {report_path}")

    # Also write a short human-readable summary
    summary_lines = ["# Evaluation Summary", "", f"Total runs: {summary.get('total_runs', 0)}", "", f"Average word count: {summary.get('avg_word_count', 0):.1f}", "", "## Runs"]
    for r in report["runs"]:
        summary_lines.append(f"- {os.path.basename(r['filename'])}: words={r['metrics']['word_count']}")

    summary_path = os.path.join("evaluation", "summary.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    print(f"Wrote summary to {summary_path}")


if __name__ == "__main__":
    main()
