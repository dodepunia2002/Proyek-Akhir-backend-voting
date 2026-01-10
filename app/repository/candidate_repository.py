from sqlalchemy.orm import Session
from app.models.candidate import Candidate

def create_candidate(db: Session, name: str):
    candidate = Candidate(name=name)
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate

def get_candidates(db: Session):
    return db.query(Candidate).all()