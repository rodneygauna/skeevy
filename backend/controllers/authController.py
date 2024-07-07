"""backend/controllers/authController.py"""
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models.userModel import User as UserModel
from schemas.userSchema import User as UserSchema


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
