"""
Helper utilities for the Laptop Agent.
"""

from datetime import datetime


def get_current_timestamp() -> str:
    """
    Returns the current timestamp as a formatted string.

    Returns:
        Formatted timestamp string (e.g., '2026-02-23 14:30:00')
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_currency(amount: int) -> str:
    """
    Formats an integer amount as Indian Rupees.

    Args:
        amount: Amount in INR as integer

    Returns:
        Formatted currency string (e.g., '₹40,000')
    """
    return f"₹{amount:,}"


def validate_budget(min_budget: int, max_budget: int) -> tuple[bool, str]:
    """
    Validates that the budget range is logical and within reasonable limits.

    Args:
        min_budget: Minimum budget in INR
        max_budget: Maximum budget in INR

    Returns:
        Tuple of (is_valid: bool, message: str)
    """
    if min_budget <= 0 or max_budget <= 0:
        return False, "Budget values must be greater than zero."

    if min_budget >= max_budget:
        return False, "Minimum budget must be less than maximum budget."

    if min_budget < 10000:
        return False, "Minimum budget should be at least ₹10,000 for laptops."

    if max_budget > 500000:
        return False, "Maximum budget exceeds ₹5,00,000. Please enter a realistic range."

    return True, "Budget range is valid."