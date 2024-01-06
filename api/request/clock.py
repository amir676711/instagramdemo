from pydantic import BaseModel

class CreateClockRequest(BaseModel):
    Time: str
class EditClockRequest(BaseModel):
    id:int
    Time:str