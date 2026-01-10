from fastapi import FastAPI
from app.database.database import Base, engine

from app.models.user import User
from app.models.candidate import Candidate
from app.models.vote import Vote

from app.routers import user, candidate, vote

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistem Voting Online")

app.include_router(user.router)
app.include_router(candidate.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "API Sistem Voting Online Berhasil Dijalankan"}