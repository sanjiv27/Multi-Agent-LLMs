from typing import List, Dict, Optional
from pydantic import BaseModel

class UserInput(BaseModel):
    """User input for diagnosis"""
    symptoms: List[str]
    age: Optional[int] = None
    gender: Optional[str] = None
    medical_history: Optional[str] = None

class AgentResponse(BaseModel):
    """Response from a specialized agent"""
    agent_type: str
    response: str
    confidence: float
    diseases: List[str]

class FinalOutput(BaseModel):
    """Final diagnosis output"""
    top_diseases: List[str]
    confidence_summary: str
    agent_responses: List[AgentResponse] 