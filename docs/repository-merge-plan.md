# Repository Merge Plan: sfosss/Housing → SfosssHousing/HousingPolicyResearch

**Status:** Blocked - Awaiting access to source repository  
**Created:** 2025-12-12  
**Last Updated:** 2025-12-12

> **Quick Start:** For a condensed version of this plan, see [repository-merge-quickstart.md](repository-merge-quickstart.md)

## Objective

Merge the contents and full commit history of the `sfosss/Housing` repository into `SfosssHousing/HousingPolicyResearch` while:
- Preserving all commit history from the source repository
- Avoiding filename conflicts by importing into a subdirectory
- Maintaining documentation links and references
- Creating a clean merge that can be reviewed via pull request

## Current Status

### Access Issue

The merge process is currently blocked due to authentication failure when attempting to fetch from `sfosss/Housing`:

```
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/sfosss/Housing/'
```

The repository appears to be private or requires specific access credentials that the current GitHub token doesn't have.

## Resolution Options

### Option 1: Grant Repository Access (Recommended)

Repository owner (`sfosss`) can grant read access to the GitHub Copilot bot:

1. Navigate to `sfosss/Housing` repository settings
2. Go to "Manage Access" or "Collaborators"
3. Add the GitHub App or bot account used by Copilot
4. Grant read permissions (minimum required)

Once access is granted, the merge can proceed automatically using the commands below.

### Option 2: Create a Git Bundle

If direct access cannot be granted, create a bundle file:

```bash
# On a machine with access to sfosss/Housing:
cd /path/to/sfosss-Housing
git bundle create housing-repo.bundle --all

# Transfer housing-repo.bundle to this repository, then:
git remote add housing-bundle housing-repo.bundle
git fetch housing-bundle
git subtree add --prefix=housing housing-bundle main
```

### Option 3: Manual Clone and Re-push

If Option 1 or 2 aren't feasible:

1. Clone `sfosss/Housing` with appropriate credentials
2. Create a new branch in that repository
3. Move all contents into a `housing/` subdirectory
4. Push to this repository as a new remote branch
5. Merge the branch via PR

## Planned Merge Process

Once access is resolved, execute the following steps:

### Step 1: Verify Remote Configuration

```bash
# Check existing remotes
git remote -v

# The housing-src remote should already be configured:
# housing-src	https://github.com/sfosss/Housing (fetch)
# housing-src	https://github.com/sfosss/Housing (push)
```

### Step 2: Fetch Source Repository

```bash
# Fetch all branches and history from the source
git fetch housing-src
```

### Step 3: Use Git Subtree to Import

```bash
# Import the entire repository into the housing/ subdirectory
# This preserves full commit history
git subtree add --prefix=housing housing-src main

# Note: To preserve individual commits, omit the --squash flag (default behavior)
# Use --squash only if the history is very large and causes performance issues
# Example with squash: git subtree add --prefix=housing housing-src main --squash
```

### Step 4: Verify the Import

```bash
# Check that the housing directory was created
ls -la housing/

# Verify commit history is preserved
git log --oneline housing/

# Check for any merge conflicts
git status
```

### Step 5: Resolve Conflicts (if any)

If conflicts occur during the subtree merge:

```bash
# View conflicted files
git status | grep "both modified"

# Resolve each conflict manually
# Then stage the resolved files
git add <resolved-files>

# Complete the merge
git commit -m "Merge sfosss/Housing into housing/ subdirectory"
```

### Step 6: Validate Documentation Links

Check that any internal links within the imported content still work:

```bash
# Search for relative links in the housing directory
grep -r "\[.*\](\.\./" housing/

# Test key documentation files
cat housing/README.md
cat housing/docs/*.md
```

### Step 7: Push to Feature Branch

```bash
# Push the merge to the feature branch
git push origin copilot/merge-sfosss-into-housing-policy
```

### Step 8: Review and Merge

1. Open a pull request from `copilot/merge-sfosss-into-housing-policy` to `main`
2. Review the changes in the PR
3. Verify that:
   - All files are in the `housing/` subdirectory
   - No conflicts with existing files
   - Commit history is preserved (check commit list in PR)
   - Documentation links work correctly
4. Request review from team members
5. Merge the PR when approved

## Expected Repository Structure After Merge

```
/
├── .github/
├── Capstone/
├── README.md
├── SECURITY.md
├── capstone/
├── comments/
├── data/
├── docs/
│   ├── repository-merge-plan.md (this file)
│   └── ... (existing docs)
├── housing/                    ← NEW: Imported from sfosss/Housing
│   ├── README.md              ← From source repository
│   ├── docs/                  ← From source repository (if exists)
│   └── ... (all other files from sfosss/Housing)
├── references/
└── scripts/
```

## Validation Checklist

After the merge is complete, verify:

- [ ] All files from `sfosss/Housing` are present in the `housing/` directory
- [ ] Commit history from `sfosss/Housing` is preserved (visible in git log)
- [ ] No filename conflicts with existing repository content
- [ ] Documentation links within `housing/` subdirectory still work
- [ ] Cross-references between repositories are documented
- [ ] No secrets or sensitive data were imported
- [ ] CI/CD pipelines still pass (if applicable)
- [ ] README.md updated to reference the new `housing/` directory

## Rollback Plan

If issues are discovered after merge:

```bash
# If not yet pushed to main:
git reset --hard origin/main

# If already merged to main (requires force push):
# 1. Identify the merge commit hash
git log --oneline --graph main

# 2. Reset to the commit before the merge
git reset --hard <commit-before-merge>

# 3. Force push (requires admin privileges)
git push --force-with-lease origin main
```

**Note:** Force pushing should be avoided if possible. Instead, create a revert commit:

```bash
# Safer alternative: revert the merge commit
git revert -m 1 <merge-commit-hash>
git push origin main
```

## Communication Plan

1. **Before merge:** Notify team members about the upcoming repository merge
2. **During merge:** Update this document with progress and any issues encountered
3. **After merge:** Send summary email with:
   - Link to the merged PR
   - Location of imported content (`housing/` directory)
   - Any breaking changes or action items
   - Updated documentation links

## Questions and Support

For questions about this merge process:
- Open an issue in `SfosssHousing/HousingPolicyResearch`
- Tag relevant team members
- Reference this document in the issue description

## Related Resources

- [Repository Merge Quick Start Guide](repository-merge-quickstart.md)
- [Git Subtree Documentation](https://git-scm.com/book/en/v1/Git-Tools-Subtree-Merging)
- [GitHub: About Merge Conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)
- [Repository Merge Troubleshooting Guide](repository-merge-troubleshooting.md)
- [Project Roadmap](project-roadmap.md)
- [Environment Setup](environment-setup.md)

---

**Document Version:** 1.0  
**Maintained by:** Housing Policy Research team  
**Review Status:** Draft - Awaiting repository access resolution
