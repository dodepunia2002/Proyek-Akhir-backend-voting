from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateResponse

router = APIRouter(prefix="/candidates", tags=["Candidates"])

@router.get("/", response_model=List[CandidateResponse])
def list_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()

@router.post("/", response_model=CandidateResponse)
def add_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    obj = Candidate(name=candidate.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj