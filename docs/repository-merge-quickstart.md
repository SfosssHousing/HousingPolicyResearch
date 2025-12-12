# Quick Start: Merging sfosss/Housing Repository

This guide provides a quick summary for completing the repository merge. For detailed information, see the [Repository Merge Plan](repository-merge-plan.md).

## Current Status

✅ **Prepared:** Documentation and automation are ready  
⏸️ **Blocked:** Waiting for access to `sfosss/Housing` repository  
📋 **Next Step:** Grant repository access (see options below)

## What's Been Done

- ✅ Remote `housing-src` configured for `https://github.com/sfosss/Housing`
- ✅ Automated merge script created: `scripts/merge-housing-repository.sh`
- ✅ Comprehensive documentation provided
- ✅ Feature branch created: `copilot/merge-sfosss-into-housing-policy`

## Access Issue

The merge is blocked by authentication failure:

```
remote: Invalid username or token.
fatal: Authentication failed for 'https://github.com/sfosss/Housing/'
```

## How to Resolve

Choose one option below:

### Option 1: Grant Bot Access (Fastest) ⭐

**For repository owner (`sfosss`):**

1. Visit: https://github.com/sfosss/Housing/settings/access
2. Invite collaborator: `copilot-swe-agent[bot]` or the user running the merge
3. Grant "Read" permissions
4. ✅ Merge can proceed automatically

### Option 2: Use Personal Access Token

**For user with access:**

1. Generate PAT: https://github.com/settings/tokens
2. Select scope: `repo` (for private) or `public_repo` (for public)
3. Update remote:
   ```bash
   cd /path/to/HousingPolicyResearch
   git remote remove housing-src
   git remote add housing-src https://<username>:<token>@github.com/sfosss/Housing.git
   ```
4. Run merge script: `./scripts/merge-housing-repository.sh`

### Option 3: Use Git Bundle

**On machine with access to sfosss/Housing:**

```bash
cd /path/to/sfosss-Housing
git bundle create housing-repo.bundle --all
```

**Transfer `housing-repo.bundle` to merge machine, then:**

```bash
cd /path/to/HousingPolicyResearch
git remote add housing-bundle housing-repo.bundle
git fetch housing-bundle
git subtree add --prefix=housing housing-bundle main
git push origin copilot/merge-sfosss-into-housing-policy
```

## Once Access is Granted

### Automatic Method (Recommended)

```bash
cd /path/to/HousingPolicyResearch
git checkout copilot/merge-sfosss-into-housing-policy
./scripts/merge-housing-repository.sh
```

The script will:
1. Verify prerequisites
2. Fetch the repository
3. Import into `housing/` subdirectory
4. Preserve full commit history
5. Validate the merge
6. Provide next steps

### Manual Method

If you prefer to run commands manually:

```bash
cd /path/to/HousingPolicyResearch
git checkout copilot/merge-sfosss-into-housing-policy

# Fetch source repository
git fetch housing-src

# Import with full history
git subtree add --prefix=housing housing-src main

# Verify
ls -la housing/
git log --oneline | head -20

# Push
git push origin copilot/merge-sfosss-into-housing-policy
```

## Expected Result

After successful merge:

```
/
├── housing/                    ← NEW: All content from sfosss/Housing
│   ├── README.md
│   └── ... (all files from source repo)
├── docs/
├── scripts/
└── ... (existing files unchanged)
```

## Verification Checklist

After merge completes:

- [ ] `housing/` directory exists
- [ ] Files are present in `housing/`
- [ ] Commit history preserved (check `git log`)
- [ ] No merge conflicts
- [ ] No file collisions with existing content
- [ ] Documentation links in `housing/` still work
- [ ] Changes pushed to feature branch

## Troubleshooting

If you encounter errors:

1. **Read the error message** - Script provides specific guidance
2. **Check troubleshooting guide:** [repository-merge-troubleshooting.md](repository-merge-troubleshooting.md)
3. **Common issues:**
   - Authentication → Grant access or use token
   - Directory exists → Check if merge already done
   - Merge conflicts → See troubleshooting guide
   - Uncommitted changes → Commit or stash them

## After Merge Completes

1. **Review the changes:**
   ```bash
   git diff origin/main...copilot/merge-sfosss-into-housing-policy
   ```

2. **Open Pull Request:**
   - Go to: https://github.com/SfosssHousing/HousingPolicyResearch/pulls
   - Create PR from `copilot/merge-sfosss-into-housing-policy` to `main`
   - Add description: "Merge sfosss/Housing into housing/ subdirectory"

3. **Request review from team**

4. **Merge when approved**

## Documentation

- 📖 [Repository Merge Plan](repository-merge-plan.md) - Detailed plan and procedures
- 🔧 [Troubleshooting Guide](repository-merge-troubleshooting.md) - Common issues and solutions
- 📜 [Script Documentation](../scripts/README.md) - About the automation script
- 🏠 [Main README](../README.md) - Repository overview

## Getting Help

- **Script help:** Run `./scripts/merge-housing-repository.sh` (reads error messages)
- **Documentation:** See links above
- **Issues:** Open a GitHub issue with error details
- **Team:** Contact repository maintainers

---

**Quick Reference:**

```bash
# Check current status
git status
git remote -v

# Run merge (once access granted)
./scripts/merge-housing-repository.sh

# Or manual commands
git fetch housing-src
git subtree add --prefix=housing housing-src main
```

**Key Files:**
- Script: `scripts/merge-housing-repository.sh`
- Plan: `docs/repository-merge-plan.md`
- Troubleshooting: `docs/repository-merge-troubleshooting.md`

**Need access?** Contact repository owner: `@sfosss`

---

**Last Updated:** 2025-12-12  
**Status:** Ready to execute (pending access)  
**Feature Branch:** `copilot/merge-sfosss-into-housing-policy`
