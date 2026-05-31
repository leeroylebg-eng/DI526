import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Spawn server.py via the mcp CLI over STDIO
server_params = StdioServerParameters(
    command="mcp", args=["run", "server.py"], env=None
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # 1. Initialise the session
            await session.initialize()
            print("Session initialized ✅\n")

            # 2. List resource templates (greeting://{name} is a template, not a static resource)
            templates = await session.list_resource_templates()
            print("=== Resource Templates ===")
            if templates.resourceTemplates:
                for t in templates.resourceTemplates:
                    print(f"  - {t.name}: {t.uriTemplate}")
            else:
                print("  (none)")

            # Also list any concrete resources
            resources = await session.list_resources()
            print("\n=== Concrete Resources ===")
            if resources.resources:
                for r in resources.resources:
                    print(f"  - {r.name}: {r.uri}")
            else:
                print("  (none — greeting is a template)")

            # 3. List tools
            tools = await session.list_tools()
            print("\n=== Tools ===")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description}")

            # 4. Read greeting://hello (substitutes {name} = "hello")
            content = await session.read_resource("greeting://hello")
            print("\n=== Read greeting://hello ===")
            print(f"  {content.contents[0].text}")

            # 5. Call the add tool with a=1, b=7
            result = await session.call_tool("add", {"a": 1, "b": 7})
            print("\n=== Call add(a=1, b=7) ===")
            print(f"  Result: {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(run())
