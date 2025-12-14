# Contributing to Housing Policy Research

Thank you for your interest in contributing to the Housing Policy Research project! This document provides guidelines for contributing to the repository.

## Getting Started

1. **Read the documentation:**
   - Review the [README](README.md) for project overview
   - Check the [Project Roadmap](docs/project-roadmap.md) for planned work
   - Familiarize yourself with our [APA Style Guide](docs/STYLE-APA.md) for citations

2. **Set up your environment:**
   - Clone the repository
   - Copy `.env.template` to `.env` and configure as needed
   - Follow the [Environment Setup Guide](docs/environment-setup.md)

3. **Check existing issues:**
   - Search for related issues before creating new ones
   - Comment on issues you'd like to work on
   - Use issue templates for consistency

## How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Documentation improvements** – Fix typos, clarify instructions, add examples
- **Research sources** – Add new citations or update existing ones
- **Integration enhancements** – Improve API configurations or automation
- **Security updates** – Report or fix security issues
- **Bug fixes** – Address errors or inconsistencies

### Contribution Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/descriptive-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make focused changes:**
   - Keep changes minimal and related to a single issue
   - Follow existing code and documentation patterns
   - Update related documentation

3. **Test your changes:**
   - Verify links work correctly
   - Test any code or scripts locally
   - Validate citation formatting
   - Ensure no secrets are committed

4. **Commit with clear messages:**
   ```bash
   git commit -m "docs: add citation for housing affordability study"
   git commit -m "fix: correct broken link in integration guide"
   git commit -m "feat: add Notion API configuration example"
   ```

5. **Submit a pull request:**
   - Use the PR template (auto-populated)
   - Reference related issues
   - Provide clear description of changes
   - Complete all relevant checklist items

## Citation and Research Standards

### Adding Research Sources

When contributing research sources, you **must**:

1. **Follow APA 7th edition format** (see [STYLE-APA.md](docs/STYLE-APA.md))
2. **Update both locations:**
   - `docs/resources-index.md` – Full citation with annotations
   - `docs/resources.csv` – Machine-readable entry
3. **Include required fields:**
   - Complete citation metadata (author, date, title, source, DOI/URL)
   - Relevance statement (why it matters)
   - Application note (how it supports research)
   - Quality flags (`[Primary source]`, `[Paywalled]`, etc.)
4. **Verify accessibility:**
   - Test all URLs and DOI links
   - Note paywalled or restricted access
   - Confirm metadata against original source

### Example Citation Entry

**In `docs/resources-index.md`:**
```markdown
### Housing Affordability

Schuetz, J. (2020). Is zoning a useful tool or a regulatory barrier? Evidence from recent research. *Cityscape: A Journal of Policy Development and Research, 22*(1), 93-110. https://doi.org/10.2139/ssrn.3522864

**Relevance:** Synthesizes recent empirical evidence on how zoning regulations affect housing supply and affordability.

**Application:** Supports policy analysis of zoning reform proposals and their potential impacts.

**Quality:** [Primary source] Peer-reviewed research synthesis published in HUD journal.
```

**In `docs/resources.csv`:**
```csv
Schuetz (2020),Is zoning a useful tool or a regulatory barrier?,2020,Cityscape,https://doi.org/10.2139/ssrn.3522864,Zoning;Affordability,[Primary source]
```

## Security Guidelines

### Prohibited Actions

❌ **Never commit:**
- API keys or tokens
- Passwords or credentials
- Private/sensitive data
- Personal information
- Production secrets

✅ **Always:**
- Use environment variables (`.env` file)
- Store secrets in password managers
- Follow least-privilege principle
- Review `SECURITY.md` before integrations
- Test with development/sandbox credentials

### Reporting Security Issues

For security vulnerabilities:
1. **Serious issues:** Use [private security reporting](https://github.com/SfosssHousing/HousingPolicyResearch/security/advisories/new)
2. **Minor concerns:** Create an issue with `[SECURITY]` tag
3. **General questions:** Review `SECURITY.md` first

## Documentation Standards

### Style Guidelines

- **Clear and concise** – Use bullet points, headings, and tables
- **Actionable** – Start with imperative verbs ("Use", "Configure", "Add")
- **Examples included** – Provide code snippets or citation samples
- **Links verified** – Test all internal and external links
- **Dates tracked** – Include "Last updated" dates where appropriate

### Markdown Conventions

- Use ATX-style headers (`#` not underlines)
- Use fenced code blocks with language identifiers
- Use relative links for internal documentation
- Use absolute URLs for external resources
- Include alt text for images

## Pull Request Guidelines

### Before Submitting

- [ ] All changes are focused and minimal
- [ ] Related documentation updated
- [ ] Links tested and working
- [ ] No secrets or sensitive data committed
- [ ] `.env` files remain gitignored
- [ ] Citations follow APA format (if applicable)
- [ ] PR template checklist completed

### Review Process

1. **Automated checks:** CodeQL and other workflows must pass
2. **Documentation review:** Clarity, accuracy, completeness
3. **Citation verification:** Format, links, metadata (if applicable)
4. **Security review:** No exposed secrets or vulnerabilities

### After Approval

- Squash commits if requested
- Update PR description if changes made during review
- Address all review comments before merge

## Common Tasks

### Update Integration Documentation

1. Review current state in `docs/integration-plan.md`
2. Document API versions, endpoints, authentication
3. Add working code examples
4. Update security notes
5. Test instructions actually work

### Fix Documentation Issues

1. Identify the problem clearly
2. Propose specific improvements
3. Update related cross-references
4. Verify all links still work
5. Update "Last modified" date

### Add Research Source

1. Use the [Research Source issue template](.github/ISSUE_TEMPLATE/research-source.md)
2. Gather complete citation information
3. Format in APA 7th edition
4. Add to both `resources-index.md` and `resources.csv`
5. Include annotations and quality flags

## Questions and Support

- **General questions:** Open a [GitHub Discussion](https://github.com/SfosssHousing/HousingPolicyResearch/discussions)
- **Bug reports:** Create an issue with relevant template
- **Documentation issues:** Use the [documentation template](.github/ISSUE_TEMPLATE/documentation.md)
- **Security concerns:** Follow [SECURITY.md](SECURITY.md) guidelines

## Code of Conduct

### Expected Behavior

- Be respectful and professional
- Welcome diverse perspectives
- Focus on constructive feedback
- Assume good intentions
- Keep discussions on-topic

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or insults
- Disruptive or trolling behavior
- Sharing others' private information
- Other unprofessional conduct

## License and Attribution

By contributing to this repository, you agree that your contributions will be licensed under the same license as the project (see repository settings).

When using AI tools (ChatGPT, Copilot, etc.) for contributions:
- Review and verify all AI-generated content
- Ensure factual accuracy and citation validity
- Follow [generative output guidelines](docs/generative-output-version-control.md)
- Take responsibility for the final submission

## Additional Resources

- [Environment Setup Guide](docs/environment-setup.md)
- [Integration Plan](docs/integration-plan.md)
- [APA Style Guide](docs/STYLE-APA.md)
- [Resources Index](docs/resources-index.md)
- [Universal Linking Guide](docs/universal-linking-guide.md)
- [Generative Output Tracking](docs/generative-output-version-control.md)

---

**Questions?** Open an issue or start a discussion. We're here to help!
