from fastapi import APIRouter

from ..models.models import Order
from ..config.db import orders_collection
from ..schemas.user import serializeList, serializeDict
from bson import ObjectId

order = APIRouter()

@order.get('/api/orders/')
async def get_orders():
    return serializeList(orders_collection.find())

@order.get("/api/orders/{id}")
async def get_order_by_id(id: str):
    order = order_collection.find_one({"_id": ObjectId(id)})
    return serializeDict(order)

@order.post("/api/orders/")
async def place_order(order: Order):
    placed_order = order_collection.insert_one(dict(order))
    return serializeDict(order_collection.find_one({"_id": ObjectId(placed_order._id)}))

@order.put("/api/orders/{order_id}")
async def update_order(order_id, order: Order):
    _order = orders_collection.find_one_and_update({"_id": ObjectId(order_id)}, {"$set":dict(order)})
    return serializeDict(orders_collection.find_one({"_id": ObjectId(id)}))

@order.delete("/api/orders/{id}")
async def delete_order(id:str):
    order_collection.delete_one({"_id":ObjectId(id)})
    return {"Response": "Order deleted successfully"}

