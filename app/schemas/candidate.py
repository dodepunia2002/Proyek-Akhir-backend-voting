from pydantic import BaseModel
from typing import Optional

class CandidateBase(BaseModel):
    name: str
    description: str

class CandidateCreate(CandidateBase):
    poll_id: int  

class CandidateUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CandidateResponse(CandidateBase):
    id: int
    poll_id: int
    class Config:
        from_attributes = True