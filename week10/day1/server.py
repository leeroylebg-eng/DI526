from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


@mcp.resource("greeting://{name}")
def greet(name: str) -> str:
    """Returns a personalized greeting for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
