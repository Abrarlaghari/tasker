#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
[[ -d .venv ]] && source .venv/bin/activate
exec uvicorn tasker.main:app --reload --port 8000
