# Environment Setup Guide

**Last Updated:** December 24, 2025  
**Status:** Ready for Implementation  

---

## Overview

This guide walks you through setting up a secure, reproducible local development environment for the Housing Policy Research project. The setup takes approximately **10-15 minutes** and requires:

- macOS or Linux (Windows users: use WSL2)
- Python 3.11+
- Git
- A text editor (VS Code, Sublime Text, etc.)

---

## Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/sfosss/HousingPolicyResearch.git
cd HousingPolicyResearch

# Verify you're on the main branch
git branch
# Expected output: * main
```

---

## Step 2: Set Up Python Virtual Environment

```bash
# Create a virtual environment
python3.11 -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Activate it (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Verify activation (you should see (.venv) in your prompt)
which python  # macOS/Linux
python -c "import sys; print(sys.prefix)"  # Should show .venv path
```

---

## Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list | grep -E "black|flake8|openai|pandas"
# Expected: All 8 packages listed
```

---

## Step 4: Configure Git Pre-Commit Hooks

```bash
# Install pre-commit hooks (prevents accidental commits of secrets)
pre-commit install

# Test that hooks work
pre-commit run --all-files

# Expected output:
# ✓ black....................................................................Passed
# ✓ flake8...................................................................Passed
# ✓ mdformat..................................................................Passed
# ✓ detect-secrets............................................................Passed
```

---

## Step 5: Configure Environment Variables

### 5a: Create Local `.env` File

```bash
# Copy template
cp .env.template .env

# Open in your editor
code .env  # or vim .env, nano .env, etc.
```

### 5b: Add API Keys

The `.env` file contains placeholders for all required API keys. You'll need to:

1. **Obtain new API keys** from each service (see Key Acquisition Guide below)
2. **Replace placeholders** with actual keys
3. **Save and close** (do NOT commit to Git)

```bash
# Verify .env is NOT committed
git status
# Expected: .env not listed (it's in .gitignore)
```

---

## API Key Acquisition Guide

### Critical: Revoke Old Exposed Keys First

⚠️ **The old keys were exposed in the repository.** Before getting new ones, **revoke the old keys** at each service:

#### 1. **OpenAI** (MOST CRITICAL - used daily)
- **Old Key Status:** REVOKE IMMEDIATELY
- **Revoke at:** https://platform.openai.com/account/api-keys
- **Get New Key:**
  1. Go to https://platform.openai.com/account/api-keys
  2. Click "Create new secret key"
  3. Copy the key (you can only see it once!)
  4. Paste into `.env` as `OPENAI_API_KEY=sk-proj-...`

#### 2. **ProPublica Congress** (Congressional voting data)
- **Old Key Status:** REVOKE
- **Revoke at:** https://projects.propublica.org/api-keys
- **Get New Key:**
  1. Go to https://www.propublica.org/datastore/api/congress-api/api-key-form
  2. Fill in the form (academic research is fine)
  3. Check email for API key
  4. Paste into `.env` as `PROPUBLICA_CONGRESS_API_KEY=...`

#### 3. **NYS Open Legislation** (NY State bills)
- **Old Key Status:** REVOKE
- **Revoke at:** https://docs.nysenate.gov/ (account settings)
- **Get New Key:**
  1. Go to https://docs.nysenate.gov/
  2. Click "API" in top menu
  3. Sign up for API access
  4. Verify email
  5. Paste into `.env` as `NYS_OPEN_LEG_API_KEY=...`

#### 4. **OpenStates** (State legislative tracking)
- **Old Key Status:** REVOKE
- **Revoke at:** https://openstates.org/api/ (your account)
- **Get New Key:**
  1. Go to https://openstates.org/api/
  2. Click "Get API Key"
  3. Sign up or log in
  4. Copy key
  5. Paste into `.env` as `OPENSTATES_API_KEY=...`

#### 5. **Legistar** (NYC legislative tracking)
- **Old Key Status:** REVOKE (contact support)
- **Get New Key:** Contact NYC Department of City Planning or Granicus support
- **Paste into `.env` as `LEGISTAR_API_KEY=...`

#### 6. **Notion** (Research notes & project management)
- **New Setup:**
  1. Go to https://www.notion.so/my-integrations
  2. Click "New Integration"
  3. Name it "Housing Policy Research"
  4. Copy the "Internal Integration Token"
  5. Paste into `.env` as `NOTION_TOKEN=...`
- **Get Database IDs:**
  1. In Notion, open your Research database
  2. Click the "Share" button → "Copy link"
  3. The URL contains the ID: `/database/{ID}`
  4. Paste into `.env` as `NOTION_RESEARCH_DB_ID={ID}`
  5. Repeat for Action Items database

#### 7. **Zotero** (Citation management)
- **New Setup:**
  1. Go to https://www.zotero.org/settings/keys
  2. Click "New Key"
  3. Name it "Housing Policy Research"
  4. Copy the key
  5. Paste into `.env` as `ZOTERO_API_KEY=...`
- **Get Library & Collection IDs:**
  1. In Zotero, go to your library
  2. Library ID is in your account settings → https://www.zotero.org/settings/account
  3. Paste into `.env` as `ZOTERO_LIBRARY_ID=...`
  4. Collection ID from the collection you want to use
  5. Paste into `.env` as `ZOTERO_COLLECTION_ID=...`

#### 8. **GitHub** (CI/CD automation - optional)
- **Get PAT (Personal Access Token):**
  1. Go to https://github.com/settings/tokens
  2. Click "Generate new token (classic)"
  3. Name it "Housing Policy Research"
  4. Scopes: `repo`, `workflow`, `write:packages`
  5. Copy token
  6. Paste into `.env` as `GITHUB_PAT=ghp_...`

#### 9. **Crossref** (Scholarly metadata - email required)
- **Just add your email:**
  ```
  CROSSREF_EMAIL=your_email@example.com
  ```

### Example `.env` File (FILLED OUT)

```bash
# Policy Research APIs
OPENAI_API_KEY=sk-proj-abc123xyz...
NOTION_TOKEN=secret_abc123...
NOTION_RESEARCH_DB_ID=database_id_123
NOTION_ACTION_ITEMS_DB_ID=database_id_456
GITHUB_PAT=ghp_abc123xyz...
ZOTERO_API_KEY=1234567890abcdefg
ZOTERO_LIBRARY_ID=12345
ZOTERO_COLLECTION_ID=ABCDE

# Legislative Data APIs
CROSSREF_EMAIL=you@example.com
OPENALEX_API_KEY=
PROPUBLICA_CONGRESS_API_KEY=abc123xyz...
NYS_OPEN_LEG_API_KEY=abc123xyz...
LEGISTAR_API_KEY=abc123xyz...
OPENSTATES_API_KEY=abc123xyz...

# Logging
LOG_LEVEL=INFO
SYNC_CHECKPOINT_DIR=.sync-state
ASSISTANT_BASE_URL=http://localhost:8000
ASSISTANT_API_TIMEOUT_MS=30000
CHATGPT_ARCHIVE_PATH=logs/chatgpt
```

---

## Step 6: Verify Setup

```bash
# 1. Check Git status
git status
# Expected: "On branch main, nothing to commit, working tree clean"

# 2. Verify pre-commit works
pre-commit run --all-files
# Expected: All checks pass (✓)

# 3. Test Python environment
python --version  # Should be 3.11+
pip list | grep -E "black|flake8|openai|pandas|pre-commit"
# Expected: All installed

# 4. Verify .env is configured (but NOT committed)
echo "OpenAI Key: $(grep OPENAI_API_KEY .env | cut -d'=' -f2)"
# Expected: Shows first 10 chars of key (don't commit output!)

# 5. Verify GitHub connection
ssh -T git@github.com
# Expected: "Hi <username>! You've successfully authenticated..."
```

---

## Troubleshooting

### Issue: Python version not found
```bash
# Solution: Install Python 3.11
brew install python@3.11  # macOS
sudo apt-get install python3.11  # Ubuntu/Debian
```

### Issue: Pre-commit hook fails
```bash
# Solution: Reinstall hooks
pre-commit clean
pre-commit install
pre-commit run --all-files
```

### Issue: Git SSH authentication fails
```bash
# Solution: Verify SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"
# Then add to GitHub: https://github.com/settings/keys
```

### Issue: `.env` file not loading in scripts
```bash
# Solution: Load manually in Python
from dotenv import load_dotenv
load_dotenv()

# Or in bash
export $(cat .env | xargs)
```

---

## Next Steps

1. ✅ Complete all 6 steps above
2. 📋 Review [Contributing Guidelines](contributing.md)
3. 🔒 Review [Security Practices](../SECURITY.md)
4. 🔗 Review [GitHub Integration Guide](integration-plan.md)
5. 🚀 Start adding research sources to `10_sources/`

---

## Support

- **Questions?** Open a GitHub issue with label `setup`
- **Errors?** Include:
  - Python version: `python --version`
  - Error message (full output)
  - Steps to reproduce
- **Security concerns?** Follow [SECURITY.md](../SECURITY.md) reporting guidelines

---

**Version:** 1.0  
**Last Updated:** 2025-12-24  
**Reviewed by:** Housing Policy Research Team
