# Housing Policy Research - Copilot Instructions

## Project Overview

This repository hosts documentation, resource management tools, and integration guidelines for collaborative housing policy research. The project focuses on evidence-based policy analysis with rigorous citation standards, secure API integrations (ChatGPT, Notion, Zotero, GitHub), and reproducible research workflows. Primary audience includes housing policy researchers, data analysts, and documentation specialists.

## Repository Structure

- `docs/` – Research documentation, style guides, integration architecture, and resource catalogs
  - `STYLE-APA.md` – APA 7th edition citation standards (mandatory for all research sources)
  - `resources-index.md` – Comprehensive catalog of research sources with annotations
  - `resources.csv` – Machine-readable resource database for automation
  - `generative-output-version-control.md` – Tracking and verification of AI-generated content
- `.github/agents/` – Custom agent configurations for specialized automation tasks (do not modify these files unless explicitly required by an issue)
- `capstone/` – Structured capstone documentation
- `comments/` – Project discussion artifacts and proposals
- `SECURITY.md` – Security policy and responsible disclosure instructions

## Technology Stack

- **Documentation:** Markdown (GitHub-flavored)
- **Citations:** APA 7th edition (strictly enforced)
- **Integrations:** OpenAI API, Notion API, Zotero API, GitHub API
- **Configuration:** Environment variables (`.env` files, never commit secrets)
- **Version Control:** Git with GitHub
- **Automation:** GitHub Actions (see `.github/workflows/`)

## Citation and Documentation Standards

### APA Citation Requirements (Critical)

All research sources MUST follow APA 7th edition format as defined in `docs/STYLE-APA.md`:

1. **Always use DOI when available** – Format as `https://doi.org/xxxxx`
2. **Include complete metadata** – Author(s), date, title, source, identifier
3. **Add annotations** – Every citation needs relevance and application notes
4. **Flag access issues** – Mark paywalled sources as `[Paywalled]`
5. **Verify links** – Test all URLs before committing

**Example citation:**
```
Schuetz, J. (2020). Is zoning a useful tool or a regulatory barrier? Evidence from recent research. Cityscape: A Journal of Policy Development and Research, 22(1), 93-110. https://doi.org/10.2139/ssrn.3522864
```

### Resource Management

When adding or modifying research sources:

1. **Update both formats:**
   - Add entry to `docs/resources-index.md` with full citation and annotation
   - Add corresponding row to `docs/resources.csv` for automation
2. **Required fields:**
   - Complete APA citation
   - Relevance statement (why it matters)
   - Application note (how it supports research)
   - Quality flags (`[Primary source]`, `[Paywalled]`, etc.)
   - Cross-references to where used in documentation
3. **Verification protocol:**
   - Confirm URL/DOI accessibility
   - Verify metadata against original source
   - Assess source quality and currency
   - Note if data is >5 years old

### Documentation Style

- **Clear and concise** – Use bullet points, headings, and tables
- **Actionable instructions** – Prefer imperative verbs ("Use X", "Configure Y")
- **Examples included** – Provide code snippets, command examples, or citation samples
- **Linked references** – Internal links to related docs, external to authoritative sources
- **Version tracking** – Include "Last updated" dates and version numbers

## Security Practices (Mandatory)

### Prohibited Actions

❌ **Never:**
- Commit API keys, tokens, or credentials to the repository
- Share sensitive data in public documentation or comments
- Use production credentials in development/testing
- Store passwords or secrets in plaintext

✅ **Always:**
- Use environment variables for secrets (see `.env.template`)
- Store secrets in password managers or GitHub Actions secrets
- Rotate integration tokens (OpenAI, Notion, Zotero) regularly
- Follow least-privilege principle for API access
- Review `SECURITY.md` before implementing integrations

### Environment Variables

Configuration pattern:
```bash
# Copy template and populate locally
cp .env.template .env
# Never commit .env file
```

