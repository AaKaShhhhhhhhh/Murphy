@echo off

:: Set up the environment
cd /d %~dp0

:: Step 1: Install dependencies
echo Installing dependencies...
pip install -r ui/requirements.txt

:: Step 2: Configure environment variables
echo Ensure .env files are configured for all servers.
if not exist mcp-servers\github-server\.env (
    echo Missing .env file for GitHub MCP server. Please configure it.
    pause
    exit /b
)
if not exist mcp-servers\slack-server\.env (
    echo Missing .env file for Slack MCP server. Please configure it.
    pause
    exit /b
)

:: Step 3: Start MCP servers
echo Starting GitHub MCP server...
start cmd /k "python mcp-servers/github-server/server.py"

echo Starting Slack MCP server...
start cmd /k "python mcp-servers/slack-server/server.py"

echo Starting Monitoring MCP server...
start cmd /k "python mcp-servers/monitoring-server/server.py"

:: Step 4: Start the Streamlit dashboard
echo Starting Streamlit dashboard...
cd ui
start cmd /k "streamlit run dashboard.py"
cd ..

:: Step 5: Final message
echo All components started. Open the dashboard at http://localhost:8501
pause