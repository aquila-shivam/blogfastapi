# api/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utils.authentication import create_jwt_token, pwd_context, get_current_user, verify_jwt_token
from models.user import User, UserCreate, UserUpdate
from database import users_collection, get_db
from bson import ObjectId
from pymongo.collection import Collection
from typing import List

router = APIRouter()

@router.post("/register", response_model=User)
def register_user(user: UserCreate, db: Collection = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict['password'] = hashed_password
    inserted_id = users_collection.insert_one(user_dict).inserted_id
    return {**user.dict(), "id": str(inserted_id), "tags": []}



@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Verify user credentials
    user = users_collection.find_one({"username": form_data.username})

    # Check if the user exists and the password is correct
    if user is None or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Generate JWT token
    token_data = {"sub": str(user["_id"]), "username": user["username"]}
    token = create_jwt_token(token_data)

    # Return the token in the response
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    # Get user from the database based on the provided username
    user = users_collection.find_one({"username": form_data.username})

    # Check if the user exists and the password is correct
    if user is None or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Generate JWT token
    token_data = {"sub": str(user["_id"]), "username": user["username"]}
    token = create_jwt_token(token_data)

    # Return the token in the response
    return {"access_token": token, "token_type": "bearer"}

@router.put("/profile", response_model=UserUpdate)
def update_profile(user: UserUpdate, current_user: UserUpdate = Depends(get_current_user), db: Collection = Depends(get_db)):
    user_id = ObjectId(current_user.id)
    users_collection.update_one({"_id": user_id}, {"$set": user.dict()})
    return user

@router.post("/tags/add", response_model=UserUpdate)
def add_tags(tags: List[str], current_user: UserUpdate = Depends(get_current_user), db: Collection = Depends(get_db)):
    user_id = ObjectId(current_user.id)
    users_collection.update_one({"_id": user_id}, {"$addToSet": {"tags": {"$each": tags}}})
    updated_user = users_collection.find_one({"_id": user_id})
    return UserUpdate(**updated_user)

@router.post("/tags/remove", response_model=UserUpdate)
def remove_tags(tags: List[str], current_user: UserUpdate = Depends(get_current_user), db: Collection = Depends(get_db)):
    user_id = ObjectId(current_user.id)
    users_collection.update_one({"_id": user_id}, {"$pullAll": {"tags": tags}})
    updated_user = users_collection.find_one({"_id": user_id})
    return UserUpdate(**updated_user)
