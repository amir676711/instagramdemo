from pydantic import BaseModel

class CreatePostRespones(BaseModel):
    id: int
    PostPicUrl: str
    TypePost: int
