from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.schemas.poll import PollCreate, PollResponse
from app.repository import poll_repository
from app.core.deps import get_current_user
from app.schemas.poll import PollCreate, PollResponse, PollUpdate

router = APIRouter()

@router.post("/", response_model=PollResponse)
def create_poll(poll: PollCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):

    return poll_repository.create_poll(db, poll, creator_id=current_user.id)

@router.get("/", response_model=List[PollResponse])
def read_polls(db: Session = Depends(get_db)):
    return poll_repository.get_all_polls(db)

@router.get("/{poll_id}", response_model=PollResponse)
def read_poll_detail(poll_id: int, db: Session = Depends(get_db)):
    poll = poll_repository.get_poll_by_id(db, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Polling not found")
    return poll

@router.delete("/{poll_id}")
def delete_poll(poll_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    poll = poll_repository.get_poll_by_id(db, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Polling not found")
    

    if current_user.role != "admin" and poll.creator_id != current_user.id:
        raise HTTPException(
            status_code=403, 
            detail="Tidak diizinkan. Hanya Admin atau Pembuat Polling yang bisa menghapus."
        )

    poll_repository.delete_poll(db, poll_id)
    return {"message": "Polling deleted successfully"}

@router.put("/{poll_id}", response_model=PollResponse)
def update_poll(poll_id: int, poll_in: PollUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):

    poll = poll_repository.get_poll_by_id(db, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Polling not found")
    
 
    if current_user.role != "admin" and poll.creator_id != current_user.id:
        raise HTTPException(
            status_code=403, 
            detail="Tidak diizinkan. Hanya Admin atau Pembuat Polling yang bisa mengedit."
        )
    
    updated_poll = poll_repository.update_poll(db, poll_id, poll_in)
    return updated_poll