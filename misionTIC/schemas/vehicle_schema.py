def vehicle_serializer(vehicle) -> dict:
    return {
        "id": str(vehicle["_id"]),
        "name": vehicle["name"],
        "brand": vehicle["brand"],
        "year": vehicle["year"],
        "type": vehicle["type"],
    }


def vehicles_serializer(vehicles) -> list:
    return [vehicle_serializer(vehicle) for vehicle in vehicles]
