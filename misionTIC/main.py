from fastapi import FastAPI
from routes.vehicle_routes import vehicle_api_router

app = FastAPI()

app.include_router(vehicle_api_router)
