"""
Agent configuration and initialization for the Laptop Agent.
Sets up the CodeAgent with all tools and model.
Prompts are loaded from prompts/prompts.yaml for clean separation of concerns.
"""

import yaml
from smolagents import CodeAgent, LiteLLMModel
from src.laptop_agent.config import Config, validate_config
from src.laptop_agent.tools.laptop_search import search_laptops
from src.laptop_agent.tools.price_finder import find_best_price


def _load_prompts() -> dict:
    """
    Loads prompt templates from the prompts.yaml file.

    Returns:
        Dictionary containing all prompt templates.

    Raises:
        FileNotFoundError: If prompts.yaml does not exist.
    """
    try:
        with open(Config.PROMPTS_PATH, "r", encoding="utf-8") as f:  # 👈 add encoding
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Prompts file not found at '{Config.PROMPTS_PATH}'. "
            "Please ensure prompts/prompts.yaml exists."
        )


def create_agent() -> CodeAgent:
    """
    Creates and configures the Laptop Agent with all tools and model.
    Loads system prompt from prompts.yaml.

    Returns:
        Configured CodeAgent instance ready to run.

    Raises:
        EnvironmentError: If required API keys are missing.
        FileNotFoundError: If prompts.yaml is missing.
    """
    # Step 1 - Validate all config before proceeding
    validate_config()

    # Step 2 - Load prompts from yaml
    prompts = _load_prompts()

    # Step 3 - Initialize the model
    model = LiteLLMModel(
        model_id=Config.MODEL_ID,
        api_key=Config.GROQ_API_KEY,
        max_tokens=Config.MAX_TOKENS,
        temperature=Config.TEMPERATURE,
    )

    # print(Config.GROQ_API_KEY)  # Debugging line to check if API key is loaded correctly

    # Step 4 - Initialize the agent with all tools and system prompt
    agent = CodeAgent(
        model=model,
        tools=[
            search_laptops,
            find_best_price,
        ],
        max_steps=Config.MAX_STEPS,
        verbosity_level=Config.VERBOSITY_LEVEL,
        instructions=prompts["instructions"],
    )

    print("✅ Configuration validated successfully.")
    print("✅ Prompts loaded from prompts.yaml.")
    print("✅ Tools loaded: search_laptops, find_best_price.")
    print("✅ Laptop Agent initialized successfully.")

    return agent