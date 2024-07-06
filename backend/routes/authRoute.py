"""backend/routes/authRoute.py"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models.userModel import User as UserModel
from models.database import get_db
from controllers.authController import create_user
from schemas.userSchema import UserCreate, UserBase


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserBase)
async def create_users(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user in the database."""
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already registered")
    return create_user(db=db, user=user)
