from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateResponse

router = APIRouter()  

@router.get("/", response_model=list[CandidateResponse])
def list_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()

@router.post("/", response_model=CandidateResponse)
def add_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    new_candidate = Candidate(name=candidate.name)
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    return new_candidate