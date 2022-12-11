from bson import ObjectId
from pydantic import BaseModel


class Vehicle(BaseModel):
    model: str
    brand: str
    year: str
    type: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "model": "sorento",
                "brand": "kia",
                "year": "2008",
                "type": "usado",
            }
        }
