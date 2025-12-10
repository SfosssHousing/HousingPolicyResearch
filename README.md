# Housing Policy Research

This repository hosts documentation and tooling for collaborative research on housing policy. Use the resources below to set up a secure, reproducible environment and coordinate work across supporting platforms.

## Getting Started

1. Clone the repository and create a local development environment (see [Environment Setup](docs/environment-setup.md)).
2. Review the [Project Roadmap](docs/project-roadmap.md) for outstanding tasks.
3. Use GitHub issues to track progress and link commits to roadmap items.

## Tooling Overview

| Tool | Purpose | Notes |
| ---- | ------- | ----- |
| ChatGPT / Codex | Draft analytical memos, code snippets, and summaries. | Secure API keys via environment variables or GitHub secrets. |
| Notion | Organize meeting notes, project plans, and shared knowledge. | Configure a private integration and restrict shared pages. |
| GitHub | Version control for documentation, data scripts, and automation. | Enable branch protection and use pull requests for review. |
| Zotero | Manage research references and citations. | Maintain a dedicated group library and export bibliographies to the repo. |

## Security Practices

- Do not commit API keys or credentials to the repository.
- Store sensitive configuration values in a password manager or as GitHub Actions secrets.
- Rotate integration tokens (OpenAI, Notion, Zotero) on a regular cadence.

## Contributing

1. Create a branch for your change.
2. Make updates and add tests or documentation as needed.
3. Run any relevant checks locally (linting, formatting, unit tests).
4. Submit a pull request referencing the related roadmap tasks or issues.

## Support

If you encounter configuration issues or discover missing documentation, open a GitHub issue with detailed context so the team can respond quickly.
This repository centralizes documentation, tooling plans, and integration guidelines for the Housing Policy Research project.

## Documentation

- [Environment Integrations and Documentation](docs/environment-integrations.md): describes the end-to-end setup for secure, bidirectional connections between ChatGPT, Codex automations, Notion, GitHub, and Zotero, and outlines follow-up tasks for the project workspace.
- `SECURITY.md`: organization-wide security policies.

## Repository Structure

```
/
├── docs/                  # Project documentation and integration guides
├── scripts/               # Automation scripts for data and chat exports (planned)
├── references/            # Bibliography exports from Zotero (planned)
├── data/                  # Research datasets (planned)
├── SECURITY.md            # Security baseline for the project
└── README.md              # This overview
```
1. Review the [Environment Integration and Documentation Plan](docs/integration-plan.md) for platform-specific setup steps.
2. Copy `.env.template` to `.env` and add the required secrets for ChatGPT, Codex, Notion, GitHub, and Zotero.
3. Install the Codex CLI (requires Node.js):
   ```bash
   npm install -g @openai/codex
   ```
4. Use GitHub Issues or Projects to track automation scripts and data synchronization tasks described in the plan.
5. For native/web clients, follow the [Universal Linking Guide](docs/universal-linking-guide.md) to keep deep links aligned with repository content.

## Repository Structure

- `docs/` – Integration architecture, security controls, universal linking guidance, and task breakdown.
  - `STYLE-APA.md` – Citation standards based on APA 7th edition
  - `resources-index.md` – Comprehensive catalog of research sources with annotations
  - `resources.csv` – Machine-readable resource database for automation
  - `generative-output-version-control.md` – Tracking and verification of AI-generated content
  - `github-actions-maintenance.md` – Workflow maintenance and action version management
- `SECURITY.md` – Security policy and responsible disclosure instructions.
- `capstone/` – Structured capstone documentation that replaces the legacy `Capstone alias` export.
- `comments/` – Project discussion artifacts and proposals.

> **Note:** Some directories are placeholders that will be populated as the integrations described in the documentation are implemented.

## Getting Started

For additional context on automation scripts, secret management, and cross-platform workflows, see [docs/integration-plan.md](docs/integration-plan.md) and the capstone notes in [`capstone/`](capstone/README.md).

## Resources and Citations

The project maintains a rigorous research database with APA-style citations:

- **[Resources Index](docs/resources-index.md)** – Comprehensive catalog of all research sources, technical documentation, and datasets with annotations
- **[Resources CSV](docs/resources.csv)** – Machine-readable database for automated bibliography generation and cross-referencing
- **[APA Style Guide](docs/STYLE-APA.md)** – House citation standards based on APA 7th edition, tailored for housing policy research
- **[Generative Output Tracking](docs/generative-output-version-control.md)** – Version control and verification system for AI-generated documentation

When citing sources in project documentation, refer to the [APA Style Guide](docs/STYLE-APA.md) for formatting requirements. All new resources should be added to both the [Resources Index](docs/resources-index.md) and [Resources CSV](docs/resources.csv).
