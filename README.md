# Housing Policy Research

This repository centralizes documentation, tooling plans, and integration guidelines for the Housing Policy Research project.

## Quick Start

1. Review the [Environment Integration and Documentation Plan](docs/integration-plan.md) for platform-specific setup steps.
2. Install the Codex CLI (requires Node.js):
   ```bash
   npm install -g @openai/codex
   ```
3. Configure your local `.env` file with scoped tokens for ChatGPT, Notion, GitHub, and Zotero.
4. Use GitHub Issues or Projects to track automation scripts and data synchronization tasks described in the plan.

## Repository Structure

- `docs/` – Integration architecture, security controls, and task breakdown.
- `SECURITY.md` – Security policy and responsible disclosure instructions.
- `capstone/` – Structured capstone documentation that replaces the legacy `Capstone alias` export.

> **Note:** Some directories are placeholders that will be populated as the integrations described in the documentation are implemented.

1. Fork or clone the repository.
2. Create feature branches for substantive changes.
3. Open pull requests with detailed descriptions and link to relevant tasks or Notion pages.
4. Run documentation linters and unit tests before submitting changes.

For additional context on automation scripts, secret management, and cross-platform workflows, see [docs/integration-plan.md](docs/integration-plan.md) and the capstone notes in [`capstone/`](capstone/README.md).
