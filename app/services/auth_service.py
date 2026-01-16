from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository import user_repository
from app.schemas.user import UserCreate

def register_new_user(db: Session, user: UserCreate):
    existing_user = user_repository.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_repository.create_user(db, user)
