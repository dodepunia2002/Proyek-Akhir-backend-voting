from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from app.repository import vote_repository, poll_repository, candidate_repository

def cast_vote(db: Session, user_id: int, poll_id: int, candidate_id: int):

    poll = poll_repository.get_poll_by_id(db, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Polling not found")

   
    if datetime.now() > poll.deadline:
        raise HTTPException(status_code=400, detail="Voting period has ended")


    if vote_repository.get_vote_by_user_and_poll(db, user_id, poll_id):
        raise HTTPException(status_code=400, detail="You have already voted in this poll")
    

    candidate = candidate_repository.get_candidate_by_id(db, candidate_id)
    if not candidate or candidate.poll_id != poll_id:
        raise HTTPException(status_code=400, detail="Invalid candidate for this poll")
        
    return vote_repository.create_vote(db, user_id, candidate_id, poll_id)