from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.vote import VoteCreate
from app.models.user import User
from app.models.candidate import Candidate
from app.models.vote import Vote

router = APIRouter()  

@router.post("/")
def vote(data: VoteCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    candidate = db.query(Candidate).filter(Candidate.id == data.candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate tidak ditemukan")

    vote = Vote(user_id=data.user_id, candidate_id=data.candidate_id)
    db.add(vote)
    db.commit()

    return {"message": "Vote berhasil"}