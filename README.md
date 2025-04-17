# MCP Client Console Application

A simple console application that uses the Model Control Protocol (MCP) to interact with a Playwright MCP server. This application allows you to give tasks to an LLM which will call tools from the MCP server to respond, while printing out which tools it's calling.

## Prerequisites

- Python 3.8 or higher
- Node.js and npm (for running the Playwright MCP server)

## Installation

1. Install the required Python packages:

```
pip install -r requirements.txt
```

2. Set your OpenAI API key in the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Run the MCP client console application:

```
python mcp_client.py
```

2. Enter your task when prompted. The application will:
   - Connect to the Playwright MCP server
   - Process your task using the LLM
   - Display which tools are being called
   - Show the final result

3. Type 'exit' to quit the application.

## Example Tasks

- "Search for information about climate change and summarize the top result"
- "Go to github.com and find the trending repositories"
- "Visit openai.com and tell me what products they offer"

## Configuration

The MCP server configuration is stored in `mcp_config.json`. You can modify this file to change the server settings.

## How It Works

1. The application creates an MCP client that connects to the Playwright MCP server
2. It initializes an LLM (GPT-4o) to process your tasks
3. When you enter a task, the LLM determines which tools to call
4. The application displays each tool call and its inputs/outputs
5. Finally, it shows the result of your task

## References

- [mcp-use GitHub Repository](https://github.com/pietrozullo/mcp-use)
- [Playwright MCP GitHub Repository](https://github.com/microsoft/playwright-mcp)
