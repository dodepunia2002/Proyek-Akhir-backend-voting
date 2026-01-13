from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user, candidate, vote
from app.routers import user as user_router
from app.routers import candidate as candidate_router
from app.routers import vote as vote_router

app = FastAPI(
    title="Sistem Voting Online",
    version="0.1.0"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API berjalan"}

app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(candidate_router.router, prefix="/candidates", tags=["Candidates"])
app.include_router(vote_router.router, prefix="/votes", tags=["Votes"])