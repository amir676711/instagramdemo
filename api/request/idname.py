from pydantic import BaseModel
from fastapi import FastAPI
class CreateIdNameRequest(BaseModel):
    idName: str

class EditIdNameRequest(BaseModel):
    id : int
    idName: str