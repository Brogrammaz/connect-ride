from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class User(BaseModel):
    username : str
    email: str
    phoneNo: int
    password: str

class TimeVenueData():
    date : str
    time: str
    location: str

class Transmission(str,Enum):
    auto = "Automatic"
    manual = "Manual"

class Category(str, Enum):
    mini = "Mini"
    truck = "Truck"
    suv = "SUV"
    luxury = "Luxury"
    van = "Van"

class Vehicle(BaseModel):
    id: Optional[UUID] = uuid4
    make: str
    model: str
    plateNo : str
    category : Category
    transmission: Transmission
    year : int
    color: str
    rates : str
    seats : int
    topSpeed : int
    images: List[str]

class Order(BaseModel):
    id: Optional[UUID] = uuid4
    pickUp : TimeVenueData
    dropOff: TimeVenueData
    vehicle: Vehicle
    user: User

    class Config:
        arbitrary_types_allowed = True

class UpdatePassword(BaseModel):
    password : str