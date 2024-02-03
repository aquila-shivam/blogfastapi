# api/blog.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from bson.objectid import ObjectId

from models.blog import Blog, BlogCreate
from models.user import User
from utils.authentication import get_current_user, get_db
from database import blogs_collection

router = APIRouter()

# CRUD Operations
@router.post("/blogs", response_model=Blog)
def create_blog(blog: BlogCreate, current_user: User = Depends(get_current_user)):
    blog_dict = blog.dict()
    blog_dict['user_id'] = current_user.id
    inserted_id = blogs_collection.insert_one(blog_dict).inserted_id
    return {**blog.dict(), "id": str(inserted_id)}

@router.get("/blogs/{blog_id}", response_model=Blog)
def read_blog(blog_id: str):
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    if blog:
        return {**blog, "id": str(blog["_id"])}
    raise HTTPException(status_code=404, detail="Blog not found")

@router.get("/blogs", response_model=List[Blog])
def read_blogs(skip: int = 0, limit: int = 10):
    blogs = list(blogs_collection.find().skip(skip).limit(limit))
    return [{**blog, "id": str(blog["_id"])} for blog in blogs]

@router.put("/blogs/{blog_id}", response_model=Blog)
def update_blog(blog_id: str, blog: BlogCreate, current_user: User = Depends(get_current_user)):
    result = blogs_collection.update_one(
        {"_id": ObjectId(blog_id), "user_id": current_user.id},
        {"$set": blog.dict()},
    )
    if result.modified_count == 1:
        return {**blog.dict(), "id": blog_id}
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/blogs/{blog_id}", response_model=Blog)
def delete_blog(blog_id: str, current_user: User = Depends(get_current_user)):
    result = blogs_collection.delete_one({"_id": ObjectId(blog_id), "user_id": current_user.id})
    if result.deleted_count == 1:
        return {"id": blog_id, **result.raw_result}
    raise HTTPException(status_code=404, detail="Blog not found")
