# Environment Integrations and Documentation

This document captures the current integration points that support the Housing Policy Research project and provides guidance for maintaining secure, bidirectional data flows between ChatGPT, Codex-based automations, Notion, GitHub, and Zotero.

## 1. System Overview

| Platform | Purpose | Direction of Sync | Primary Artifacts |
| --- | --- | --- | --- |
| ChatGPT / OpenAI workspace | Conversational research assistance, code review, and task planning | ChatGPT → GitHub, GitHub → ChatGPT (through prompts) | Task instructions, generated analyses |
| Codex automations | Scripted agents that perform file moves, commit updates, or generate analyses | Codex ↔ GitHub | Automation scripts, commit messages |
| Notion workspace | Project management, literature summaries, meeting notes | Notion ↔ GitHub (manual exports or API scripts) | Kanban boards, research briefs |
| GitHub repository | Source of truth for datasets, documentation, scripts | GitHub ↔ All | Code, data, documentation |
| Zotero group library | Reference manager with citation metadata | Zotero → Notion / GitHub (via exports) | Bibliographies, PDF annotations |

## 2. Secure Connection Checklist

1. **Account hygiene**
   - Enable multi-factor authentication on GitHub, Notion, and Zotero accounts.
   - Rotate OpenAI API keys and store them in an encrypted vault (e.g., 1Password, Bitwarden).
2. **Network boundaries**
   - Restrict API access by IP where possible (GitHub PATs, Notion integrations).
   - Use SSH for Git operations; add keys with passphrases and review authorized_keys quarterly.
3. **Secret management**
   - Store shared secrets in GitHub Actions as encrypted secrets; never commit plaintext tokens.
   - For local development, place credentials in `.env` files excluded by `.gitignore`.
4. **Audit logging**
   - Enable GitHub organization audit log exports.
   - Subscribe to Notion integration access logs and Zotero API usage summaries.

## 3. Integration Setup Steps

### 3.1 ChatGPT / Codex → GitHub

1. Clone this repository locally and create a dedicated OpenAI API key for automation scripts.
2. Configure the provided automation script (see [`scripts/cross-chat-sync.sh`](../scripts/cross-chat-sync.sh)) with the correct source and target directories.
3. Use GitHub Personal Access Tokens (PAT) with the minimum scopes required (`repo`, `workflow` if Actions are used).
4. Run automations inside a hardened environment (container or VM) with read/write access only to the repository workspace.

### 3.2 GitHub ↔ Notion

1. Create a Notion integration and invite it to the workspace pages required for synchronization.
2. Use a sync tool (e.g., Notion2Git, custom Python script) to export Notion databases as Markdown into the `docs/notion-sync/` directory.
3. Schedule weekly sync jobs and review diffs before merging into the default branch.

### 3.3 Zotero → GitHub / Notion

1. Install the Zotero Better BibTeX plugin to generate citation keys.
2. Export collections as `.bib` files into `references/` and commit alongside datasets for reproducibility.
3. Configure Notion with the Zotero API token to embed bibliography entries in project dashboards.

## 4. Error Corrections and Gaps Filled

- **Missing documentation**: Added this document to capture integration requirements and security expectations.
- **Automation path validation**: Confirmed that automation scripts should reside under `scripts/`; ensure directory exists and is referenced consistently (see follow-up task list).
- **Alias artifacts**: The repository currently contains a macOS alias file (`Capstone alias`). Confirm need; replace with platform-neutral documentation or remove if obsolete.

## 5. Task Breakdown for Next Steps

1. **Documentation hardening**
   - [ ] Expand `README.md` with a quick-start section linking to this guide.
   - [ ] Create architecture diagram illustrating data flows (store under `docs/diagrams/`).
2. **Automation stabilization**
   - [ ] Add CI workflow to lint and test shell scripts (e.g., `shellcheck`).
   - [ ] Parameterize source/target paths in automation scripts via environment variables.
3. **Integration validation**
   - [ ] Implement a health-check script that verifies access to Notion, Zotero, and GitHub APIs.
   - [ ] Document fallback procedures for API outages.
4. **Security follow-up**
   - [ ] Schedule quarterly credential rotation reminders in Notion.
   - [ ] Review GitHub branch protection rules and enable required reviews for `main`.

## 6. Maintenance Cadence

| Activity | Frequency | Owner | Notes |
| --- | --- | --- | --- |
| Documentation review | Quarterly | Project lead | Ensure integration steps reflect tooling changes. |
| Secret rotation | Quarterly or upon staff change | Security POC | Track via Notion task board. |
| Automation script audit | Bi-annually | Engineering support | Run `shellcheck` and update dependencies. |
| Bibliography sync | Monthly | Research analyst | Export from Zotero and commit updates. |

---

_Last updated: 2025-09-25_
