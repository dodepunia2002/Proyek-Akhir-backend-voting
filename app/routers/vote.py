from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas.vote import VoteCreate, VoteResult
from app.services import vote_service
from app.repository import vote_repository
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/")
def vote(vote_in: VoteCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    vote_service.cast_vote(db, current_user.id, vote_in.candidate_id)
    return {"message": "Vote cast successfully"}

@router.get("/results", response_model=List[VoteResult])
def results(db: Session = Depends(get_db)):
    results = vote_repository.get_voting_results(db)
    return [{"candidate_name": r[0], "total_votes": r[1]} for r in results]
