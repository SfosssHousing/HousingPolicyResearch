# Environment Integration and Documentation Plan

This document captures the setup guidance and project tasks required to connect ChatGPT, Codex, Notion, GitHub, and Zotero securely for the Housing Policy Research environment. It also tracks reverse-connection validation so every platform exchange is auditable and repeatable.

## 1. Prerequisites

- **Node.js and npm**: Install the current LTS release from [nodejs.org](https://nodejs.org/).
- **Python 3.10+**: Required for automation scripts or API clients.
- **Package Managers**: `pipx` (Python) and `npm` (Node.js) are recommended for isolating tooling.
- **Version Control**: Git 2.40+ configured with SSH and/or HTTPS credentials.
- **Secret Storage**: Use a password manager or secret manager (e.g., 1Password, Bitwarden, GitHub Encrypted Secrets) to store API keys.

### Installing the Codex CLI

To install the Codex CLI globally once Node.js is available, run:

```bash
npm install -g @openai/codex
```

If global installs are restricted, use `npx @openai/codex` or install inside a project-specific `node_modules` directory.

## 2. Secure Connection Architecture

| System        | Purpose                                | Required Credentials                      | Storage Recommendation                |
|---------------|----------------------------------------|--------------------------------------------|---------------------------------------|
| ChatGPT (API) | Conversational automation & analysis   | OpenAI API key                             | Environment variables or secret store |
| Codex CLI     | Code generation & command assistance   | Same OpenAI API key                        | `.env` files excluded from Git        |
| Notion        | Knowledge base & documentation         | Notion integration token & database IDs    | Secret manager + local `.env` file    |
| GitHub        | Source control & Actions               | Personal access token (PAT) with minimal scopes | Git credential manager or SSH keys |
| Zotero        | Reference management                   | Zotero API key and library ID              | Secret manager + `.env` file          |

The recommended pattern is:

1. Store all secrets in a password manager.
2. Provide each developer with scoped tokens (no shared master tokens).
3. Load tokens into local development environments via `.env` files added to `.gitignore`.
4. Replicate the variables in GitHub repository secrets for CI/CD automation.

## 3. Connection Workflows

### 3.1 ChatGPT & Codex

1. Generate an OpenAI API key from the OpenAI dashboard.
2. Export the key before running CLI tools:

   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

3. Test the CLI:

   ```bash
   codex --help
   ```

4. Document standard prompts, rate limits, and logging practices in the team wiki.

**Reverse check:** Archive prompt/response pairs into `logs/chatgpt/` (or a Notion page) after each milestone so GitHub reflects AI-assisted decisions.

### 3.2 Notion Integration

1. Create a Notion internal integration and capture the secret token.
2. Share the required workspace pages or databases with the integration user.
3. Record database IDs for content synchronization (e.g., research log, literature review).
4. Configure a synchronization script (Python or Node) that reads from GitHub markdown and updates Notion blocks using the Notion API.
5. Log operations with timestamps for auditing.

### 3.3 GitHub Automation

1. Configure Git remotes over SSH for developers; use deploy keys for read-only automation if required.
2. Store PATs with minimal scopes (e.g., `repo`, `workflow`) in GitHub Secrets for Actions.
3. Create GitHub Actions workflows that:
   - Lint documentation (`markdownlint`, `vale`).
   - Sync notes to Notion or Zotero via scheduled jobs.
   - Archive prompts and outputs from ChatGPT sessions to the repo.

### 3.4 Zotero Integration

1. Generate a Zotero API key scoped to the research library.
2. Use the Zotero Web API or `pyzotero` client to fetch and push literature metadata.
3. Maintain a mapping file (e.g., `data/zotero-mapping.json`) that links Zotero items to Notion pages and GitHub issue IDs.
4. Ensure synchronization scripts respect rate limits and handle retries with exponential backoff.

## 4. Reverse Data Flows

- **ChatGPT to GitHub**: Archive finalized prompts and responses into version-controlled markdown files.
- **GitHub to Notion**: Publish documentation updates to Notion knowledge bases.
- **Notion to Zotero**: Convert curated reading lists into Zotero collections through the API.
- **Zotero to GitHub**: Export annotations into the repository for reproducibility.

Automate each pipeline with CI jobs or scheduled tasks that authenticate using stored secrets. Include logging to a secure datastore (e.g., CloudWatch, Datadog) for traceability.

### Verification Steps for Secure Connections

1. **Credential Audit** – Confirm each platform token (ChatGPT, Codex CLI, Notion, GitHub, Zotero) is present in both the local `.env` file and the GitHub Secrets store with matching scopes.
2. **Connection Tests** – Run a dry-run command or API call for every integration, capturing success logs in the repository (e.g., `logs/connection-checks/`).
3. **Reverse Flow Validation** – Execute the reverse synchronization paths (GitHub→Notion, Notion→Zotero, Zotero→GitHub) in a staging environment and review audit logs for unauthorized access attempts.
4. **Security Review** – Verify that logs exclude sensitive payloads, rotate tokens post-test, and document findings in the capstone tracker within `capstone/`.

## 5. Security Controls

- **Secret Rotation**: Rotate API keys every 90 days or immediately after role changes.
- **Least Privilege**: Scope each token to the minimal set of permissions.
- **Network Security**: Use VPN or SSO where possible; avoid running integrations from unsecured networks.
- **Audit Trails**: Maintain logs of automation runs and human access to integrations.
- **Dependency Management**: Pin versions in `package.json`/`requirements.txt` and enable Dependabot in GitHub.

## 6. Validation Checklist

- [ ] Document stored in `docs/` and linked from README.
- [ ] All `.env` examples exclude real credentials.
- [ ] GitHub repository secrets mirror local `.env` keys.
- [ ] Integration scripts provide logging and error handling.
- [ ] Backups exist for Notion databases and Zotero libraries.

## 7. Task Breakdown & Next Steps

1. **Documentation Cleanup**
   - Replace corrupted `Capstone alias` file with structured markdown or archive reference details. *(Completed: migrated to `capstone/README.md`.)*
   - Expand README with project overview and integration quick links.

2. **Secret Management Implementation**
   - Select a shared secret manager.
   - Draft `.env.template` covering ChatGPT, Codex, Notion, GitHub, and Zotero keys.

3. **Automation Scripts**
   - Prototype Node or Python scripts for each data flow (ChatGPT→GitHub, GitHub→Notion, etc.).
   - Add unit tests and linting configuration.

4. **CI/CD Integration**
   - Configure GitHub Actions workflows for linting, synchronization, and backups.
   - Add status badges to the README once pipelines are live.

5. **Security Review**
   - Conduct a quarterly review of access logs and key rotations.
   - Document incident response procedures specific to data integrations.

6. **Governance & Reporting**
   - Establish ownership for each integration and define SLAs.
   - Schedule monthly review meetings; log decisions in Notion.

7. **Reverse-Connection Validation**
   - Stand up `logs/connection-checks/` with dated subfolders for each dry run.
   - Capture ChatGPT→GitHub, GitHub→Notion, Notion→Zotero, and Zotero→GitHub test evidence and rotate keys after completion.
   - Add a short runbook in `docs/connection-check-runbook.md` describing how to re-run the checks when tokens change.

8. **Generative Output Hardening**
   - Align prompt libraries to the pattern matrix in `docs/NYC_Housing_Subsidy_Reform_Ops_Manual.md` and the report blueprint.
   - Configure evaluation harness thresholds (citation coverage, accuracy, scope adherence) and record results in Notion.
   - Tag Git commits with the report version string (`Housing_Subsidy_Reform_MASTER_v[VERSION]_[YYYYMMDD]`) for traceability.

## 8. Generative Output Roadmap

To coordinate automation and AI-assisted deliverables, track the following workstreams in GitHub Projects and reference them from the `capstone/` documentation:

1. **Prompt Library** – Curate reusable ChatGPT and Codex prompts aligned to housing policy research goals; version them in `docs/prompts/`.
2. **Evaluation Harness** – Implement scripts that score generative outputs against acceptance criteria (accuracy, citation coverage, compliance).
3. **Human-in-the-Loop Reviews** – Define reviewer roles, review cadences, and escalation paths for questionable outputs.
4. **Data Governance** – Map data sources, retention policies, and redaction requirements before automating publication workflows.
5. **Reporting Automation** – Combine data from GitHub issues, Notion databases, and Zotero annotations into scheduled briefs or dashboards.

## 9. References

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Notion API Reference](https://developers.notion.com/reference/intro)
- [GitHub Actions Security Guide](https://docs.github.com/en/actions/security-guides)
- [Zotero Web API](https://www.zotero.org/support/dev/web_api/v3/start)

