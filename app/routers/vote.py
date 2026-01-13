from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.vote import VoteCreate
from app.core.database import get_db
from app.models.vote import Vote

router = APIRouter()

@router.post("/")
def vote(data: VoteCreate, db: Session = Depends(get_db)):
    vote = Vote(
        user_id=data.user_id,
        candidate_id=data.candidate_id
    )
    db.add(vote)
    db.commit()
    return {"message": "Vote berhasil"}