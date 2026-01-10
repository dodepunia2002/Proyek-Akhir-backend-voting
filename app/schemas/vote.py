from pydantic import BaseModel

class VoteCreate(BaseModel):
    user_id: int
    candidate_id: int