from openai import OpenAI
from dotenv import load_dotenv
from mcp_client import (connect, disconnect, discover_tools, execute_tool)
import asyncio
import os

#Load Configuration
load_dotenv()

#Create AI Client
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

def build_tool_descriptions(tools):
    descriptions = ""
    for tool in tools:
        descriptions += f"""Tool: {tool.name} Description: {tool.description}
        ---------------------------"""
    
    return descriptions

def planner(user_request, tools):
    
    tool_description = build_tool_descriptions(tools)

    prompt=f"""
        You are an AI Planner. Available tools {tool_description}
        Instructions
        1. Select the best tool
        2. Reply ONLY with the tool name
        3. Do not explain
        User Request: {user_request}
        """

    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    tool_name = response.choices[0].message.content

    return tool_name.strip()

def generate_response(user_request, tool_result):

    prompt = f"""
        The user asked: {user_request}
        The tool returned: {tool_result}
        Answer naturally.
        """

    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


async def main():
    client = await connect()

    tools = await discover_tools(client)
    
    print()
    print("Available tools")
    print("---------------")

    for tool in tools:
        print(tool.name)

    user_request = input("User: ")
    tool_name = planner(user_request, tools)

    print()
    print("Planner Selected: ", tool_name)

    tool_result = await execute_tool(client, tool_name)

    print(tool_result)

    final_answer = generate_response(user_request, tool_result)

    print()
    print(final_answer)

    await disconnect(client)

if __name__ == "__main__":
    asyncio.run(main())


