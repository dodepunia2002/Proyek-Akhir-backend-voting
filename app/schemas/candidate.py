from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str

class CandidateResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True