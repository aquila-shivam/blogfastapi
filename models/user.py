# models/user.py
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    id: Optional[str]
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    tags: List[str] = []

class User(UserBase):
    id: Optional[str]  # Adjust this based on your use case
    tags: List[str] = []

    class Config:
        orm_mode = True
