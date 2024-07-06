"""backend/main.py"""
from fastapi import FastAPI

from routes.petRoute import router as pet_router
from routes.authRoute import router as auth_router
from models.database import engine, Base
from models import *


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth_router)
app.include_router(pet_router)
