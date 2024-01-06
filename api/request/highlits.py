from pydantic import BaseModel

class CreateHighlitsRequest(BaseModel):
    PicUrl: str
    Name: str

class EditHighlitsRequest(BaseModel):
    id: int
    PicUrl: str
    Name: str