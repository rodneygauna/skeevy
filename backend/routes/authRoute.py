"""backend/routes/authRoute.py"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from models.userModel import User as UserModel
from models.database import get_db
from controllers.authController import (
    create_user, verify_password, authenticate_user,
)
from schemas.userSchema import UserCreate, UserBase


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserBase)
async def create_users(db: Session = Depends(get_db), user: UserCreate):
    """Create a new user in the database."""
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already registered")
    return create_user(db=db, user=user)


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
) -> Token:
    """Authenticate a user and return an access token."""
    user = authenticate_user(
        db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password")
    return {"access_token": user.email, "token_type": "bearer"}
