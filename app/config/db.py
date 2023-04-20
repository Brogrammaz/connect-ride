from pymongo import MongoClient
from urllib.parse import quote_plus
import dns
from dotenv import dotenv_values

config = dotenv_values(".env")
conn = MongoClient(config.get("DATABASE_CONNECTION_URL"))

db = conn['ConnectRide']

user_collection = db["users"]
orders_collection = db["orders"]
vehicle_collection = db["vehicles"]