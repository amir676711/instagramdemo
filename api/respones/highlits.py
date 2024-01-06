from pydantic import BaseModel

class CreateHighlitsRespones(BaseModel):
    id: int
    PicUrl: str
    Name: str