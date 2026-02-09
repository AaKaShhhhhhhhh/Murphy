#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

info() { echo "[setup] $*"; }
warn() { echo "[setup][WARN] $*" >&2; }
err() { echo "[setup][ERROR] $*" >&2; }

die() {
  err "$*"
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "Missing required command: $1"
}

version_ge() {
  # returns 0 if $1 >= $2 (semver-ish, numeric dot segments)
  # usage: version_ge "3.10" "3.9"
  local a b IFS=.
  read -r -a a <<<"$1"
  read -r -a b <<<"$2"
  local len=${#a[@]}
  (( ${#b[@]} > len )) && len=${#b[@]}
  for ((i=0; i<len; i++)); do
    local ai=${a[i]:-0}
    local bi=${b[i]:-0}
    if ((10#$ai > 10#$bi)); then return 0; fi
    if ((10#$ai < 10#$bi)); then return 1; fi
  done
  return 0
}

info "Checking prerequisites..."
require_cmd python
require_cmd node
require_cmd npm

PY_VER="$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")"
if ! version_ge "$PY_VER" "3.10"; then
  die "Python 3.10+ required (found $PY_VER)."
fi

NODE_VER_RAW="$(node -v | sed 's/^v//')"
NODE_MAJOR="${NODE_VER_RAW%%.*}"
if [[ -z "$NODE_MAJOR" ]] || (( NODE_MAJOR < 16 )); then
  die "Node.js 16+ required (found v$NODE_VER_RAW)."
fi

info "Ensuring project folders exist..."
mkdir -p \
  mcp-servers/slack-server \
  mcp-servers/monitoring-server \
  mcp-servers/github-server \
  agents workflows ui docs tests

if ! command -v uv >/dev/null 2>&1; then
  info "uv not found; installing uv..."
  if command -v curl >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
  elif command -v wget >/dev/null 2>&1; then
    wget -qO- https://astral.sh/uv/install.sh | sh
  else
    die "Neither curl nor wget found; install uv manually: https://astral.sh/uv"
  fi

  # Try common install locations
  export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

  command -v uv >/dev/null 2>&1 || die "uv installed but not on PATH. Restart your shell or add ~/.local/bin (or ~/.cargo/bin) to PATH."
fi

info "Installing MCP Inspector globally (npm)..."
if npm ls -g --depth=0 @modelcontextprotocol/inspector >/dev/null 2>&1; then
  info "MCP Inspector already installed."
else
  if ! npm install -g @modelcontextprotocol/inspector; then
    warn "Failed to install MCP Inspector globally via npm."
    warn "You may need admin rights or a user-level npm prefix."
    warn "Continuing setup (Inspector install is optional for running code)."
  fi
fi

info "Creating uv virtual environment in .venv..."
uv venv .venv

info "Installing Python dependencies (editable + dev extras)..."
# Use uv's pip interface to install from pyproject.toml
uv pip install -e ".[dev]"

info "Done. Next steps:"
info "- Copy env file: cp .env.example .env"
info "- Run UI (once ui/app.py exists): uv run streamlit run ui/app.py"
