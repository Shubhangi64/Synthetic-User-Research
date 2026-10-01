from pydantic import BaseModel
from typing import List, Dict, Optional


class InsightResult(BaseModel):
    """
    Represents research insights extracted from synthetic responses.
    """

    insight_id: Optional[int] = None

    experiment_id: int

    summary: str

    recurring_themes: List[str]

    sentiment: Dict[str, int]

    agreement_patterns: List[str]

    disagreement_patterns: List[str]

    behavioral_trends: List[str]

    feature_preferences: List[str]

    concerns: List[str]

    research_implications: List[str]

    limitations: List[str]

    would_use_count: int

    would_use_average: float