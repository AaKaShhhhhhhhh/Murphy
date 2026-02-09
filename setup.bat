@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "PROJECT_ROOT=%~dp0"
cd /d "%PROJECT_ROOT%" || (echo [setup][ERROR] Failed to cd to project root & exit /b 1)

echo [setup] Checking prerequisites...

where python >nul 2>nul || (echo [setup][ERROR] Python not found on PATH & exit /b 1)
where node >nul 2>nul || (echo [setup][ERROR] Node.js not found on PATH & exit /b 1)
where npm >nul 2>nul || (echo [setup][ERROR] npm not found on PATH & exit /b 1)

for /f "usebackq tokens=1,2" %%A in (`python -c "import sys; print(f'{sys.version_info.major} {sys.version_info.minor}')"`) do (
  set "PY_MAJOR=%%A"
  set "PY_MINOR=%%B"
)
if not defined PY_MAJOR (echo [setup][ERROR] Could not detect Python version & exit /b 1)

if %PY_MAJOR% LSS 3 (
  echo [setup][ERROR] Python 3.10+ required (found %PY_MAJOR%.%PY_MINOR%)
  exit /b 1
)
if %PY_MAJOR% EQU 3 if %PY_MINOR% LSS 10 (
  echo [setup][ERROR] Python 3.10+ required (found %PY_MAJOR%.%PY_MINOR%)
  exit /b 1
)

for /f "usebackq tokens=1 delims=." %%A in (`node -p "process.versions.node"`) do set "NODE_MAJOR=%%A"
if not defined NODE_MAJOR (echo [setup][ERROR] Could not detect Node.js version & exit /b 1)
if %NODE_MAJOR% LSS 16 (
  for /f "usebackq" %%V in (`node -v`) do set "NODE_VER=%%V"
  echo [setup][ERROR] Node.js 16+ required (found %NODE_VER%)
  exit /b 1
)

echo [setup] Ensuring project folders exist...
for %%D in (
  "mcp-servers\slack-server"
  "mcp-servers\monitoring-server"
  "mcp-servers\github-server"
  "agents"
  "workflows"
  "ui"
  "docs"
  "tests"
) do (
  if not exist %%D mkdir %%D >nul 2>nul
)

where uv >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
  echo [setup] uv not found; installing uv...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "iwr -useb https://astral.sh/uv/install.ps1 | iex"
  if %ERRORLEVEL% NEQ 0 (
    echo [setup][ERROR] Failed to install uv. Install manually from https://astral.sh/uv
    exit /b 1
  )
)

REM Re-check uv (may not be in PATH in this session)
where uv >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
  set "UV_EXE=%USERPROFILE%\.local\bin\uv.exe"
  if exist "%UV_EXE%" (
    set "UV=%UV_EXE%"
  ) else (
    set "UV_EXE=%USERPROFILE%\.cargo\bin\uv.exe"
    if exist "%UV_EXE%" (
      set "UV=%UV_EXE%"
    ) else (
      echo [setup][ERROR] uv installed but not found on PATH.
      echo [setup][ERROR] Restart your terminal or add %USERPROFILE%\.local\bin (or .cargo\bin) to PATH.
      exit /b 1
    )
  )
) else (
  set "UV=uv"
)

echo [setup] Installing MCP Inspector globally (npm)...
npm ls -g --depth=0 @modelcontextprotocol/inspector >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  echo [setup] MCP Inspector already installed.
) else (
  npm install -g @modelcontextprotocol/inspector
  if %ERRORLEVEL% NEQ 0 (
    echo [setup][WARN] Failed to install MCP Inspector globally. You may need admin rights.
    echo [setup][WARN] Continuing setup...
  )
)

echo [setup] Creating uv virtual environment in .venv...
"%UV%" venv .venv
if %ERRORLEVEL% NEQ 0 (echo [setup][ERROR] Failed to create venv & exit /b 1)

echo [setup] Installing Python dependencies (editable + dev extras)...
"%UV%" pip install -e ".[dev]"
if %ERRORLEVEL% NEQ 0 (
  echo [setup][ERROR] Failed to install dependencies.
  echo [setup][ERROR] If this is a network/cert issue, retry or configure your proxy.
  exit /b 1
)

echo [setup] Done. Next steps:
echo [setup] - Copy env file: copy .env.example .env
echo [setup] - Run UI (once ui\app.py exists): uv run streamlit run ui\app.py

endlocal
exit /b 0
