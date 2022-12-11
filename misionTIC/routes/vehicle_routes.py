from fastapi import APIRouter
from config.database import collection_name
from models.vehicles_model import Vehicle
from schemas.vehicle_schema import vehicle_serializer, vehicles_serializer
from bson import ObjectId

vehicle_api_router = APIRouter()


# retrieve
@vehicle_api_router.get("/")
async def get_vehicles():
    vehicles = vehicles_serializer(collection_name.find())
    return {"status": "ok", "data": vehicles}


@vehicle_api_router.get("/{id}")
async def get_vehicle(id: str):
    return vehicles_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@vehicle_api_router.post("/")
async def create_vehicle(vehicle: Vehicle):
    _id = collection_name.insert_one(dict(vehicle))
    return vehicles_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@vehicle_api_router.put("/{id}")
async def update_vehicle(id: str, vehicle: Vehicle):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(vehicle)
    })
    return vehicles_serializer(collection_name.find({"_id": ObjectId(id)}))


# delete
@vehicle_api_router.delete("/{id}")
async def delete_vehicle(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
