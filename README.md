# Intelligent Incident Response (Hackathon)

An "Intelligent Incident Response" system built for a hackathon using:
- **MCP (Model Context Protocol)** servers for tool access (Slack, GitHub, Monitoring)
- **Archestra.AI** for orchestration of agents/workflows
- **Streamlit** for a lightweight incident dashboard

This repo is intentionally structured for fast iteration with clear separation between:
- **tooling (MCP servers)**
- **decisioning (agents + workflows)**
- **presentation (UI)**

## Project Structure

```
intelligent-incident-response/
  mcp-servers/
    slack-server/          # MCP server that posts/reads Slack signals
    monitoring-server/     # MCP server that ingests metrics/logs/alerts
    github-server/         # MCP server for GitHub issues, PRs, incidents-as-code
  agents/                  # Archestra.AI agent configurations
  workflows/               # Orchestration workflows / playbooks
  ui/                      # Streamlit dashboard
  docs/                    # Documentation (architecture, runbooks)
  tests/                   # Unit/integration tests
  .env.example             # Environment variable template
  .gitignore
  pyproject.toml
  setup.sh                 # Mac/Linux setup
  setup.bat                # Windows setup
```

## Quick Start

### 1) Prerequisites

- Python **3.10+**
- Node.js **16+** (used for the MCP Inspector)

### 2) Setup

Mac/Linux:

```bash
cd intelligent-incident-response
./setup.sh
```

Windows (cmd.exe):

```bat
cd intelligent-incident-response
setup.bat
```

### 3) Configure environment

Copy the example env file and fill in your secrets:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 4) Run the Streamlit UI

Once setup is complete:

```bash
uv run streamlit run ui/app.py
```

(You will create `ui/app.py` as part of the UI implementation.)

## Development Notes

- Python dependencies are managed via **uv** (fast, reproducible installs).
- MCP Inspector is installed via **npm** and can be used to connect to MCP servers during development.
- Secrets should go in `.env` (never commit it).

## Next Implementation Steps (suggested)

- Implement each MCP server entrypoint under `mcp-servers/*`.
- Define Archestra.AI agents under `agents/` and workflows/playbooks under `workflows/`.
- Add a minimal Streamlit dashboard in `ui/` to show open incidents and recommended actions.
- Add tests in `tests/` for server handlers and workflow logic.
