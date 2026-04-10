#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="${PROJECT_ROOT}/.venv"
REQUIREMENTS_FILE="${PROJECT_ROOT}/requirements.txt"
ENV_TEMPLATE="${PROJECT_ROOT}/.env.template"
ENV_FILE="${PROJECT_ROOT}/.env"

usage() {
  cat <<USAGE
Usage: ./setup.sh [--ci]

Options:
  --ci    Run in CI mode (no prompts, run pre-commit after install)
USAGE
}

RUN_CI=false
case "${1-}" in
  "" )
    # No arguments: default interactive mode, RUN_CI remains false
    ;;
  --ci )
    RUN_CI=true
    ;;
  --help )
    usage
    exit 0
    ;;
  * )
    echo "Error: Unknown option: ${1-}" >&2
    echo >&2
    usage >&2
    exit 1
    ;;
esac

ensure_python() {
  if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is required but not found on PATH." >&2
    exit 1
  fi
}

create_venv() {
  if [[ ! -d "${VENV_PATH}" ]]; then
    python3 -m venv "${VENV_PATH}"
  fi
  # shellcheck disable=SC1091
  source "${VENV_PATH}/bin/activate"
}

install_dependencies() {
  python -m pip install --upgrade pip
  if [[ -f "${REQUIREMENTS_FILE}" ]]; then
    python -m pip install -r "${REQUIREMENTS_FILE}"
  fi
}

prepare_environment_file() {
  if [[ -f "${ENV_TEMPLATE}" && ! -f "${ENV_FILE}" ]]; then
    cp "${ENV_TEMPLATE}" "${ENV_FILE}"
    echo "Copied ${ENV_TEMPLATE} to ${ENV_FILE}. Populate it with your credentials."
  fi
}

ensure_tracked_directories() {
  mkdir -p "${PROJECT_ROOT}/logs" "${PROJECT_ROOT}/artifacts" "${PROJECT_ROOT}/docs/prompts"
  # avoid creating untracked directories that are not committed or ignored
}

install_pre_commit() {
  if command -v pre-commit >/dev/null 2>&1; then
    pre-commit install --install-hooks
    if [[ "${RUN_CI}" == true ]]; then
      pre-commit run --all-files
    fi
  else
    echo "pre-commit not installed in this environment; skipping hook installation."
  fi
}

main() {
  ensure_python
  create_venv
  install_dependencies
  prepare_environment_file
  ensure_tracked_directories
  install_pre_commit
  echo "Setup complete. Activate the virtual environment with: source ${VENV_PATH}/bin/activate"
}

main "$@"
