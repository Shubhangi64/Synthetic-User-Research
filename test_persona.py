from src.models import Persona


persona = Persona(
    persona_id=1,
    name="Marcus Vance",
    age=34,
    occupation="Cybersecurity Analyst",
    location="Austin, TX",

    personality_traits=[
        "analytical",
        "skeptical",
        "pragmatic",
        "privacy-conscious"
    ],

    behavioral_patterns=[
        "researches products carefully",
        "checks multiple reviews",
        "compares prices"
    ],

    psychological_profile=[
        "values privacy",
        "prefers evidence-based decisions"
    ],

    price_sensitivity=3,
    brand_loyalty=2,
    review_dependence=5,
    technology_adoption=5
)


print(persona)
print()
print("Name:", persona.name)
print("Age:", persona.age)