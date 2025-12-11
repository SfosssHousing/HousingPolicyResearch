# macOS Preflight Checks - Quick Reference

**Version**: 0.3-macos-arm64  
**Optimized for**: Apple Silicon (arm64) macOS

## Quick Start

```bash
# Navigate to scripts directory
cd capstone/scripts

# Make executable (first time only)
chmod +x preflight_macos.sh preflight_check.py

# Run preflight checks
./preflight_macos.sh
```

## What Gets Checked

✅ **Python Environment** - Version 3.8+ required  
✅ **Git Configuration** - user.name and user.email  
✅ **GitHub API** - Connectivity test  
✅ **Disk Space** - Free space warnings  
✅ **Homebrew** - Package manager detection  
✅ **Xcode CLT** - Command Line Tools verification  
✅ **Rosetta 2** - Translation layer for x86 apps  
✅ **SMART Health** - Disk health monitoring (requires smartmontools)  
✅ **iCloud Sync** - Detects if working in iCloud Drive (limited sampling)

## Requirements

### Minimum
- macOS 11.0+ (Big Sur or later)
- Python 3.8+

### Recommended
- Xcode Command Line Tools: `xcode-select --install`
- Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- smartmontools: `brew install smartmontools`

## Output

Reports are saved to `capstone/reports/`:
- `preflight_check_YYYYMMDD_HHMMSS.json` - Machine-readable
- `preflight_check_YYYYMMDD_HHMMSS.md` - Human-readable

## Environment Variables (Optional)

```bash
# Copy template and edit
cp .env.template .env

# Add your settings
GITHUB_TOKEN=your_token_here
PREFLIGHT_VERBOSE=true
```

**⚠️ Never commit .env file!**

## SMART Disk Checks

SMART checks detect early signs of disk failure:

```bash
# Install smartmontools
brew install smartmontools

# Run preflight (may prompt for sudo)
./preflight_macos.sh

# Manual SMART check
sudo smartctl -a /dev/disk0
```

## iCloud Drive Recommendations

If you see iCloud sync warnings:

1. **Move repository outside iCloud Drive**
   ```bash
   # Recommended locations
   ~/Developer/
   ~/Projects/
   ~/Code/
   ```

2. **Disable Desktop & Documents sync**
   - System Settings → Apple ID → iCloud → iCloud Drive → Options
   - Uncheck "Desktop & Documents Folders"

## Troubleshooting

### Python not found
```bash
# Install via Homebrew
brew install python@3.11

# Verify
python3 --version
```

### Permission denied
```bash
# Make executable
chmod +x preflight_macos.sh
```

### SMART checks require sudo
```bash
# Run with elevated privileges
sudo ./preflight_macos.sh
```

### GitHub API timeout
```bash
# Check connectivity
curl -i https://api.github.com

# Check proxy settings
echo $http_proxy
echo $https_proxy
```

## Exit Codes

- `0` - All checks passed or warnings only
- `1` - One or more checks failed (critical errors)

## Platform Wrappers

- **macOS**: `./preflight_macos.sh`
- **Linux**: `./preflight_linux.sh`
- **Windows**: `.\preflight_windows.ps1`

All wrappers call the same Python script with platform-specific setup.

## CI/CD Integration

See `.github/workflows/preflight.yml` for GitHub Actions configuration.

Artifacts are uploaded for each run:
- `preflight-report-macos-{run_number}` - JSON reports
- `preflight-markdown-macos-{run_number}` - Markdown reports

## More Information

- **Full Documentation**: `capstone/dashboard/README.md`
- **Python Script**: `preflight_check.py`
- **Environment Template**: `.env.template`

---

**Dry-Run Safe**: This script only produces reports and does not modify system state.
