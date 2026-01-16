from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base
from app.routers import auth, candidate, vote

# Buat tabel otomatis
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistem Voting Online")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)
# --------------------------------------------------

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(candidate.router, prefix="/candidates", tags=["Candidates"])
app.include_router(vote.router, prefix="/votes", tags=["Votes"])

@app.get("/")
def root():
    return {"message": "Welcome to Voting System API"}