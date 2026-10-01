from pydantic import BaseModel, Field
from typing import List


class Persona(BaseModel):
    persona_id: int | None = None

    name: str
    age: int = Field(ge=18, le=100)
    occupation: str
    location: str

    personality_traits: List[str]
    behavioral_patterns: List[str]
    psychological_profile: List[str]

    price_sensitivity: int = Field(ge=1, le=5)
    brand_loyalty: int = Field(ge=1, le=5)
    review_dependence: int = Field(ge=1, le=5)
    technology_adoption: int = Field(ge=1, le=5)