from sqlalchemy.orm import Session
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate

def get_candidates(db: Session):
    return db.query(Candidate).all()

def create_candidate(db: Session, candidate: CandidateCreate):
    new_candidate = Candidate(name=candidate.name)
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    return new_candidate