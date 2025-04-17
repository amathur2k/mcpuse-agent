import asyncio
import os
import sys
import time
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('mcp_test')

async def run_test(task="navigate to bluestone.com", timeout=60):
    """Run the MCP client with a specific task."""
    print(f"🧪 Testing MCP client with task: '{task}'")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY") == "your_openai_api_key_here":
        print("⚠️ Please set your OPENAI_API_KEY in the .env file")
        return
    
    try:
        # Create MCPClient from configuration file
        logger.debug("Creating MCPClient from config file")
        client = MCPClient.from_config_file("mcp_config.json")
        
        # Create LLM
        logger.debug("Creating LLM")
        llm = ChatOpenAI(model="gpt-4o-mini")
        
        # Create agent with the client
        logger.debug("Creating MCPAgent")
        agent = MCPAgent(
            llm=llm, 
            client=client, 
            max_steps=30,
            verbose=True
        )
    except Exception as e:
        logger.error(f"Error during initialization: {str(e)}")
        print(f"\n❌ ERROR during initialization: {str(e)}")
        return
    
    print("🤖 Starting test run...")
    print(f"🔍 Task: {task}")
    
    try:
        # Run the query with timeout
        print("\n⏳ Processing the task...")
        print("\n🔧 Tool calls will be displayed in the agent's verbose output...")
        print(f"\n⏲ Timeout set to {timeout} seconds...")
        
        start_time = time.time()
        
        # First, try to initialize the agent with a short timeout
        logger.debug("Initializing agent")
        try:
            init_task = asyncio.create_task(agent.initialize())
            await asyncio.wait_for(init_task, timeout=15)
            logger.debug("Agent initialized successfully")
        except asyncio.TimeoutError:
            print("\n⚠️ Initialization timeout! The MCP server is taking too long to start.")
            print("\n🔍 This is likely due to issues with the Playwright MCP server.")
            print("\n💡 Try running 'npx @playwright/mcp@latest' manually to check for errors.")
            return
        except Exception as e:
            logger.error(f"Error during agent initialization: {str(e)}")
            print(f"\n❌ ERROR during agent initialization: {str(e)}")
            return
            
        # Now run the task with the main timeout
        logger.debug(f"Running task: {task}")
        try:
            result = await asyncio.wait_for(agent.run(task), timeout=timeout)
            end_time = time.time()
            logger.debug("Task completed successfully")
        except asyncio.TimeoutError:
            print("\n⚠️ Timeout reached! The operation took too long to complete.")
            print("\n🔍 This might be due to issues with the Playwright MCP server.")
            print("\n💡 Try checking the mcp_config.json file and ensure the arguments are correct.")
            return
        except Exception as e:
            logger.error(f"Error during task execution: {str(e)}")
            print(f"\n❌ ERROR during task execution: {str(e)}")
            return
        
        # Print result
        print("\n✅ RESULT:")
        print(result)
        print(f"\n⏱️ Time taken: {end_time - start_time:.2f} seconds")
        print("\n🎉 Test completed successfully!")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\n❌ Test failed!")

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Test the MCP client with a specific task')
    parser.add_argument('--task', default='navigate to bluestone.com', help='Task to run in the MCP client')
    parser.add_argument('--timeout', type=int, default=60, help='Timeout in seconds for the MCP client')
    args = parser.parse_args()
    
    # Run the test
    asyncio.run(run_test(args.task, args.timeout))
