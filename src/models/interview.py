from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Interview(BaseModel):
    """
    Represents a conversation between a researcher and a persona.
    """

    interview_id: Optional[int] = None

    experiment_id: int
    persona_id: int


class InterviewMessage(BaseModel):
    """
    Represents one message in an interview.
    """

    message_id: Optional[int] = None

    interview_id: int

    role: str
    content: str

    timestamp: datetime