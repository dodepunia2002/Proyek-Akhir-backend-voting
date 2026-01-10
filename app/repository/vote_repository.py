from sqlalchemy.orm import Session
from app.models.vote import Vote

def create_vote(db: Session, user_id: int, candidate_id: int):
    vote = Vote(user_id=user_id, candidate_id=candidate_id)
    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote