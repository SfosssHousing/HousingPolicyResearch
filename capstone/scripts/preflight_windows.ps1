# preflight_windows.ps1 - Windows PowerShell wrapper for preflight_check.py
#
# Wrapper for running preflight checks on Windows systems.
#

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "preflight_check.py"

Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Windows Preflight Health Check" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python 3 is available
$PythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonCmd = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $PythonCmd = "python3"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $PythonCmd = "py"
}

if (-not $PythonCmd) {
    Write-Host "❌ Error: Python 3 is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Install Python 3.8+ from https://www.python.org" -ForegroundColor Yellow
    exit 1
}

# Verify Python version
$PythonVersion = & $PythonCmd --version 2>&1
Write-Host "Found Python: $PythonVersion"

# Check if preflight_check.py exists
if (-not (Test-Path $PythonScript)) {
    Write-Host "❌ Error: preflight_check.py not found at $PythonScript" -ForegroundColor Red
    exit 1
}

# Load environment variables if .env exists
$EnvFile = Join-Path $ScriptDir ".env"
if (Test-Path $EnvFile) {
    Write-Host "📋 Loading environment from $EnvFile"
    Get-Content $EnvFile | ForEach-Object {
        if ($_ -match '^([^#].+?)=(.+)$') {
            $name = $matches[1].Trim()
            $value = $matches[2].Trim()
            Set-Item -Path "env:$name" -Value $value
        }
    }
}

# Run the Python preflight checker
Write-Host "Running preflight checks..."
Write-Host ""

& $PythonCmd $PythonScript
$ExitCode = $LASTEXITCODE

Write-Host ""
if ($ExitCode -eq 0) {
    Write-Host "✅ Preflight checks completed successfully" -ForegroundColor Green
} else {
    Write-Host "⚠️  Preflight checks completed with errors (exit code: $ExitCode)" -ForegroundColor Yellow
}

exit $ExitCode
