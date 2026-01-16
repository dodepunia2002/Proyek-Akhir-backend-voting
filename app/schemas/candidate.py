from pydantic import BaseModel
from typing import Optional

class CandidateBase(BaseModel):
    name: str
    description: str

class CandidateCreate(CandidateBase):
    pass

# Schema baru untuk Update (field opsional)
class CandidateUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CandidateResponse(CandidateBase):
    id: int
    class Config:
        from_attributes = True
