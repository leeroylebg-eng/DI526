from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CalcDemo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Returns the product of two integers."""
    return a * b


@mcp.resource("ops://list")
def list_ops() -> str:
    """Returns the list of available math operations."""
    return "add\nmultiply"


if __name__ == "__main__":
    mcp.run()
