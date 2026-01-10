from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str

class CandidateResponse(CandidateCreate):
    id: int

    class Config:
        from_attributes = True