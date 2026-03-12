# 💻 Laptop Buying Agent

An AI-powered laptop recommendation and price comparison agent for the Indian market. Built with [smolagents](https://github.com/huggingface/smolagents), [Groq](https://groq.com), and [Gradio](https://gradio.app).

## 📌 What It Does

- 🔍 **Find laptops** within your budget range with real-time search
- 📊 **Compare specs** across multiple models
- 💰 **Find best prices** across Amazon, Flipkart, Croma, Reliance Digital and more
- 🤖 **AI-powered** — understands natural language queries

---

## 🖥️ Demo

> Type your query in natural language:

```
"Find me the best laptops between 40000 and 60000 rupees for a student"
"What are good gaming laptops under 80000 rupees?"
"Find best price for ASUS Vivobook 16 Intel Core i5 13th Gen"
"I need a lightweight laptop for business under 70000 rupees"
```

---

## 🏗️ Project Structure

```
laptop-agent/
│
├── src/
│   └── laptop_agent/
│       ├── __init__.py
│       ├── agent.py              # Agent configuration
│       ├── config.py             # All settings and constants
│       │
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── laptop_search.py  # Laptop search tool
│       │   └── price_finder.py   # Price comparison tool
│       │
│       └── utils/
│           ├── __init__.py
│           └── helpers.py        # Reusable utilities
│
├── tests/
│   ├── test_laptop_search.py
│   └── test_price_finder.py
│
├── docs/
│   ├── getting_started.md
│   └── tools.md
│
├── prompts/
│   └── prompts.yaml              # Agent prompt templates
│
├── app.py                        # Entry point - Gradio UI
├── requirements.txt
├── requirements-dev.txt
├── .env.example
└── README.md
```

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
| AI Framework | [smolagents](https://github.com/huggingface/smolagents) |
| LLM | Llama 3.3 70B via [Groq](https://groq.com) (free) |
| Search | [Tavily API](https://tavily.com) (free tier) |
| UI | [Gradio](https://gradio.app) |
| Language | Python 3.12 |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/laptop-agent.git
cd laptop-agent
```

### 2. Create and activate virtual environment

```bash
# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API keys

Copy the example env file and fill in your keys:

```bash
cp .env.example .env
```

Edit `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

**Getting API keys (both free):**
- **Groq:** [console.groq.com](https://console.groq.com) → API Keys → Create API Key
- **Tavily:** [tavily.com](https://tavily.com) → Sign up → Dashboard → API Key

### 5. Run the app

```bash
python app.py
```

Open your browser at **http://127.0.0.1:7860**

---

## 🛠️ Tools

### `search_laptops(min_budget, max_budget, preferences)`

Searches for laptops within a budget range using real-time web search.

| Parameter | Type | Description |
|---|---|---|
| `min_budget` | int | Minimum budget in INR |
| `max_budget` | int | Maximum budget in INR |
| `preferences` | str | Optional: 'gaming', 'student', 'business', etc. |

### `find_best_price(laptop_model)`

Finds the best current prices for a specific laptop model across Indian sellers.

| Parameter | Type | Description |
|---|---|---|
| `laptop_model` | str | Full model name e.g. 'HP Pavilion 15 Intel Core i5 12th Gen' |

---

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src
```

---

## 📦 Development Setup

Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

### Code formatting

```bash
black src/ tests/
```

### Linting

```bash
flake8 src/ tests/
```

### Type checking

```bash
mypy src/
```

---

## 🔒 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GROQ_API_KEY` | Yes | Groq API key for LLM |
| `TAVILY_API_KEY` | Yes | Tavily API key for search |

---

## ⚠️ Disclaimer

Prices shown are indicative and fetched from real-time web search. Always verify prices on the seller's website before making a purchase. Prices may change without notice.

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Built with ❤️ for the Indian market.

---

## 🙏 Acknowledgements

- [HuggingFace smolagents](https://github.com/huggingface/smolagents) for the agent framework
- [Groq](https://groq.com) for blazing fast free LLM inference
- [Tavily](https://tavily.com) for AI-optimized search
- [Gradio](https://gradio.app) for the UI framework
