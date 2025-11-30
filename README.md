# Housing Policy Research

This repository hosts documentation and tooling for collaborative research on housing policy. Use the resources below to set up a secure, reproducible environment and coordinate work across supporting platforms.

## Getting Started

1. Clone the repository and create a local development environment (see [Environment Setup](docs/environment-setup.md)).
2. Review the [Project Roadmap](docs/project-roadmap.md) for outstanding tasks.
3. Read the [Repository Rulesets and Integration Controls](docs/rulesets.md) for security and connectivity requirements.
4. Use GitHub issues to track progress and link commits to roadmap items.

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
