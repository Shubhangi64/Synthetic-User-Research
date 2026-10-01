from pydantic import BaseModel, Field
from typing import List


class Experiment(BaseModel):
    experiment_id: int | None = None

    name: str
    product_name: str
    product_description: str

    target_audience: str
    research_objective: str

    research_questions: List[str] = Field(default_factory=list)