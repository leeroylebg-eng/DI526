import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AirbnbStub")

LISTINGS = {
    "paris": [
        {"id": "P001", "name": "Cozy Studio near Eiffel Tower", "price_night": 85,  "rating": 4.8},
        {"id": "P002", "name": "Montmartre Artist Loft",         "price_night": 110, "rating": 4.6},
        {"id": "P003", "name": "Modern Flat in Le Marais",        "price_night": 130, "rating": 4.9},
    ],
    "london": [
        {"id": "L001", "name": "Shoreditch Brick Lane Apartment", "price_night": 95,  "rating": 4.7},
        {"id": "L002", "name": "Covent Garden Studio",            "price_night": 120, "rating": 4.5},
    ],
    "nyc": [
        {"id": "N001", "name": "Brooklyn Heights Studio",   "price_night": 150, "rating": 4.8},
        {"id": "N002", "name": "Manhattan Midtown Room",    "price_night": 200, "rating": 4.4},
    ],
}


@mcp.tool()
def airbnb_search(city: str, max_price: int = 500) -> str:
    """Search Airbnb listings for a city. Optionally filter by max price per night."""
    results = LISTINGS.get(city.lower(), [])
    filtered = [l for l in results if l["price_night"] <= max_price]
    if not filtered:
        return json.dumps({"listings": [], "city": city,
                           "message": f"No listings under ${max_price}/night."})
    return json.dumps({"city": city, "count": len(filtered), "listings": filtered}, indent=2)


if __name__ == "__main__":
    mcp.run()
