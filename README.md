# Housing Policy Research

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
  - `STYLE-APA.md` – Citation standards based on APA 7th edition
  - `resources-index.md` – Comprehensive catalog of research sources with annotations
  - `resources.csv` – Machine-readable resource database for automation
  - `generative-output-version-control.md` – Tracking and verification of AI-generated content
- `SECURITY.md` – Security policy and responsible disclosure instructions.
- `capstone/` – Structured capstone documentation that replaces the legacy `Capstone alias` export.
- `comments/` – Project discussion artifacts and proposals.

## Contributing

1. Fork or clone the repository.
2. Create feature branches for substantive changes.
3. Open pull requests with detailed descriptions and link to relevant tasks or Notion pages.
4. Run documentation linters and unit tests before submitting changes.

For additional context on automation scripts, secret management, and cross-platform workflows, see [docs/integration-plan.md](docs/integration-plan.md) and the capstone notes in [`capstone/`](capstone/README.md).

## Resources and Citations

The project maintains a rigorous research database with APA-style citations:

- **[Resources Index](docs/resources-index.md)** – Comprehensive catalog of all research sources, technical documentation, and datasets with annotations
- **[Resources CSV](docs/resources.csv)** – Machine-readable database for automated bibliography generation and cross-referencing
- **[APA Style Guide](docs/STYLE-APA.md)** – House citation standards based on APA 7th edition, tailored for housing policy research
- **[Generative Output Tracking](docs/generative-output-version-control.md)** – Version control and verification system for AI-generated documentation

When citing sources in project documentation, refer to the [APA Style Guide](docs/STYLE-APA.md) for formatting requirements. All new resources should be added to both the [Resources Index](docs/resources-index.md) and [Resources CSV](docs/resources.csv).
