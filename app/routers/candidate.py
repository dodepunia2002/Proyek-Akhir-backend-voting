from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.schemas.candidate import CandidateCreate, CandidateResponse
from app.repository.candidate_repository import create_candidate, get_candidates

router = APIRouter(prefix="/candidates", tags=["Candidates"])

@router.post("/", response_model=CandidateResponse)
def add_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    return create_candidate(db, candidate.name)

@router.get("/", response_model=list[CandidateResponse])
def list_candidates(db: Session = Depends(get_db)):
    return get_candidates(db)