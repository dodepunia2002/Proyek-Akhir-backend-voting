from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Poll(Base):
    __tablename__ = "polls"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    deadline = Column(DateTime)
    is_active = Column(Boolean, default=True)
    

    creator_id = Column(Integer, ForeignKey("users.id"))
    
    # Relasi
    creator = relationship("User", back_populates="polls")
    candidates = relationship("Candidate", back_populates="poll", cascade="all, delete-orphan") # Auto hapus kandidat jika poll dihapus
    votes = relationship("Vote", back_populates="poll", cascade="all, delete-orphan")