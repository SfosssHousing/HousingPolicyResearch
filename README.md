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

## Quick Start

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
- `SECURITY.md` – Security policy and responsible disclosure instructions.
- `capstone/` – Structured capstone documentation that replaces the legacy `Capstone alias` export.

## Contributing

1. Fork or clone the repository.
2. Create feature branches for substantive changes.
3. Open pull requests with detailed descriptions and link to relevant tasks or Notion pages.
4. Run documentation linters and unit tests before submitting changes.

For additional context on automation scripts, secret management, and cross-platform workflows, see [docs/integration-plan.md](docs/integration-plan.md) and the capstone notes in [`capstone/`](capstone/README.md).