Required variables are documented in `.env.template`.

## Contributing Guidelines

### Before Making Changes

1. **Review existing documentation:**
   - Check `docs/project-roadmap.md` for planned work
   - Read relevant style guides (`STYLE-APA.md`, etc.)
   - Search existing issues for related discussions
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/descriptive-name
   ```
3. **Make minimal, focused changes:**
   - One logical change per commit
   - Update related documentation
   - Add/update tests if applicable

### Pull Request Requirements

1. **Reference related issues:** Link to roadmap tasks or GitHub issues
2. **Descriptive title and body:** Explain what changed and why
3. **Documentation updates:** Keep docs in sync with code/config changes
4. **Citation verification:** If adding sources, confirm APA compliance
5. **No secrets committed:** Double-check `.env` files are gitignored

### Code Review Focus Areas

- Documentation clarity and completeness
- Citation format and accuracy
- Security best practices followed
- Links tested and working
- Consistency with existing patterns

## Common Tasks

### Adding a New Research Source

1. **Gather complete citation information:**
   - Author(s), publication date, title, source, DOI/URL
   - Verify URL is accessible
2. **Format in APA 7th edition:**
   - Follow examples in `docs/STYLE-APA.md`
   - Use proper capitalization (sentence case for titles)
3. **Add to both locations:**
   - `docs/resources-index.md` – Full entry with annotation
   - `docs/resources.csv` – Corresponding database row
4. **Include required fields:**
   - Relevance: One sentence on why it matters
   - Application: One sentence on how it's used
   - Quality flags: Source type and access status
   - Cross-references: Where cited in documentation

### Updating Integration Documentation

1. **Review current state:** Check `docs/integration-plan.md`
2. **Document changes:** API versions, authentication methods, endpoints
3. **Update examples:** Code snippets, configuration samples
4. **Test instructions:** Verify setup steps actually work
5. **Update security notes:** Flag any new credentials or permissions needed

### Managing Generative AI Output

When using ChatGPT, Codex, or similar tools:

1. **Version control:** Follow `docs/generative-output-version-control.md` guidelines
2. **Verification:** Human review required for all AI-generated content
3. **Attribution:** Note when content is AI-assisted
4. **Quality checks:** Verify facts, citations, and recommendations
5. **Iterate:** Refine prompts and outputs until meeting standards

## Key Documentation Links

- [Environment Setup Guide](docs/environment-setup.md)
- [Integration Plan](docs/integration-plan.md)
- [Project Roadmap](docs/project-roadmap.md)
- [APA Style Guide](docs/STYLE-APA.md)
- [Resources Index](docs/resources-index.md)
- [Generative Output Tracking](docs/generative-output-version-control.md)
- [Universal Linking Guide](docs/universal-linking-guide.md)

## Anti-Patterns to Avoid

❌ **Don't:**
- Copy citations from secondary sources without verification
- Add resources without proper APA formatting
- Commit configuration files with hardcoded credentials
- Make broad changes without documenting rationale
- Skip annotation requirements for citations
- Use broken or redirected URLs without noting issues

✅ **Do:**
- Start with project roadmap to understand priorities
- Follow established conventions and patterns
- Ask questions via GitHub issues when uncertain
- Keep documentation up-to-date with changes
- Verify every citation against original source
- Use persistent identifiers (DOI) whenever possible

## Questions and Support

- **Documentation issues:** Open an issue with label `documentation`
- **Security concerns:** Follow `SECURITY.md` reporting guidelines
- **Integration problems:** Reference `docs/connection-checks.md` for API connectivity troubleshooting
- **Style questions:** Consult `docs/STYLE-APA.md` for citation formatting or open issue
- **Roadmap updates:** Discuss in issues with label `roadmap`

## Version Information

**Version:** 1.0  
**Last Updated:** 2025-12-02  
**Maintained by:** Housing Policy Research team  
**Review cadence:** Quarterly or when major changes occur
