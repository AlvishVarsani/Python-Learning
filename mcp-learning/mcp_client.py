import os
import json
import asyncio

from openai import OpenAI
from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters #This is for stdio
from mcp.client.sse import sse_client #This is for sse

load_dotenv()
MODEL = os.getenv("GROQ_MODEL")
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


async def main():

    # server_params = StdioServerParameters(
    #     command="python",
    #     args=["/home/alvishvarsani/ALL/Python/Practice/mcp-learning/mcp_server.py"],
    # )

    # async with stdio_client(server_params) as (read_stream, write_stream):
    
    async with sse_client("http://localhost:8000/sse") as (read_stream,write_stream):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            # Discover MCP tools
            tools_result = await session.list_tools()

            print("\nDiscovered MCP Tools:")
            for tool in tools_result.tools:
                print("-", tool.name)

            openai_tools = []

            for tool in tools_result.tools:
                openai_tools.append(
                    {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description or "",
                            "parameters": tool.inputSchema,
                        },
                    }
                )

            while True:

                user_input = input("\nYou: ")

                if user_input.lower() in {"quit", "exit"}:
                    break

                messages = [
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ]

                response = client.chat.completions.create(
                    model=MODEL,
                    messages=messages,
                    tools=openai_tools,
                    tool_choice="auto",
                )

                msg = response.choices[0].message

                # If the model has chosen to call a tool, we need to handle that
                if msg.tool_calls:

                    for tool_call in msg.tool_calls:

                        tool_name = tool_call.function.name

                        arguments = json.loads(
                            tool_call.function.arguments
                        )

                        print(
                            f"\nCalling MCP Tool: "
                            f"{tool_name}({arguments})"
                        )

                        tool_result = await session.call_tool(
                            tool_name,
                            arguments,
                        )

                        result_text = ""

                        for item in tool_result.content:
                            if hasattr(item, "text"):
                                result_text += item.text

                        messages.append(
                            msg.model_dump(exclude_none=True)
                        )

                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": result_text,
                            }
                        )

                    final_response = (
                        client.chat.completions.create(
                            model=MODEL,
                            messages=messages,
                        )
                    )

                    print(
                        "\nAssistant:",
                        final_response.choices[0]
                        .message.content
                    )

                else:
                    print(
                        "\nAssistant:",
                        msg.content
                    )


if __name__ == "__main__":
    asyncio.run(main())