# app/models/userModel.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    mobile = Column(Integer)

    pets = relationship("Pet", back_populates="users")
