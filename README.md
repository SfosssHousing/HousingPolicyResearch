# Housing Policy Research

This repository centralizes documentation, tooling plans, and integration guidelines for the Housing Policy Research project.

## Quick Start

1. Review the [Environment Integration and Documentation Plan](docs/integration-plan.md) for platform-specific setup steps.
2. Walk through the [Environment Readiness Checklist](docs/environment-readiness.md) to validate secrets and both connection directions before running automation.
3. Copy `.env.template` to `.env` and add the required secrets for ChatGPT, Codex, Notion, GitHub, and Zotero.
4. Install the Codex CLI (requires Node.js):
   ```bash
   npm install -g @openai/codex
   ```
5. Use GitHub Issues or Projects to track automation scripts and data synchronization tasks described in the plan.
6. For native/web clients, follow the [Universal Linking Guide](docs/universal-linking-guide.md) to keep deep links aligned with repository content.

## Repository Structure

- `docs/` – Integration architecture, security controls, universal linking guidance, and task breakdown.
- `docs/resource-index.md` – Entry point for finding documentation and archiving generative outputs.
- `SECURITY.md` – Security policy and responsible disclosure instructions.
- `capstone/` – Structured capstone documentation that replaces the legacy `Capstone alias` export.

## Contributing

1. Fork or clone the repository.
2. Create feature branches for substantive changes.
3. Open pull requests with detailed descriptions and link to relevant tasks or Notion pages.
4. Run documentation linters and unit tests before submitting changes.

For additional context on automation scripts, secret management, and cross-platform workflows, see [docs/integration-plan.md](docs/integration-plan.md) and the capstone notes in [`capstone/`](capstone/README.md).
