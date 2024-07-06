"""backend/schemas/userSchema.py"""
from pydantic import BaseModel, EmailStr
from .petSchema import Pet


class UserBase(BaseModel):
    """User base schema"""
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: int


class UserCreate(UserBase):
    """User create schema"""
    password: str


class User(UserBase):
    """User schema"""
    id: int
    is_active: bool
    pets: list[Pet] = []

    class Config:
        """Pydantic configuration"""
        from_attributes = True
