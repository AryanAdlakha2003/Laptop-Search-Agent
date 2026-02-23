"""
Unit tests for the Laptop Search Tool.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.laptop_agent.tools.laptop_search import search_laptops


class TestLaptopSearch:
    """Test cases for search_laptops tool."""

    @patch("src.laptop_agent.tools.laptop_search.TavilyClient")
    def test_successful_search(self, mock_tavily):
        """Test that search returns formatted results successfully."""
        # Arrange - mock the Tavily response
        mock_client = MagicMock()
        mock_tavily.return_value = mock_client
        mock_client.search.return_value = {
            "answer": "Top laptops in this budget are...",
            "results": [
                {
                    "title": "Best laptops under 60000",
                    "url": "https://example.com",
                    "content": "Here are the best laptops..."
                }
            ]
        }

        # Act
        result = search_laptops(40000, 60000, "student")

        # Assert
        assert "₹40,000" in result
        assert "₹60,000" in result
        assert "Best laptops under 60000" in result

    @patch("src.laptop_agent.tools.laptop_search.TavilyClient")
    def test_empty_results(self, mock_tavily):
        """Test handling when no results are returned."""
        mock_client = MagicMock()
        mock_tavily.return_value = mock_client
        mock_client.search.return_value = {"results": []}

        result = search_laptops(40000, 60000)

        assert "No laptops found" in result

    @patch("src.laptop_agent.tools.laptop_search.TavilyClient")
    def test_api_error_handling(self, mock_tavily):
        """Test graceful handling of API errors."""
        mock_tavily.side_effect = Exception("API Error")

        result = search_laptops(40000, 60000)

        assert "Error searching for laptops" in result