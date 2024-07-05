from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    password_hash: str
    firstname: str
    lastname: str
