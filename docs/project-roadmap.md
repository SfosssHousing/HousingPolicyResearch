# Project Roadmap and Next Steps

This roadmap captures actionable follow-up work for the Housing Policy Research project. Update the checklist as milestones are completed.

## 0. Project Setup (Completed)

- [x] Create `.gitignore` file to exclude sensitive data and build artifacts
- [x] Add `.env.template` with required environment variables
- [x] Create consolidated `requirements.txt` for Python dependencies
- [x] Add pre-commit hooks configuration for code quality
- [x] Create automated setup script (`setup.sh`)
- [x] Add connection validation script for API integrations
- [x] Create directory structure for logs, artifacts, and documentation
- [x] Update README with quick start guide
- [x] Document setup process in environment-setup.md
- [x] Add CONTRIBUTING.md with contribution guidelines

## 1. Documentation Enhancements

- [ ] Convert the legacy `Capstone alias` document into structured Markdown (determine whether to archive or reformat).
- [ ] Populate `README.md` with a project overview, research goals, and pointers to relevant datasets.
- [ ] Draft a citation management guide linking Zotero collections to repository outputs.

## 2. Data and Analysis Pipeline

- [ ] Define the primary research questions and hypotheses in `docs/research-plan.md`.
- [ ] Inventory available datasets (HUD, ACS, local housing authorities) and document access requirements.
- [ ] Prototype an ETL workflow (e.g., Python notebooks or scripts) to normalize housing policy datasets.

## 3. Tool Integrations

- [ ] Implement a GitHub Action that syncs meeting notes from Notion to the `/notes` directory.
- [ ] Create a script or workflow to export Zotero bibliographies automatically into `docs/references.bib`.
- [ ] Establish a secure workflow for capturing ChatGPT outputs and committing summarized insights.

## 4. Quality Assurance

- [x] Add pre-commit hooks for linting Markdown and Python code (`markdownlint`, `flake8`, `black`)
- [ ] Configure continuous integration tests to run analytical notebooks or scripts when added
- [ ] Establish a data validation checklist ensuring reproducibility of published results
- [ ] Add unit tests for core scripts (generate_policy_proposal.py, evaluate_policy_proposal.py)

## 5. Governance and Security

- [ ] Document onboarding/offboarding steps for collaborators, including GitHub access levels.
- [ ] Set up a secrets rotation calendar for OpenAI, Notion, and Zotero integrations.
- [ ] Draft an incident response plan for data or credential exposure.

---

**Last updated:** 2025-12-02

## Next Immediate Steps

1. **Configure GitHub Secrets**: Add `OPENAI_API_KEY`, `NOTION_API_KEY`, and `ZOTERO_API_KEY` to repository secrets
2. **Test Automated Workflows**: Verify GitHub Actions workflows run successfully with configured secrets
3. **Begin Data Analysis**: Start prototyping ETL workflows for housing policy datasets
4. **Populate Prompts Library**: Document reusable ChatGPT/Codex prompts in `docs/prompts/`
