from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    user_name: str

class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str
