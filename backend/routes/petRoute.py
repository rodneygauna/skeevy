"""backend/routes/petRoute.py"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.petModel import Pet as PetModel
from models.database import get_db
from controllers.petController import create_pet
from schemas.petSchema import PetCreate


router = APIRouter(
    prefix="/pets",
    tags=["pets"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=PetCreate)
async def create_pets(pet: PetCreate, db: Session = Depends(get_db)):
    """Create a new pet in the database."""
    db_pet = db.query(PetModel).filter(PetModel.name == pet.name).first()
    if db_pet:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pet already registered")
    return create_pet(db=db, pet=pet)
