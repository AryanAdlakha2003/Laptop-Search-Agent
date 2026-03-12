"""
Laptop Agent - Gradio UI
Entry point for the application.
"""

import gradio as gr
from src.laptop_agent.agent import create_agent
from src.laptop_agent.config import Config

# Initialize agent once at startup
agent = create_agent()


def chat(message: str, history: list) -> str:
    """
    Processes user message and returns agent response.

    Args:
        message: User's input message
        history: Conversation history from Gradio

    Returns:
        Agent's response as a string
    """
    try:
        response = agent.run(message)
        return str(response)
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"


def create_ui() -> gr.Blocks:
    """
    Creates and configures the Gradio UI.

    Returns:
        Configured Gradio Blocks interface
    """
    with gr.Blocks(title=Config.APP_TITLE) as demo:

        # Header
        gr.Markdown(
            """
            # 💻 Laptop Buying Assistant
            ### Your AI-powered laptop advisor for the Indian market

            I can help you:
            - 🔍 Find laptops within your budget
            - 📊 Compare specifications
            - 💰 Find the best prices across Amazon, Flipkart, Croma and more

            **Just tell me your budget and what you'll use the laptop for!**
            """
        )

        # Chat interface
        chatbot = gr.ChatInterface(
            fn=chat,
            chatbot=gr.Chatbot(
                height=500,
                placeholder="Ask me about laptops! e.g. 'Find me laptops between 40000 and 60000 rupees for a student'",
            ),
            textbox=gr.Textbox(
                placeholder="Type your message here...",
                container=False,
                scale=7,
            ),
            examples=[
                "Find me the best laptops between 40000 and 60000 rupees for a student",
                "What are good gaming laptops under 80000 rupees?",
                "Find best price for ASUS Vivobook 16 Intel Core i5 13th Gen",
                "I need a lightweight laptop for business under 70000 rupees",
            ],
        )

        # Footer
        gr.Markdown(
            """
            ---
            ⚠️ **Disclaimer:** Prices shown are indicative. Always verify on the seller's
            website before purchasing. Prices may change without notice.
            """
        )

    return demo

def chat(message: str, history: list) -> str:
    """
    Processes user message and returns agent response.

    Args:
        message: User's input message
        history: Conversation history from Gradio

    Returns:
        Agent's response as a string
    """
    try:
        response = agent.run(message)
        if response is None:
            return "I found some options! Please check the results above and let me know which laptop you'd like to explore further."
        return str(response)
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

if __name__ == "__main__":
    ui = create_ui()
    ui.launch(
        server_port=Config.SERVER_PORT,
        share=Config.SHARE_APP,
        show_error=True,
        theme=gr.themes.Soft(),   # 👈 moved to launch() for Gradio 6.0
    )