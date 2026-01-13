from fastapi import FastAPI
from app.database.database import engine, Base


import app.models.user
import app.models.candidate
import app.models.vote

from app.routers import user, candidate, vote

app = FastAPI(title="Sistem Voting Online")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(candidate.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "API berjalan"}