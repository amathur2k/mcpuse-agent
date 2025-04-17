@echo off
echo 🚀 Running MCP client test...
call conda activate mcpuse

REM Check if a task was provided
if "%1"=="" (
    python test_mcp_client.py --timeout 300
) else (
    python test_mcp_client.py --task "%*" --timeout 300
)
