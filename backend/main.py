"""backend/main.py"""
from fastapi import FastAPI

from routes.petRoute import router as pet_router
from models.database import engine, Base
from models import *


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(pet_router)
