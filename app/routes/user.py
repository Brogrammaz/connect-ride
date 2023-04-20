from fastapi import APIRouter

from ..models.models import User, UpdatePassword
from ..config.db import user_collection
from ..schemas.user import serializeList, serializeDict
from bson import ObjectId
from .. import utils


user = APIRouter()

@user.get('/api/users/')
async def find_all_users():
    return serializeList(user_collection.find())

@user.get('/api/users/{id}')
async def find_user(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    return serializeDict(user)

@user.post("/api/users/")
async def create_user(user: User):

    # hash the password -> user.password before storage.
    hashed_password = utils.hash_pwd(user.password)
    user.password = hashed_password

    user_collection.insert_one(dict(user))
    return serializeList(user_collection.find())

@user.put("/api/users/{id}")
async def update_user(id, user: User):
    user_collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(user_collection.find_one({"_id":ObjectId(id)}))

@user.put("/api/users/{user_id}/password")
async def update_password(user_id, password:UpdatePassword):
    _user = user_collection.find_one({'_id':ObjectId(user_id)}) 
    if _user:
        _user['password'] = password.password
        return {"Password changed successfully!"}
    else:
        return {"error": "User not found"}

@user.delete("/api/users/{id}")
async def delete_user(id):
    user_collection.delete_one({"_id": ObjectId(id)})
    return {"Response":"Request Successful"}