# Repository Merge Troubleshooting Guide

This guide helps resolve common issues encountered when merging the `sfosss/Housing` repository into `SfosssHousing/HousingPolicyResearch`.

## Issue: Authentication Failed

**Error Message:**
```
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/sfosss/Housing/'
```

**Cause:** The repository is private or requires authentication that the current credentials don't provide.

### Solution 1: Grant Repository Access (Recommended)

**For repository owner (`sfosss`):**

1. Go to https://github.com/sfosss/Housing/settings/access
2. Click "Invite a collaborator" or "Manage access"
3. Add the user account performing the merge
4. Grant "Read" permissions (minimum required)

**For automated systems (GitHub Actions, Copilot):**

1. Go to repository settings → Actions → General
2. Under "Workflow permissions", ensure read access is granted
3. Or create a Personal Access Token (PAT) with `repo` scope
4. Add the token to GitHub Secrets
5. Configure git to use the token securely:
   ```bash
   # Recommended: Use Git Credential Manager (secure storage)
   git config --global credential.helper manager
   
   # Alternative: Use OS-specific secure storage
   # macOS: git config --global credential.helper osxkeychain
   # Linux: git config --global credential.helper libsecret
   # Windows: git config --global credential.helper wincred
   ```

**Security Warning:** Avoid using `credential.helper store` as it saves credentials in plaintext. Use platform-specific credential managers instead.

### Solution 2: Use SSH Instead of HTTPS

If you have SSH keys configured with GitHub:

```bash
# Remove the existing remote
git remote remove housing-src

# Add the remote using SSH URL
git remote add housing-src git@github.com:sfosss/Housing.git

# Verify SSH access
ssh -T git@github.com

# Try fetching again
git fetch housing-src
```

### Solution 3: Use a Personal Access Token (PAT)

1. Generate a PAT at https://github.com/settings/tokens
2. Select scope: `repo` (for private repos) or `public_repo` (for public repos)
3. Copy the token
4. Update the remote URL with the token:
   ```bash
   git remote remove housing-src
   git remote add housing-src https://<username>:<token>@github.com/sfosss/Housing.git
   git fetch housing-src
   ```

**Security Warning:** Never commit tokens to the repository. Use environment variables or credential helpers.

### Solution 4: Use Git Credential Manager

```bash
# Install Git Credential Manager (if not already installed)
# On Ubuntu/Debian:
sudo apt-get install git-credential-manager

# On macOS:
brew install git-credential-manager

# Configure git to use the credential manager
git config --global credential.helper manager

# Try fetching again (will prompt for credentials)
git fetch housing-src
```

## Issue: Repository Not Found

**Error Message:**
```
fatal: repository 'https://github.com/sfosss/Housing.git/' not found
```

**Possible Causes:**
1. Repository doesn't exist at that URL
2. Repository name is misspelled
3. Repository was deleted or moved
4. You don't have access (same error as authentication failed)

**Solutions:**

1. **Verify the repository exists:**
   - Visit https://github.com/sfosss/Housing in a web browser
   - If you see a 404 page, the repository doesn't exist or you don't have access

2. **Check for typos:**
   ```bash
   # List current remotes
   git remote -v
   
   # Check the URL carefully for typos
   # If wrong, update it:
   git remote set-url housing-src https://github.com/correct/path.git
   ```

3. **Search for the correct repository:**
   ```bash
   # Use GitHub CLI to search
   gh repo list sfosss
   
   # Or use the GitHub web interface to browse the user's repositories
   ```

4. **Verify with the repository owner:**
   - Contact `sfosss` to confirm the repository exists
   - Ask for the correct repository URL
   - Request access if needed

## Issue: Merge Conflicts

**Error Message:**
```
Auto-merging failed; fix conflicts and then commit the result.
```

**This happens when:**
- Files with the same name exist in both repositories
- Git can't automatically merge the content

**Solution:**

1. **Check which files have conflicts:**
   ```bash
   git status
   ```

2. **View conflicted files:**
   ```bash
   git ls-files -u
   ```

3. **For each conflicted file:**
   ```bash
   # Open the file in an editor
   # Look for conflict markers:
   # <<<<<<< HEAD
   # (your changes)
   # =======
   # (incoming changes)
   # >>>>>>> housing-src/main
   
   # Resolve the conflict by choosing one version or merging manually
   # Remove the conflict markers
   ```

