from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b


@mcp.tool()
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

if __name__ == "__main__":
 """This use for the stdio transport, which is the default transport for MCP.
It allows the server to communicate with the client over standard input and output streams.
"""    
#mcp.run() 

""" If you want to run the server with an HTTP transport instead, you can use the following code.
This will start an HTTP server on port 8000, and the client can communicate with it using HTTP requests.
"""
mcp.run(transport="sse")