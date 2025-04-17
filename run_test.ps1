# PowerShell script to run the MCP client test
Write-Host "🚀 Running MCP client test..." -ForegroundColor Cyan

# Activate conda environment and run the test script
conda activate mcpuse
if ($args.Count -gt 0) {
    python test_mcp_client.py $args[0]
} else {
    python test_mcp_client.py
}
