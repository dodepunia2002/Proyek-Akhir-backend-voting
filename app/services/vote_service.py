from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.vote import Vote
from app.models.user import User
from app.models.candidate import Candidate
from app.schemas.vote import VoteCreate

def create_vote(db: Session, vote: VoteCreate):
    
    user = db.query(User).filter(User.id == vote.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    
    candidate = db.query(Candidate).filter(Candidate.id == vote.candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate tidak ditemukan")

    
    existing_vote = db.query(Vote).filter(Vote.user_id == vote.user_id).first()
    if existing_vote:
        raise HTTPException(status_code=400, detail="User sudah melakukan vote")

    new_vote = Vote(
        user_id=vote.user_id,
        candidate_id=vote.candidate_id
    )

    db.add(new_vote)
    db.commit()
    return {"message": "Vote berhasil"}