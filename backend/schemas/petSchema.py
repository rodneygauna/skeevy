"""backend/schemas/petSchema.py"""
from pydantic import BaseModel


class PetBase(BaseModel):
    """Pet base schema"""
    name: str


class PetCreate(PetBase):
    """Pet create schema"""
    pass


class Pet(PetBase):
    """Pet schema"""
    id: int

    class Config:
        """Pydantic configuration"""
        from_attributes = True
