"""
Unit tests for the Price Finder Tool.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.laptop_agent.tools.price_finder import find_best_price, _identify_seller


class TestPriceFinder:
    """Test cases for find_best_price tool."""

    @patch("src.laptop_agent.tools.price_finder.TavilyClient")
    def test_successful_price_search(self, mock_tavily):
        """Test that price search returns formatted results."""
        # Arrange
        mock_client = MagicMock()
        mock_tavily.return_value = mock_client
        mock_client.search.return_value = {
            "answer": "Best price for this laptop is ₹55,990 on Amazon",
            "results": [
                {
                    "title": "HP Pavilion 15 - Amazon.in",
                    "url": "https://amazon.in/hp-pavilion-15",
                    "content": "HP Pavilion 15 Intel Core i5 price ₹55,990"
                },
                {
                    "title": "HP Pavilion 15 - Flipkart",
                    "url": "https://flipkart.com/hp-pavilion-15",
                    "content": "HP Pavilion 15 price ₹56,490"
                }
            ]
        }

        # Act
        result = find_best_price("HP Pavilion 15 Intel Core i5")

        # Assert
        assert "HP Pavilion 15 Intel Core i5" in result
        assert "Amazon India" in result
        assert "Flipkart" in result

    @patch("src.laptop_agent.tools.price_finder.TavilyClient")
    def test_empty_results(self, mock_tavily):
        """Test handling when no prices are found."""
        mock_client = MagicMock()
        mock_tavily.return_value = mock_client
        mock_client.search.return_value = {"results": []}

        result = find_best_price("Unknown Laptop XYZ 9999")

        assert "No prices found" in result
        assert "exact model name" in result

    @patch("src.laptop_agent.tools.price_finder.TavilyClient")
    def test_api_error_handling(self, mock_tavily):
        """Test graceful handling of API errors."""
        mock_tavily.side_effect = Exception("API connection failed")

        result = find_best_price("HP Pavilion 15")

        assert "Error finding prices" in result

    def test_identify_seller_amazon(self):
        """Test seller identification for Amazon."""
        result = _identify_seller("https://amazon.in/product/123")
        assert "Amazon" in result

    def test_identify_seller_flipkart(self):
        """Test seller identification for Flipkart."""
        result = _identify_seller("https://flipkart.com/product/123")
        assert "Flipkart" in result

    def test_identify_unknown_seller(self):
        """Test seller identification for unknown seller."""
        result = _identify_seller("https://unknownstore.com/product")
        assert "Online Seller" in result