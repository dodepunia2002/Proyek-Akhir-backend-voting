from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.schemas.candidate import CandidateResponse

class PollBase(BaseModel):
    title: str
    description: str
    deadline: datetime  

class PollUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None

class PollCreate(PollBase):
    pass

class PollResponse(PollBase):
    id: int
    is_active: bool
   
    candidates: List[CandidateResponse] = []

    class Config:
        from_attributes = True