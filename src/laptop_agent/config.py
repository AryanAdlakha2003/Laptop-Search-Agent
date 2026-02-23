"""
Configuration management for Laptop Agent.
Loads and validates all environment variables and project-wide constants.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Central configuration class.
    All settings and constants are defined here.
    """

    # -------------------------
    # API Keys
    # -------------------------
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")

    # -------------------------
    # Model Settings
    # -------------------------
    MODEL_ID: str = "groq/llama-3.3-70b-versatile"
    MAX_TOKENS: int = 2096
    TEMPERATURE: float = 0.5

    # -------------------------
    # Agent Settings
    # -------------------------
    MAX_STEPS: int = 10
    VERBOSITY_LEVEL: int = 1

    # -------------------------
    # Search Settings
    # -------------------------
    MAX_SEARCH_RESULTS: int = 5

    # -------------------------
    # App Settings
    # -------------------------
    APP_TITLE: str = "💻 Laptop Buying Agent"
    APP_DESCRIPTION: str = (
        "I help you find and compare laptops within your budget "
        "and find the best prices from online sellers."
    )
    SERVER_PORT: int = 7860
    SHARE_APP: bool = False

    PROMPTS_PATH: str = "prompts/prompts.yaml"


def validate_config() -> None:
    """
    Validates that all required environment variables are set.
    Raises EnvironmentError if any required key is missing.
    """
    required_keys = {
        "GROQ_API_KEY": Config.GROQ_API_KEY,
        "TAVILY_API_KEY": Config.TAVILY_API_KEY,
    }

    missing = [key for key, value in required_keys.items() if not value]

    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            "Please check your .env file."
        )

    print("✅ Configuration validated successfully.")