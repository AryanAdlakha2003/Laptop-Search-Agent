"""
Price Finder Tool for finding the best prices for a specific laptop model
across multiple online sellers in India.
Uses Tavily Search API to fetch real-time pricing data.
"""

from datetime import datetime
from smolagents import tool
from tavily import TavilyClient
from src.laptop_agent.config import Config


# Major Indian online sellers to search across
INDIAN_SELLERS = [
    "amazon.in",
    "flipkart.com",
    "croma.com",
    "reliance digital",
    "vijay sales",
]


@tool
def find_best_price(laptop_model: str) -> str:
    """
    Finds the best current prices for a specific laptop model
    across major Indian online sellers.

    Args:
        laptop_model: The exact laptop model name to search for
                     (e.g., 'HP Pavilion 15 Intel Core i5 12th Gen')

    Returns:
        A formatted string containing prices from different sellers
        with links to purchase pages, sorted by price.
    """
    try:
        client = TavilyClient(api_key=Config.TAVILY_API_KEY)

        current_year = datetime.now().year

        # Build a targeted price comparison query
        query = (
            f"{laptop_model} best price India {current_year} "
            f"buy online Amazon Flipkart Croma"
        )

        # Search using Tavily
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=Config.MAX_SEARCH_RESULTS,
            include_answer=True,
            # Focus search on shopping/seller domains
            include_domains=INDIAN_SELLERS,
        )

        return _format_price_results(response, laptop_model)

    except Exception as e:
        return f"Error finding prices for '{laptop_model}': {str(e)}"


def _format_price_results(response: dict, laptop_model: str) -> str:
    """
    Formats raw Tavily response into a clean price comparison output.

    Args:
        response: Raw response from Tavily API
        laptop_model: Laptop model name for display

    Returns:
        Formatted string of price comparisons across sellers
    """
    output = []
    output.append(f"💰 Price Comparison: {laptop_model}\n")
    output.append("=" * 60)

    # Add Tavily's summarized answer if available
    if response.get("answer"):
        output.append("\n📋 Price Summary:")
        output.append(response["answer"])
        output.append("")

    results = response.get("results", [])

    if not results:
        return (
            f"No prices found for '{laptop_model}'.\n"
            "Try using the exact model name including generation "
            "and variant (e.g., 'Dell Inspiron 15 3520 i5 12th Gen 16GB')"
        )

    output.append("🛒 Available From These Sellers:\n")

    for i, result in enumerate(results, 1):
        # Identify which seller this result is from
        seller = _identify_seller(result.get("url", ""))

        output.append(f"{i}. {seller}")
        output.append(f"   📄 {result.get('title', 'No title')}")
        output.append(f"   🔗 {result.get('url', '')}")
        output.append(f"   {result.get('content', '')[:250]}...")
        output.append("")

    output.append("⚠️  Note: Prices may vary. Always verify on the seller's website before purchasing.")

    return "\n".join(output)


def _identify_seller(url: str) -> str:
    """
    Identifies the seller name from a URL.

    Args:
        url: The URL of the product page

    Returns:
        Human readable seller name with emoji
    """
    seller_map = {
        "amazon": "🛍️  Amazon India",
        "flipkart": "🛍️  Flipkart",
        "croma": "🛍️  Croma",
        "reliancedigital": "🛍️  Reliance Digital",
        "vijaysales": "🛍️  Vijay Sales",
    }

    url_lower = url.lower()
    for key, name in seller_map.items():
        if key in url_lower:
            return name

    return "🛍️  Online Seller"