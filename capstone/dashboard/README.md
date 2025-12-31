# Preflight Dashboard - macOS Runbook

This directory contains documentation and reports for the preflight health check system optimized for Apple Silicon (macOS arm64).

## Overview

The preflight system performs comprehensive system health checks before running automation tasks or development workflows. It is designed to be **dry-run safe**: all scripts only produce local JSON and Markdown reports and do not modify system state.

## Quick Start (macOS)

### Prerequisites

- macOS 11.0+ (Big Sur or later)
- Python 3.8+
- Xcode Command Line Tools (recommended)
- Homebrew (recommended)

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/SfosssHousing/HousingPolicyResearch.git
   cd HousingPolicyResearch
   ```

2. **Navigate to the scripts directory**:
   ```bash
   cd capstone/scripts
   ```

3. **Make scripts executable**:
   ```bash
   chmod +x preflight_macos.sh preflight_check.py
   ```

4. **Optional: Install smartmontools for SMART checks**:
   ```bash
   brew install smartmontools
   ```

### Running Preflight Checks

#### Basic Usage (macOS)

```bash
cd capstone/scripts
./preflight_macos.sh
```

#### Direct Python Invocation

```bash
cd capstone/scripts
python3 preflight_check.py
```

#### With Environment Variables

```bash
# Copy and configure environment template
cp .env.template .env
# Edit .env with your settings (e.g., GITHUB_TOKEN)

# Run with environment loaded
./preflight_macos.sh
```

### Understanding Results

After running preflight checks, you'll find reports in `capstone/reports/`:

- **JSON Report**: `preflight_check_YYYYMMDD_HHMMSS.json` - Machine-readable results
- **Markdown Report**: `preflight_check_YYYYMMDD_HHMMSS.md` - Human-readable summary

#### Status Indicators

- ✅ **PASS**: Check completed successfully, no issues
- ⚠️ **WARN**: Check completed but found potential issues (non-blocking)
- ❌ **FAIL**: Check failed, action required
- ⏭️ **SKIP**: Check was skipped (not applicable or tool not available)

## Checks Performed

### 1. Python Environment
- Verifies Python 3.8+ installation
- Checks for virtual environment
- Reports Python version and executable path

### 2. Git Configuration
- Verifies Git installation
- Checks `user.name` and `user.email` configuration
- Reports Git version

### 3. GitHub API Connectivity
- Tests reachability of `https://api.github.com`
- Validates API response codes
- Useful for CI/CD validation

### 4. Disk Space
- Reports total, used, and free disk space
- Warns if less than 10GB free
- Fails if less than 2GB free

### 5. macOS-Specific Checks
- **Homebrew**: Detects and reports Homebrew installation
- **Xcode Command Line Tools**: Verifies Xcode CLT installation
- **Rosetta 2**: Checks Rosetta 2 status (for arm64 Macs)
- **Architecture**: Reports system architecture (arm64 vs x86_64)

### 6. SMART Disk Health (Best-Effort)
- Scans for disk devices using `smartctl`
- Checks SMART health status for each disk
- **Note**: May require `sudo` privileges for full functionality
- Skipped if `smartmontools` not installed

### 7. iCloud Sync Detection
- Samples files in iCloud Drive for sync status
- Uses `xattr` to detect iCloud-specific attributes
- **Limited sampling** (max 50 files) to avoid long runs on large repos
- Warns if working within iCloud Drive (can cause sync conflicts)

## Best Practices

### For Apple Silicon (arm64) Macs

1. **Install Rosetta 2** (if running x86 apps):
   ```bash
   softwareupdate --install-rosetta
   ```

2. **Use native arm64 Homebrew**:
   ```bash
   # Homebrew for arm64 installs to /opt/homebrew
   which brew  # Should show /opt/homebrew/bin/brew
   ```

3. **Avoid working in iCloud Drive** for large repositories:
   - iCloud sync can interfere with Git operations
   - Clone repos to `~/Developer` or `~/Projects` instead

### SMART Checks

SMART checks provide early warning for disk failures. If you see warnings:

1. **Review SMART attributes**:
   ```bash
   sudo smartctl -a /dev/diskX
   ```

2. **Back up important data** immediately if health check fails

3. **Consider disk replacement** if multiple SMART attributes are failing

### Environment Variables

Store secrets in `.env` (never commit this file):

```bash
# Example .env
GITHUB_TOKEN=ghp_your_token_here
PREFLIGHT_VERBOSE=true
```

## Troubleshooting

### "smartctl: command not found"

SMART checks will be skipped. Install smartmontools:
```bash
brew install smartmontools
```

### "Permission denied" for SMART checks

Some SMART operations require root privileges:
```bash
sudo ./preflight_macos.sh
```

### "Python 3.8+ required"

Install or upgrade Python:
```bash
brew install python@3.11
```

### iCloud Sync Warnings

If you see warnings about iCloud syncing:

1. **Move repository outside iCloud Drive**:
   ```bash
   mv ~/Library/Mobile\ Documents/com~apple~CloudDocs/project ~/Developer/project
   ```

2. **Disable iCloud Desktop & Documents sync**:
   - System Settings → Apple ID → iCloud → iCloud Drive → Options
   - Uncheck "Desktop & Documents Folders"

### GitHub API Connectivity Issues

1. **Check internet connection**
2. **Verify proxy/firewall settings**
3. **Test manually**:
   ```bash
   curl -i https://api.github.com
   ```

## CI/CD Integration

The preflight checks are designed for CI/CD integration. See `.github/workflows/preflight.yml` for GitHub Actions configuration.

### Workflow Features

- Runs on macOS runners (latest)
- Uploads JSON reports as artifacts
- Fails build if critical checks fail
- Continues on warnings

### Viewing CI Results

1. Navigate to **Actions** tab in GitHub
2. Select **Preflight Checks** workflow
3. Download JSON artifact from successful runs

## Next Steps

### Immediate Actions

1. ✅ Run preflight checks locally to establish baseline
2. ✅ Review any warnings or errors
3. ✅ Install recommended tools (Homebrew, smartmontools)
4. ✅ Configure environment variables if needed

### Integration Tasks

1. 📋 Set up automated preflight checks in CI/CD pipeline
2. 📋 Configure scheduled runs (e.g., daily health checks)
3. 📋 Integrate results with monitoring/alerting systems
4. 📋 Document team-specific conventions and thresholds

### Future Enhancements

- Add network latency checks
- Integrate with external monitoring services
- Add custom health check plugins
- Dashboard UI for historical trends
- Automated remediation suggestions

## Additional Resources

- **Python Script**: `../scripts/preflight_check.py` - Main check logic
- **macOS Wrapper**: `../scripts/preflight_macos.sh` - Platform-specific wrapper
- **Environment Template**: `../scripts/.env.template` - Configuration template
- **GitHub Workflow**: `../../.github/workflows/preflight.yml` - CI configuration

## Support

For issues or questions:

1. Check the [main repository README](../../README.md)
2. Review [integration documentation](../../docs/integration-plan.md)
3. Open an issue on GitHub with preflight check results attached

---

**Version**: 0.3-macos-arm64  
**Last Updated**: 2025-12-07  
**Platform**: macOS arm64 (Apple Silicon)
