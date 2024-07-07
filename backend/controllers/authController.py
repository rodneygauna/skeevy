"""backend/controllers/authController.py"""
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models.userModel import User as UserModel
from schemas.userSchema import (
    User as UserSchema,
    UserCreate as UserCreateSchema,
)

# TODO: Move these to a .env file and generate a new secret key
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# TODO: Look at using just bcrypt instead of passlib
# See issue: https://github.com/pyca/bcrypt/issues/684#issuecomment-1902590553
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: UserSchema):
    """Create a new user in the database."""
    db_user = UserModel(
        email=user.email,
        password=bcrypt_context.hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_password(plain_password: str, hashed_password: str):
    """Verify the password provided by the user."""
    return bcrypt_context.verify(plain_password, hashed_password)


def get_user(db, email: str):
    if email in db:
        user_dict = db[email]
        return UserCreateSchema(**user_dict)


def authenticate_user(db: Session, email: str, password: str):
    """Authenticate a user and return the user if successful."""
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create an access token for the user."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user
