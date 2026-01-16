from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository import vote_repository, candidate_repository

def cast_vote(db: Session, user_id: int, candidate_id: int):
    if vote_repository.get_vote_by_user(db, user_id):
        raise HTTPException(status_code=400, detail="You have already voted")
    
    if not candidate_repository.get_candidate_by_id(db, candidate_id):
        raise HTTPException(status_code=404, detail="Candidate not found")
        
    return vote_repository.create_vote(db, user_id, candidate_id)
