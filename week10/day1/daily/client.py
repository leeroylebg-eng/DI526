import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="mcp", args=["run", "server.py"], env=None
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # 1. Initialize
            await session.initialize()
            print("Session initialized ✅\n")

            # 2. List resources
            resources = await session.list_resources()
            print("=== Resources ===")
            if resources.resources:
                for r in resources.resources:
                    print(f"  - {r.name}: {r.uri}")
            else:
                print("  (none)")

            # 3. List tools
            tools = await session.list_tools()
            print("\n=== Tools ===")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description}")

            # 4. Read cities://list
            content = await session.read_resource("cities://list")
            print("\n=== cities://list ===")
            print(content.contents[0].text)

            # 5. Call get_weather for Paris
            result = await session.call_tool("get_weather", {"city": "Paris"})
            raw = result.content[0].text
            print("=== get_weather('Paris') ===")
            # Pretty-print if JSON
            try:
                print(json.dumps(json.loads(raw), indent=2))
            except Exception:
                print(raw)

            # 6. Test unknown city (error handling)
            result_err = await session.call_tool("get_weather", {"city": "Atlantis"})
            print("\n=== get_weather('Atlantis') — error handling ===")
            print(result_err.content[0].text)


if __name__ == "__main__":
    asyncio.run(run())
