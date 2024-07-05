"""backend/models/userModel.py"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


class User(Base):
    """User model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(Integer)

    pets = relationship("Pet", back_populates="user")
