#!/bin/bash
#
# preflight_linux.sh - Linux wrapper for preflight_check.py
#
# Lightweight wrapper for running preflight checks on Linux systems.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/preflight_check.py"

echo "==================================="
echo "Linux Preflight Health Check"
echo "==================================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed or not in PATH"
    echo "Install Python 3.8+ via your package manager:"
    echo "  Ubuntu/Debian: sudo apt-get install python3"
    echo "  Fedora/RHEL: sudo dnf install python3"
    exit 1
fi

# Check if preflight_check.py exists
if [ ! -f "${PYTHON_SCRIPT}" ]; then
    echo "❌ Error: preflight_check.py not found at ${PYTHON_SCRIPT}"
    exit 1
fi

# Load environment variables if .env exists
ENV_FILE="${SCRIPT_DIR}/.env"
if [ -f "${ENV_FILE}" ]; then
    echo "📋 Loading environment from ${ENV_FILE}"
    set -a
    source "${ENV_FILE}"
    set +a
fi

# Run the Python preflight checker
echo "Running preflight checks..."
echo ""

python3 "${PYTHON_SCRIPT}"
exit_code=$?

echo ""
if [ $exit_code -eq 0 ]; then
    echo "✅ Preflight checks completed successfully"
else
    echo "⚠️  Preflight checks completed with errors (exit code: $exit_code)"
fi

exit $exit_code
