from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base

from app.models import user, candidate, vote, poll 
from app.routers import auth, candidate, vote, poll as poll_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistem Voting Online")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(poll_router.router, prefix="/polls", tags=["Polls"]) # Router Baru
app.include_router(candidate.router, prefix="/candidates", tags=["Candidates"])
app.include_router(vote.router, prefix="/votes", tags=["Votes"])

@app.get("/")
def root():
    return {"message": "Welcome to Voting System API"}