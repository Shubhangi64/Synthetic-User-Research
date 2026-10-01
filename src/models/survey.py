from pydantic import BaseModel, Field
from typing import Optional


class SurveyQuestion(BaseModel):
    """
    Represents one research question.
    """

    question_id: Optional[int] = None
    experiment_id: Optional[int] = None

    question_text: str
    question_type: str = "open_text"


class SurveyResponse(BaseModel):
    """
    Represents one persona's response to one survey question.
    """

    response_id: Optional[int] = None

    persona_id: int
    question_id: int

    answer: str

    score: Optional[int] = Field(
        default=None,
        ge=1,
        le=5
    )
    