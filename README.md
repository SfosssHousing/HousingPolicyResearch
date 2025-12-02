# Housing Policy Research

This repository hosts documentation and tooling for collaborative research on housing policy. Use the resources below to set up a secure, reproducible environment and coordinate work across supporting platforms.

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/SfosssHousing/HousingPolicyResearch.git
cd HousingPolicyResearch

# 2. Run the setup script
./setup.sh

# 3. Configure your environment variables
cp .env.template .env
# Edit .env and add your API keys

# 4. Activate the virtual environment
source .venv/bin/activate

# 5. Validate connections
python scripts/validate_connections.py
```

## Getting Started

1. Follow the Quick Start steps above to set up your development environment
2. Review the [Environment Setup Guide](docs/environment-setup.md) for detailed configuration
3. Read the [Project Roadmap](docs/project-roadmap.md) for current priorities
4. Check the [Repository Rulesets](docs/rulesets.md) for security and integration requirements
5. Use GitHub issues to track progress and link commits to roadmap items

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

## Directory Structure

```
HousingPolicyResearch/
├── .github/            # GitHub Actions workflows
├── artifacts/          # Generated policy proposals and outputs
├── capstone/           # Capstone project documentation
├── docs/               # Main documentation
│   ├── prompts/        # Reusable AI prompts
│   ├── outputs/        # AI-generated content archives
│   └── audit-notes/    # Security and compliance logs
├── evaluation/         # Policy proposal evaluation scripts
├── logs/               # Application and integration logs
├── scripts/            # Automation and integration scripts
├── .env.template       # Environment variable template
├── .gitignore          # Git exclusion rules
├── requirements.txt    # Python dependencies
└── setup.sh           # Automated setup script
```

## Development Workflow

1. **Branch**: Create a feature branch from `main`
2. **Develop**: Make changes and test locally
3. **Lint**: Run `pre-commit run --all-files` before committing
4. **Test**: Validate scripts with sample data (when tests exist)
5. **Submit**: Open a pull request with clear description
6. **Review**: Address feedback and merge when approved

## Pre-commit Hooks

This project uses pre-commit hooks to maintain code quality:

```bash
# Install hooks (done automatically by setup.sh)
pre-commit install

# Run manually on all files
pre-commit run --all-files

# Update hook versions
pre-commit autoupdate
```

## Contributing

1. Create a branch for your change
2. Make updates and add tests or documentation as needed
3. Run linting and formatting checks (`pre-commit run --all-files`)
4. Submit a pull request referencing related roadmap tasks or issues

## Support

If you encounter configuration issues or discover missing documentation, open a GitHub issue with detailed context so the team can respond quickly.
