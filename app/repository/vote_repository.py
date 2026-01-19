from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.vote import Vote
from app.models.candidate import Candidate


def get_vote_by_user_and_poll(db: Session, user_id: int, poll_id: int):
    return db.query(Vote).filter(
        Vote.user_id == user_id, 
        Vote.poll_id == poll_id
    ).first()

def create_vote(db: Session, user_id: int, candidate_id: int, poll_id: int):
    db_vote = Vote(user_id=user_id, candidate_id=candidate_id, poll_id=poll_id)
    db.add(db_vote)
    db.commit()
    return db_vote

def get_voting_results(db: Session, poll_id: int):
    return db.query(
        Candidate.name, func.count(Vote.id).label("total_votes")
    ).outerjoin(Vote, Candidate.id == Vote.candidate_id)\
     .filter(Candidate.poll_id == poll_id)\
     .group_by(Candidate.id).all()