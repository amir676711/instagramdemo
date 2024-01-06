from pydantic import BaseModel
from typing import Optional
class CreateClockRespones(BaseModel):
    id:int
    Time: str