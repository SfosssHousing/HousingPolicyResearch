#!/usr/bin/env bash
set -euo pipefail

# Paths (edit to match your environment)
SRC_DIR="${HOME}/Downloads"
TARGET_DIR="$(git rev-parse --show-toplevel)/Capstone/indexes"

# Pattern(s) to move
PATTERN='cross_chat_*.csv'

# Ensure target exists
mkdir -p "$TARGET_DIR"

shopt -s nullglob
moved_any=0
for f in "${SRC_DIR}"/$PATTERN; do
  ts=$(date +"%Y%m%d_%H%M%S")
  base="$(basename "$f")"
  # Normalize to dated name if not already dated
  if [[ "$base" =~ ^cross_chat_.*\.csv$ ]]; then
    new="cross_chat_${ts}.csv"
  else
    new="${base%.csv}_${ts}.csv"
  fi
  mv -v "$f" "${TARGET_DIR}/${new}"
  moved_any=1
done
shopt -u nullglob

if [[ $moved_any -eq 0 ]]; then
  echo "No files matching '${PATTERN}' in ${SRC_DIR}"
  exit 0
fi

# Optional Git commit if run with --commit
if [[ "${1-}" == "--commit" ]]; then
  if git -C "$TARGET_DIR/.." rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    REPO_DIR="$(cd "$TARGET_DIR/.." && pwd)"
    git -C "$REPO_DIR" add indexes
    git -C "$REPO_DIR" commit -m "chore(indexes): update cross-chat CSVs $(date +"%Y-%m-%d %H:%M:%S")"
    echo "Committed to Git repo at $REPO_DIR"
  else
    echo "Note: ${TARGET_DIR}/.. is not a Git repo. Skipping commit."
  fi
fi
