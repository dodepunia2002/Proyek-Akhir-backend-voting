from sqlalchemy.orm import Session
from app.models.poll import Poll
from app.schemas.poll import PollCreate, PollUpdate

def get_all_polls(db: Session):
    return db.query(Poll).all()

def get_poll_by_id(db: Session, poll_id: int):
    return db.query(Poll).filter(Poll.id == poll_id).first()

# Update: Terima creator_id
def create_poll(db: Session, poll: PollCreate, creator_id: int):
    db_poll = Poll(
        title=poll.title,
        description=poll.description,
        deadline=poll.deadline,
        creator_id=creator_id 
    )
    db.add(db_poll)
    db.commit()
    db.refresh(db_poll)
    return db_poll


def delete_poll(db: Session, poll_id: int):
    poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if poll:
        db.delete(poll)
        db.commit()
        return True
    return False


def update_poll(db: Session, poll_id: int, poll_data: PollUpdate):
    db_poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if not db_poll:
        return None
    
    if poll_data.title:
        db_poll.title = poll_data.title
    if poll_data.description:
        db_poll.description = poll_data.description
    if poll_data.deadline:
        db_poll.deadline = poll_data.deadline
        
    db.commit()
    db.refresh(db_poll)
    return db_poll
