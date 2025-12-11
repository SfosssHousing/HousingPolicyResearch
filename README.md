# Housing Policy Research

This repository houses automation scripts, documentation, and datasets that support housing policy analysis projects. The workspace integrates with several external services (ChatGPT, Codex-based automations, Notion, GitHub, and Zotero) to manage research workflows and bibliographic data.

## Documentation

- [Environment Integrations and Documentation](docs/environment-integrations.md): describes the end-to-end setup for secure, bidirectional connections between ChatGPT, Codex automations, Notion, GitHub, and Zotero, and outlines follow-up tasks for the project workspace.
- `SECURITY.md`: organization-wide security policies.

## Repository Structure

```
/
├── .devcontainer/         # Development container configuration
├── .github/               # GitHub workflows and configuration
│   └── workflows/         # CI/CD workflow definitions
├── Capstone/              # Automation target directory
│   └── indexes/           # Cross-chat CSV exports and data indexes
├── capstone/              # Capstone project documentation
├── comments/              # Issue comments and discussion archives
├── data/                  # Research datasets (planned)
├── docs/                  # Project documentation and integration guides
├── references/            # Bibliography exports from Zotero (planned)
├── scripts/               # Automation scripts for data and chat exports
├── SECURITY.md            # Security baseline for the project
└── README.md              # This overview
```

> **Note:** Some directories are placeholders that will be populated as the integrations described in the documentation are implemented.

## Getting Started

1. Clone the repository and review the [integration guide](docs/environment-integrations.md) to configure secure connections between external platforms.
2. Set up local environment variables and secret storage before running any automation scripts.
3. Use feature branches and pull requests to contribute changes, following the task breakdown identified in the documentation.

## Support

For questions or support requests, open an issue in this repository with the relevant context and links to Notion or Zotero resources when appropriate.
