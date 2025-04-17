@echo off
echo Running MCP client test...
call conda activate mcpuse
python temp_test_script.py
exit /b %ERRORLEVEL%
