from bson import ObjectId
from pymongo import *
from pydantic import *
from typing import *

client = MongoClient("mongodb://127.0.0.1:27017/?readPreference=primary")

db = client.users
collection = db.get_collection('mcq')


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class McqModel(BaseModel):
    id: int = Field(default_factory=PyObjectId, alias="_id")
    Grade: int = Field()
    Semesters: int = Field()
    Modules: str = Field()
    Question: str = Field()
    Choice_A: str = Field()
    Choice_B: str = Field()
    Choice_C: str = Field()
    Choice_D: str = Field()
    Choice_E: Optional[str] = Field()
    Answer: str = Field()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class McqModelUpdate(BaseModel):
    id: int = Field(default_factory=PyObjectId, alias="_id")
    Grade: Optional[int] = Field()
    Semesters: Optional[int] = Field()
    Modules: Optional[str] = Field()
    Question: Optional[str] = Field()
    Choice_A: Optional[str] = Field()
    Choice_B: Optional[str] = Field()
    Choice_C: Optional[str] = Field()
    Choice_D: Optional[str] = Field()
    Choice_E: Optional[str] = Field()
    Answer: Optional[str] = Field()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class GetModule(BaseModel):
    Grade: int
    Semester: int
    Module: Optional[str]

