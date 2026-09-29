import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
RESULTS_DIR = ROOT_DIR / "results"
DATA_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)
load_dotenv(ROOT_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite").strip()

PRODUCT = "AI Personal Shopping Platform"
PRODUCT_DESCRIPTION = """
An AI-powered personal shopping platform that provides:
- AI product recommendations
- Price comparison
- Personalized shopping feed
- Review summarization
- Virtual try-on
- Price-drop alerts
- Budget-based shopping
- Brand comparison
- Alternative product suggestions
- Return-policy comparison
- AI shopping assistant
"""
TARGET_AUDIENCE = "Online shoppers aged 18–40"
RESEARCH_OBJECTIVE = (
    "To understand the preferences, expectations, concerns, and behavioral "
    "responses of online shoppers toward an AI-powered personal shopping platform."
)

DEFAULT_QUESTIONS = [
    "What do you think about using AI for personal shopping recommendations?",
    "Would you trust this platform when buying an expensive product? Why?",
    "Which feature would be most useful to you and why?",
    "What is your biggest concern about using this platform?",
    "How important are price comparison and price-drop alerts to you?",
    "Would you use this product? Give a score from 1 to 5 and explain your reason.",
]

SCENARIOS = {
    "shopping": {
        "product": PRODUCT,
        "description": PRODUCT_DESCRIPTION,
        "target_audience": TARGET_AUDIENCE,
        "research_objective": RESEARCH_OBJECTIVE,
        "questions": DEFAULT_QUESTIONS,
    },
    "fitness": {
        "product": "AI Fitness and Workout Platform",
        "description": "An AI fitness platform that creates personalized workout plans, tracks progress, recommends exercises, and provides nutrition guidance.",
        "target_audience": "Adults aged 18–40 interested in fitness",
        "research_objective": "Understand user expectations, trust concerns, personalization needs, and willingness to use an AI fitness platform.",
        "questions": [
            "What do you think about AI-generated workout plans?",
            "Would you trust AI recommendations for your fitness routine? Why?",
            "Which feature would be most useful to you?",
            "What concerns would you have about sharing fitness data?",
            "Would you use this product? Give a score from 1 to 5 and explain why.",
        ],
    },
    "grocery": {
        "product": "AI Online Grocery Shopping Platform",
        "description": "An online grocery platform using AI for product recommendations, budget planning, shopping lists, substitutions, and personalized offers.",
        "target_audience": "Adults who regularly purchase groceries online",
        "research_objective": "Understand convenience, price sensitivity, trust, and personalization preferences in AI-assisted grocery shopping.",
        "questions": [
            "Would AI-generated grocery recommendations be useful to you?",
            "How important is price comparison when buying groceries?",
            "Would you allow AI to create a shopping list for you?",
            "What would make you distrust an AI grocery recommendation?",
            "Would you use this product? Give a score from 1 to 5 and explain why.",
        ],
    },
}
