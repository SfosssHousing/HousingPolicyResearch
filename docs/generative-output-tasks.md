# Generative Output Task Breakdown

This runbook expands on Section 9 of `docs/integration-plan.md` and captures the actionable steps required to operationalize generative AI deliverables for the Housing Policy Research initiative.

## 1. Prompt Library

1. Create `docs/prompts/` with subfolders per research theme (e.g., zoning, affordability).
2. Standardize frontmatter fields: `title`, `objective`, `model`, `temperature`, `reviewer`.
3. Build a `scripts/prompt_validator.py` utility that lints YAML frontmatter and verifies citations.
4. Automate publishing to Notion using the Notion sync workflow described in `docs/connection-checks.md`.

## 2. Evaluation Harness

1. Define acceptance criteria in `docs/evaluation-matrix.md` (accuracy, citations, compliance).
2. Implement scoring scripts:
   - **Python**: `scripts/evaluate_outputs.py` to parse transcripts/logs and compute metrics.
   - **Node.js**: optional CLI for integration with Codex prompts.
3. Store evaluation reports in `reports/generative/` with timestamps.
4. Gate merges by running the evaluation harness inside GitHub Actions.

## 3. Human-in-the-Loop Reviews

1. Configure a Notion database for reviews with fields: `Output Link`, `Reviewer`, `Status`, `Risks`.
2. Update GitHub issue templates to include a "Review required" checkbox.
3. Add an automation that comments on PRs when reviews are overdue, pulling data from Notion.
4. Document escalation paths in `docs/governance.md`.

## 4. Data Governance

1. Inventory all datasets referenced in prompts and note sensitivity levels.
2. Tag files in GitHub with `data-classification` labels (e.g., `restricted`, `public`).
3. Update `.gitattributes` to block large or restricted files from being pushed without approval.
4. Mirror retention policies in Notion and Zotero notes, referencing ticket IDs for traceability.

## 5. Reporting Automation

1. Combine GitHub issue metrics, Notion task status, and Zotero citation counts via scheduled workflows.
2. Generate a weekly markdown brief in `reports/status/` and post a summary to Notion.
3. Provide universal links (see `docs/universal-linking-guide.md`) in the brief so mobile users can open sections directly.
4. Archive the generated briefs via ChatGPT/Codex logging to maintain provenance.

## 6. Implementation Tracker

Use GitHub Projects or Issues to track the above workstreams. For each item, include:

- Definition of done.
- Owner and due date.
- Linked automation scripts and datasets.
- Security review checklist reference.

## 7. Immediate Readiness Actions

Use these concrete steps to unblock the next generative deliverables:

1. Run the Raycast extension using `ray run .` to bypass TypeScript React type conflicts; capture build notes in `docs/logs/raycast-build.md`.
2. Install Quarto with APA support (`quarto add wjschne/apaquarto`) and update the policy brief and bill-drafting templates with current project metadata.
3. Populate `00_admin/settings.yaml` with API endpoints and keys (kept out of Git) so ChatGPT/Codex prompts can reach the backend.
4. Export the **Add Source**, **Draft Section**, and **Bill Sweep** Shortcuts into a new `shortcuts/` folder to document triggers and data flows.
5. Record validation results for ChatGPT/Codex, Notion, GitHub, and Zotero connections in `logs/connection-checks/` to prove round-trip sync works before publishing generated outputs.

Following this breakdown keeps the generative AI roadmap transparent and tightly integrated with the repository's security and automation controls.
