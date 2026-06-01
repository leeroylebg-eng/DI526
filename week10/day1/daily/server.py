import logging
import sys
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                    format="[SERVER] %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

mcp = FastMCP("WeatherDemo")

WEATHER_DB = {
    "paris":  {"city": "Paris",  "temp_c": 21, "condition": "sunny"},
    "london": {"city": "London", "temp_c": 14, "condition": "cloudy"},
    "nyc":    {"city": "NYC",    "temp_c": 18, "condition": "partly cloudy"},
    "tokyo":  {"city": "Tokyo",  "temp_c": 26, "condition": "humid"},
    "sydney": {"city": "Sydney", "temp_c": 22, "condition": "clear"},
}


@mcp.tool()
def get_weather(city: str) -> dict:
    """Returns static weather data for a supported city."""
    logger.info(f"get_weather called → city={city!r}")
    data = WEATHER_DB.get(city.lower())
    if data:
        return data
    supported = ", ".join(c.title() for c in WEATHER_DB)
    return {"error": f"City '{city}' not found. Supported: {supported}"}


@mcp.resource("cities://list")
def list_cities() -> str:
    """Returns a newline-separated list of supported cities."""
    logger.info("cities://list resource read")
    return "\n".join(c.title() for c in WEATHER_DB)


if __name__ == "__main__":
    mcp.run()
