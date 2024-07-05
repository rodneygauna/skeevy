from fastapi import FastAPI
from contextlib import asynccontextmanager
from models.userModel import User
from database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

