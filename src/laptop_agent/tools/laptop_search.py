"""
Laptop Search Tool for finding and comparing laptops within a budget range.
Uses Tavily Search API to fetch real-time laptop data.
"""

from smolagents import tool
from tavily import TavilyClient
from datetime import datetime
from src.laptop_agent.config import Config


@tool
def search_laptops(
    min_budget: int,
    max_budget: int,
    preferences: str = ""
) -> str:
    """
    Searches for laptops within a specified budget range and returns
    a comparison of the best options available.

    Args:
        min_budget: Minimum budget in INR (e.g., 40000)
        max_budget: Maximum budget in INR (e.g., 60000)
        preferences: Optional preferences like 'gaming', 'lightweight',
                    'business', 'student' etc.

    Returns:
        A formatted string containing laptop recommendations with
        specs and approximate prices.
    """
    try:
        client = TavilyClient(api_key=Config.TAVILY_API_KEY)
        current_year = datetime.now().year
        # Build a specific search query
        query = (
            f"best laptops in India between {min_budget} to {max_budget} rupees "
            f"{current_year} specifications comparison"
        )

        # Add preferences to query if provided
        if preferences:
            query += f" for {preferences}"

        # Search using Tavily
        response = client.search(
            query=query,
            search_depth="advanced",        # deeper, better results
            max_results=Config.MAX_SEARCH_RESULTS,
            include_answer=True,            # get a summarized answer too
        )

        # Format the results cleanly for the agent
        return _format_laptop_results(response, min_budget, max_budget)

    except Exception as e:
        return f"Error searching for laptops: {str(e)}"


def _format_laptop_results(
    response: dict,
    min_budget: int,
    max_budget: int
) -> str:
    """
    Formats raw Tavily response into clean readable output for the agent.

    Args:
        response: Raw response from Tavily API
        min_budget: Minimum budget for display
        max_budget: Maximum budget for display

    Returns:
        Formatted string of laptop results
    """
    output = []
    output.append(
        f"🔍 Laptop Search Results (Budget: ₹{min_budget:,} - ₹{max_budget:,})\n"
    )
    output.append("=" * 60)

    # Add Tavily's summarized answer if available
    if response.get("answer"):
        output.append("\n📋 Summary:")
        output.append(response["answer"])
        output.append("")

    # Add individual search results
    results = response.get("results", [])

    if not results:
        return "No laptops found for the given budget range. Try adjusting your budget."

    output.append(f"📌 Top {len(results)} Sources Found:\n")

    for i, result in enumerate(results, 1):
        output.append(f"{i}. {result.get('title', 'No title')}")
        output.append(f"   🔗 {result.get('url', '')}")
        output.append(f"   {result.get('content', '')[:200]}...")  # first 200 chars
        output.append("")

    return "\n".join(output)