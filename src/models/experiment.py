from pydantic import BaseModel, Field
from typing import List, Optional


class Experiment(BaseModel):
    """
    Represents a product research experiment.
    """

    experiment_id: Optional[int] = None

    name: str
    product_name: str
    product_description: str

    target_audience: str
    research_objective: str

    research_questions: List[str] = Field(default_factory=list)