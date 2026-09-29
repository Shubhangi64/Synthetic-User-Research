import json
#import uuid
from .ai_client import generate_json
from .config import DATA_DIR, PRODUCT, PRODUCT_DESCRIPTION, RESEARCH_OBJECTIVE, TARGET_AUDIENCE
from .experiment import load_personas, save_personas

PERSONA_TEMPLATE = {
    "name": "", "age": 0, "occupation": "", "location": "", "income": "",
    "personality_traits": [], "communication_style": "", "decision_making_style": "",
    "shopping_frequency": "", "price_sensitivity": "", "brand_loyalty": "",
    "review_dependence": "", "technology_adoption": "", "impulse_buying": "",
    "goals": [], "motivations": [], "pain_points": [], "concerns": [], "values": [],
    "preferred_categories": [], "preferred_brands": [], "budget_preference": "",
    "important_product_factors": [], "profile_summary": ""
}

def _summary(personas):
    return [{k: p.get(k) for k in ["name","age","occupation","personality_traits","shopping_frequency","price_sensitivity","brand_loyalty","review_dependence","technology_adoption","impulse_buying"]} for p in personas]

def generate_persona(existing_personas):
    prompt = f"""
You are a Synthetic User Persona Generation Agent.
PRODUCT: {PRODUCT}
PRODUCT DESCRIPTION: {PRODUCT_DESCRIPTION}
TARGET AUDIENCE: {TARGET_AUDIENCE}
RESEARCH OBJECTIVE: {RESEARCH_OBJECTIVE}
EXISTING PERSONAS:
{json.dumps(_summary(existing_personas), indent=2)}

Create ONE new synthetic research participant. Make the participant substantially different from existing personas. Vary age, occupation, location, personality, shopping behavior, technology adoption, price sensitivity, brand loyalty, review dependence, impulse buying, motivations, concerns and preferred categories.

The persona must be internally consistent. High price sensitivity should mean stronger interest in price/discounts; high review dependence should mean checking reviews; low technology adoption should mean more caution around AI; privacy-conscious users should have stronger privacy concerns. Some personas may like the product, some may be neutral, and some may be skeptical.

Return ONLY valid JSON using exactly this structure:
{json.dumps(PERSONA_TEMPLATE, indent=2)}
"""
    persona = generate_json(prompt)
    #persona["id"] = str(uuid.uuid4())
    return persona

def generate_to_target(target=20):

    personas = load_personas()

    print(f"\nCurrently available personas: {len(personas)}")

    while len(personas) < target:

        next_number = len(personas) + 1

        print("\n" + "=" * 60)
        print(f"Generating Persona {next_number}...")
        print("=" * 60)

        persona = generate_persona(personas)

        personas.append(persona)

        # Automatically assigns IDs 1, 2, 3...
        save_personas(personas, generated=True)

        print(f"✓ Persona {next_number} saved")
        print(f"✓ Total personas: {len(personas)}")

    print("\n" + "=" * 60)
    print(f"✓ PERSONA GENERATION COMPLETE")
    print(f"✓ Total Personas: {len(personas)}")
    print("=" * 60)

    return personas

def print_personas(personas):
    print("\n" + "=" * 80 + "\nSYNTHETIC PERSONAS\n" + "=" * 80)
    for index, p in enumerate(personas, 1):
        print(f"\nPERSONA {index}\n{'-'*60}")
        for label, key in [("Name","name"),("Age","age"),("Occupation","occupation"),("Location","location"),("Personality","personality_traits"),("Price Sensitivity","price_sensitivity"),("Brand Loyalty","brand_loyalty"),("Review Dependence","review_dependence"),("Technology Adoption","technology_adoption"),("Summary","profile_summary")]:
            value = p.get(key)
            if isinstance(value, list): value = ", ".join(value)
            print(f"{label}: {value}")
