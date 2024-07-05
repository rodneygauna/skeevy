"""backend/controllers/petController.py"""
from sqlalchemy.orm import Session

from models.petModel import Pet as PetModel
from schemas.petSchema import Pet as PetSchema


def get_pets(db: Session):
    """Get all pets from the database."""
    return db.query(PetModel).all()


def create_pet(db: Session, pet: PetSchema):
    """Create a new pet in the database."""
    db_pet = PetModel(**pet.model_dump())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet
