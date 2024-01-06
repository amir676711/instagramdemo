from pydantic import BaseModel

class CreateIdNameRespones(BaseModel):
    id: int
    idName: str