"""backend/schemas/userSchema.py"""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """User base schema"""
    email: EmailStr
    password_hash: str
    first_name: str
    last_name: str
    phone_number: int


class UserCreate(UserBase):
    """User create schema"""
    pass


class User(UserBase):
    """User schema"""
    id: int

    class Config:
        """Pydantic configuration"""
        from_attributes = True
