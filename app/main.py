from fastapi import FastAPI
from .routes.user import user
from .routes.order import order
from .routes.vehicle import vehicle

app = FastAPI()

app.include_router(user)
app.include_router(order)
app.include_router(vehicle)


