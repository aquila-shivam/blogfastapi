# models/blog.py
from typing import List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: str

    class Config:
        orm_mode = True
