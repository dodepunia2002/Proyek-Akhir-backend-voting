from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.schemas.vote import VoteCreate
from app.repository.vote_repository import create_vote

router = APIRouter(prefix="/votes", tags=["Votes"])

@router.post("/")
def vote(data: VoteCreate, db: Session = Depends(get_db)):
    return create_vote(db, data.user_id, data.candidate_id)