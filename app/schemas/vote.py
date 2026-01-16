from pydantic import BaseModel

class VoteCreate(BaseModel):
    candidate_id: int

class VoteResult(BaseModel):
    candidate_name: str
    total_votes: int
