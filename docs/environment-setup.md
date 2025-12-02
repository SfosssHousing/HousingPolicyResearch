# Environment Setup and Secure Connection Guide

Use this runbook to configure a local or CI environment for the Housing Policy Research project and to verify secure, bidirectional connections across ChatGPT, Codex, Notion, GitHub, and Zotero.

## 1) Prepare the workspace

1. Install prerequisites: Node.js (LTS), Python 3.10+, Git 2.40+, and `pipx`.
2. Copy `.env.template` to `.env` (do **not** commit `.env`).
3. Add scoped tokens and IDs:
   - `OPENAI_API_KEY`, `OPENAI_ORG_ID`
   - `NOTION_TOKEN`, relevant database IDs
   - `GITHUB_PAT` or SSH key path; `GITHUB_WEBHOOK_SECRET` if webhooks are used
   - `ZOTERO_API_KEY`, `ZOTERO_LIBRARY_ID`, `ZOTERO_COLLECTION_ID`
4. Store the same keys in GitHub repository secrets for CI with identical variable names.
5. Install the Codex CLI: `npm install -g @openai/codex` (or `npx @openai/codex`).

## 2) Connection tests (forward paths)

Run these once secrets are populated:

| System | Command | Success signal | Log target |
| --- | --- | --- | --- |
| ChatGPT API | `curl https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"` | HTTP 200 + model list | `logs/connection-checks/YYYY-MM-DD_chatgpt.md` |
| Codex CLI | `codex --version` | Version printed | Same log as ChatGPT |
| Notion | `python scripts/notion_ping.py` | HTTP 200 for target database | `logs/connection-checks/YYYY-MM-DD_notion.md` |
| GitHub | `gh api user` **or** `curl https://api.github.com/user -H "Authorization: token $GITHUB_PAT"` | Authenticated user JSON | `logs/connection-checks/YYYY-MM-DD_github.md` |
| Zotero | `python scripts/zotero_ping.py` | Library metadata returned | `logs/connection-checks/YYYY-MM-DD_zotero.md` |

## 3) Reverse-flow validation

Confirm data can flow back into GitHub or across systems while respecting security controls:

- **GitHub → Notion**: Trigger the `notion-sync.yml` workflow; verify the corresponding Notion database updates within 5 minutes and shows the latest commit metadata.
- **Notion → Zotero**: Export a curated view via the Notion API and ingest it with the Zotero sync script; confirm new items appear with `source=notion` in Zotero.
- **Zotero → GitHub**: Run `python scripts/zotero_to_github.py --dry-run`; inspect generated markdown in `logs/zotero-exports/` for correct citations and redaction.
- **ChatGPT/Codex → GitHub**: Archive transcripts to `logs/generative/` using the metadata template; ensure related issues link back to the archive.

For each reverse-flow run, record timestamps, inputs, and sanitized outputs in `logs/connection-checks/`.

## 4) Security checkpoints

- Rotate all tokens every 90 days; document rotation dates in the Capstone tracker.
- Ensure `.env` and any key files remain ignored by Git.
- Restrict PAT scopes to `repo` and `workflow`; avoid `delete_repo` and `admin` scopes.
- Review automation logs for accidental secret leakage; purge and re-issue keys if leakage is detected.
- Require reviewers for PRs that touch sync scripts or credentials.

## 5) Quick remediation steps

- **API failure**: Regenerate the token, confirm it is shared with the integration user (Notion) or has active billing (OpenAI).
- **Permission error**: Re-share Notion databases or adjust GitHub PAT scopes.
- **Network blocks**: Retry over VPN/SSO networks and confirm outbound HTTPS is allowed to the target API domains.
- **Data mismatch**: Re-run the reverse-flow script with verbose logging and attach the log to a GitHub issue for triage.

## 6) Next actions

- Schedule a weekly connection check using the commands above and capture results under `logs/connection-checks/`.
- Add CI jobs that fail builds when connection or reverse-flow checks return non-zero status codes.
- Link each archived transcript in `logs/generative/` to its originating GitHub issue and Notion page to keep provenance intact.
