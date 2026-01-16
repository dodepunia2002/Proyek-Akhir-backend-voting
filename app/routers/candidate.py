from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas.candidate import CandidateCreate, CandidateResponse, CandidateUpdate
from app.repository import candidate_repository
from app.core.deps import get_current_user

router = APIRouter()


@router.get("/", response_model=List[CandidateResponse])
def read_candidates(db: Session = Depends(get_db)):
    return candidate_repository.get_all_candidates(db)


@router.post("/", response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return candidate_repository.create_candidate(db, candidate)


@router.put("/{candidate_id}", response_model=CandidateResponse)
def update_candidate(candidate_id: int, candidate: CandidateUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    updated_candidate = candidate_repository.update_candidate(db, candidate_id, candidate)
    if not updated_candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return updated_candidate

# DELETE (Hapus) - Butuh Login
@router.delete("/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    success = candidate_repository.delete_candidate(db, candidate_id)
    if not success:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return {"message": "Candidate deleted successfully"}