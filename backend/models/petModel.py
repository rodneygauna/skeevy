"""backend/models/petModel.py"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Pet(Base):
    """Pet model"""
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="pets")
