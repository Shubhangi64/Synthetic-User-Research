from pydantic import BaseModel, Field
from typing import Optional


class ValidationResult(BaseModel):
    """
    Represents the validation result for a synthetic response.
    """

    validation_id: Optional[int] = None

    persona_id: int

    consistency_score: int = Field(
        ge=1,
        le=5
    )

    realism_score: int = Field(
        ge=1,
        le=5
    )

    status: str

    issues: Optional[str] = None

    explanation: Optional[str] = None