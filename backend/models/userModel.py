"""backend/models/userModel.py"""
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    """User model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(Integer)
    is_active = Column(Boolean, default=True)

    pets = relationship("Pet", back_populates="user")
