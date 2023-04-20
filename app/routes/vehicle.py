from fastapi import APIRouter

from ..models.models import Vehicle
from ..config.db import vehicle_collection
from ..schemas.user import serializeDict, serializeList
from bson import ObjectId

vehicle = APIRouter()

@vehicle.get('/api/vehicles/')
async def get_all_vehicles():
    return serializeList(vehicle_collection.find())

@vehicle.get("/api/vehicles/{id}")
async def get_vehicle(id):
    return serializeDict(vehicle_collection.find_one(
        {"_id": ObjectId(id)}
    ))

@vehicle.put('/api/vehicles/{id}')
async def update_vehicle(id, vehicle: Vehicle):
    vehicle_collection.find_one(
        {"_id": ObjectId(id)},
        {"$set": dict(vehicle)}
        )
    return serializeDict(vehicle_collection.find_one(
        {"_id": ObjectId(id)}
    ))

@vehicle.delete('/api/vehicle/{id}')
async def delete_vehicle(id):
    vehicle_collection.delete_one(
        {"_id": ObjectId(id)}
    )
    return {"Response":"Vehicle deleted successfully!"}