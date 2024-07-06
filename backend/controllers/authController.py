"""backend/controllers/authController.py"""
from sqlalchemy.orm import Session

from models.userModel import User as UserModel
from schemas.userSchema import User as UserSchema


def create_user(db: Session, user: UserSchema):
    """Create a new user in the database."""
    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