4. **Stage resolved files:**
   ```bash
   git add <resolved-file>
   ```

5. **Complete the merge:**
   ```bash
   git commit -m "Resolve merge conflicts from sfosss/Housing"
   ```

**Prevention:** Using `git subtree add --prefix=housing` should prevent most conflicts by putting everything in a subdirectory.

## Issue: Large Repository Size

**Symptom:**
- Fetch or merge operation is very slow
- Uses excessive disk space
- Times out during clone/fetch

**Solutions:**

1. **Use shallow clone (lose history):**
   ```bash
   git fetch --depth=1 housing-src
   git subtree add --prefix=housing housing-src main --squash
   ```

2. **Use squash option (lose individual commits):**
   ```bash
   git subtree add --prefix=housing housing-src main --squash
   ```

3. **Clone incrementally:**
   ```bash
   # Fetch with limited depth
   git fetch --depth=100 housing-src
   
   # If successful, fetch more
   git fetch --deepen=100 housing-src
   
   # Repeat until you have enough history
   ```

4. **Use Git LFS for large files:**
   ```bash
   # Install Git LFS
   git lfs install
   
   # Track large files
   git lfs track "*.zip" "*.tar.gz" "*.dmg"
   
   # Fetch with LFS
   git lfs fetch housing-src
   ```

## Issue: Divergent Histories

**Error Message:**
```
fatal: refusing to merge unrelated histories
```

**Cause:** The two repositories have completely separate commit histories.

**Solution:**

When using `git subtree add`, this is actually expected and handled automatically. If you encounter this error:

```bash
# The --allow-unrelated-histories flag is built into git subtree
# It should work automatically, but if not:
git merge --allow-unrelated-histories housing-src/main
```

## Issue: Script Fails with "Target directory already exists"

**Error Message:**
```
The 'housing' directory already exists!
```

**Cause:** A previous merge attempt created the directory, or you're running the script twice.

**Solutions:**

1. **Check if merge was already completed:**
   ```bash
   ls -la housing/
   git log --oneline | grep -i housing
   ```

2. **If merge is incomplete, remove and retry:**
   ```bash
   rm -rf housing/
   ./scripts/merge-housing-repository.sh
   ```

3. **If merge is complete:**
   - No action needed, the merge is done
   - Skip to verification steps in the merge plan

## Issue: Script Won't Run

**Error Message:**
```
bash: ./scripts/merge-housing-repository.sh: Permission denied
```

**Cause:** Script doesn't have execute permissions.

**Solution:**
```bash
chmod +x scripts/merge-housing-repository.sh
./scripts/merge-housing-repository.sh
```

## Issue: Uncommitted Changes

**Error Message:**
```
You have uncommitted changes. Please commit or stash them first.
```

**Cause:** The merge script requires a clean working directory to avoid data loss.

**Solutions:**

1. **Commit your changes:**
   ```bash
   git add -A
   git commit -m "Save work before merge"
   ./scripts/merge-housing-repository.sh
   ```

2. **Stash your changes:**
   ```bash
   git stash save "WIP before merge"
   ./scripts/merge-housing-repository.sh
   # After merge completes:
   git stash pop
   ```

3. **Discard changes (careful!):**
   ```bash
   git reset --hard HEAD
   ./scripts/merge-housing-repository.sh
   ```

## Getting Help

If you encounter an issue not covered in this guide:

1. **Check the merge plan:** [docs/repository-merge-plan.md](repository-merge-plan.md)
2. **Review git status and logs:**
   ```bash
   git status
   git log --oneline -10
   git remote -v
   ```
3. **Open a GitHub issue:**
   - Include the full error message
   - Include relevant git commands and their output
   - Tag the repository maintainer
4. **Contact the team:**
   - Mention in team chat or email
   - Reference this troubleshooting guide
   - Include what solutions you've already tried

## Additional Resources

- [Git Subtree Documentation](https://git-scm.com/book/en/v1/Git-Tools-Subtree-Merging)
- [GitHub Authentication](https://docs.github.com/en/authentication)
- [Git Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)
- [Resolving Merge Conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts)
- [Repository Merge Plan](repository-merge-plan.md)
- [Environment Setup Guide](environment-setup.md)

---

**Last Updated:** 2025-12-12  
**Maintainer:** Housing Policy Research team  
**Version:** 1.0
