from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
 
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    

    poll_id = Column(Integer, ForeignKey("polls.id"))
    
    poll = relationship("Poll", back_populates="votes")