from sqlalchemy.orm import Session
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateUpdate

def get_all_candidates(db: Session):
    return db.query(Candidate).all()

def get_candidate_by_id(db: Session, candidate_id: int):
    return db.query(Candidate).filter(Candidate.id == candidate_id).first()

def create_candidate(db: Session, candidate: CandidateCreate):
    db_candidate = Candidate(name=candidate.name, description=candidate.description)
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

# Fitur Baru: Update
def update_candidate(db: Session, candidate_id: int, candidate: CandidateUpdate):
    db_candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not db_candidate:
        return None
    
    if candidate.name:
        db_candidate.name = candidate.name
    if candidate.description:
        db_candidate.description = candidate.description
        
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

# Fitur Baru: Delete
def delete_candidate(db: Session, candidate_id: int):
    db_candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not db_candidate:
        return False
        
    db.delete(db_candidate)
    db.commit()
    return True