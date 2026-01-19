from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database.database import get_db
from app.schemas.vote import VoteCreate, VoteResult
from app.services import vote_service
from app.repository import vote_repository, poll_repository
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/")
def vote(vote_in: VoteCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    vote_service.cast_vote(db, current_user.id, vote_in.poll_id, vote_in.candidate_id)
    return {"message": "Vote cast successfully"}

@router.get("/results/{poll_id}", response_model=List[VoteResult])
def results(poll_id: int, db: Session = Depends(get_db)):

    poll = poll_repository.get_poll_by_id(db, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Polling not found")


    if datetime.now() < poll.deadline:
        raise HTTPException(status_code=400, detail="Hasil voting tertutup sampai batas waktu berakhir.")

    results = vote_repository.get_voting_results(db, poll_id)
    return [{"candidate_name": r[0], "total_votes": r[1]} for r in results]