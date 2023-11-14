"""Pets > Models"""

# Imports
from src import db
from src.models import BaseModel


class Pet(BaseModel):
    """Pet model"""

    __tablename__ = "pets"

    name = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    pet_type = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(
        db.String(255), nullable=False, default="default_pet.jpg")


class UserPet(BaseModel):
    """User <---> Pet relationship model"""

    __tablename__ = "user_pets"

    relationship_type = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"))
