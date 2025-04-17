import asyncio
import os
import json
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY") == "your_openai_api_key_here":
        print("⚠️ Please set your OPENAI_API_KEY in the .env file")
        return
    
    # Create MCPClient from configuration file
    client = MCPClient.from_config_file("mcp_config.json")
    
    # Create LLM
    llm = ChatOpenAI(model="gpt-4.1")
    
    # Create agent with the client
    agent = MCPAgent(
        llm=llm, 
        client=client, 
        max_steps=30,
        verbose=True
    )
    
    print("🤖 MCP Client Console Application")
    print("--------------------------------")
    print("Type 'exit' to quit the application")
    
    while True:
        # Get user input
        user_query = input("\n🔍 Enter your task: ")
        
        # Check if user wants to exit
        if user_query.lower() == 'exit':
            print("👋 Goodbye!")
            break
        
        try:
            # Run the query
            print("\n⏳ Processing your request...")
            print("\n🔧 Tool calls will be displayed in the agent's verbose output...")
            start_time = time.time()
            result = await agent.run(user_query)
            end_time = time.time()
            
            # Print result
            print("\n✅ RESULT:")
            print(result)
            print(f"\n⏱️ Time taken: {end_time - start_time:.2f} seconds")
            
        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
