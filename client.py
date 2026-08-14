from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "maths":{
                "command":"python",
                "args":["mathserver.py"],## ensure absolute location of the file
                "transport":"stdio"
            },
            "weather":{
                "url":"http://127.0.0.1:8000/mcp", #ensure server is running here
                "transport":"streamable-http"
            }
        }
    )
    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="llama3.1:latest")
    agent = create_react_agent(model,tools)

    math_response = await agent.ainvoke({"messages":[
        {"role":"user","content":"what is 2345 * 1097"}
    ]})

    weather_response = await agent.ainvoke({"messages":[
        {"role":"user","content":"what is the weather like today"}
    ]})

    print("math response",math_response["messages"][-1].content)
    print("weather response",weather_response["messages"][-1].content)

asyncio.run(main())

    
    

    