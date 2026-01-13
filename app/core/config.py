import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./voting.db")
APP_NAME = "Sistem Voting Online"