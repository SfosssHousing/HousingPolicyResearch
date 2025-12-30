# Housing Policy Research Environment Setup

This document records the current understanding of the tools that support the Housing Policy Research project and describes how to configure them securely.

## Goals

- Maintain a reproducible research workspace for the project repository.
- Connect writing and analysis tools (ChatGPT/Codex, Notion, GitHub, and Zotero) while keeping API credentials and personal data secure.
- Provide guidance for validating the links between systems.

## Repository Preparation (GitHub)

1. **Clone the repository**

   ```bash
   git clone git@github.com:<ORG>/HousingPolicyResearch.git
   cd HousingPolicyResearch
   ```

   Replace `<ORG>` with the organization or user namespace that hosts the repository.

1. **Create a Python environment (recommended)**
   If analysis notebooks or scripts are added later, create an isolated Python environment so dependencies do not conflict with global packages.

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   ```

1. **Install tooling dependencies**

   - `pre-commit` (for linting/formatting hooks) – `pip install pre-commit`
   - `mkdocs` (for Markdown-based documentation) – `pip install mkdocs`
   - `sphinx` (for reStructuredText-based documentation) – `pip install sphinx`\
     *(Install only one, as needed, if documentation will be generated.)*

1. **Configure Git hooks**

   ```bash
   pre-commit install
   ```

   Hooks help enforce code quality checks before commits are pushed.

## ChatGPT / Codex Integration

| Task               | Recommended Action                                                                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication     | Generate an OpenAI API key from https://platform.openai.com/account/api-keys. Store it in a secrets manager or in your shell profile as `OPENAI_API_KEY`.                                   |
| Secure Storage     | Use environment variables or encrypted secrets (`gh secret set`)—never commit keys to the repository.                                                                                       |
| Access             | Ensure the repository has a `.gitignore` file that blocks `.env` or credential files. If it does not exist, create one as shown below.                                                      |
| Reverse Connection | If the project requires feedback from ChatGPT to GitHub, use scripts or GitHub Actions that call the OpenAI API with stored secrets. Log responses in Markdown files committed to the repo. |

**Sample `.gitignore` for sensitive files:**

```gitignore
# Python virtual environments
.venv/
venv/

# Environment variable files
.env
.env.*

# API keys and credentials
*.key
*.pem

# macOS and system files
.DS_Store
## Notion Workspace

1. **Create an integration** in Notion via **Settings & Members → Integrations → Develop your own integrations**.
2. **Store the Notion secret** in a password manager or GitHub secret such as `NOTION_API_KEY`.
3. **Share target pages or databases** with the integration to grant access.
4. **Automate sync**
   - Use a scheduled script (Python + `notion-client`) or an automation service (Zapier/Make) to push updates from GitHub documentation into Notion.
   - For reverse sync (Notion → GitHub), export structured data (Markdown/CSV) and commit changes via a bot account or GitHub Action.
5. **Security checklist**
   - Rotate the integration token quarterly.
   - Limit page/database sharing to only what the integration needs.

## Zotero Library

1. Install the [Zotero desktop application](https://www.zotero.org/).
2. Create a private group library for the project.
3. Generate an API key from **Settings → Feeds/API** with read/write permissions for the project group only.
4. Use the `pyzotero` library (Python) or the Zotero web API to export bibliographies into this repository (for example, `docs/references.bib`).
5. Store the key securely and rotate annually. Do not commit the key.

## Automation and Continuous Integration

- **GitHub Actions:** Use repository secrets (`Settings → Secrets and variables → Actions`) for API keys. Reference them in workflow files using `${{ secrets.OPENAI_API_KEY }}` etc.
- **Local scripts:** Read secrets from environment variables or encrypted `.env` files (`dotenv` library) excluded by `.gitignore`.
- **Validation:** After configuration, run lightweight scripts to confirm each integration can authenticate and exchange data. Create a new file at `docs/integration-status.md` (if it does not exist) and log the results there.

## Troubleshooting and Error Correction

| Issue | Resolution Steps |
| ----- | ---------------- |
| Missing API keys | Generate new keys and update your secrets manager and GitHub Actions secrets. |
| Unauthorized errors | Ensure the integration has access to the correct Notion pages or Zotero libraries. |
| Sync conflicts | Adopt a single source of truth per content type (e.g., Zotero for citations, GitHub for documentation) and automate one-way exports with manual review for the reverse direction. |

## Documentation Maintenance

- Update this document whenever new tools are added or access procedures change.
- Document any scripts used to push/pull data between systems.
- Track secret rotation dates in a secure, shared password manager.

## Validation Checklist

- [ ] All API keys stored outside of the repository.
- [ ] GitHub Actions secrets configured for OpenAI, Notion, and Zotero.
- [ ] Automated tests or scripts confirm that read/write operations succeed for each integration.
- [ ] README links to this document.
- [ ] Next steps documented in `docs/project-roadmap.md`.

```
