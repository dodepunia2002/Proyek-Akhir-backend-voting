from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.vote import VoteCreate
from app.services.vote_service import create_vote

router = APIRouter(prefix="/votes", tags=["Votes"])

@router.post("/")
def vote(vote: VoteCreate, db: Session = Depends(get_db)):
    return create_vote(db, vote)